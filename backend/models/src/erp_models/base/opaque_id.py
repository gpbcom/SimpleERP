from __future__ import annotations

# Standard library imports
from typing import ClassVar, Type

# Third-party imports
from pydantic import Field, JsonValue, field_validator

# First-party imports
from erp_models.base.exceptions import SEOpaqueIdInvalidValue
from erp_models.base.frozen_erp_model import FrozenErpModel


class OpaqueId(FrozenErpModel):
    """A text identifier whose content means nothing to its holder.

    Attributes:
        INVALID_VALUE (Type[Exception]): The exception raised for an invalid ``value``.
        value (str): The identifier, stripped of surrounding spaces.

    Notes:
        - Subclasses only set their own ``INVALID_VALUE``, so the rule lives in one place.
    """

    INVALID_VALUE: ClassVar[Type[Exception]] = SEOpaqueIdInvalidValue

    value: str = Field(description="The identifier, a non-empty text.")

    @field_validator("value", mode="before")
    def validate_value(cls, value: JsonValue) -> JsonValue:
        """Validate ``value``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            Exception: ``INVALID_VALUE`` when it is not a text, or is empty.
        """
        if not isinstance(value, str):
            raise cls.INVALID_VALUE(
                f"Invalid value: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        stripped = value.strip()
        if not stripped:
            raise cls.INVALID_VALUE(
                f"Invalid value: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return stripped
