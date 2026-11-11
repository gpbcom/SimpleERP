from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class DeploymentState(StrEnum):
    """The state of a deployment status, as GitHub names it.

    Attributes:
        ERROR: The deployment could not run.
        FAILURE: The deployment failed.
        INACTIVE: A later deployment replaced it.
        IN_PROGRESS: It runs.
        QUEUED: It waits for a runner.
        PENDING: It waits to start.
        SUCCESS: It succeeded.
    """

    ERROR = "error"
    FAILURE = "failure"
    INACTIVE = "inactive"
    IN_PROGRESS = "in_progress"
    QUEUED = "queued"
    PENDING = "pending"
    SUCCESS = "success"
