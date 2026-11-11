from __future__ import annotations

# Standard library imports
import argparse
import json
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, List, Optional, TextIO, Tuple

# First-party imports
from harness_core.git.exceptions import SEGitError
from harness_core.git.git_repository import GitRepository
from harness_core.lifecycle.runnable import Runnable
from harness_core.models.catalogs.exceptions import SEYamlCatalogUnreadable
from harness_core.terminal.human_confirmation import HumanConfirmation
from ticket_docs.api.cli.ticket_docs_parser import TicketDocsParser
from ticket_docs.models.checks.exceptions import SEInvalidFolderRulesException
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.models.enums import TicketDocsCommand
from ticket_docs.models.evidence.exceptions import SEInvalidActionsRunException, SEInvalidRunRequestException
from ticket_docs.models.evidence.run_request import RunRequest
from ticket_docs.models.github.exceptions import (
    SEInvalidBoardFieldException,
    SEInvalidBoardProjectException,
    SEInvalidGithubCatalogException,
)
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.models.hooks.file_hook_payload import FileHookPayload
from ticket_docs.models.hooks.hook_payload import HookPayload
from ticket_docs.service.factories.default.default_service_factory import DefaultServiceFactory
from ticket_docs.service.factories.service_factory import ServiceFactory
from ticket_docs.service.github.exceptions import SEBoardStatusUnknownError, SEGithubServiceError
from ticket_docs.storage.github.exceptions import SEGhError
from ticket_docs.storage.permits.exceptions import SESquashPermitStoreError


class TicketDocsCli(Runnable):
    """The ``ticket-docs`` command line: record runs, check and index ticket folders, archive, and answer the hooks.

    Attributes:
        USAGE_ERROR_EXIT_CODE (int): The exit code of a usage error.
        FAILURE_EXIT_CODE (int): The exit code of a failed command or of a check with problems.
        HOOKS (Tuple[TicketDocsCommand, ...]): The commands that answer a Claude Code hook.
        SETTINGS_ERRORS (Tuple[type[Exception], ...]): The errors of a catalogue that cannot be read.
        FAILURES (Tuple[type[Exception], ...]): The errors of git and GitHub reported as a failure.
        arguments (List[str]): The command line, without the program name.
        rules_file (Path): The folder rules catalogue.
        catalog_file (Path): The GitHub catalogue.
        stdin (TextIO): Where a hook's input is read.
        stdout (TextIO): Where results and a hook's answer go.
        stderr (TextIO): Where errors go.
        caller_cwd (Path): The folder ``ticket-docs`` was called from.
        confirmation (HumanConfirmation): The terminal of the person, which ``allow-squash`` requires.
        logger (Logger): Logger instance.
        options (Optional[argparse.Namespace]): The parsed command line.
        services (Optional[ServiceFactory]): The services, once the catalogues are read.
        exit_code (int): The exit code: the command's for ``record-run``, 1 for problems or failures, 2 for a usage
            error, always 0 for the hooks.

    Notes:
        - **The hooks never fail and never print logs**: an error of any kind ends them silently with exit code 0,
          because their standard output is Claude Code's answer.
        - Only this layer prints: the logs go to the harness log file.
    """

    USAGE_ERROR_EXIT_CODE: ClassVar[int] = 2
    FAILURE_EXIT_CODE: ClassVar[int] = 1
    HOOKS: ClassVar[Tuple[TicketDocsCommand, ...]] = (
        TicketDocsCommand.GIT_GATE,
        TicketDocsCommand.TIME_REMINDER,
        TicketDocsCommand.FILE_GATE,
    )
    SETTINGS_ERRORS: ClassVar[Tuple[type[Exception], ...]] = (
        SEYamlCatalogUnreadable,
        SEInvalidFolderRulesException,
        SEInvalidGithubCatalogException,
        SEInvalidBoardProjectException,
        SEInvalidBoardFieldException,
    )
    FAILURES: ClassVar[Tuple[type[Exception], ...]] = (
        SEGitError,
        SEGhError,
        SEGithubServiceError,
        SEInvalidActionsRunException,
        SESquashPermitStoreError,
    )

    def __init__(
        self,
        arguments: List[str],
        rules_file: Path,
        catalog_file: Path,
        stdin: TextIO,
        stdout: TextIO,
        stderr: TextIO,
        caller_cwd: Path,
        confirmation: HumanConfirmation,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the command line, the catalogues and the streams.

        Args:
            arguments (List[str]): The command line, without the program name.
            rules_file (Path): The folder rules catalogue.
            catalog_file (Path): The GitHub catalogue.
            stdin (TextIO): Where a hook's input is read.
            stdout (TextIO): Where results and a hook's answer go.
            stderr (TextIO): Where errors go.
            caller_cwd (Path): The folder ``ticket-docs`` was called from.
            confirmation (HumanConfirmation): The terminal of the person, which ``allow-squash`` requires.
            logger (Optional[Logger]): Logger instance.
        """
        self.arguments = arguments
        self.rules_file = rules_file
        self.catalog_file = catalog_file
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.caller_cwd = caller_cwd
        self.confirmation = confirmation
        self.logger = logger if logger else getLogger(__name__)
        self.options: Optional[argparse.Namespace] = None
        self.services: Optional[ServiceFactory] = None
        self.exit_code = 0

    ############################
    # Internal Helpers Methods #
    ############################

    def _fail(self, message: str, exit_code: int) -> None:
        """Report an error.

        Args:
            message (str): What went wrong.
            exit_code (int): The exit code to end with.
        """
        self.logger.warning("ticket-docs failed with exit code %d.", exit_code)
        print(f"ticket-docs: {message}", file=self.stderr)
        self.exit_code = exit_code

    def _hook(self, services: ServiceFactory, command: TicketDocsCommand) -> None:
        """Answer a hook: refuse a command before it runs, or add context after it ran.

        Args:
            services (ServiceFactory): The services.
            command (TicketDocsCommand): The hook's command.
        """
        payload = HookPayload.from_json(self.stdin.read())
        if payload is None:
            return
        cwd = payload.cwd or self.caller_cwd
        if command is TicketDocsCommand.GIT_GATE:
            reason = services.git_gate().refusal(payload.command, cwd)
            answer = {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": reason}
        else:
            reason = services.time_reminder().reminder(payload.command, cwd)
            answer = {"hookEventName": "PostToolUse", "additionalContext": reason}
        if reason is not None:
            print(json.dumps({"hookSpecificOutput": answer}), file=self.stdout)

    def _file_hook(self, services: ServiceFactory) -> None:
        """Answer the hook on the file tools: refuse a file in a folder of the guards' state.

        Args:
            services (ServiceFactory): The services.
        """
        payload = FileHookPayload.from_json(self.stdin.read())
        if payload is None:
            return
        reason = services.file_gate().refusal(payload.path, payload.cwd or self.caller_cwd)
        if reason is not None:
            answer = {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": reason}
            print(json.dumps({"hookSpecificOutput": answer}), file=self.stdout)

    def _record_run(self, services: ServiceFactory, options: argparse.Namespace) -> None:
        """Record a run.

        Args:
            services (ServiceFactory): The services.
            options (argparse.Namespace): The command line.
        """
        command = options.argv[1:] if options.argv[:1] == ["--"] else options.argv
        try:
            request = RunRequest.model_validate(
                {
                    "ticket": options.ticket,
                    "kind": options.kind,
                    "where": options.where,
                    "check": options.check,
                    "what": options.what,
                    "expectation": options.expect,
                    "command": command,
                    "run_id": options.run_id,
                }
            )
            recorder = services.run_recorder(request)
        except (SEInvalidRunRequestException, SEGitError) as error:
            self._fail(str(error), self.USAGE_ERROR_EXIT_CODE)
            return
        recorder.execute()
        print(recorder.verdict, file=self.stdout)
        self.exit_code = recorder.exit_code

    def _check(self, services: ServiceFactory, options: argparse.Namespace) -> None:
        """Check a ticket folder and print its problems.

        Args:
            services (ServiceFactory): The services.
            options (argparse.Namespace): The command line.
        """
        checker = services.ticket_checker(options.key, options.offline)
        checker.execute()
        for problem in checker.problems:
            print(problem, file=self.stdout)
        self.exit_code = self.FAILURE_EXIT_CODE if checker.problems else 0

    def _allow_squash(self, services: ServiceFactory, options: argparse.Namespace) -> None:
        """Grant the permit of the squash staged now, once the person at the terminal typed back the code shown.

        Args:
            services (ServiceFactory): The services.
            options (argparse.Namespace): The command line.
        """
        repository = GitRepository.discover(self.caller_cwd, self.logger)
        question = (
            f"Allow one squash commit of {options.key} on {repository.current_branch()} with the files staged now?"
        )
        if not self.confirmation.confirm(question):
            self._fail(
                "only the human, in their own terminal, can allow a squash. "  # noqa: E501
                "No terminal could be opened or the code shown there was not typed back, so no permit was written.",
                self.FAILURE_EXIT_CODE,
            )
            return
        permits = services.squash_permits()
        permit = permits.grant(options.key, repository)
        if permit is None:
            self._fail(
                f"the current branch does not carry {options.key}: no permit was written.", self.FAILURE_EXIT_CODE
            )
            return
        path = permits.store.path(permit.ticket)
        print(
            f"{path}: one squash commit of {permit.ticket} on {permit.branch} is allowed until "
            f"{permit.expires_at.astimezone():%H:%M}. Commit it now, without staging anything else.",
            file=self.stdout,
        )

    def _dispatch(self, services: ServiceFactory, options: argparse.Namespace) -> None:
        """Run one command.

        Args:
            services (ServiceFactory): The services.
            options (argparse.Namespace): The command line.
        """
        match TicketDocsCommand(options.command):
            case TicketDocsCommand.RECORD_RUN:
                self._record_run(services, options)
            case TicketDocsCommand.CHECK:
                self._check(services, options)
            case TicketDocsCommand.REPORT_INDEX:
                print(services.report_index().write(options.output), file=self.stdout)
            case TicketDocsCommand.HISTORY_BUNDLE:
                print(services.history_bundler().bundle(options.key), file=self.stdout)
            case TicketDocsCommand.ARCHIVE:
                archiver = services.evidence_archiver(options.dry_run)
                url = archiver.archive(options.key)
                print("\n".join(archiver.gh.planned) if options.dry_run else url, file=self.stdout)
            case TicketDocsCommand.BOARD:
                services.board_mover().move(options.key, options.status)
                print(f"{options.key} is {options.status} on the board.", file=self.stdout)
            case TicketDocsCommand.FILE_GATE:
                self._file_hook(services)
            case TicketDocsCommand.ALLOW_SQUASH:
                self._allow_squash(services, options)
            case TicketDocsCommand.GIT_GATE | TicketDocsCommand.TIME_REMINDER:
                self._hook(services, TicketDocsCommand(options.command))

    ############################
    # Publicly Exposed Methods #
    ############################

    def initialize(self) -> None:
        """Parse the command line, read the catalogues and build the services."""
        try:
            self.options = TicketDocsParser(self.logger).build().parse_args(self.arguments)
        except SystemExit as error:
            self.exit_code = error.code if isinstance(error.code, int) else self.USAGE_ERROR_EXIT_CODE
            self.logger.warning("ticket-docs was called with a command line it does not read.")
            return
        try:
            rules = FolderRules.load(self.rules_file)
            catalog = GithubCatalog.load(self.catalog_file)
        except self.SETTINGS_ERRORS as error:
            self.logger.error("The catalogues cannot be read: %s.", type(error).__name__)
            if TicketDocsCommand(self.options.command) not in self.HOOKS:
                self._fail(f"a catalogue of ticket-docs cannot be read: {error}", self.USAGE_ERROR_EXIT_CODE)
            return
        root = getattr(self.options, "root", None)
        self.services = DefaultServiceFactory(self.caller_cwd, root, rules, catalog, self.logger)
        self.logger.debug("ticket-docs %s is ready.", self.options.command)

    def run(self) -> None:
        """Run the command given on the command line."""
        if self.options is None or self.services is None:
            return
        command = TicketDocsCommand(self.options.command)
        if command in self.HOOKS:
            try:
                self._dispatch(self.services, self.options)
            except Exception as error:  # noqa: BLE001 - a hook must never break the tool call it answers
                self.logger.error("The %s hook failed and stays silent: %s.", command.value, type(error).__name__)
            self.exit_code = 0
            return
        try:
            self._dispatch(self.services, self.options)
        except SEBoardStatusUnknownError as error:
            self._fail(str(error), self.USAGE_ERROR_EXIT_CODE)
        except self.FAILURES as error:
            self._fail(str(error), self.FAILURE_EXIT_CODE)
        self.logger.info("ticket-docs %s ended with exit code %d.", command.value, self.exit_code)

    def close(self) -> None:
        """Release nothing: the command line holds no resource."""
        self.logger.debug("ticket-docs closed.")
