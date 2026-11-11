from __future__ import annotations

# Standard library imports
import argparse
import json
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, List, Optional, TextIO, Tuple

# Third-party imports
from pydantic import JsonValue

# First-party imports
from ai_cost.api.cli.ai_cost_parser import AiCostParser
from ai_cost.models.commands.exceptions import SEInvalidPaidCommandCatalogException, SEInvalidPaidCommandException
from ai_cost.models.enums import AiCostCommand, RunStatus
from ai_cost.models.ledger.exceptions import (
    SEInvalidCostRunException,
    SEInvalidLedgerException,
)
from ai_cost.models.pricing.exceptions import SEInvalidModelPriceException, SEInvalidPriceTableException
from ai_cost.models.settings.caller_environment import CallerEnvironment
from ai_cost.models.settings.exceptions import SEInvalidCallerEnvironmentException, SEInvalidGuardSettingsException
from ai_cost.models.settings.guard_settings import GuardSettings
from ai_cost.service.factories.default.default_service_factory import DefaultServiceFactory
from ai_cost.service.factories.service_factory import ServiceFactory
from ai_cost.service.ledgers.exceptions import SELedgerServiceError
from harness_core.lifecycle.runnable import Runnable
from harness_core.terminal.human_confirmation import HumanConfirmation


class AiCostCli(Runnable):
    """The ``ai-cost`` command line: run a paid test, report a ticket, charge, raise a cap, answer the hook.

    Attributes:
        USAGE_ERROR_EXIT_CODE (int): The exit code of a usage error.
        REFUSED_EXIT_CODE (int): The exit code of a cap raise refused because no human confirmed it.
        HOOK_EVENT (str): The hook the gate answers.
        DENY (str): The hook's refusal decision.
        USAGE_ERRORS (Tuple[type[Exception], ...]): The errors reported as a usage error.
        SETTINGS_ERRORS (Tuple[type[Exception], ...]): The errors of a settings or catalogue file.
        arguments (List[str]): The command line, without the program name.
        settings_file (Path): The versioned settings file.
        settings (Optional[GuardSettings]): The enforcing settings, read from ``settings_file`` when ``None``.
        environment (Optional[CallerEnvironment]): The caller's values, read from the environment when ``None``.
        stdin (TextIO): Where the hook's input is read.
        stdout (TextIO): Where results and the hook's answer go.
        stderr (TextIO): Where errors and run summaries go.
        confirmation (HumanConfirmation): The terminal of the person, which ``raise-cap`` requires.
        logger (Logger): Logger instance.
        options (Optional[argparse.Namespace]): The parsed command line.
        services (Optional[ServiceFactory]): The guard's services, once the settings are read.
        settings_error (Optional[str]): Why the settings could not be read.
        exit_code (int): The exit code: the test's own for ``run``, 3 when refused or killed, 2 on a usage error.

    Notes:
        - **``gate`` always exits 0** and prints the hook's JSON answer only when it refuses. When its settings or
          the paid command file cannot be read, it refuses, so that a broken install does not let paid tests through.
        - Only this layer prints: the logs go to the harness log file, never to the console.
        - **``raise-cap`` needs a person at the controlling terminal (``/dev/tty``) who types back the code shown
          there**, a barrier of its own besides the gate: Claude's Bash tool has no terminal, so the command exits 3
          there. It guards against mistakes, not against a deliberate forgery by a process of the same user.
    """

    USAGE_ERROR_EXIT_CODE: ClassVar[int] = 2
    REFUSED_EXIT_CODE: ClassVar[int] = 3
    HOOK_EVENT: ClassVar[str] = "PreToolUse"
    DENY: ClassVar[str] = "deny"
    USAGE_ERRORS: ClassVar[Tuple[type[Exception], ...]] = (
        SEInvalidLedgerException,
        SEInvalidCostRunException,
        SELedgerServiceError,
    )
    SETTINGS_ERRORS: ClassVar[Tuple[type[Exception], ...]] = (
        SEInvalidGuardSettingsException,
        SEInvalidCallerEnvironmentException,
        SEInvalidPaidCommandCatalogException,
        SEInvalidPaidCommandException,
        SEInvalidPriceTableException,
        SEInvalidModelPriceException,
    )

    def __init__(
        self,
        arguments: List[str],
        settings_file: Path,
        settings: Optional[GuardSettings],
        environment: Optional[CallerEnvironment],
        stdin: TextIO,
        stdout: TextIO,
        stderr: TextIO,
        confirmation: HumanConfirmation,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the command line and its streams.

        Args:
            arguments (List[str]): The command line, without the program name.
            settings_file (Path): The versioned settings file.
            settings (Optional[GuardSettings]): The enforcing settings, read from ``settings_file`` when ``None``.
            environment (Optional[CallerEnvironment]): The caller's values, read from the environment when ``None``.
            stdin (TextIO): Where the hook's input is read.
            stdout (TextIO): Where results and the hook's answer go.
            stderr (TextIO): Where errors and run summaries go.
            confirmation (HumanConfirmation): The terminal of the person, which ``raise-cap`` requires.
            logger (Optional[Logger]): Logger instance.
        """
        self.arguments = arguments
        self.settings_file = settings_file
        self.settings = settings
        self.environment = environment
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.confirmation = confirmation
        self.logger = logger if logger else getLogger(__name__)
        self.options: Optional[argparse.Namespace] = None
        self.services: Optional[ServiceFactory] = None
        self.settings_error: Optional[str] = None
        self.exit_code = 0

    ############################
    # Internal Helpers Methods #
    ############################

    def _fail(self, message: str) -> None:
        """Report a usage error.

        Args:
            message (str): What went wrong.
        """
        self.logger.warning("ai-cost usage error: %s", message)
        print(f"ai-cost: {message}", file=self.stderr)
        self.exit_code = self.USAGE_ERROR_EXIT_CODE

    def _refuse(self, message: str) -> None:
        """Refuse a cap raise no human confirmed.

        Args:
            message (str): Why it is refused.
        """
        self.logger.warning("ai-cost raise-cap refused: %s", message)
        print(f"ai-cost: {message}", file=self.stderr)
        self.exit_code = self.REFUSED_EXIT_CODE

    def _raise_cap(self, services: ServiceFactory, options: argparse.Namespace) -> None:
        """Raise a ticket's cap, once the person at the terminal typed back the code shown there.

        Args:
            services (ServiceFactory): The guard's services.
            options (argparse.Namespace): The command line.
        """
        if not self.confirmation.confirm(f"Raise the AI test cap of {options.ticket} to ${options.usd}?"):
            self._refuse(
                "Only the human, in their own terminal, can raise a ticket's cap. "  # noqa: E501
                "No terminal could be opened or the code shown there was not typed back, so the cap of "
                f"{options.ticket} is unchanged."
            )
            return
        ledger = services.ledger_service().raise_cap(options.ticket, options.usd)
        state = f"blocked: {ledger.block_reason}" if ledger.block_reason else "open"
        print(
            f"{ledger.ticket}: cap ${ledger.cap_usd:.2f}, ${ledger.spent_usd:.4f} spent, {state}.",
            file=self.stdout,
        )

    def _deny(self, reason: str) -> None:
        """Print the hook's refusal.

        Args:
            reason (str): Why the command must not run.
        """
        answer = {
            "hookSpecificOutput": {
                "hookEventName": self.HOOK_EVENT,
                "permissionDecision": self.DENY,
                "permissionDecisionReason": reason,
            }
        }
        print(json.dumps(answer), file=self.stdout)

    def _hook_command(self) -> Optional[str]:
        """Read the Bash command from the hook's input.

        Returns:
            Optional[str]: The command, ``None`` when the input holds none.
        """
        try:
            payload: JsonValue = json.loads(self.stdin.read() or "null")
        except ValueError:
            self.logger.warning("The hook's input is not JSON: nothing to decide.")
            return None
        tool_input = payload.get("tool_input") if isinstance(payload, dict) else None
        command = tool_input.get("command") if isinstance(tool_input, dict) else None
        return command if isinstance(command, str) and command.strip() else None

    def _gate(self, services: Optional[ServiceFactory]) -> None:
        """Answer the PreToolUse hook on Bash.

        Args:
            services (Optional[ServiceFactory]): The guard's services, ``None`` when the settings cannot be read.
        """
        command = self._hook_command()
        if command is None:
            return
        if services is None:
            self._deny(
                f"The AI test cost guard cannot read its settings: {self.settings_error} "  # noqa: E501
                "Fix .claude/skills/ai-test-cost/conf/settings.yaml before running commands."
            )
            return
        try:
            refusal = services.command_gate().refusal(command)
        except self.SETTINGS_ERRORS as error:
            self.logger.error("The gate cannot read its files: %s.", type(error).__name__)
            self._deny(f"The AI test cost guard cannot read its paid command file: {error}")
            return
        if refusal is not None:
            self._deny(refusal)

    def _run(self, services: ServiceFactory, options: argparse.Namespace) -> None:
        """Run a paid AI test through the guard.

        Args:
            services (ServiceFactory): The guard's services.
            options (argparse.Namespace): The command line.
        """
        command = options.argv[1:] if options.argv[:1] == ["--"] else options.argv
        if not command:
            self._fail("give the command after --.")
            return
        meter = services.usage_meter()
        if meter.measurable and not meter.ready() and not options.soft:
            self._fail(
                "ANTHROPIC_ADMIN_KEY is not set, so the run cannot be measured. "  # noqa: E501
                "Set it, or add --soft to charge the estimate and correct it later with ai-cost charge."
            )
            return
        guarded = services.guarded_run(
            options.ticket,
            options.label or " ".join(command),
            command,
            options.estimate_usd,
            options.soft,
            options.on_kill,
        )
        guarded.execute()
        result = guarded.result
        self.exit_code = guarded.exit_code
        if result is None:
            return
        ledger = services.ledger_service().ledger(options.ticket)
        note = f" ({result.note})" if result.note else ""
        print(
            f"ai-cost: run {result.id} {result.status.value}: ${result.cost_usd:.4f}, "
            f"{ledger.ticket} ${ledger.spent_usd:.4f} of ${ledger.cap_usd:.2f}{note}",
            file=self.stderr,
        )

    def _status(self, services: ServiceFactory, ticket: str) -> None:
        """Print a ticket's spend and runs, its ended runs settled first.

        Args:
            services (ServiceFactory): The guard's services.
            ticket (str): The ticket.
        """
        ledger = services.ledger_service().settle(ticket)
        blocked = f", blocked: {ledger.block_reason}" if ledger.block_reason else ""
        print(
            f"{ledger.ticket}: ${ledger.spent_usd:.4f} of ${ledger.cap_usd:.2f}, "
            f"${ledger.remaining_usd:.4f} left{blocked}",
            file=self.stdout,
        )
        for run in ledger.runs:
            final = "final" if run.settled or run.status == RunStatus.REFUSED else "not final"
            note = f" ({run.note})" if run.note else ""
            print(
                f"  {run.id} {run.status.value} {final} ${run.cost_usd:.4f} "
                f"(estimate ${run.estimate_usd:.2f}) {run.label}{note}",
                file=self.stdout,
            )

    def _dispatch(self, services: ServiceFactory, options: argparse.Namespace) -> None:
        """Run one command.

        Args:
            services (ServiceFactory): The guard's services.
            options (argparse.Namespace): The command line.
        """
        match AiCostCommand(options.command):
            case AiCostCommand.RUN:
                self._run(services, options)
            case AiCostCommand.STATUS:
                self._status(services, options.ticket)
            case AiCostCommand.REMAINING:
                print(f"{services.ledger_service().settle(options.ticket).remaining_usd:.4f}", file=self.stdout)
            case AiCostCommand.CHARGE:
                charge = services.ledger_service().charge(options.ticket, options.usd, options.label, options.note)
                print(f"Charged ${charge.cost_usd:.4f} to {options.ticket}.", file=self.stdout)
            case AiCostCommand.RAISE_CAP:
                self._raise_cap(services, options)
            case AiCostCommand.GATE:
                self._gate(services)

    ############################
    # Publicly Exposed Methods #
    ############################

    def initialize(self) -> None:
        """Parse the command line, read the settings and build the services."""
        try:
            self.options = AiCostParser(self.logger).build().parse_args(self.arguments)
        except SystemExit as error:
            self.exit_code = error.code if isinstance(error.code, int) else self.USAGE_ERROR_EXIT_CODE
            self.logger.warning("ai-cost was called with a command line it does not read.")
            return
        try:
            settings = self.settings if self.settings is not None else GuardSettings.load(self.settings_file)
            environment = self.environment if self.environment is not None else CallerEnvironment()
        except self.SETTINGS_ERRORS as error:
            self.settings_error = str(error)
            self.logger.error("The guard's settings cannot be read: %s.", type(error).__name__)
            return
        self.services = DefaultServiceFactory(settings, environment, self.logger)
        self.logger.debug("ai-cost %s is ready.", self.options.command)

    def run(self) -> None:
        """Run the command given on the command line."""
        if self.options is None:
            return
        if AiCostCommand(self.options.command) == AiCostCommand.GATE:
            self._gate(self.services)
            return
        if self.services is None:
            self._fail(f"the guard's settings cannot be read: {self.settings_error}")
            return
        try:
            self._dispatch(self.services, self.options)
        except self.USAGE_ERRORS as error:
            self._fail(str(error))
        except self.SETTINGS_ERRORS as error:
            self._fail(f"a file of the guard cannot be read: {error}")
        self.logger.info("ai-cost %s ended with exit code %d.", self.options.command, self.exit_code)

    def close(self) -> None:
        """Release nothing: the command line holds no resource."""
        self.logger.debug("ai-cost closed.")
