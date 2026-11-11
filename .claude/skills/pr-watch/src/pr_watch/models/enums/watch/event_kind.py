from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class EventKind(StrEnum):
    """What a pull request needs from its ticket's session.

    Attributes:
        REBASE_CONFLICT: Its head no longer merges into its base without conflict.
        CHECKS_FAILED: A check run or a CI workflow run of its head failed, was cancelled or timed out.
        STAGE_FAILED: A ``dev`` or ``qa`` deployment of its head, or a run of the stage workflow, failed.
        CHANGES_REQUESTED: A reviewer's standing decision asks for changes.
        REVIEW_COMMENTS: Someone else commented on it since the last run.
        QA_WAITING: A ``qa`` deployment has waited for its approval longer than allowed.
    """

    REBASE_CONFLICT = "rebase_conflict"
    CHECKS_FAILED = "checks_failed"
    STAGE_FAILED = "stage_failed"
    CHANGES_REQUESTED = "changes_requested"
    REVIEW_COMMENTS = "review_comments"
    QA_WAITING = "qa_waiting"
