from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar

# Third-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from pydantic import Field, JsonValue, field_validator

# First-party imports
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.refusals.exceptions import (
    SERefusalCodeInvalidActionKey,
    SERefusalCodeInvalidCode,
    SERefusalCodeInvalidReason,
    SERefusalCodeInvalidReference,
    SERefusalCodeInvalidStatus,
    SERefusalCodeInvalidTitleKey,
    SERefusalCodeInvalidWhyKey,
)


class RefusalCode(FrozenErpModel):
    """One refusal of the catalogue: its reason, its code, its HTTP status and the keys of what a person reads.

    Attributes:
        CODE_PATTERN (str): The pattern of ``code`` and ``reference``.
        KEY_PATTERN (str): The pattern of the translation keys.
        STATUS_MIN (int): The lowest HTTP status.
        STATUS_MAX (int): The highest HTTP status.
        reason (RefusalReason): Why a request is refused.
        code (str): The code of the error pattern, such as ``RIGHTS-DENIED-01``.
        status (int): The HTTP status of the refusal.
        title_key (str): The translation key of the title.
        why_key (str): The translation key of the reason.
        action_key (str): The translation key of what to do next.
        reference (str): The small support reference.

    Notes:
        - It mirrors the entry of the error catalogue of ``erp_models``, with the reason and the status added.
        - The strict patterns leave no room for free text or a secret (REQ-T05-03).
        - The ``*_key`` fields hold translation keys, which are not secrets, as the catalogue of ``erp_models`` does.
        - ``None`` has no default to become, so it is refused with the field's exception.
    """

    CODE_PATTERN: ClassVar[str] = r"^[A-Z][A-Z0-9]*(-[A-Z0-9]+)*-[0-9]{2}$"
    KEY_PATTERN: ClassVar[str] = r"^[a-z][a-z0-9_]*(\.[a-z0-9_]+)+$"
    STATUS_MIN: ClassVar[int] = 400
    STATUS_MAX: ClassVar[int] = 599

    reason: RefusalReason = Field(description="Why a request is refused.")
    code: str = Field(description="The code of the error pattern, such as RIGHTS-DENIED-01.")
    status: int = Field(description="The HTTP status of the refusal.")
    title_key: str = Field(description="The translation key of the title.")
    why_key: str = Field(description="The translation key of the reason.")
    action_key: str = Field(description="The translation key of the action to take.")
    reference: str = Field(description="The small support reference, such as RIGHTS-DENIED-01.")

    @field_validator("reason", mode="before")
    def validate_reason(cls, value: JsonValue) -> JsonValue:
        """Validate ``reason``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The reason, unchanged.

        Raises:
            SERefusalCodeInvalidReason: When it is not the value of a ``RefusalReason``.
        """
        if isinstance(value, RefusalReason):
            return value
        if not isinstance(value, str) or value not in {reason.value for reason in RefusalReason}:
            raise SERefusalCodeInvalidReason(
                f"Invalid reason: {value!r}. "  # noqa: E501
                f"Must be one of {[reason.value for reason in RefusalReason]}."
            )
        return value

    @field_validator("code", mode="before")
    def validate_code(cls, value: JsonValue) -> JsonValue:
        """Validate ``code``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SERefusalCodeInvalidCode: When it is not a text, or does not match ``CODE_PATTERN``.
        """
        if not isinstance(value, str) or re.fullmatch(cls.CODE_PATTERN, value.strip()) is None:
            raise SERefusalCodeInvalidCode(
                f"Invalid code: {value!r}. "  # noqa: E501
                "Must be a code such as RIGHTS-DENIED-01."
            )
        return value.strip()

    @field_validator("status", mode="before")
    def validate_status(cls, value: JsonValue) -> JsonValue:
        """Validate ``status``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The status, unchanged.

        Raises:
            SERefusalCodeInvalidStatus: When it is not an integer in [``STATUS_MIN``, ``STATUS_MAX``].
        """
        if isinstance(value, bool) or not isinstance(value, int) or not cls.STATUS_MIN <= value <= cls.STATUS_MAX:
            raise SERefusalCodeInvalidStatus(
                f"Invalid status: {value!r}. "  # noqa: E501
                f"Must be in [{cls.STATUS_MIN}, {cls.STATUS_MAX}]."
            )
        return value

    @field_validator("title_key", mode="before")
    def validate_title_key(cls, value: JsonValue) -> JsonValue:
        """Validate ``title_key``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SERefusalCodeInvalidTitleKey: When it is not a text, or does not match ``KEY_PATTERN``.
        """
        if not isinstance(value, str) or re.fullmatch(cls.KEY_PATTERN, value.strip()) is None:
            raise SERefusalCodeInvalidTitleKey(
                f"Invalid title_key: {value!r}. "  # noqa: E501
                "Must be a translation key such as errors.rights_denied_01.title."
            )
        return value.strip()

    @field_validator("why_key", mode="before")
    def validate_why_key(cls, value: JsonValue) -> JsonValue:
        """Validate ``why_key``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SERefusalCodeInvalidWhyKey: When it is not a text, or does not match ``KEY_PATTERN``.
        """
        if not isinstance(value, str) or re.fullmatch(cls.KEY_PATTERN, value.strip()) is None:
            raise SERefusalCodeInvalidWhyKey(
                f"Invalid why_key: {value!r}. "  # noqa: E501
                "Must be a translation key such as errors.rights_denied_01.why."
            )
        return value.strip()

    @field_validator("action_key", mode="before")
    def validate_action_key(cls, value: JsonValue) -> JsonValue:
        """Validate ``action_key``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SERefusalCodeInvalidActionKey: When it is not a text, or does not match ``KEY_PATTERN``.
        """
        if not isinstance(value, str) or re.fullmatch(cls.KEY_PATTERN, value.strip()) is None:
            raise SERefusalCodeInvalidActionKey(
                f"Invalid action_key: {value!r}. "  # noqa: E501
                "Must be a translation key such as errors.rights_denied_01.action."
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
            SERefusalCodeInvalidReference: When it is not a text, or does not match ``CODE_PATTERN``.
        """
        if not isinstance(value, str) or re.fullmatch(cls.CODE_PATTERN, value.strip()) is None:
            raise SERefusalCodeInvalidReference(
                f"Invalid reference: {value!r}. "  # noqa: E501
                "Must be a support reference such as RIGHTS-DENIED-01."
            )
        return value.strip()
