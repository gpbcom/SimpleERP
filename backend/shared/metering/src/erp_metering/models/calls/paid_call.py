from __future__ import annotations

# Standard library imports
from decimal import Decimal
from typing import Optional, Union

# First-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.ids.company_id import CompanyId
from erp_models.ids.exceptions import SECompanyIdInvalidValue
from erp_models.money.exceptions import SEInvalidMoneyException
from erp_models.money.money import Money

# Third-party imports
from pydantic import Field, JsonValue, ValidationError, field_validator

from erp_metering.models.calls.exceptions import (
    SEPaidCallInvalidCompanyId,
    SEPaidCallInvalidConnector,
    SEPaidCallInvalidEstimatedCost,
    SEPaidCallInvalidFeature,
    SEPaidCallInvalidLegalDuty,
    SEPaidCallInvalidModule,
    SEPaidCallInvalidUserId,
)


class PaidCall(FrozenErpModel):
    """One call to a paid service, as the metering client announces it before making it.

    Attributes:
        company_id (CompanyId): The company the call is made for.
        module (str): The module that makes the call, a budget scope of D398.
        feature (str): The feature that makes the call, a budget scope of D398.
        connector (Optional[str]): The connector the call goes through, if any.
        user_id (Optional[str]): The user the call is made for, if any.
        estimated_cost (Money): The cost reserved before the call, never negative.
        legal_duty (bool): Whether the call is a legal duty, which a budget never stops (BR-F22-06).
    """

    company_id: CompanyId = Field(description="The company the call is made for.")
    module: str = Field(description="The module that makes the call, a non-empty text.")
    feature: str = Field(description="The feature that makes the call, a non-empty text.")
    connector: Optional[str] = Field(default=None, description="The connector the call goes through, if any.")
    user_id: Optional[str] = Field(default=None, description="The user the call is made for, if any.")
    estimated_cost: Money = Field(description="The cost to reserve before the call, never negative.")
    legal_duty: bool = Field(default=False, description="Whether the call is a legal duty that a budget never stops.")

    @field_validator("company_id", mode="before")
    def validate_company_id(cls, value: Union[JsonValue, CompanyId]) -> CompanyId:
        """Validate ``company_id``.

        Args:
            value (Union[JsonValue, CompanyId]): The raw input, an id or its mapping.

        Returns:
            CompanyId: The company id.

        Raises:
            SEPaidCallInvalidCompanyId: When it is not a company id.
        """
        if isinstance(value, CompanyId):
            return value
        if isinstance(value, dict):
            try:
                return CompanyId.model_validate(value)
            except (ValidationError, SECompanyIdInvalidValue) as error:
                raise SEPaidCallInvalidCompanyId(
                    f"Invalid company_id: {value!r}. "  # noqa: E501
                    "Must be a company id."
                ) from error
        raise SEPaidCallInvalidCompanyId(
            f"Invalid company_id: {value!r}. "  # noqa: E501
            "Must be a company id."
        )

    @field_validator("module", mode="before")
    def validate_module(cls, value: JsonValue) -> JsonValue:
        """Validate ``module``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEPaidCallInvalidModule: When it is not a text, or is empty.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEPaidCallInvalidModule(
                f"Invalid module: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

    @field_validator("feature", mode="before")
    def validate_feature(cls, value: JsonValue) -> JsonValue:
        """Validate ``feature``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEPaidCallInvalidFeature: When it is not a text, or is empty.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEPaidCallInvalidFeature(
                f"Invalid feature: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

    @field_validator("connector", mode="before")
    def validate_connector(cls, value: JsonValue) -> JsonValue:
        """Validate ``connector``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped, or ``None``.

        Raises:
            SEPaidCallInvalidConnector: When it is not a text, or is empty.
        """
        if value is None:
            return None
        if not isinstance(value, str) or not value.strip():
            raise SEPaidCallInvalidConnector(
                f"Invalid connector: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

    @field_validator("user_id", mode="before")
    def validate_user_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``user_id``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped, or ``None``.

        Raises:
            SEPaidCallInvalidUserId: When it is not a text, or is empty.
        """
        if value is None:
            return None
        if not isinstance(value, str) or not value.strip():
            raise SEPaidCallInvalidUserId(
                f"Invalid user_id: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

    @field_validator("estimated_cost", mode="before")
    def validate_estimated_cost(cls, value: Union[JsonValue, Money]) -> Money:
        """Validate ``estimated_cost``.

        Args:
            value (Union[JsonValue, Money]): The raw input, an amount or its mapping.

        Returns:
            Money: The amount.

        Raises:
            SEPaidCallInvalidEstimatedCost: When it is not an amount, or is negative.
        """
        if isinstance(value, Money):
            money = value
        elif isinstance(value, dict):
            try:
                money = Money.model_validate(value)
            except (ValidationError, SEInvalidMoneyException) as error:
                raise SEPaidCallInvalidEstimatedCost(
                    f"Invalid estimated_cost: {value!r}. "  # noqa: E501
                    "Must be an amount with its currency."
                ) from error
        else:
            raise SEPaidCallInvalidEstimatedCost(
                f"Invalid estimated_cost: {value!r}. "  # noqa: E501
                "Must be an amount with its currency."
            )
        if money.amount < Decimal(0):
            raise SEPaidCallInvalidEstimatedCost(
                f"Invalid estimated_cost: {value!r}. "  # noqa: E501
                "Must not be negative."
            )
        return money

    @field_validator("legal_duty", mode="before")
    def validate_legal_duty(cls, value: JsonValue) -> JsonValue:
        """Validate ``legal_duty``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The boolean, or ``False`` when it is ``None``.

        Raises:
            SEPaidCallInvalidLegalDuty: When it is not a boolean.
        """
        if value is None:
            return False
        if not isinstance(value, bool):
            raise SEPaidCallInvalidLegalDuty(
                f"Invalid legal_duty: {value!r}. "  # noqa: E501
                "Must be a boolean."
            )
        return value
