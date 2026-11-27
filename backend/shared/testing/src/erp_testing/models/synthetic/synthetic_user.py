from __future__ import annotations

# Third-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.ids.company_id import CompanyId
from erp_models.ids.record_id import RecordId
from pydantic import Field, JsonValue, field_validator

# First-party imports
from erp_testing.models.synthetic.exceptions import (
    SESyntheticUserInvalidCompanyId,
    SESyntheticUserInvalidEmail,
    SESyntheticUserInvalidId,
    SESyntheticUserInvalidName,
)
from erp_testing.models.synthetic.synthetic_catalog import SyntheticCatalog


class SyntheticUser(FrozenErpModel):
    """One generated user of a generated company, with an invented name and a reserved e-mail address.

    Attributes:
        id (RecordId): The identifier of the user.
        company_id (CompanyId): The identifier of the user's company.
        name (str): The invented name, stripped of surrounding spaces.
        email (str): The e-mail address, on a reserved domain.

    Notes:
        - **The address must be on a reserved domain**, checked by ``SyntheticCatalog.is_reserved_domain``, so that
          the rule is written once and no generated address can reach a real mailbox.
        - ``None`` has no default to become, so it is refused with the field's exception.
    """

    id: RecordId = Field(description="The identifier of the user.")
    company_id: CompanyId = Field(description="The identifier of the user's company.")
    name: str = Field(description="The invented name of the user.")
    email: str = Field(description="The e-mail address, on a reserved domain.")

    @field_validator("id", mode="before")
    def validate_id(cls, value: JsonValue | RecordId) -> JsonValue | RecordId:
        """Validate ``id``.

        Args:
            value (JsonValue | RecordId): The raw input.

        Returns:
            JsonValue | RecordId: The identifier, unchanged.

        Raises:
            SESyntheticUserInvalidId: When it is neither a ``RecordId`` nor its mapping.
        """
        if not isinstance(value, (RecordId, dict)):
            raise SESyntheticUserInvalidId(
                f"Invalid id: {value!r}. "  # noqa: E501
                "Must be a RecordId."
            )
        return value

    @field_validator("company_id", mode="before")
    def validate_company_id(cls, value: JsonValue | CompanyId) -> JsonValue | CompanyId:
        """Validate ``company_id``.

        Args:
            value (JsonValue | CompanyId): The raw input.

        Returns:
            JsonValue | CompanyId: The identifier, unchanged.

        Raises:
            SESyntheticUserInvalidCompanyId: When it is neither a ``CompanyId`` nor its mapping.
        """
        if not isinstance(value, (CompanyId, dict)):
            raise SESyntheticUserInvalidCompanyId(
                f"Invalid company_id: {value!r}. "  # noqa: E501
                "Must be a CompanyId."
            )
        return value

    @field_validator("name", mode="before")
    def validate_name(cls, value: JsonValue) -> JsonValue:
        """Validate ``name``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The name, stripped.

        Raises:
            SESyntheticUserInvalidName: When it is not a text, or is empty.
        """
        if not isinstance(value, str) or not value.strip():
            raise SESyntheticUserInvalidName(
                f"Invalid name: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

    @field_validator("email", mode="before")
    def validate_email(cls, value: JsonValue) -> JsonValue:
        """Validate ``email``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The address, stripped.

        Raises:
            SESyntheticUserInvalidEmail: When it is not a text with one ``@``, a name and a reserved domain.
        """
        if not isinstance(value, str) or value.strip().count("@") != 1:
            raise SESyntheticUserInvalidEmail(
                f"Invalid email: {value!r}. "  # noqa: E501
                "Must be a text with one @."
            )
        local, domain = value.strip().split("@")
        if not local or not SyntheticCatalog.is_reserved_domain(domain):
            raise SESyntheticUserInvalidEmail(
                f"Invalid email: {value!r}. "  # noqa: E501
                "Must have a name before the @ and a reserved domain after it."
            )
        return value.strip()
