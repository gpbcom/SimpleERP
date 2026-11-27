from __future__ import annotations

# Standard library imports
from typing import ClassVar

# First-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel

# Third-party imports
from pydantic import Field, JsonValue, field_validator

from erp_platform.models.problems.exceptions import (
    SEProblemDetailsInvalidCode,
    SEProblemDetailsInvalidDetail,
    SEProblemDetailsInvalidStatus,
    SEProblemDetailsInvalidTitle,
)


class ProblemDetails(FrozenErpModel):
    """The problem+json body of every error answer (REQ-T05-03, D122).

    Attributes:
        STATUS_MIN (int): The lowest HTTP status of an error.
        STATUS_MAX (int): The highest HTTP status of an error.
        title (str): The translation key of the title.
        status (int): The HTTP status.
        detail (str): The translation key of the reason.
        code (str): The support reference of the error, such as ``SITE-CLOSE-01``.

    Notes:
        - There is no ``type`` member: the ``code`` names the problem.
        - No field has a default, so ``None`` is refused with the field's own exception.
    """

    STATUS_MIN: ClassVar[int] = 400
    STATUS_MAX: ClassVar[int] = 599

    title: str = Field(description="The translation key of the title.")
    status: int = Field(description="The HTTP status.")
    detail: str = Field(description="The translation key of the reason.")
    code: str = Field(description="The support reference of the error, such as SITE-CLOSE-01.")

    @field_validator("title", mode="before")
    def validate_title(cls, value: JsonValue) -> JsonValue:
        """Validate ``title``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEProblemDetailsInvalidTitle: When it is not a non-empty text.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEProblemDetailsInvalidTitle(
                f"Invalid title: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
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
            SEProblemDetailsInvalidStatus: When it is not an integer in ``[STATUS_MIN, STATUS_MAX]``.
        """
        if isinstance(value, bool) or not isinstance(value, int) or not cls.STATUS_MIN <= value <= cls.STATUS_MAX:
            raise SEProblemDetailsInvalidStatus(
                f"Invalid status: {value!r}. "  # noqa: E501
                f"Must be an integer in [{cls.STATUS_MIN}, {cls.STATUS_MAX}]."
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
            SEProblemDetailsInvalidDetail: When it is not a non-empty text.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEProblemDetailsInvalidDetail(
                f"Invalid detail: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
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
            SEProblemDetailsInvalidCode: When it is not a non-empty text.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEProblemDetailsInvalidCode(
                f"Invalid code: {value!r}. "  # noqa: E501
                "Must be a non-empty text."
            )
        return value.strip()
