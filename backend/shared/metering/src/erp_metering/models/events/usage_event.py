from __future__ import annotations

# Standard library imports
from decimal import Decimal
from typing import ClassVar, Optional, Union

# First-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.money.exceptions import SEInvalidMoneyException
from erp_models.money.money import Money
from erp_models.times.exceptions import SEInvalidUtcTimestampException
from erp_models.times.utc_timestamp import UtcTimestamp

# Third-party imports
from pydantic import Field, JsonValue, ValidationError, field_validator

from erp_metering.models.calls.exceptions import SEInvalidPaidCallException
from erp_metering.models.calls.paid_call import PaidCall
from erp_metering.models.events.exceptions import (
    SEUsageEventInvalidActualCost,
    SEUsageEventInvalidCall,
    SEUsageEventInvalidOverBudget,
    SEUsageEventInvalidReservationId,
    SEUsageEventInvalidSettledAt,
)


class UsageEvent(FrozenErpModel):
    """The usage event written through the outbox for each settled paid call.

    Attributes:
        EVENT_TYPE (ClassVar[str]): The type of the event on the bus.
        call (PaidCall): The call that was made.
        reservation_id (Optional[str]): The reservation the call was made under, if any.
        actual_cost (Money): What the call really cost, never negative.
        over_budget (bool): Whether the cost went over the budget, as a legal-duty call may (BR-F22-06).
        settled_at (UtcTimestamp): When the call was settled, in UTC.
    """

    EVENT_TYPE: ClassVar[str] = "metering.usage"

    call: PaidCall = Field(description="The paid call that was made.")
    reservation_id: Optional[str] = Field(default=None, description="The reservation of the call, if any.")
    actual_cost: Money = Field(description="What the call really cost, never negative.")
    over_budget: bool = Field(default=False, description="Whether the cost went over the budget.")
    settled_at: UtcTimestamp = Field(description="When the call was settled, in UTC.")

    @field_validator("call", mode="before")
    def validate_call(cls, value: Union[JsonValue, PaidCall]) -> PaidCall:
        """Validate ``call``.

        Args:
            value (Union[JsonValue, PaidCall]): The raw input, a call or its mapping.

        Returns:
            PaidCall: The call.

        Raises:
            SEUsageEventInvalidCall: When it is not a paid call.
        """
        if isinstance(value, PaidCall):
            return value
        if isinstance(value, dict):
            try:
                return PaidCall.model_validate(value)
            except (ValidationError, SEInvalidPaidCallException) as error:
                raise SEUsageEventInvalidCall(
                    f"Invalid call: {value!r}. "  # noqa: E501
                    "Must be a paid call."
                ) from error
        raise SEUsageEventInvalidCall(
            f"Invalid call: {value!r}. "  # noqa: E501
            "Must be a paid call."
        )

    @field_validator("reservation_id", mode="before")
    def validate_reservation_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``reservation_id``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped, or ``None``.

        Raises:
            SEUsageEventInvalidReservationId: When it is not a text, or is empty.
        """
        if value is None:
            return None
        if not isinstance(value, str) or not value.strip():
            raise SEUsageEventInvalidReservationId(
                f"Invalid reservation_id: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

    @field_validator("actual_cost", mode="before")
    def validate_actual_cost(cls, value: Union[JsonValue, Money]) -> Money:
        """Validate ``actual_cost``.

        Args:
            value (Union[JsonValue, Money]): The raw input, an amount or its mapping.

        Returns:
            Money: The amount.

        Raises:
            SEUsageEventInvalidActualCost: When it is not an amount, or is negative.
        """
        if isinstance(value, Money):
            money = value
        elif isinstance(value, dict):
            try:
                money = Money.model_validate(value)
            except (ValidationError, SEInvalidMoneyException) as error:
                raise SEUsageEventInvalidActualCost(
                    f"Invalid actual_cost: {value!r}. "  # noqa: E501
                    "Must be an amount with its currency."
                ) from error
        else:
            raise SEUsageEventInvalidActualCost(
                f"Invalid actual_cost: {value!r}. "  # noqa: E501
                "Must be an amount with its currency."
            )
        if money.amount < Decimal(0):
            raise SEUsageEventInvalidActualCost(
                f"Invalid actual_cost: {value!r}. "  # noqa: E501
                "Must not be negative."
            )
        return money

    @field_validator("over_budget", mode="before")
    def validate_over_budget(cls, value: JsonValue) -> JsonValue:
        """Validate ``over_budget``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The boolean, or ``False`` when it is ``None``.

        Raises:
            SEUsageEventInvalidOverBudget: When it is not a boolean.
        """
        if value is None:
            return False
        if not isinstance(value, bool):
            raise SEUsageEventInvalidOverBudget(
                f"Invalid over_budget: {value!r}. "  # noqa: E501
                "Must be a boolean."
            )
        return value

    @field_validator("settled_at", mode="before")
    def validate_settled_at(cls, value: Union[JsonValue, UtcTimestamp]) -> UtcTimestamp:
        """Validate ``settled_at``.

        Args:
            value (Union[JsonValue, UtcTimestamp]): The raw input, a timestamp or its mapping.

        Returns:
            UtcTimestamp: The timestamp.

        Raises:
            SEUsageEventInvalidSettledAt: When it is not a UTC timestamp.
        """
        if isinstance(value, UtcTimestamp):
            return value
        if isinstance(value, dict):
            try:
                return UtcTimestamp.model_validate(value)
            except (ValidationError, SEInvalidUtcTimestampException) as error:
                raise SEUsageEventInvalidSettledAt(
                    f"Invalid settled_at: {value!r}. "  # noqa: E501
                    "Must be a timezone-aware instant."
                ) from error
        raise SEUsageEventInvalidSettledAt(
            f"Invalid settled_at: {value!r}. "  # noqa: E501
            "Must be a timezone-aware instant."
        )
