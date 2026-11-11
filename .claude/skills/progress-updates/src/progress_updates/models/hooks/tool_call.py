from __future__ import annotations

# Standard library imports
import json
from typing import Self

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from progress_updates.models.hooks.exceptions import (
    SEToolCallInvalidBackground,
    SEToolCallInvalidToolName,
    SEToolCallUnreadable,
)


class ToolCall(BaseModel):
    """The tool call a ``PostToolUse`` hook reports: which tool, and whether it runs in the background.

    Attributes:
        tool_name (str): The tool, such as ``Bash`` or ``Agent``.
        background (bool): Whether the call asked to run in the background.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    tool_name: str = Field(description="The tool, such as Bash or Agent.", examples=["Bash"])
    background: bool = Field(default=False, description="Whether it runs in the background.", examples=[True])

    @field_validator("tool_name", mode="before")
    def validate_tool_name(cls, value: JsonValue) -> JsonValue:
        """Validate ``tool_name``.

        Args:
            value (JsonValue): The raw name.

        Returns:
            JsonValue: The name, stripped.

        Raises:
            SEToolCallInvalidToolName: When the name is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEToolCallInvalidToolName(
                f"Invalid tool_name: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("background", mode="before")
    def validate_background(cls, value: JsonValue) -> JsonValue:
        """Validate ``background``.

        Args:
            value (JsonValue): The raw flag.

        Returns:
            JsonValue: The flag, or the default when ``None``.

        Raises:
            SEToolCallInvalidBackground: When the value is not a boolean.
        """
        if value is None:
            return cls.model_fields["background"].get_default(call_default_factory=True)
        if not isinstance(value, bool):
            raise SEToolCallInvalidBackground(
                f"Invalid background: {value!r}. "  # noqa: E501
                "Must be true or false."
            )
        return value

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def from_json(cls, text: str) -> Self:
        """Read the tool call of a ``PostToolUse`` hook payload.

        Args:
            text (str): The JSON Claude Code writes on the hook's standard input.

        Returns:
            Self: The tool call.

        Raises:
            SEToolCallUnreadable: When the text is not a JSON object naming a tool.
        """
        try:
            data = json.loads(text)
        except json.JSONDecodeError as error:
            raise SEToolCallUnreadable(
                "The hook payload cannot be read. "  # noqa: E501
                "It is not JSON."
            ) from error
        if not isinstance(data, dict) or "tool_name" not in data:
            raise SEToolCallUnreadable(
                "The hook payload cannot be read. "  # noqa: E501
                "It names no tool."
            )
        tool_input = data.get("tool_input")
        background = isinstance(tool_input, dict) and tool_input.get("run_in_background") is True
        return cls.model_validate({"tool_name": data["tool_name"], "background": background})
