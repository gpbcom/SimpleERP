from __future__ import annotations

# Standard library imports
import json
from pathlib import Path
from typing import ClassVar, Optional, Tuple

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from ticket_docs.models.hooks.exceptions import SEFileHookPayloadInvalidCwd, SEFileHookPayloadInvalidPath


class FileHookPayload(BaseModel):
    """What a Claude Code hook on a file tool (Write, Edit, MultiEdit, NotebookEdit) is told: the file and the folder.

    Attributes:
        PATH_KEYS (Tuple[str, ...]): The keys of ``tool_input`` that name the file, by tool.
        path (str): The file the tool writes, as Claude gave it.
        cwd (Optional[Path]): The folder the session runs in, when the hook gives it.

    Notes:
        Claude Code sends more keys (session, tool name, contents): ``from_json`` keeps only these two.
    """

    PATH_KEYS: ClassVar[Tuple[str, ...]] = ("file_path", "notebook_path")

    model_config = ConfigDict(extra="forbid", frozen=True)

    path: str = Field(description="The file the tool writes.", examples=["/repo/src/a.py"])
    cwd: Optional[Path] = Field(default=None, description="The folder the session runs in.", examples=["/repo"])

    @field_validator("path", mode="before")
    def validate_path(cls, value: JsonValue) -> JsonValue:
        """Validate ``path``.

        Args:
            value (JsonValue): The raw path.

        Returns:
            JsonValue: The path, stripped.

        Raises:
            SEFileHookPayloadInvalidPath: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEFileHookPayloadInvalidPath(
                f"Invalid path: {value!r}. "  # noqa: E501
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
            SEFileHookPayloadInvalidCwd: When the value is not a non-empty path.
        """
        if value is None:
            return None
        text = str(value) if isinstance(value, Path) else value
        if not isinstance(text, str) or not text.strip():
            raise SEFileHookPayloadInvalidCwd(
                f"Invalid cwd: {value!r}. "  # noqa: E501
                "Must be a non-empty path."
            )
        return text.strip()

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def from_json(cls, text: str) -> Optional[FileHookPayload]:
        """Read the hook's input.

        Args:
            text (str): The JSON Claude Code writes on the hook's standard input.

        Returns:
            Optional[FileHookPayload]: The file and the folder, ``None`` when the input names no file.
        """
        try:
            payload: JsonValue = json.loads(text or "null")
        except ValueError:
            return None
        tool_input = payload.get("tool_input") if isinstance(payload, dict) else None
        found = [tool_input.get(key) for key in cls.PATH_KEYS] if isinstance(tool_input, dict) else []
        paths = [path for path in found if isinstance(path, str) and path.strip()]
        if not paths:
            return None
        cwd = payload.get("cwd") if isinstance(payload, dict) else None
        return cls.model_validate({"path": paths[0], "cwd": cwd if isinstance(cwd, str) and cwd.strip() else None})
