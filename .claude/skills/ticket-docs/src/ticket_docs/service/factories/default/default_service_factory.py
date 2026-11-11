from __future__ import annotations

# Standard library imports
import tempfile
from logging import Logger
from pathlib import Path
from typing import ClassVar, Optional

# First-party imports
from harness_core.git.exceptions import SEGitError
from harness_core.git.git_repository import GitRepository
from harness_core.shell.shell_command_splitter import ShellCommandSplitter
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.models.evidence.run_request import RunRequest
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.checks.doc1.doc1_check import Doc1Check
from ticket_docs.service.checks.evidence.audit_check import AuditCheck
from ticket_docs.service.checks.evidence.claims_check import ClaimsCheck
from ticket_docs.service.checks.evidence.readme_fields_check import ReadmeFieldsCheck
from ticket_docs.service.checks.evidence.reports_check import ReportsCheck
from ticket_docs.service.checks.evidence.tdd_check import TddCheck
from ticket_docs.service.checks.folder.content_check import ContentCheck
from ticket_docs.service.checks.folder.evidence_index_check import EvidenceIndexCheck
from ticket_docs.service.checks.folder.required_files_check import RequiredFilesCheck
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.progress.handover_check import HandoverCheck
from ticket_docs.service.checks.progress.progress_table_check import ProgressTableCheck
from ticket_docs.service.checks.progress.pull_request_check import PullRequestCheck
from ticket_docs.service.checks.progress.stage_check import StageCheck
from ticket_docs.service.checks.progress.status_file_check import StatusFileCheck
from ticket_docs.service.checks.ticket_checker import TicketChecker
from ticket_docs.service.checks.ticket_folder import TicketFolder
from ticket_docs.service.factories.service_factory import ServiceFactory
from ticket_docs.service.github.board_mover import BoardMover
from ticket_docs.service.github.evidence_archiver import EvidenceArchiver
from ticket_docs.service.history.history_bundler import HistoryBundler
from ticket_docs.service.hooks.file_gate import FileGate
from ticket_docs.service.hooks.git_gate import GitGate
from ticket_docs.service.hooks.git_invocations import GitInvocations
from ticket_docs.service.hooks.time_reminder import TimeReminder
from ticket_docs.service.index.report_index import ReportIndex
from ticket_docs.service.paths.code_paths import CodePaths
from ticket_docs.service.paths.tickets_root import TicketsRoot
from ticket_docs.service.permits.squash_permits import SquashPermits
from ticket_docs.service.runs.command_shape import CommandShape
from ticket_docs.service.runs.readme_renderer import ReadmeRenderer
from ticket_docs.service.runs.run_recorder import RunRecorder
from ticket_docs.storage.evidence.evidence_repository import EvidenceRepository
from ticket_docs.storage.evidence.report_reader import ReportReader
from ticket_docs.storage.github.gh_client import GhClient
from ticket_docs.storage.processes.command_runner import CommandRunner
from ticket_docs.storage.tickets.ticket_repository import TicketRepository


class DefaultServiceFactory(ServiceFactory):
    """Builds the services from the caller's folder, its repository and the skill's catalogues.

    Attributes:
        RULES_FILE (Path): The ticket documentation rules, relative to the repository root, for DOC-1.
        SCRATCH_PREFIX (str): The prefix of the temporary folder an archive is zipped in.
        caller_cwd (Path): The folder ``ticket-docs`` was called from.
        root (Optional[Path]): The tickets folder given with ``--root``, found from the repository when ``None``.
        rules (FolderRules): What a ticket folder holds.
        catalog (GithubCatalog): Where simple-erp lives on GitHub.
        logger (Logger): Logger instance.

    Notes:
        - The repository is read only when a service needs it, so the hooks start fast and ``check --root`` works
          from any folder.
        - The ticket checker reads commits in the repository that holds the tickets folder.
    """

    RULES_FILE: ClassVar[Path] = Path(".claude") / "rules" / "ticket-documentation.md"
    SCRATCH_PREFIX: ClassVar[str] = "ticket-docs-"

    def __init__(
        self,
        caller_cwd: Path,
        root: Optional[Path],
        rules: FolderRules,
        catalog: GithubCatalog,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the caller's folder and the catalogues.

        Args:
            caller_cwd (Path): The folder ``ticket-docs`` was called from.
            root (Optional[Path]): The tickets folder given with ``--root``, found from the repository when ``None``.
            rules (FolderRules): What a ticket folder holds.
            catalog (GithubCatalog): Where simple-erp lives on GitHub.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.caller_cwd = caller_cwd
        self.root = root
        self.rules = rules
        self.catalog = catalog

    ############################
    # Internal Helpers Methods #
    ############################

    def _repository(self) -> GitRepository:
        """Find the caller's repository.

        Returns:
            GitRepository: The repository at the caller folder's top level.

        Raises:
            SEGitCommandFailedError: When the caller's folder is not in a repository.
        """
        return GitRepository.discover(self.caller_cwd, self.logger)

    def _gh(self, dry_run: bool = False) -> GhClient:
        """Build the gh client of the repository.

        Args:
            dry_run (bool): Whether to list the commands instead of running them.

        Returns:
            GhClient: The client.
        """
        return GhClient(self.catalog.full_name, dry_run=dry_run, logger=self.logger)

    def _invocations(self) -> GitInvocations:
        """Build the reader of git commands.

        Returns:
            GitInvocations: The reader.
        """
        return GitInvocations(ShellCommandSplitter(self.logger), self.logger)

    ############################
    # Publicly Exposed Methods #
    ############################

    def tickets_root(self) -> Path:
        """Give the ``docs/tickets`` folder: the ``--root`` one, else the caller's repository's.

        Returns:
            Path: The tickets folder.
        """
        return self.root if self.root is not None else TicketsRoot(self.logger).of(self._repository())

    def run_recorder(self, request: RunRequest) -> RunRecorder:
        """Build the recorder of one run.

        Args:
            request (RunRequest): What to record.

        Returns:
            RunRecorder: The recorder, not run yet.
        """
        return RunRecorder(
            request,
            self._repository(),
            self.caller_cwd,
            EvidenceRepository(self.tickets_root(), self.logger),
            CommandRunner(self.logger),
            ReportReader(self.logger),
            self._gh(),
            CommandShape(self.logger, ShellCommandSplitter(self.logger)),
            ReadmeRenderer(self.logger),
            self.logger,
        )

    def ticket_checker(self, key: str, offline: bool) -> TicketChecker:
        """Build the checker of one ticket folder.

        Args:
            key (str): The ticket.
            offline (bool): Whether to leave GitHub out.

        Returns:
            TicketChecker: The checker, not run yet.
        """
        root = self.tickets_root()
        tables = MarkdownTables(self.logger)
        evidence = EvidenceRepository(root, self.logger)
        tickets = TicketRepository(root, self.logger)
        try:
            repository: Optional[GitRepository] = GitRepository.discover(root if root.is_dir() else self.caller_cwd)
        except SEGitError:
            self.logger.warning("The tickets folder is not in a repository: the TDD commits are not checked.")
            repository = None
        checks = [
            RequiredFilesCheck(self.rules, self.logger),
            ContentCheck(self.rules, tables, self.logger),
            EvidenceIndexCheck(self.logger),
            ProgressTableCheck(self.rules, tables, self.logger),
            StageCheck(self.rules, tables, self.logger),
            PullRequestCheck(self.catalog, tables, self.logger),
            HandoverCheck(tables, self.logger),
            StatusFileCheck(self.rules, tables, self.logger),
            ReadmeFieldsCheck(self.logger),
            ClaimsCheck(self.rules, tables, self.logger),
            ReportsCheck(
                ReportIndex(evidence, tickets, self.logger),
                tickets,
                evidence,
                self._gh(),
                self.catalog,
                offline,
                self.logger,
            ),
            TddCheck(repository, CodePaths(self.rules, self.logger), tables, self.logger),
            AuditCheck(tables, self.logger),
            Doc1Check(root.parent.parent / self.RULES_FILE, CommandRunner(self.logger), self.logger),
        ]
        folder = TicketFolder(key, tickets, evidence, tables, self.logger)
        return TicketChecker(folder, checks, self.logger)

    def report_index(self) -> ReportIndex:
        """Build the evidence index.

        Returns:
            ReportIndex: The index.
        """
        root = self.tickets_root()
        return ReportIndex(EvidenceRepository(root, self.logger), TicketRepository(root, self.logger), self.logger)

    def history_bundler(self) -> HistoryBundler:
        """Build the history bundler.

        Returns:
            HistoryBundler: The bundler.
        """
        evidence = EvidenceRepository(self.tickets_root(), self.logger)
        return HistoryBundler(self._repository(), evidence, self.catalog, self.logger)

    def evidence_archiver(self, dry_run: bool) -> EvidenceArchiver:
        """Build the archiver, zipping into a new temporary folder.

        Args:
            dry_run (bool): Whether to list the gh commands instead of running them.

        Returns:
            EvidenceArchiver: The archiver.
        """
        scratch = Path(tempfile.mkdtemp(prefix=self.SCRATCH_PREFIX))
        tickets = TicketRepository(self.tickets_root(), self.logger)
        return EvidenceArchiver(tickets, self._gh(dry_run), self.catalog, self._repository(), scratch, self.logger)

    def board_mover(self) -> BoardMover:
        """Build the board mover.

        Returns:
            BoardMover: The mover.
        """
        return BoardMover(self._gh(), self.catalog, self.logger)

    def git_gate(self) -> GitGate:
        """Build the gate of the ``PreToolUse`` hook.

        Returns:
            GitGate: The gate.
        """
        paths = CodePaths(self.rules, self.logger)
        return GitGate(self._invocations(), paths, TicketsRoot(self.logger), self.catalog, self.logger)

    def time_reminder(self) -> TimeReminder:
        """Build the reminder of the ``PostToolUse`` hook.

        Returns:
            TimeReminder: The reminder.
        """
        return TimeReminder(self._invocations(), TicketsRoot(self.logger), self.logger)

    def squash_permits(self) -> SquashPermits:
        """Build the squash permits of the person's home folder.

        Returns:
            SquashPermits: The permits, lasting as ``folder-rules.yaml`` says.
        """
        return SquashPermits.default(self.rules, self.logger)

    def file_gate(self) -> FileGate:
        """Build the gate of the ``PreToolUse`` hook on the file tools.

        Returns:
            FileGate: The gate.
        """
        return FileGate(self.rules, self.logger)
