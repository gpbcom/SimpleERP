from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar

# Third-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.ids.company_id import CompanyId
from pydantic import Field, JsonValue, field_validator

# First-party imports
from erp_testing.models.synthetic.exceptions import (
    SESyntheticCompanyInvalidId,
    SESyntheticCompanyInvalidName,
    SESyntheticCompanyInvalidSector,
)


class SyntheticCompany(FrozenErpModel):
    """One generated company, with an invented name.

    Attributes:
        SECTOR_PATTERN (str): The pattern of a sector code.
        id (CompanyId): The identifier of the company.
        name (str): The invented name, stripped of surrounding spaces.
        sector (str): The sector code, such as ``sc01``.

    Notes:
        - ``None`` has no default to become, so it is refused with the field's exception.
        - A sector is not stripped, so that a code followed by a line break is refused.
    """

    SECTOR_PATTERN: ClassVar[str] = r"sc[0-9]{2}"

    id: CompanyId = Field(description="The identifier of the company.")
    name: str = Field(description="The invented name of the company.")
    sector: str = Field(description="The sector code, such as sc01.")

    @field_validator("id", mode="before")
    def validate_id(cls, value: JsonValue | CompanyId) -> JsonValue | CompanyId:
        """Validate ``id``.

        Args:
            value (JsonValue | CompanyId): The raw input.

        Returns:
            JsonValue | CompanyId: The identifier, unchanged.

        Raises:
            SESyntheticCompanyInvalidId: When it is neither a ``CompanyId`` nor its mapping.
        """
        if not isinstance(value, (CompanyId, dict)):
            raise SESyntheticCompanyInvalidId(
                f"Invalid id: {value!r}. "  # noqa: E501
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
            SESyntheticCompanyInvalidName: When it is not a text, or is empty.
        """
        if not isinstance(value, str) or not value.strip():
            raise SESyntheticCompanyInvalidName(
                f"Invalid name: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

    @field_validator("sector", mode="before")
    def validate_sector(cls, value: JsonValue) -> JsonValue:
        """Validate ``sector``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The sector code, unchanged.

        Raises:
            SESyntheticCompanyInvalidSector: When it is not a text that matches ``SECTOR_PATTERN``.
        """
        if not isinstance(value, str) or re.fullmatch(cls.SECTOR_PATTERN, value) is None:
            raise SESyntheticCompanyInvalidSector(
                f"Invalid sector: {value!r}. "  # noqa: E501
                "Must be a code such as sc01."
            )
        return value
