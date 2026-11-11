from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class TicketDocsCommand(StrEnum):
    """The commands of the ``ticket-docs`` command line.

    Attributes:
        RECORD_RUN (str): Run a command, or read an Actions run, into an evidence folder.
        CHECK (str): Check a ticket folder against the skill and the rules.
        REPORT_INDEX (str): Write the index of every evidence folder of every ticket.
        HISTORY_BUNDLE (str): Save the branch's commits before a squash.
        ARCHIVE (str): Upload the ticket folder to its evidence pre-release.
        BOARD (str): Move the ticket's issue on the project board.
        GIT_GATE (str): Answer the ``PreToolUse`` hook on Bash.
        TIME_REMINDER (str): Answer the ``PostToolUse`` hook on Bash.
        ALLOW_SQUASH (str): Grant the one-shot permit of a GIT-4 squash, from the human's own terminal.
        FILE_GATE (str): Answer the ``PreToolUse`` hook on the file tools.
    """

    RECORD_RUN = "record-run"
    CHECK = "check"
    REPORT_INDEX = "report-index"
    HISTORY_BUNDLE = "history-bundle"
    ARCHIVE = "archive"
    BOARD = "board"
    GIT_GATE = "git-gate"
    TIME_REMINDER = "time-reminder"
    ALLOW_SQUASH = "allow-squash"
    FILE_GATE = "file-gate"
