from __future__ import annotations

# First-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel

# Third-party imports
from pydantic import Field, JsonValue, field_validator

from erp_platform.models.contracts.enums import ContractChangeKind
from erp_platform.models.contracts.exceptions import SEContractChangeInvalidKind, SEContractChangeInvalidLocation


class ContractChange(FrozenErpModel):
    """One breaking change between the committed OpenAPI document and the live one (REQ-T05-05).

    Attributes:
        kind (ContractChangeKind): What changed.
        location (str): The JSON pointer of what changed, starting with ``#/``.

    Notes:
        No field has a default, so ``None`` is refused with the field's own exception.
    """

    kind: ContractChangeKind = Field(description="What changed.")
    location: str = Field(description="The JSON pointer of what changed, starting with #/.")

    @field_validator("kind", mode="before")
    def validate_kind(cls, value: JsonValue) -> JsonValue:
        """Validate ``kind``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The kind, as text.

        Raises:
            SEContractChangeInvalidKind: When it is not the exact value of a ``ContractChangeKind``.
        """
        if not isinstance(value, str) or value not in {kind.value for kind in ContractChangeKind}:
            raise SEContractChangeInvalidKind(
                f"Invalid kind: {value!r}. "  # noqa: E501
                "Must be one of the values of ContractChangeKind."
            )
        return str(value)

    @field_validator("location", mode="before")
    def validate_location(cls, value: JsonValue) -> JsonValue:
        """Validate ``location``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The pointer, stripped.

        Raises:
            SEContractChangeInvalidLocation: When it is not a JSON pointer starting with ``#/``.
        """
        if not isinstance(value, str) or not value.strip().startswith("#/"):
            raise SEContractChangeInvalidLocation(
                f"Invalid location: {value!r}. "  # noqa: E501
                "Must be a JSON pointer starting with '#/'."
            )
        return value.strip()
