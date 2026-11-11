from __future__ import annotations

# Standard library imports
from decimal import Decimal, InvalidOperation
from typing import ClassVar, FrozenSet, List, Optional

# Third-party imports
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    JsonValue,
    computed_field,
    field_serializer,
    field_validator,
    model_validator,
)

# First-party imports
from ai_cost.models.ledger.cost_run import CostRun
from ai_cost.models.ledger.exceptions import (
    SELedgerInvalidBlockReason,
    SELedgerInvalidCapUsd,
    SELedgerInvalidRuns,
    SELedgerInvalidTicket,
)
from harness_core.models.branches.branch_name import BranchName


class Ledger(BaseModel):
    """The paid AI test runs of one ticket, against its cap.

    Attributes:
        DERIVED (FrozenSet[str]): The keys the JSON file holds for its readers, worked out again on load.
        ticket (str): The ticket, ``GH-<issue number>``.
        cap_usd (Decimal): The most the ticket's paid AI tests may cost together, in USD.
        block_reason (Optional[str]): Why new paid runs are refused, ``None`` while the ticket is open.
        runs (List[CostRun]): Each run and charge, oldest first.

    Notes:
        - **The JSON file is read by other tools**: it holds ``ticket``, ``cap_usd``, ``spent_usd`` (numbers) and
          ``blocked`` at its top level. ``spent_usd``, ``remaining_usd`` and ``blocked`` are computed, so they can
          never disagree with the runs and the block reason.
        - The ticket key is checked with ``BranchName.TICKET_PATTERN``, so that it can name a file safely.
    """

    DERIVED: ClassVar[FrozenSet[str]] = frozenset({"spent_usd", "remaining_usd", "blocked"})

    model_config = ConfigDict(extra="forbid", frozen=True)

    ticket: str = Field(description="The ticket, GH-<issue number>.", examples=["GH-12"])
    cap_usd: Decimal = Field(
        description="The most the ticket's paid AI tests may cost together, in USD.", examples=["20"]
    )
    block_reason: Optional[str] = Field(
        default=None,
        description="Why new paid runs are refused, None while the ticket is open.",
        examples=["run 20261110-091502-3fa2c1 killed at $18.04"],
    )
    runs: List[CostRun] = Field(default_factory=list, description="Each run and charge, oldest first.", examples=[[]])

    @model_validator(mode="before")
    @classmethod
    def drop_derived(cls, data: JsonValue) -> JsonValue:
        """Drop the computed keys a ledger file holds.

        Args:
            data (JsonValue): The raw ledger.

        Returns:
            JsonValue: The ledger without ``spent_usd``, ``remaining_usd`` and ``blocked``.
        """
        if isinstance(data, dict):
            return {key: value for key, value in data.items() if key not in cls.DERIVED}
        return data

    @field_validator("ticket", mode="before")
    def validate_ticket(cls, value: JsonValue) -> JsonValue:
        """Validate ``ticket``.

        Args:
            value (JsonValue): The raw ticket key.

        Returns:
            JsonValue: The ticket key, stripped.

        Raises:
            SELedgerInvalidTicket: When the key does not look like ``GH-12``.
        """
        if not isinstance(value, str) or not BranchName.TICKET_PATTERN.match(value.strip()):
            raise SELedgerInvalidTicket(
                f"Invalid ticket: {value!r}. "  # noqa: E501
                "Must look like GH-12."
            )
        return value.strip()

    @field_validator("cap_usd", mode="before")
    def validate_cap_usd(cls, value: JsonValue) -> JsonValue:
        """Validate ``cap_usd``.

        Args:
            value (JsonValue): The raw cap: a number or a decimal string.

        Returns:
            JsonValue: The cap as a decimal string.

        Raises:
            SELedgerInvalidCapUsd: When the cap is not an amount above zero.
        """
        if value is None or isinstance(value, bool):
            raise SELedgerInvalidCapUsd(
                f"Invalid cap_usd: {value!r}. "  # noqa: E501
                "Must be an amount in USD."
            )
        try:
            amount = Decimal(str(value))
        except InvalidOperation as error:
            raise SELedgerInvalidCapUsd(
                f"Invalid cap_usd: {value!r}. "  # noqa: E501
                "Must be an amount in USD."
            ) from error
        if not amount.is_finite() or amount <= 0:
            raise SELedgerInvalidCapUsd(
                f"Invalid cap_usd: {value!r}. "  # noqa: E501
                "Must be above zero."
            )
        return str(amount)

    @field_validator("block_reason", mode="before")
    def validate_block_reason(cls, value: JsonValue) -> JsonValue:
        """Validate ``block_reason``.

        Args:
            value (JsonValue): The raw reason, or ``None``.

        Returns:
            JsonValue: The reason, stripped, or ``None``.

        Raises:
            SELedgerInvalidBlockReason: When the reason is not a non-empty string.
        """
        if value is None:
            return None
        if not isinstance(value, str) or not value.strip():
            raise SELedgerInvalidBlockReason(
                f"Invalid block_reason: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("runs", mode="before")
    def validate_runs(cls, value: JsonValue) -> JsonValue:
        """Validate ``runs``.

        Args:
            value (JsonValue): The raw runs.

        Returns:
            JsonValue: The runs, or the default for ``None``.

        Raises:
            SELedgerInvalidRuns: When the value is not a list.
        """
        if value is None:
            return []
        if not isinstance(value, list):
            raise SELedgerInvalidRuns(
                f"Invalid runs: {value!r}. "  # noqa: E501
                "Must be a list of runs."
            )
        return value

    ############################
    # Publicly Exposed Methods #
    ############################

    @computed_field  # type: ignore[prop-decorator]
    @property
    def spent_usd(self) -> Decimal:
        """What the ticket's runs cost so far, in USD."""
        return sum((run.cost_usd for run in self.runs), Decimal("0"))

    @computed_field  # type: ignore[prop-decorator]
    @property
    def remaining_usd(self) -> Decimal:
        """What the ticket may still spend, in USD, never below zero."""
        return max(Decimal("0"), self.cap_usd - self.spent_usd)

    @computed_field  # type: ignore[prop-decorator]
    @property
    def blocked(self) -> bool:
        """Whether new paid runs are refused until the cap is raised."""
        return self.block_reason is not None

    @field_serializer("cap_usd", "spent_usd", "remaining_usd", when_used="json")
    def serialize_amount(self, value: Decimal) -> float:
        """Write an amount as a JSON number.

        Args:
            value (Decimal): The amount.

        Returns:
            float: The same amount, a number for the tools that read the ledger.
        """
        return float(value)
