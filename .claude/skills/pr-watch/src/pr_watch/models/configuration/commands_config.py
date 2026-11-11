from __future__ import annotations

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.configuration.exceptions import (
    SECommandsConfigInvalidClaude,
    SECommandsConfigInvalidNotifier,
    SECommandsConfigInvalidOpener,
    SECommandsConfigInvalidTerminal,
    SECommandsConfigInvalidVscode,
)
from pr_watch.models.validation.field_rules import FieldRules


class CommandsConfig(BaseModel):
    """The desktop programs the watcher starts.

    Attributes:
        claude (str): The Claude Code command.
        vscode (str): The VS Code command, used to bring the window of a session's folder forward.
        opener (str): The command that opens a ``vscode://`` link.
        notifier (str): The command that shows a desktop notification.
        terminal (str): The terminal used when VS Code is not installed.

    Notes:
        Tests point them at small scripts, so that nothing opens on the desktop.
    """

    model_config = ConfigDict(extra="forbid")

    claude: str = Field(description="The Claude Code command.", examples=["claude"])
    vscode: str = Field(
        description="The VS Code command, used to bring the window of a session's folder forward.", examples=["code"]
    )
    opener: str = Field(description="The command that opens a ``vscode://`` link.", examples=["xdg-open"])
    notifier: str = Field(description="The command that shows a desktop notification.", examples=["notify-send"])
    terminal: str = Field(description="The terminal used when VS Code is not installed.", examples=["gnome-terminal"])

    @field_validator("claude", mode="before")
    def validate_claude(cls, value: JsonValue) -> JsonValue:
        """Validate ``claude``.

        Args:
            value (JsonValue): The raw claude.

        Returns:
            JsonValue: The claude.

        Raises:
            SECommandsConfigInvalidClaude: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SECommandsConfigInvalidClaude, "claude")

    @field_validator("vscode", mode="before")
    def validate_vscode(cls, value: JsonValue) -> JsonValue:
        """Validate ``vscode``.

        Args:
            value (JsonValue): The raw vscode.

        Returns:
            JsonValue: The vscode.

        Raises:
            SECommandsConfigInvalidVscode: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SECommandsConfigInvalidVscode, "vscode")

    @field_validator("opener", mode="before")
    def validate_opener(cls, value: JsonValue) -> JsonValue:
        """Validate ``opener``.

        Args:
            value (JsonValue): The raw opener.

        Returns:
            JsonValue: The opener.

        Raises:
            SECommandsConfigInvalidOpener: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SECommandsConfigInvalidOpener, "opener")

    @field_validator("notifier", mode="before")
    def validate_notifier(cls, value: JsonValue) -> JsonValue:
        """Validate ``notifier``.

        Args:
            value (JsonValue): The raw notifier.

        Returns:
            JsonValue: The notifier.

        Raises:
            SECommandsConfigInvalidNotifier: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SECommandsConfigInvalidNotifier, "notifier")

    @field_validator("terminal", mode="before")
    def validate_terminal(cls, value: JsonValue) -> JsonValue:
        """Validate ``terminal``.

        Args:
            value (JsonValue): The raw terminal.

        Returns:
            JsonValue: The terminal.

        Raises:
            SECommandsConfigInvalidTerminal: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SECommandsConfigInvalidTerminal, "terminal")
