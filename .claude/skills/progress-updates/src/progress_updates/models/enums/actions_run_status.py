from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class ActionsRunStatus(StrEnum):
    """The status of a GitHub Actions run, as ``gh run list`` gives it.

    Attributes:
        IN_PROGRESS (str): Running.
        QUEUED (str): Waiting for a runner.
        WAITING (str): Waiting for an approval.
        PENDING (str): Waiting to be queued.
        REQUESTED (str): Requested, not queued yet.
        COMPLETED (str): Finished.
    """

    IN_PROGRESS = "in_progress"
    QUEUED = "queued"
    WAITING = "waiting"
    PENDING = "pending"
    REQUESTED = "requested"
    COMPLETED = "completed"
