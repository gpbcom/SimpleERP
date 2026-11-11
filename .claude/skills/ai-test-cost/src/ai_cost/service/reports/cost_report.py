from __future__ import annotations

# Standard library imports
from datetime import datetime
from decimal import Decimal
from logging import Logger, getLogger
from string import Template
from typing import ClassVar, List, Optional

# First-party imports
from ai_cost.models.enums import RunStatus
from ai_cost.models.ledger.cost_run import CostRun
from ai_cost.models.ledger.ledger import Ledger


class CostReport:
    """Writes the text of a ticket's ``COST.md`` from its ledger.

    Attributes:
        WARNING_SHARE (Decimal): The share of the cap above which the ticket is flagged.
        LABEL_LENGTH (int): Characters of a label kept in a cell.
        NOTE_LENGTH (int): Characters of a note kept in a cell.
        COMMAND_LENGTH (int): Characters of a command kept in a cell.
        MODELS_LENGTH (int): Characters of the models cell.
        EMPTY_ROW (str): The row shown before the first run.
        logger (Logger): Logger instance.
    """

    WARNING_SHARE: ClassVar[Decimal] = Decimal("0.8")
    LABEL_LENGTH: ClassVar[int] = 60
    NOTE_LENGTH: ClassVar[int] = 80
    COMMAND_LENGTH: ClassVar[int] = 70
    MODELS_LENGTH: ClassVar[int] = 120
    EMPTY_ROW: ClassVar[str] = "| no run yet |  |  |  |  |  |  |  |  |  |  |  |"

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _cell(self, text: str, length: int) -> str:
        """Make a text safe for a table cell.

        Args:
            text (str): The text.
            length (int): Characters kept.

        Returns:
            str: The text on one line, its pipes escaped, cut to the length.
        """
        flat = " ".join(text.split()).replace("|", "\\|")
        return flat if len(flat) <= length else flat[: length - 3] + "..."

    def _time(self, moment: Optional[datetime]) -> str:
        """Format a moment in local time.

        Args:
            moment (Optional[datetime]): The moment.

        Returns:
            str: ``YYYY-MM-DD HH:MM``, or ``-`` when unknown.
        """
        return moment.astimezone().strftime("%Y-%m-%d %H:%M") if moment else "-"

    def _row(self, run: CostRun, cumulative: Decimal, left: Decimal) -> str:
        """Write the row of one run.

        Args:
            run (CostRun): The run.
            cumulative (Decimal): What the ticket spent up to this run, included.
            left (Decimal): What the ticket could still spend after this run.

        Returns:
            str: The Markdown row.
        """
        final = run.settled or run.status == RunStatus.REFUSED
        status = run.status.value.replace("_", " ") + ("" if final else " (not final)")
        note = f" ({self._cell(run.note, self.NOTE_LENGTH)})" if run.note else ""
        models = ", ".join(f"{model} ${usage.cost_usd:.4f}" for model, usage in run.usage.items()) or "none"
        return (
            f"| `{run.id}` | {status} | {run.source.value} | {self._cell(run.label, self.LABEL_LENGTH)}{note} "
            f"| `{self._cell(run.command, self.COMMAND_LENGTH)}` | {self._time(run.started_on)} "
            f"| {self._time(run.finished_on)} | ${run.estimate_usd:.2f} | ${run.cost_usd:.4f} | ${cumulative:.4f} "
            f"| ${left:.4f} | {self._cell(models, self.MODELS_LENGTH)} |"
        )

    def _status(self, ledger: Ledger) -> str:
        """Say where the ticket stands against its cap.

        Args:
            ledger (Ledger): The ledger.

        Returns:
            str: Blocked with its reason, near the cap, or within it.
        """
        if ledger.block_reason is not None:
            return f"blocked: {ledger.block_reason}"
        if ledger.spent_usd >= self.WARNING_SHARE * ledger.cap_usd:
            return "above 80 % of the cap"
        return "within the cap"

    ############################
    # Publicly Exposed Methods #
    ############################

    def render(self, ledger: Ledger, template: str, price_source: str) -> str:
        """Write the text of a ticket's ``COST.md``.

        Args:
            ledger (Ledger): The ledger.
            template (str): The layout, with ``string.Template`` placeholders.
            price_source (str): Where the prices come from.

        Returns:
            str: The Markdown text.
        """
        rows: List[str] = []
        cumulative = Decimal("0")
        for run in ledger.runs:
            cumulative += run.cost_usd
            rows.append(self._row(run, cumulative, max(Decimal("0"), ledger.cap_usd - cumulative)))
        text = Template(template).substitute(
            ticket=ledger.ticket,
            cap=f"${ledger.cap_usd:.2f}",
            spent=f"${ledger.spent_usd:.4f}",
            remaining=f"${ledger.remaining_usd:.4f}",
            status=self._status(ledger),
            rows="\n".join(rows) if rows else self.EMPTY_ROW,
            price_source=price_source,
        )
        self.logger.debug("Rendered the COST.md of %s: %d runs.", ledger.ticket, len(rows))
        return text
