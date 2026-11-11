from __future__ import annotations

# Standard library imports
import re

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from ai_cost.models.commands.exceptions import SEPaidCommandInvalidName, SEPaidCommandInvalidPattern


class PaidCommand(BaseModel):
    """A shell command that calls a paid AI.

    Attributes:
        name (str): What the command is.
        pattern (str): The Python regular expression that finds it in a shell command.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    name: str = Field(description="What the command is.", examples=["front-end AI judge of the screenshots"])
    pattern: str = Field(
        description="The Python regular expression that finds it in a shell command.",
        examples=[r"\bnpm\s+run\s+judge\b"],
    )

    @field_validator("name", mode="before")
    def validate_name(cls, value: JsonValue) -> JsonValue:
        """Validate ``name``.

        Args:
            value (JsonValue): The raw name.

        Returns:
            JsonValue: The name, stripped.

        Raises:
            SEPaidCommandInvalidName: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEPaidCommandInvalidName(
                f"Invalid name: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("pattern", mode="before")
    def validate_pattern(cls, value: JsonValue) -> JsonValue:
        """Validate ``pattern``.

        Args:
            value (JsonValue): The raw regular expression.

        Returns:
            JsonValue: The regular expression.

        Raises:
            SEPaidCommandInvalidPattern: When the value is not a non-empty, valid regular expression.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEPaidCommandInvalidPattern(
                f"Invalid pattern: {value!r}. "  # noqa: E501
                "Must be a non-empty regular expression."
            )
        try:
            re.compile(value)
        except re.error as error:
            raise SEPaidCommandInvalidPattern(
                f"Invalid pattern: {value!r}. "  # noqa: E501
                f"Python cannot compile it: {error}."
            ) from error
        return value
