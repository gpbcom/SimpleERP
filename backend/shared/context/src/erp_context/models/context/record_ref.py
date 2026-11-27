from __future__ import annotations

# Standard library imports
from typing import Optional

# Third-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.ids.company_id import CompanyId
from pydantic import Field, JsonValue, field_validator

# First-party imports
from erp_context.models.context.exceptions import (
    SERecordRefInvalidCompanyId,
    SERecordRefInvalidRecordId,
    SERecordRefInvalidRecordType,
)


class RecordRef(FrozenErpModel):
    """A reference to a record, or to a kind of record, of one company.

    Attributes:
        record_type (str): The kind of record, stripped of surrounding spaces.
        company_id (CompanyId): The company that owns the record.
        record_id (Optional[str]): The identifier of the record, ``None`` for the kind alone.
    """

    record_type: str = Field(description="The kind of record, a non-empty text.")
    company_id: CompanyId = Field(description="The company that owns the record.")
    record_id: Optional[str] = Field(default=None, description="The identifier of the record, if one is meant.")

    @field_validator("record_type", mode="before")
    def validate_record_type(cls, value: JsonValue) -> JsonValue:
        """Validate ``record_type``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SERecordRefInvalidRecordType: When it is not a text, or is empty.
        """
        if not isinstance(value, str) or not value.strip():
            raise SERecordRefInvalidRecordType(
                f"Invalid record_type: {value!r}. "  # noqa: E501
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
            SERecordRefInvalidCompanyId: When it is neither a ``CompanyId`` nor its mapping.
        """
        if not isinstance(value, (CompanyId, dict)):
            raise SERecordRefInvalidCompanyId(
                f"Invalid company_id: {value!r}. "  # noqa: E501
                "Must be a CompanyId."
            )
        return value

    @field_validator("record_id", mode="before")
    def validate_record_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``record_id``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped, or the default for ``None``.

        Raises:
            SERecordRefInvalidRecordId: When it is not a text, or is empty.
        """
        if value is None:
            return cls.model_fields["record_id"].get_default(call_default_factory=True)
        if not isinstance(value, str) or not value.strip():
            raise SERecordRefInvalidRecordId(
                f"Invalid record_id: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()
