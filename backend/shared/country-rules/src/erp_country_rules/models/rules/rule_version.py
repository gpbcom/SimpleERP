from __future__ import annotations

# Standard library imports
import datetime
from collections.abc import Mapping
from decimal import Decimal, InvalidOperation
from typing import Optional, Union

from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.exceptions import SEInvalidModelException
from erp_models.money.money import Money

# Third-party imports
from pydantic import Field, JsonValue, ValidationError, field_validator, model_validator

# First-party imports
from erp_country_rules.models.exceptions import (
    SERuleVersionEndsBeforeStart,
    SERuleVersionInvalidValidFrom,
    SERuleVersionInvalidValidTo,
    SERuleVersionInvalidValue,
)


class RuleVersion(FrozenErpModel):
    """One value of a country rule, with the days it is in force.

    Attributes:
        valid_from (datetime.date): The first day the value is in force.
        valid_to (Optional[datetime.date]): The last day the value is in force, inclusive, or ``None`` when open.
        value (Union[Money, Decimal]): The value, an exact decimal or an amount with its currency.

    Notes:
        - **Floats are refused for ``value``**, because they are not exact (REQ-T10-03).
        - A ``datetime`` is refused for the dates, because a rule is read by the day of the fact.
    """

    valid_from: datetime.date = Field(description="The first day the value is in force.")
    valid_to: Optional[datetime.date] = Field(
        default=None, description="The last day the value is in force, inclusive, or none when open."
    )
    value: Union[Money, Decimal] = Field(description="The value, an exact decimal or an amount with its currency.")

    ############################
    # Internal Helpers Methods #
    ############################

    @classmethod
    def _to_date(cls, value: JsonValue) -> Optional[datetime.date]:
        """Read a date from a date or an ISO date string.

        Args:
            value (JsonValue): The raw input.

        Returns:
            Optional[datetime.date]: The date, or ``None`` when the input is neither a date nor an ISO date string.
        """
        if isinstance(value, datetime.datetime):
            return None
        if isinstance(value, datetime.date):
            return value
        if isinstance(value, str):
            try:
                return datetime.date.fromisoformat(value.strip())
            except ValueError:
                return None
        return None

    ##############
    # Validators #
    ##############

    @field_validator("valid_from", mode="before")
    def validate_valid_from(cls, value: JsonValue) -> JsonValue:
        """Validate ``valid_from``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The date.

        Raises:
            SERuleVersionInvalidValidFrom: When it is not a date or an ISO date string.
        """
        parsed = cls._to_date(value)
        if parsed is None:
            raise SERuleVersionInvalidValidFrom(
                f"Invalid valid_from: {value!r}. "  # noqa: E501
                "Must be a date or an ISO date string."
            )
        return parsed.isoformat()

    @field_validator("valid_to", mode="before")
    def validate_valid_to(cls, value: JsonValue) -> JsonValue:
        """Validate ``valid_to``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The date, or the default when the input is ``None``.

        Raises:
            SERuleVersionInvalidValidTo: When it is not a date or an ISO date string.
        """
        if value is None:
            return cls.model_fields["valid_to"].get_default(call_default_factory=True)
        parsed = cls._to_date(value)
        if parsed is None:
            raise SERuleVersionInvalidValidTo(
                f"Invalid valid_to: {value!r}. "  # noqa: E501
                "Must be a date or an ISO date string."
            )
        return parsed.isoformat()

    @field_validator("value", mode="before")
    def validate_value(cls, value: JsonValue) -> Union[Money, Decimal]:
        """Validate ``value``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            Union[Money, Decimal]: An exact finite decimal, or an amount with its currency.

        Raises:
            SERuleVersionInvalidValue: When it is a boolean, a float, an empty or non-numeric text, not finite, or an
                invalid money mapping.
        """
        if isinstance(value, Money):
            return value
        if isinstance(value, Mapping):
            try:
                return Money.model_validate(dict(value))
            except (ValidationError, SEInvalidModelException) as error:
                raise SERuleVersionInvalidValue(
                    f"Invalid value: {value!r}. "  # noqa: E501
                    "Must be a valid money mapping."
                ) from error
        if isinstance(value, bool) or not isinstance(value, (str, int, Decimal)):
            raise SERuleVersionInvalidValue(
                f"Invalid value: {value!r}. "  # noqa: E501
                "Must be a text, an integer, a Decimal or a money mapping, never a float."
            )
        try:
            parsed = Decimal(value.strip() if isinstance(value, str) else value)
        except InvalidOperation as error:
            raise SERuleVersionInvalidValue(
                f"Invalid value: {value!r}. "  # noqa: E501
                "Must be a decimal number."
            ) from error
        if not parsed.is_finite():
            raise SERuleVersionInvalidValue(
                f"Invalid value: {value!r}. "  # noqa: E501
                "Must be a finite number."
            )
        return parsed

    @model_validator(mode="after")
    def validate_period(self) -> RuleVersion:
        """Check that the version does not end before it starts.

        Returns:
            RuleVersion: The same version.

        Raises:
            SERuleVersionEndsBeforeStart: When ``valid_to`` is before ``valid_from``.
        """
        if self.valid_to is not None and self.valid_to < self.valid_from:
            raise SERuleVersionEndsBeforeStart(
                f"Invalid valid_to: {self.valid_to.isoformat()!r}. "  # noqa: E501
                f"Must not be before valid_from {self.valid_from.isoformat()!r}."
            )
        return self
