from __future__ import annotations

import re

# Standard library imports
from decimal import Decimal, InvalidOperation
from typing import ClassVar, List

# Third-party imports
from pydantic import Field, JsonValue, field_validator

# First-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.money.exceptions import SEMoneyCurrencyMismatch, SEMoneyInvalidAmount, SEMoneyInvalidCurrency


class Money(FrozenErpModel):
    """An exact decimal amount with its currency.

    Attributes:
        CURRENCY_PATTERN (str): The ISO 4217 alphabetic form of a currency code.
        amount (Decimal): The exact amount, with the scale it was given.
        currency (str): The ISO 4217 alphabetic code, such as ``EUR``.

    Notes:
        - **Floats are refused**, because a float already carries a binary error (``0.1 + 0.2 != 0.3``) before any
          sum is made. An amount is given as a text, an integer or a ``Decimal``.
        - No rounding is applied here: rounding and conversion follow the country pack (D293).
    """

    CURRENCY_PATTERN: ClassVar[str] = r"^[A-Z]{3}$"

    amount: Decimal = Field(description="The exact amount, as a decimal.")
    currency: str = Field(description="The ISO 4217 alphabetic code of the currency.")

    @field_validator("amount", mode="before")
    def validate_amount(cls, value: JsonValue) -> Decimal:
        """Validate ``amount``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            Decimal: The amount, with its scale kept.

        Raises:
            SEMoneyInvalidAmount: When it is a float, a boolean, not finite, not a number or not a decimal text.
        """
        if isinstance(value, (bool, float)):
            raise SEMoneyInvalidAmount(
                f"Invalid amount: {value!r}. "  # noqa: E501
                "Must be an exact decimal given as a text, an integer or a Decimal, never a float."
            )
        if isinstance(value, str):
            stripped = value.strip()
            if not stripped:
                raise SEMoneyInvalidAmount(
                    f"Invalid amount: {value!r}. "  # noqa: E501
                    "Must be a non-empty text."
                )
            try:
                parsed = Decimal(stripped)
            except InvalidOperation as error:
                raise SEMoneyInvalidAmount(
                    f"Invalid amount: {value!r}. "  # noqa: E501
                    "Must be a decimal number."
                ) from error
        elif isinstance(value, (int, Decimal)):
            parsed = Decimal(value)
        else:
            raise SEMoneyInvalidAmount(
                f"Invalid amount: {value!r}. "  # noqa: E501
                "Must be a text, an integer or a Decimal."
            )
        if not parsed.is_finite():
            raise SEMoneyInvalidAmount(
                f"Invalid amount: {value!r}. "  # noqa: E501
                "Must be a finite number."
            )
        return parsed

    @field_validator("currency", mode="before")
    def validate_currency(cls, value: JsonValue) -> JsonValue:
        """Validate ``currency``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The code, stripped.

        Raises:
            SEMoneyInvalidCurrency: When it is not three upper-case letters.
        """
        if not isinstance(value, str):
            raise SEMoneyInvalidCurrency(
                f"Invalid currency: {value!r}. "  # noqa: E501
                f"Must match {cls.CURRENCY_PATTERN}."
            )
        stripped = value.strip()
        if re.fullmatch(cls.CURRENCY_PATTERN, stripped) is None:
            raise SEMoneyInvalidCurrency(
                f"Invalid currency: {value!r}. "  # noqa: E501
                f"Must match {cls.CURRENCY_PATTERN}."
            )
        return stripped

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def zero(cls, currency: str) -> Money:
        """Build a zero amount.

        Args:
            currency (str): The currency code.

        Returns:
            Money: Zero in that currency.
        """
        return cls(amount=Decimal(0), currency=currency)

    def add(self, other: Money) -> Money:
        """Add another amount to this one.

        Args:
            other (Money): The amount to add.

        Returns:
            Money: A new amount, the sum, with this currency.

        Raises:
            SEMoneyCurrencyMismatch: When the currencies differ.
        """
        if self.currency != other.currency:
            raise SEMoneyCurrencyMismatch(
                f"Currency mismatch: {self.currency} and {other.currency}. "  # noqa: E501
                "Must be the same currency."
            )
        return Money(amount=self.amount + other.amount, currency=self.currency)

    @classmethod
    def total(cls, currency: str, lines: List[Money]) -> Money:
        """Sum amounts in one currency.

        Args:
            currency (str): The currency of the total.
            lines (List[Money]): The amounts to sum.

        Returns:
            Money: The exact sum, zero when there are no lines.

        Raises:
            SEMoneyCurrencyMismatch: When a line is in another currency.
        """
        result = cls.zero(currency)
        for line in lines:
            result = result.add(line)
        return result
