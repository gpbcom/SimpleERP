from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class TaskState(StrEnum):
    """The state of a task an update reports.

    Attributes:
        DONE (str): Finished with success.
        RUNNING (str): Still running.
        WAITING (str): Waiting for something: an approval, a queue, an answer.
        FAILED (str): Finished with a failure.
        WARNING (str): Degraded: a source not read, an invalid run.
    """

    DONE = "done"
    RUNNING = "running"
    WAITING = "waiting"
    FAILED = "failed"
    WARNING = "warning"
