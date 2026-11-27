from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar

# Third-party imports
from pydantic import Field, JsonValue, field_validator

# First-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.errors.entries.exceptions import (
    SEErrorCodeEntryInvalidAction,
    SEErrorCodeEntryInvalidReference,
    SEErrorCodeEntryInvalidTitle,
    SEErrorCodeEntryInvalidWhy,
)


class ErrorCodeEntry(FrozenErpModel):
    """One code of the error catalogue: what a person reads, as translation keys, and its support reference.

    Attributes:
        MESSAGE_KEY_PATTERN (str): The pattern of ``title``, ``why`` and ``action``.
        REFERENCE_PATTERN (str): The pattern of ``reference``.
        title (str): The translation key of the title.
        why (str): The translation key of the reason.
        action (str): The translation key of what to do next.
        reference (str): The small support reference, such as ``SITE-CLOSE-01``.

    Notes:
        - The strict patterns leave no room for free text or a secret (REQ-T05-03).
        - ``None`` has no default to become, so it is refused with the field's exception.
        - The fields are not named ``*_key``, which AGENT.md reserves for secret store entries.
    """

    MESSAGE_KEY_PATTERN: ClassVar[str] = r"^[a-z][a-z0-9_]*(\.[a-z0-9_]+)+$"
    REFERENCE_PATTERN: ClassVar[str] = r"^[A-Z][A-Z0-9]*(-[A-Z0-9]+)*-[0-9]{2}$"

    title: str = Field(description="The translation key of the title.")
    why: str = Field(description="The translation key of the reason.")
    action: str = Field(description="The translation key of the action to take.")
    reference: str = Field(description="The small support reference, such as SITE-CLOSE-01.")

    @field_validator("title", mode="before")
    def validate_title(cls, value: JsonValue) -> JsonValue:
        """Validate ``title``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEErrorCodeEntryInvalidTitle: When it is not a text, or does not match ``MESSAGE_KEY_PATTERN``.
        """
        if not isinstance(value, str) or re.fullmatch(cls.MESSAGE_KEY_PATTERN, value.strip()) is None:
            raise SEErrorCodeEntryInvalidTitle(
                f"Invalid title: {value!r}. "  # noqa: E501
                "Must be a translation key such as errors.site_close_01.title."
            )
        return value.strip()

    @field_validator("why", mode="before")
    def validate_why(cls, value: JsonValue) -> JsonValue:
        """Validate ``why``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEErrorCodeEntryInvalidWhy: When it is not a text, or does not match ``MESSAGE_KEY_PATTERN``.
        """
        if not isinstance(value, str) or re.fullmatch(cls.MESSAGE_KEY_PATTERN, value.strip()) is None:
            raise SEErrorCodeEntryInvalidWhy(
                f"Invalid why: {value!r}. "  # noqa: E501
                "Must be a translation key such as errors.site_close_01.why."
            )
        return value.strip()

    @field_validator("action", mode="before")
    def validate_action(cls, value: JsonValue) -> JsonValue:
        """Validate ``action``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEErrorCodeEntryInvalidAction: When it is not a text, or does not match ``MESSAGE_KEY_PATTERN``.
        """
        if not isinstance(value, str) or re.fullmatch(cls.MESSAGE_KEY_PATTERN, value.strip()) is None:
            raise SEErrorCodeEntryInvalidAction(
                f"Invalid action: {value!r}. "  # noqa: E501
                "Must be a translation key such as errors.site_close_01.action."
            )
        return value.strip()

    @field_validator("reference", mode="before")
    def validate_reference(cls, value: JsonValue) -> JsonValue:
        """Validate ``reference``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEErrorCodeEntryInvalidReference: When it is not a text, or does not match ``REFERENCE_PATTERN``.
        """
        if not isinstance(value, str) or re.fullmatch(cls.REFERENCE_PATTERN, value.strip()) is None:
            raise SEErrorCodeEntryInvalidReference(
                f"Invalid reference: {value!r}. "  # noqa: E501
                "Must be a support reference such as SITE-CLOSE-01."
            )
        return value.strip()
