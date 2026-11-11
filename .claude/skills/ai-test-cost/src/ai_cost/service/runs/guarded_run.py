from __future__ import annotations

# Standard library imports
import os
import shlex
import signal
import subprocess
from datetime import datetime
from decimal import Decimal
from logging import Logger, getLogger
from typing import ClassVar, Dict, List, Optional, Tuple

# First-party imports
from ai_cost.models.enums import CostSource, RunStatus
from ai_cost.models.ledger.cost_run import CostRun
from ai_cost.models.settings.caller_environment import CallerEnvironment
from ai_cost.models.settings.guard_settings import GuardSettings
from ai_cost.service.ledgers.ledger_service import LedgerService
from ai_cost.service.usage.exceptions import SEUsageMeasureFailedError
from ai_cost.service.usage.usage_meter import UsageMeter
from harness_core.lifecycle.runnable import Runnable


class GuardedRun(Runnable):
    """Runs one paid AI test within its ticket's cap: refused when it cannot fit, killed when the cap is near.

    Attributes:
        REFUSED_EXIT_CODE (int): The exit code of a run refused or killed at the cap.
        NOT_STARTED_EXIT_CODE (int): The exit code of a command that could not start.
        INTERRUPTED_EXIT_CODE (int): The exit code of a run stopped by Ctrl-C.
        STOP_GRACE_S (int): Seconds a stopped run has to end before it is killed.
        ON_KILL_TIMEOUT_S (int): Seconds the stop command may take.
        RUN_ID_VARIABLE (str): The variable that gives the child its run id.
        TICKET_VARIABLE (str): The variable that gives the child its ticket.
        INTERRUPTED_NOTE (str): The note of a run stopped by Ctrl-C.
        FAILED_EXIT_CODE (int): The exit code of a run the guard stopped because it could not be measured.
        ticket (str): The ticket the cost is charged to.
        label (str): What the run tests.
        command (List[str]): The command and its arguments.
        estimate_usd (Decimal): What the run is expected to cost.
        soft (bool): Whether the run is charged its estimate instead of being measured.
        on_kill (Optional[str]): The command that stops what the run started elsewhere.
        settings (GuardSettings): The enforcing settings.
        environment (CallerEnvironment): The caller's folder.
        ledgers (LedgerService): The ledgers.
        meter (UsageMeter): Measures the run.
        logger (Logger): Logger instance.
        process (Optional[subprocess.Popen[bytes]]): The running command.
        result (Optional[CostRun]): The run as recorded, once refused or ended.
        exit_code (int): The command's exit code, 3 when refused or killed at the cap.

    Notes:
        - The command runs in its own session, so the whole process group is killed at the cap, children
          included.
        - **The child gets ``AI_COST_RUN_ID`` and ``AI_COST_TICKET``**, so that a test marked ``llm`` can refuse to
          run outside the guard.
        - A run that cannot be measured ``max_unmeasured`` times in a row is stopped: the cap cannot be enforced
          blind.
    """

    REFUSED_EXIT_CODE: ClassVar[int] = 3
    NOT_STARTED_EXIT_CODE: ClassVar[int] = 127
    INTERRUPTED_EXIT_CODE: ClassVar[int] = 130
    STOP_GRACE_S: ClassVar[int] = 15
    ON_KILL_TIMEOUT_S: ClassVar[int] = 120
    RUN_ID_VARIABLE: ClassVar[str] = "AI_COST_RUN_ID"
    INTERRUPTED_NOTE: ClassVar[str] = "interrupted by hand"
    FAILED_EXIT_CODE: ClassVar[int] = 1
    TICKET_VARIABLE: ClassVar[str] = "AI_COST_TICKET"

    def __init__(
        self,
        ticket: str,
        label: str,
        command: List[str],
        estimate_usd: Decimal,
        soft: bool,
        on_kill: Optional[str],
        settings: GuardSettings,
        environment: CallerEnvironment,
        ledgers: LedgerService,
        meter: UsageMeter,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the run.

        Args:
            ticket (str): The ticket the cost is charged to.
            label (str): What the run tests.
            command (List[str]): The command and its arguments.
            estimate_usd (Decimal): What the run is expected to cost.
            soft (bool): Whether the run is charged its estimate instead of being measured.
            on_kill (Optional[str]): The command that stops what the run started elsewhere.
            settings (GuardSettings): The enforcing settings.
            environment (CallerEnvironment): The caller's folder.
            ledgers (LedgerService): The ledgers.
            meter (UsageMeter): Measures the run.
            logger (Optional[Logger]): Logger instance.
        """
        self.ticket = ticket
        self.label = label
        self.command = command
        self.estimate_usd = estimate_usd
        self.soft = soft
        self.on_kill = on_kill
        self.settings = settings
        self.environment = environment
        self.ledgers = ledgers
        self.meter = meter
        self.logger = logger if logger else getLogger(__name__)
        self.process: Optional[subprocess.Popen[bytes]] = None
        self.result: Optional[CostRun] = None
        self.exit_code = 0

    ############################
    # Internal Helpers Methods #
    ############################

    def _now(self) -> datetime:
        """Give the current local time, with its time zone."""
        return datetime.now().astimezone()

    def _measure(self, run: CostRun) -> CostRun:
        """Measure a run from its start until now.

        Args:
            run (CostRun): The run.

        Returns:
            CostRun: The run with its usage and cost.

        Raises:
            SEUsageMeasureFailedError: When the measure fails.
        """
        usage = self.meter.measure(run.started_on, self._now())
        cost = sum((model.cost_usd for model in usage.values()), Decimal("0"))
        return run.model_copy(update={"usage": usage, "cost_usd": cost})

    def _stop(self, process: subprocess.Popen[bytes], on_kill: Optional[str]) -> None:
        """Stop the run's whole process group, then run its stop command.

        Args:
            process (subprocess.Popen[bytes]): The run.
            on_kill (Optional[str]): The command that stops what the run started elsewhere.
        """
        self.logger.warning("Stopping the process group %d of %s.", process.pid, self.ticket)
        try:
            os.killpg(process.pid, signal.SIGTERM)
            process.wait(timeout=self.STOP_GRACE_S)
        except subprocess.TimeoutExpired:
            self.logger.warning("Process group %d still running after %d s: killed.", process.pid, self.STOP_GRACE_S)
            os.killpg(process.pid, signal.SIGKILL)
            process.wait()
        except ProcessLookupError:
            self.logger.debug("Process group %d had already ended.", process.pid)
        if on_kill:
            try:
                done = subprocess.run(
                    shlex.split(on_kill), capture_output=True, text=True, timeout=self.ON_KILL_TIMEOUT_S, check=False
                )
            except (OSError, ValueError, subprocess.TimeoutExpired) as error:
                self.logger.error("The stop command %r failed: %s.", on_kill, type(error).__name__)
                return
            self.logger.warning("The stop command %r exited with %d.", on_kill, done.returncode)

    def _watch(
        self, run: CostRun, process: subprocess.Popen[bytes]
    ) -> Tuple[CostRun, Optional[RunStatus], Optional[str]]:
        """Measure a running test until it ends, and stop it at the kill threshold.

        Args:
            run (CostRun): The run.
            process (subprocess.Popen[bytes]): Its process.

        Returns:
            Tuple[CostRun, Optional[RunStatus], Optional[str]]: The run, its status when it was stopped (``None``
            when it ended by itself) and why it was stopped.
        """
        failures = 0
        while True:
            try:
                process.wait(timeout=self.settings.poll_interval_s)
                return run, None, None
            except subprocess.TimeoutExpired:
                self.logger.debug("Run %s still running.", run.id)
            except KeyboardInterrupt:
                self._stop(process, None)
                return run, RunStatus.FAILED, self.INTERRUPTED_NOTE
            if run.source != CostSource.USAGE_REPORT:
                continue
            try:
                run = self._measure(run)
            except SEUsageMeasureFailedError as error:
                failures += 1
                self.logger.warning("Run %s: measure %d failed: %s", run.id, failures, error)
                if failures >= self.settings.max_unmeasured:
                    self._stop(process, self.on_kill)
                    return run, RunStatus.FAILED, f"stopped: its cost could not be measured {failures} times in a row"
                continue
            failures = 0
            ledger = self.ledgers.record(self.ticket, run)
            self.logger.info(
                "Run %s: $%s so far, $%s of $%s spent.", run.id, run.cost_usd, ledger.spent_usd, ledger.cap_usd
            )
            if ledger.spent_usd >= self.settings.kill_ratio * ledger.cap_usd:
                self._stop(process, self.on_kill)
                reason = (
                    f"killed at ${ledger.spent_usd:.2f}, {self.settings.kill_ratio * 100:.0f} % "
                    f"of the ${ledger.cap_usd:.2f} cap"
                )
                return run, RunStatus.KILLED_AT_CAP, reason

    def _finish(
        self, run: CostRun, process: subprocess.Popen[bytes], status: Optional[RunStatus], reason: Optional[str]
    ) -> CostRun:
        """Record a run's end.

        Args:
            run (CostRun): The run.
            process (subprocess.Popen[bytes]): Its ended process.
            status (Optional[RunStatus]): Its status when it was stopped, ``None`` when it ended by itself.
            reason (Optional[str]): Why it was stopped.

        Returns:
            CostRun: The run as recorded.
        """
        code = process.returncode
        if run.source == CostSource.USAGE_REPORT:
            try:
                run = self._measure(run)
            except SEUsageMeasureFailedError as error:
                self.logger.warning("Run %s: the last measure failed, the run settles later: %s", run.id, error)
        else:
            run = run.model_copy(update={"cost_usd": run.estimate_usd, "settled": True})
        final = status or (RunStatus.DONE if code == 0 else RunStatus.FAILED)
        run = run.model_copy(update={"finished_on": self._now(), "exit_code": code, "status": final, "note": reason})
        ledger = self.ledgers.record(self.ticket, run, reason if final == RunStatus.KILLED_AT_CAP else None)
        self.logger.info(
            "Run %s %s: $%s, $%s of $%s spent.", run.id, final, run.cost_usd, ledger.spent_usd, ledger.cap_usd
        )
        return run

    def _child_environment(self, run: CostRun) -> Dict[str, str]:
        """Give the child the caller's environment plus its run id and ticket.

        Args:
            run (CostRun): The run.

        Returns:
            Dict[str, str]: The child's environment.
        """
        return {**os.environ, self.RUN_ID_VARIABLE: run.id, self.TICKET_VARIABLE: self.ticket}

    ############################
    # Publicly Exposed Methods #
    ############################

    def initialize(self) -> None:
        """Admit the run, or record it as refused."""
        soft = self.soft or not self.meter.measurable
        source = CostSource.ESTIMATE if soft else CostSource.USAGE_REPORT
        run = self.ledgers.new_run(self.ticket, self.label, shlex.join(self.command), self.estimate_usd, source)
        self.result = self.ledgers.admit(self.ticket, run)
        if self.result.status == RunStatus.REFUSED:
            self.exit_code = self.REFUSED_EXIT_CODE
            self.logger.warning("Run %s of %s refused: %s.", run.id, self.ticket, self.result.note)

    def run(self) -> None:
        """Run the command, measure it while it runs, and record its end."""
        run = self.result
        if run is None or run.status != RunStatus.RUNNING:
            return
        try:
            self.process = subprocess.Popen(
                self.command, cwd=self.environment.caller_cwd, env=self._child_environment(run), start_new_session=True
            )
        except OSError as error:
            self.logger.error("Run %s could not start: %s.", run.id, type(error).__name__)
            failed = run.model_copy(
                update={
                    "status": RunStatus.FAILED,
                    "note": f"could not start: {type(error).__name__}: {error}",
                    "finished_on": self._now(),
                    "settled": True,
                }
            )
            self.ledgers.record(self.ticket, failed)
            self.result = failed
            self.exit_code = self.NOT_STARTED_EXIT_CODE
            return
        self.logger.info("Started run %s of %s: process %d.", run.id, self.ticket, self.process.pid)
        run, status, reason = self._watch(run, self.process)
        self.result = self._finish(run, self.process, status, reason)
        match self.result.status:
            case RunStatus.KILLED_AT_CAP:
                self.exit_code = self.REFUSED_EXIT_CODE
            case RunStatus.FAILED if status is not None:
                self.exit_code = (
                    self.INTERRUPTED_EXIT_CODE if reason == self.INTERRUPTED_NOTE else self.FAILED_EXIT_CODE
                )
            case _:
                self.exit_code = self.process.returncode

    def close(self) -> None:
        """Stop the command if it still runs, when the run ended on an error."""
        if self.process is not None and self.process.poll() is None:
            self.logger.error("Run of %s left running after an error: stopping it.", self.ticket)
            self._stop(self.process, self.on_kill)
