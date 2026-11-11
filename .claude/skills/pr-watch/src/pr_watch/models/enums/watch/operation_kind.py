from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class OperationKind(StrEnum):
    """What happened to a watched pull request.

    Attributes:
        REGISTERED: The watch started or changed owner.
        DETECTED: The watcher found an event.
        REOPENED: The ticket's session was reopened with ``/pr-watch <KEY>`` typed.
        NOTIFIED: A desktop notification was shown.
        ACKED: The session took an event.
        REBASED: The session rebased the branch.
        FIXED: The session fixed a problem.
        WAITING_PUSH: The session waits for the approval to push.
        PUSHED: The session pushed.
        QA_STARTED: The session started the QA stage run.
        MERGED: The pull request was merged.
        CLOSED: The pull request was closed without merge.
        WARNING: Something could not be checked or delivered.
        NOTE: A note from the session.
    """

    REGISTERED = "registered"
    DETECTED = "detected"
    REOPENED = "reopened"
    NOTIFIED = "notified"
    ACKED = "acked"
    REBASED = "rebased"
    FIXED = "fixed"
    WAITING_PUSH = "waiting_push"
    PUSHED = "pushed"
    QA_STARTED = "qa_started"
    MERGED = "merged"
    CLOSED = "closed"
    WARNING = "warning"
    NOTE = "note"
