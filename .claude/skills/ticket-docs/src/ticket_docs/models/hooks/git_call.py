from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import List

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from ticket_docs.models.hooks.exceptions import (
    SEGitCallInvalidArguments,
    SEGitCallInvalidDirectory,
    SEGitCallInvalidSubcommand,
)


class GitCall(BaseModel):
    """One git command found in a Bash command line, with the folder it runs in.

    Attributes:
        subcommand (str): The git command, such as ``push`` or ``commit``.
        arguments (List[str]): Its arguments, git's global options left out.
        directory (Path): The folder git runs in, ``cd`` and ``-C`` applied.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    subcommand: str = Field(description="The git command.", examples=["push"])
    arguments: List[str] = Field(default_factory=list, description="Its arguments.", examples=[["origin", "main"]])
    directory: Path = Field(description="The folder git runs in.", examples=["/repo"])

    @field_validator("subcommand", mode="before")
    def validate_subcommand(cls, value: JsonValue) -> JsonValue:
        """Validate ``subcommand``.

        Args:
            value (JsonValue): The raw git command.

        Returns:
            JsonValue: The command.

        Raises:
            SEGitCallInvalidSubcommand: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEGitCallInvalidSubcommand(
                f"Invalid subcommand: {value!r}. "  # noqa: E501
                "Must be a git command such as push."
            )
        return value.strip()

    @field_validator("arguments", mode="before")
    def validate_arguments(cls, value: JsonValue) -> JsonValue:
        """Validate ``arguments``.

        Args:
            value (JsonValue): The raw arguments, or ``None``.

        Returns:
            JsonValue: The arguments, empty for ``None``.

        Raises:
            SEGitCallInvalidArguments: When the value is not a list of strings.
        """
        if value is None:
            return []
        if not isinstance(value, list) or not all(isinstance(word, str) for word in value):
            raise SEGitCallInvalidArguments(
                f"Invalid arguments: {value!r}. "  # noqa: E501
                "Must be a list of words."
            )
        return value

    @field_validator("directory", mode="before")
    def validate_directory(cls, value: JsonValue) -> JsonValue:
        """Validate ``directory``.

        Args:
            value (JsonValue): The raw folder, a ``Path`` or a string.

        Returns:
            JsonValue: The folder as text.

        Raises:
            SEGitCallInvalidDirectory: When the value is not a non-empty path.
        """
        text = str(value) if isinstance(value, Path) else value
        if not isinstance(text, str) or not text.strip():
            raise SEGitCallInvalidDirectory(
                f"Invalid directory: {value!r}. "  # noqa: E501
                "Must be a non-empty path."
            )
        return text
