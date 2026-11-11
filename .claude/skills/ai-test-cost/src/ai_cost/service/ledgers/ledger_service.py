from __future__ import annotations

# Standard library imports
from datetime import datetime, timedelta
from decimal import Decimal
from logging import Logger, getLogger
from typing import ClassVar, Optional
from uuid import uuid4

# First-party imports
from ai_cost.models.enums import CostSource, RunStatus
from ai_cost.models.ledger.cost_run import CostRun
from ai_cost.models.ledger.ledger import Ledger
from ai_cost.models.settings.guard_settings import GuardSettings
from ai_cost.service.ledgers.exceptions import SELedgerReadFailedError
from ai_cost.service.reports.cost_report import CostReport
from ai_cost.service.usage.exceptions import SEUsageMeasureFailedError
from ai_cost.service.usage.usage_meter import UsageMeter
from ai_cost.storage.ledgers.exceptions import SELedgerStoreError
from ai_cost.storage.ledgers.ledger_repository import LedgerRepository
from ai_cost.storage.reports.cost_file_repository import CostFileRepository


class LedgerService:
    """Everything the guard does with a ticket's ledger: admit, record, settle, charge and raise the cap.

    Attributes:
        MARGIN_S (int): Seconds after a run's end whose usage still counts as the run's.
        settings (GuardSettings): The enforcing settings.
        repository (LedgerRepository): Where the ledgers are kept.
        cost_files (CostFileRepository): Where each ticket's ``COST.md`` is written.
        meter (UsageMeter): Measures an ended run again when it settles.
        report (CostReport): Writes the text of a ``COST.md``.
        price_source (str): Where the prices come from, for ``COST.md``.
        logger (Logger): Logger instance.

    Notes:
        - Every change happens under the ticket's lock, on the ledger read again under that lock.
        - Every save rewrites the ticket's ``COST.md``, so the evidence never lags behind the ledger.
        - A run's measured cost is final only ``settle_s`` after its end, because the usage report lags.
    """

    MARGIN_S: ClassVar[int] = 60

    def __init__(
        self,
        settings: GuardSettings,
        repository: LedgerRepository,
        cost_files: CostFileRepository,
        meter: UsageMeter,
        report: CostReport,
        price_source: str,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the settings, the stores, the meter and the report.

        Args:
            settings (GuardSettings): The enforcing settings.
            repository (LedgerRepository): Where the ledgers are kept.
            cost_files (CostFileRepository): Where each ticket's ``COST.md`` is written.
            meter (UsageMeter): Measures an ended run again when it settles.
            report (CostReport): Writes the text of a ``COST.md``.
            price_source (str): Where the prices come from, for ``COST.md``.
            logger (Optional[Logger]): Logger instance.
        """
        self.settings = settings
        self.repository = repository
        self.cost_files = cost_files
        self.meter = meter
        self.report = report
        self.price_source = price_source
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _now(self) -> datetime:
        """Give the current local time, with its time zone."""
        return datetime.now().astimezone()

    def _checked(self, ticket: str) -> str:
        """Check a ticket key before it names a lock or a file.

        Args:
            ticket (str): The ticket.

        Returns:
            str: The ticket key, stripped.

        Raises:
            SELedgerInvalidTicket: When the key is not a ticket.
        """
        return Ledger(ticket=ticket, cap_usd=self.settings.default_cap_usd).ticket

    def _load(self, ticket: str) -> Ledger:
        """Read a ticket's ledger, or start one with the default cap.

        Args:
            ticket (str): The ticket.

        Returns:
            Ledger: The ledger.

        Raises:
            SELedgerInvalidTicket: When the key is not a ticket.
            SELedgerReadFailedError: When the ledger file cannot be read.
        """
        empty = Ledger(ticket=self._checked(ticket), cap_usd=self.settings.default_cap_usd)
        try:
            ledger = self.repository.read(empty.ticket)
        except SELedgerStoreError as error:
            self.logger.error("The ledger of %s cannot be read.", ticket)
            raise SELedgerReadFailedError(
                f"The ledger of {ticket} cannot be read. "  # noqa: E501
                f"{error}"
            ) from error
        return ledger if ledger is not None else empty

    def _save(self, ledger: Ledger) -> Ledger:
        """Write a ledger and its ``COST.md``. The caller holds the ticket's lock.

        Args:
            ledger (Ledger): The ledger.

        Returns:
            Ledger: The same ledger.
        """
        self.repository.save(ledger)
        content = self.report.render(ledger, self.cost_files.template(), self.price_source)
        if self.cost_files.write(ledger.ticket, content) is None:
            self.logger.warning("The COST.md of %s was not written: the ledger still holds every run.", ledger.ticket)
        return ledger

    def _with_run(self, ledger: Ledger, run: CostRun) -> Ledger:
        """Put a run in a ledger, replacing the run of the same id.

        Args:
            ledger (Ledger): The ledger.
            run (CostRun): The run.

        Returns:
            Ledger: A new ledger holding the run.
        """
        runs = [run if known.id == run.id else known for known in ledger.runs]
        if all(known.id != run.id for known in ledger.runs):
            runs.append(run)
        return ledger.model_copy(update={"runs": runs})

    def _settle(self, ledger: Ledger) -> Ledger:
        """Measure again the ended runs whose usage has all arrived, and block a ticket that reached its cap.

        Args:
            ledger (Ledger): The ledger. The caller holds the ticket's lock.

        Returns:
            Ledger: The ledger, saved when it changed.
        """
        limit = self._now() - timedelta(seconds=self.settings.settle_s)
        changed = False
        for run in ledger.runs:
            if run.settled or run.finished_on is None or run.finished_on > limit:
                continue
            if run.source != CostSource.USAGE_REPORT:
                continue
            end = run.finished_on + timedelta(seconds=self.MARGIN_S)
            try:
                usage = self.meter.measure(run.started_on, end)
            except SEUsageMeasureFailedError as error:
                self.logger.warning("Run %s of %s not settled yet: %s", run.id, ledger.ticket, error)
                continue
            cost = sum((model.cost_usd for model in usage.values()), Decimal("0"))
            ledger = self._with_run(ledger, run.model_copy(update={"usage": usage, "cost_usd": cost, "settled": True}))
            changed = True
            self.logger.info("Settled run %s of %s at $%s.", run.id, ledger.ticket, cost)
        if ledger.block_reason is None and ledger.spent_usd >= ledger.cap_usd:
            reason = f"${ledger.spent_usd:.2f} spent, the ${ledger.cap_usd:.2f} cap is reached"
            ledger = ledger.model_copy(update={"block_reason": reason})
            changed = True
            self.logger.warning("Blocked %s: %s.", ledger.ticket, reason)
        return self._save(ledger) if changed else ledger

    ############################
    # Publicly Exposed Methods #
    ############################

    def ledger(self, ticket: str) -> Ledger:
        """Read a ticket's ledger without changing it.

        Args:
            ticket (str): The ticket.

        Returns:
            Ledger: The ledger, a new one with the default cap when the ticket has none yet.
        """
        return self._load(ticket)

    def new_run(self, ticket: str, label: str, command: str, estimate_usd: Decimal, source: CostSource) -> CostRun:
        """Start the record of a run, not saved yet.

        Args:
            ticket (str): The ticket.
            label (str): What the run tests.
            command (str): The command run.
            estimate_usd (Decimal): What the run is expected to cost.
            source (CostSource): Where its cost will come from.

        Returns:
            CostRun: A running run, identified by its start and a random suffix.
        """
        started = self._now()
        run = CostRun(
            id=f"{started:%Y%m%d-%H%M%S}-{uuid4().hex[:6]}",
            label=label,
            command=command,
            started_on=started,
            estimate_usd=estimate_usd,
            status=RunStatus.RUNNING,
            source=source,
        )
        self.logger.debug("New run %s for %s.", run.id, ticket)
        return run

    def settle(self, ticket: str) -> Ledger:
        """Settle the ended runs of a ticket.

        Args:
            ticket (str): The ticket.

        Returns:
            Ledger: The ledger.
        """
        with self.repository.lock(self._checked(ticket)):
            return self._settle(self._load(ticket))

    def admit(self, ticket: str, run: CostRun) -> CostRun:
        """Record a run that may start, or refuse it.

        Args:
            ticket (str): The ticket.
            run (CostRun): The running run.

        Returns:
            CostRun: The run recorded as running, or refused with the reason in its note.

        Notes:
            A run is refused when the ticket is blocked or when its estimate is above what the ticket has left.
        """
        with self.repository.lock(self._checked(ticket)):
            ledger = self._settle(self._load(ticket))
            refusal: Optional[str] = None
            if ledger.block_reason is not None:
                refusal = f"the ticket is blocked: {ledger.block_reason}. Only the human raises the cap"
            elif run.estimate_usd > ledger.remaining_usd:
                refusal = (
                    f"the ${run.estimate_usd:.2f} estimate is above the ${ledger.remaining_usd:.2f} left "
                    f"of the ${ledger.cap_usd:.2f} cap"
                )
            if refusal is not None:
                refused = run.model_copy(
                    update={
                        "status": RunStatus.REFUSED,
                        "note": refusal,
                        "finished_on": run.started_on,
                        "settled": True,
                    }
                )
                self._save(self._with_run(ledger, refused))
                self.logger.warning("Refused run %s of %s: %s.", run.id, ledger.ticket, refusal)
                return refused
            self._save(self._with_run(ledger, run))
            self.logger.info("Admitted run %s of %s, estimated at $%s.", run.id, ledger.ticket, run.estimate_usd)
            return run

    def record(self, ticket: str, run: CostRun, block_reason: Optional[str] = None) -> Ledger:
        """Record a run's progress or end, and block the ticket when asked.

        Args:
            ticket (str): The ticket.
            run (CostRun): The run.
            block_reason (Optional[str]): Why the ticket must be blocked, ``None`` to leave it as it is.

        Returns:
            Ledger: The ledger saved.
        """
        with self.repository.lock(self._checked(ticket)):
            ledger = self._with_run(self._load(ticket), run)
            if block_reason is not None:
                ledger = ledger.model_copy(update={"block_reason": block_reason})
                self.logger.warning("Blocked %s: %s.", ledger.ticket, block_reason)
            self.logger.debug("Recorded run %s of %s: %s, $%s.", run.id, ledger.ticket, run.status, run.cost_usd)
            return self._save(ledger)

    def charge(self, ticket: str, cost_usd: Decimal, label: str, note: Optional[str]) -> CostRun:
        """Charge a cost measured elsewhere to a ticket.

        Args:
            ticket (str): The ticket.
            cost_usd (Decimal): The cost, in USD.
            label (str): What it was.
            note (Optional[str]): Where the figure comes from.

        Returns:
            CostRun: The charge, recorded and settled.
        """
        now = self._now()
        charge = CostRun(
            id=f"{now:%Y%m%d-%H%M%S}-{uuid4().hex[:6]}-charge",
            label=label,
            command="charged by hand",
            started_on=now,
            finished_on=now,
            estimate_usd=cost_usd,
            cost_usd=cost_usd,
            status=RunStatus.DONE,
            source=CostSource.CHARGED,
            settled=True,
            note=note,
        )
        with self.repository.lock(self._checked(ticket)):
            self._settle(self._save(self._with_run(self._load(ticket), charge)))
        self.logger.info("Charged $%s to %s: %s.", cost_usd, ticket, label)
        return charge

    def raise_cap(self, ticket: str, cap_usd: Decimal) -> Ledger:
        """Set a ticket's cap, and unblock it when the new cap leaves room below the kill threshold.

        Args:
            ticket (str): The ticket.
            cap_usd (Decimal): The new cap, in USD.

        Returns:
            Ledger: The ledger saved.
        """
        with self.repository.lock(self._checked(ticket)):
            ledger = self._load(ticket)
            room = ledger.spent_usd < self.settings.kill_ratio * cap_usd
            reason = None if room else ledger.block_reason
            updated = Ledger(ticket=ledger.ticket, cap_usd=cap_usd, block_reason=reason, runs=ledger.runs)
            self.logger.info(
                "Set the cap of %s to $%s, %s.",
                ticket,
                cap_usd,
                "open" if updated.block_reason is None else "still blocked",
            )
            return self._save(updated)
