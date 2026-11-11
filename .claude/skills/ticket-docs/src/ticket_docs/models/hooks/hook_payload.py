from __future__ import annotations

# Standard library imports
import json
from pathlib import Path
from typing import Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from ticket_docs.models.hooks.exceptions import SEHookPayloadInvalidCommand, SEHookPayloadInvalidCwd


class HookPayload(BaseModel):
    """What a Claude Code hook on the Bash tool is told: the command and its folder.

    Attributes:
        command (str): The Bash command.
        cwd (Optional[Path]): The folder the session runs in, when the hook gives it.

    Notes:
        Claude Code sends more keys (session, tool name, transcript): ``from_json`` keeps only these two.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    command: str = Field(description="The Bash command.", examples=["git commit -m 'x'"])
    cwd: Optional[Path] = Field(default=None, description="The folder the session runs in.", examples=["/repo"])

    @field_validator("command", mode="before")
    def validate_command(cls, value: JsonValue) -> JsonValue:
        """Validate ``command``.

        Args:
            value (JsonValue): The raw command.

        Returns:
            JsonValue: The command, stripped.

        Raises:
            SEHookPayloadInvalidCommand: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEHookPayloadInvalidCommand(
                f"Invalid command: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("cwd", mode="before")
    def validate_cwd(cls, value: JsonValue) -> JsonValue:
        """Validate ``cwd``.

        Args:
            value (JsonValue): The raw folder, a ``Path``, or ``None``.

        Returns:
            JsonValue: The folder as text, or ``None``.

        Raises:
            SEHookPayloadInvalidCwd: When the value is not a non-empty path.
        """
        if value is None:
            return None
        text = str(value) if isinstance(value, Path) else value
        if not isinstance(text, str) or not text.strip():
            raise SEHookPayloadInvalidCwd(
                f"Invalid cwd: {value!r}. "  # noqa: E501
                "Must be a non-empty path."
            )
        return text.strip()

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def from_json(cls, text: str) -> Optional[HookPayload]:
        """Read the hook's input.

        Args:
            text (str): The JSON Claude Code writes on the hook's standard input.

        Returns:
            Optional[HookPayload]: The command and its folder, ``None`` when the input holds no command.
        """
        try:
            payload: JsonValue = json.loads(text or "null")
        except ValueError:
            return None
        tool_input = payload.get("tool_input") if isinstance(payload, dict) else None
        command = tool_input.get("command") if isinstance(tool_input, dict) else None
        if not isinstance(command, str) or not command.strip():
            return None
        cwd = payload.get("cwd") if isinstance(payload, dict) else None
        return cls.model_validate({"command": command, "cwd": cwd if isinstance(cwd, str) and cwd.strip() else None})
