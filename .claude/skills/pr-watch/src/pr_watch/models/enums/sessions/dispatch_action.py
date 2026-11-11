from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class DispatchAction(StrEnum):
    """How the events of a ticket reached its session.

    Attributes:
        REOPENED_VSCODE: The session was opened in VS Code with ``/pr-watch <KEY>`` typed.
        OPENED_TERMINAL: The closed session was resumed in a terminal.
        NOTIFIED: A desktop notification was shown.
    """

    REOPENED_VSCODE = "reopened_vscode"
    OPENED_TERMINAL = "opened_terminal"
    NOTIFIED = "notified"
