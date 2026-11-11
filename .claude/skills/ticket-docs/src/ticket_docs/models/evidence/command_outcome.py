from __future__ import annotations

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from ticket_docs.models.evidence.exceptions import SECommandOutcomeInvalidExitCode, SECommandOutcomeInvalidOutput


class CommandOutcome(BaseModel):
    """How a command that was run ended.

    Attributes:
        exit_code (int): Its exit code, negative when a signal stopped it.
        output (str): What it wrote on its standard output and error, in order.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    exit_code: int = Field(description="Its exit code, negative when a signal stopped it.", examples=[0, 1])
    output: str = Field(default="", description="What it wrote on its standard output and error, in order.")

    @field_validator("exit_code", mode="before")
    def validate_exit_code(cls, value: JsonValue) -> JsonValue:
        """Validate ``exit_code``.

        Args:
            value (JsonValue): The raw exit code.

        Returns:
            JsonValue: The exit code.

        Raises:
            SECommandOutcomeInvalidExitCode: When the value is not a whole number.
        """
        if isinstance(value, bool) or not isinstance(value, int):
            raise SECommandOutcomeInvalidExitCode(
                f"Invalid exit_code: {value!r}. "  # noqa: E501
                "Must be a whole number."
            )
        return value

    @field_validator("output", mode="before")
    def validate_output(cls, value: JsonValue) -> JsonValue:
        """Validate ``output``.

        Args:
            value (JsonValue): The raw output, or ``None``.

        Returns:
            JsonValue: The output, empty for ``None``.

        Raises:
            SECommandOutcomeInvalidOutput: When the value is not a string.
        """
        if value is None:
            return ""
        if not isinstance(value, str):
            raise SECommandOutcomeInvalidOutput(
                f"Invalid output: {type(value).__name__}. "  # noqa: E501
                "Must be text."
            )
        return value
