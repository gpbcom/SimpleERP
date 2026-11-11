from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class ProgressCommand(StrEnum):
    """The commands of ``progress-updates``.

    Attributes:
        STATUS (str): Print one update.
        WATCH (str): Print one line every interval while something runs.
        HOOK (str): Answer Claude Code's ``PostToolUse`` hook.
    """

    STATUS = "status"
    WATCH = "watch"
    HOOK = "hook"
