from __future__ import annotations

# Standard library imports
from json import dumps
from typing import ClassVar, Dict

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from erp_testing.models.stand_in.exceptions import (
    SEStandInAnswerInvalidBody,
    SEStandInAnswerInvalidHeaders,
    SEStandInAnswerInvalidStatus,
)


class StandInAnswer(BaseModel):
    """What a stand-in server answers.

    Attributes:
        STATUS_MIN (int): The lowest HTTP status.
        STATUS_MAX (int): The highest HTTP status.
        status (int): The HTTP status of the answer.
        body (JsonValue): The JSON body, ``None`` for no body.
        headers (Dict[str, str]): The response headers.
    """

    STATUS_MIN: ClassVar[int] = 100
    STATUS_MAX: ClassVar[int] = 599

    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    status: int = Field(default=200, description="The HTTP status of the answer.")
    body: JsonValue = Field(default=None, description="The JSON body, none for no body.")
    headers: Dict[str, str] = Field(default_factory=dict, description="The response headers.")

    @field_validator("status", mode="before")
    def validate_status(cls, value: JsonValue) -> JsonValue:
        """Validate ``status``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The status, or the default when it is ``None``.

        Raises:
            SEStandInAnswerInvalidStatus: When it is not an integer within the HTTP bounds.
        """
        if value is None:
            return cls.model_fields["status"].get_default(call_default_factory=True)
        if isinstance(value, bool) or not isinstance(value, int) or not cls.STATUS_MIN <= value <= cls.STATUS_MAX:
            raise SEStandInAnswerInvalidStatus(
                f"Invalid status: {value!r}. "  # noqa: E501
                f"Must be an integer in [{cls.STATUS_MIN}, {cls.STATUS_MAX}]."
            )
        return value

    @field_validator("body", mode="before")
    def validate_body(cls, value: JsonValue) -> JsonValue:
        """Validate ``body``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The body as it is.

        Raises:
            SEStandInAnswerInvalidBody: When it cannot be serialised to JSON.
        """
        try:
            dumps(value)
        except (TypeError, ValueError) as error:
            raise SEStandInAnswerInvalidBody(
                f"Invalid body: {type(value).__name__}. "  # noqa: E501
                "Must be serialisable to JSON."
            ) from error
        return value

    @field_validator("headers", mode="before")
    def validate_headers(cls, value: JsonValue) -> JsonValue:
        """Validate ``headers``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The headers, or the default when it is ``None``.

        Raises:
            SEStandInAnswerInvalidHeaders: When it is not a mapping of texts to texts.
        """
        if value is None:
            return cls.model_fields["headers"].get_default(call_default_factory=True)
        if not isinstance(value, dict) or not all(
            isinstance(key, str) and isinstance(item, str) for key, item in value.items()
        ):
            raise SEStandInAnswerInvalidHeaders(
                f"Invalid headers: {value!r}. "  # noqa: E501
                "Must be a mapping of texts to texts."
            )
        return value
