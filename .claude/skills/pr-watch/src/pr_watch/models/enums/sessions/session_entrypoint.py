from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class SessionEntrypoint(StrEnum):
    """Where a Claude Code session runs, as Claude Code names it.

    Attributes:
        VSCODE: The VS Code extension.
        CLI: A terminal.
    """

    VSCODE = "claude-vscode"
    CLI = "cli"
