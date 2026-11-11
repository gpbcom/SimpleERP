from __future__ import annotations

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.sessions.exceptions import (
    SECostLedgerInvalidBlocked,
    SECostLedgerInvalidCapUsd,
    SECostLedgerInvalidSpentUsd,
    SECostLedgerInvalidTicket,
)
from pr_watch.models.validation.field_rules import FieldRules


class CostLedger(BaseModel):
    """What a ticket's AI tests cost so far, read from the ai-test-cost ledger.

    Attributes:
        ticket (str): The ticket.
        cap_usd (float): The ticket's cap, in USD.
        spent_usd (float): What was spent so far, in USD.
        blocked (bool): Whether the cap stopped the paid tests.

    Notes:
        Only these four keys of the ledger are read, so that the ledger may grow without breaking the summary page.
    """

    model_config = ConfigDict(extra="forbid")

    ticket: str = Field(description="The ticket.", examples=["GH-12"])
    cap_usd: float = Field(description="The ticket's cap, in USD.", examples=[20.0])
    spent_usd: float = Field(description="What was spent so far, in USD.", examples=[3.25])
    blocked: bool = Field(description="Whether the cap stopped the paid tests.", examples=[False])

    @field_validator("ticket", mode="before")
    def validate_ticket(cls, value: JsonValue) -> JsonValue:
        """Validate ``ticket``.

        Args:
            value (JsonValue): The raw ticket.

        Returns:
            JsonValue: The ticket.

        Raises:
            SECostLedgerInvalidTicket: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SECostLedgerInvalidTicket, "ticket")

    @field_validator("cap_usd", mode="before")
    def validate_cap_usd(cls, value: JsonValue) -> JsonValue:
        """Validate ``cap_usd``.

        Args:
            value (JsonValue): The raw cap usd.

        Returns:
            JsonValue: The cap usd.

        Raises:
            SECostLedgerInvalidCapUsd: When the value is not a number of zero or more.
        """
        return FieldRules.amount(value, SECostLedgerInvalidCapUsd, "cap_usd")

    @field_validator("spent_usd", mode="before")
    def validate_spent_usd(cls, value: JsonValue) -> JsonValue:
        """Validate ``spent_usd``.

        Args:
            value (JsonValue): The raw spent usd.

        Returns:
            JsonValue: The spent usd.

        Raises:
            SECostLedgerInvalidSpentUsd: When the value is not a number of zero or more.
        """
        return FieldRules.amount(value, SECostLedgerInvalidSpentUsd, "spent_usd")

    @field_validator("blocked", mode="before")
    def validate_blocked(cls, value: JsonValue) -> JsonValue:
        """Validate ``blocked``.

        Args:
            value (JsonValue): The raw blocked.

        Returns:
            JsonValue: The blocked.

        Raises:
            SECostLedgerInvalidBlocked: When the value is not a boolean.
        """
        return FieldRules.flag(value, SECostLedgerInvalidBlocked, "blocked")
