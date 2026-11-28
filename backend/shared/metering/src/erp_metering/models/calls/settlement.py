from __future__ import annotations

# Standard library imports
from decimal import Decimal
from typing import Union

# First-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.money.exceptions import SEInvalidMoneyException
from erp_models.money.money import Money

# Third-party imports
from pydantic import Field, JsonValue, ValidationError, field_validator

from erp_metering.models.calls.exceptions import SESettlementInvalidActualCost, SESettlementInvalidReservationId


class Settlement(FrozenErpModel):
    """The real cost of a paid call, given back against its reservation.

    Attributes:
        reservation_id (str): The reservation the call was made under.
        actual_cost (Money): What the call really cost, zero or more.

    Notes:
        - A call that failed is settled with a zero cost, which releases the whole reservation.
    """

    reservation_id: str = Field(description="The identifier of the reservation, a non-empty text.")
    actual_cost: Money = Field(description="What the call really cost, never negative.")

    @field_validator("reservation_id", mode="before")
    def validate_reservation_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``reservation_id``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SESettlementInvalidReservationId: When it is not a text, or is empty.
        """
        if not isinstance(value, str) or not value.strip():
            raise SESettlementInvalidReservationId(
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
            SESettlementInvalidActualCost: When it is not an amount, or is negative.
        """
        if isinstance(value, Money):
            money = value
        elif isinstance(value, dict):
            try:
                money = Money.model_validate(value)
            except (ValidationError, SEInvalidMoneyException) as error:
                raise SESettlementInvalidActualCost(
                    f"Invalid actual_cost: {value!r}. "  # noqa: E501
                    "Must be an amount with its currency."
                ) from error
        else:
            raise SESettlementInvalidActualCost(
                f"Invalid actual_cost: {value!r}. "  # noqa: E501
                "Must be an amount with its currency."
            )
        if money.amount < Decimal(0):
            raise SESettlementInvalidActualCost(
                f"Invalid actual_cost: {value!r}. "  # noqa: E501
                "Must not be negative."
            )
        return money
