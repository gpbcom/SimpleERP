from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class RunConclusion(StrEnum):
    """How a GitHub Actions run ended, as ``gh run view --json conclusion`` gives it.

    Attributes:
        SUCCESS (str): Every job passed.
        FAILURE (str): A job failed.
        CANCELLED (str): The run was cancelled.
        SKIPPED (str): The run was skipped.
        TIMED_OUT (str): A job ran out of time.
        ACTION_REQUIRED (str): The run waits for an approval.
        NEUTRAL (str): The run ended without a verdict.
        STALE (str): GitHub gave up on the run.
        STARTUP_FAILURE (str): The run could not start.
        PENDING (str): The run has not ended yet.
    """

    SUCCESS = "success"
    FAILURE = "failure"
    CANCELLED = "cancelled"
    SKIPPED = "skipped"
    TIMED_OUT = "timed_out"
    ACTION_REQUIRED = "action_required"
    NEUTRAL = "neutral"
    STALE = "stale"
    STARTUP_FAILURE = "startup_failure"
    PENDING = ""
