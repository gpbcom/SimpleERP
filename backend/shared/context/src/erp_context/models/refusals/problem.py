from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar, Optional

# Third-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from pydantic import Field, JsonValue, field_validator

# First-party imports
from erp_context.models.refusals.exceptions import (
    SEProblemInvalidAction,
    SEProblemInvalidCode,
    SEProblemInvalidDetail,
    SEProblemInvalidInstance,
    SEProblemInvalidReference,
    SEProblemInvalidStatus,
    SEProblemInvalidTitle,
    SEProblemInvalidType,
)


class Problem(FrozenErpModel):
    """The problem+json body of a refused request, as RFC 9457 defines it.

    Attributes:
        CODE_PATTERN (str): The pattern of ``code`` and ``reference``.
        KEY_PATTERN (str): The pattern of ``title``, ``detail`` and ``action``.
        STATUS_MIN (int): The lowest HTTP status.
        STATUS_MAX (int): The highest HTTP status.
        type (str): The problem type, ``about:blank`` unless a page describes it.
        title (str): The translation key of the title.
        status (int): The HTTP status.
        detail (str): The translation key of the reason.
        code (str): The code of the error pattern.
        action (str): The translation key of what to do next.
        reference (str): The small support reference.
        instance (Optional[str]): The identifier of this occurrence, such as the request id.

    Notes:
        - The members hold keys and codes only: never a secret, a stack trace or a typed value (REQ-T05-03).
        - ``None`` becomes the default for ``type`` and ``instance``, and is refused elsewhere.
    """

    CODE_PATTERN: ClassVar[str] = r"^[A-Z][A-Z0-9]*(-[A-Z0-9]+)*-[0-9]{2}$"
    KEY_PATTERN: ClassVar[str] = r"^[a-z][a-z0-9_]*(\.[a-z0-9_]+)+$"
    STATUS_MIN: ClassVar[int] = 400
    STATUS_MAX: ClassVar[int] = 599

    type: str = Field(default="about:blank", description="The problem type, about:blank unless a page describes it.")
    title: str = Field(description="The translation key of the title.")
    status: int = Field(description="The HTTP status.")
    detail: str = Field(description="The translation key of the reason.")
    code: str = Field(description="The code of the error pattern, such as RIGHTS-DENIED-01.")
    action: str = Field(description="The translation key of the action to take.")
    reference: str = Field(description="The small support reference.")
    instance: Optional[str] = Field(default=None, description="The identifier of this occurrence.")

    @field_validator("type", mode="before")
    def validate_type(cls, value: JsonValue) -> JsonValue:
        """Validate ``type``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped, or the default for ``None``.

        Raises:
            SEProblemInvalidType: When it is not a text, or is empty.
        """
        if value is None:
            return cls.model_fields["type"].get_default(call_default_factory=True)
        if not isinstance(value, str) or not value.strip():
            raise SEProblemInvalidType(
                f"Invalid type: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()

    @field_validator("title", mode="before")
    def validate_title(cls, value: JsonValue) -> JsonValue:
        """Validate ``title``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEProblemInvalidTitle: When it is not a text, or does not match ``KEY_PATTERN``.
        """
        if not isinstance(value, str) or re.fullmatch(cls.KEY_PATTERN, value.strip()) is None:
            raise SEProblemInvalidTitle(
                f"Invalid title: {value!r}. "  # noqa: E501
                "Must be a translation key such as errors.rights_denied_01.title."
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
            SEProblemInvalidStatus: When it is not an integer in [``STATUS_MIN``, ``STATUS_MAX``].
        """
        if isinstance(value, bool) or not isinstance(value, int) or not cls.STATUS_MIN <= value <= cls.STATUS_MAX:
            raise SEProblemInvalidStatus(
                f"Invalid status: {value!r}. "  # noqa: E501
                f"Must be in [{cls.STATUS_MIN}, {cls.STATUS_MAX}]."
            )
        return value

    @field_validator("detail", mode="before")
    def validate_detail(cls, value: JsonValue) -> JsonValue:
        """Validate ``detail``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEProblemInvalidDetail: When it is not a text, or does not match ``KEY_PATTERN``.
        """
        if not isinstance(value, str) or re.fullmatch(cls.KEY_PATTERN, value.strip()) is None:
            raise SEProblemInvalidDetail(
                f"Invalid detail: {value!r}. "  # noqa: E501
                "Must be a translation key such as errors.rights_denied_01.why."
            )
        return value.strip()

    @field_validator("code", mode="before")
    def validate_code(cls, value: JsonValue) -> JsonValue:
        """Validate ``code``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEProblemInvalidCode: When it is not a text, or does not match ``CODE_PATTERN``.
        """
        if not isinstance(value, str) or re.fullmatch(cls.CODE_PATTERN, value.strip()) is None:
            raise SEProblemInvalidCode(
                f"Invalid code: {value!r}. "  # noqa: E501
                "Must be a code such as RIGHTS-DENIED-01."
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
            SEProblemInvalidAction: When it is not a text, or does not match ``KEY_PATTERN``.
        """
        if not isinstance(value, str) or re.fullmatch(cls.KEY_PATTERN, value.strip()) is None:
            raise SEProblemInvalidAction(
                f"Invalid action: {value!r}. "  # noqa: E501
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
            SEProblemInvalidReference: When it is not a text, or does not match ``CODE_PATTERN``.
        """
        if not isinstance(value, str) or re.fullmatch(cls.CODE_PATTERN, value.strip()) is None:
            raise SEProblemInvalidReference(
                f"Invalid reference: {value!r}. "  # noqa: E501
                "Must be a support reference such as RIGHTS-DENIED-01."
            )
        return value.strip()

    @field_validator("instance", mode="before")
    def validate_instance(cls, value: JsonValue) -> JsonValue:
        """Validate ``instance``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped, or ``None``.

        Raises:
            SEProblemInvalidInstance: When it is not a text, or is empty.
        """
        if value is None:
            return None
        if not isinstance(value, str) or not value.strip():
            raise SEProblemInvalidInstance(
                f"Invalid instance: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()
