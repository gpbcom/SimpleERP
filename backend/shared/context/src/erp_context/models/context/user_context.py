from __future__ import annotations

# Third-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.ids.company_id import CompanyId
from pydantic import Field, JsonValue, field_validator

# First-party imports
from erp_context.models.context.exceptions import SEUserContextInvalidCompanyId, SEUserContextInvalidUserId


class UserContext(FrozenErpModel):
    """The user and the company a request acts for.

    Attributes:
        user_id (str): The identifier of the user, stripped of surrounding spaces.
        company_id (CompanyId): The company the user acts in.
    """

    user_id: str = Field(description="The identifier of the user, a non-empty text.")
    company_id: CompanyId = Field(description="The company the user acts in.")

    @field_validator("user_id", mode="before")
    def validate_user_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``user_id``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEUserContextInvalidUserId: When it is not a text, or is empty.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEUserContextInvalidUserId(
                f"Invalid user_id: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

    @field_validator("company_id", mode="before")
    def validate_company_id(cls, value: JsonValue | CompanyId) -> JsonValue | CompanyId:
        """Validate ``company_id``.

        Args:
            value (JsonValue | CompanyId): The raw input.

        Returns:
            JsonValue | CompanyId: The company id, or its raw form for Pydantic to build.

        Raises:
            SEUserContextInvalidCompanyId: When it is neither a ``CompanyId`` nor its mapping.
        """
        if not isinstance(value, (CompanyId, dict)):
            raise SEUserContextInvalidCompanyId(
                f"Invalid company_id: {value!r}. "  # noqa: E501
                "Must be a CompanyId."
            )
        return value
