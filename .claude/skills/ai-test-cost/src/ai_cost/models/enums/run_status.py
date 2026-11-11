from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class RunStatus(StrEnum):
    """Where a paid AI test run stands.

    Attributes:
        RUNNING (str): The command is running.
        DONE (str): The command ended with exit code 0.
        FAILED (str): The command failed, could not start, could not be measured or was interrupted.
        KILLED_AT_CAP (str): The guard killed the command when the ticket reached its kill threshold.
        REFUSED (str): The guard did not start the command.
    """

    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"
    KILLED_AT_CAP = "killed_at_cap"
    REFUSED = "refused"
