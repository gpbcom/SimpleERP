from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class CheckConclusion(StrEnum):
    """How a check run or a workflow run ended, as GitHub names it.

    Attributes:
        SUCCESS: It passed.
        FAILURE: It failed.
        NEUTRAL: It ended without a verdict.
        CANCELLED: It was cancelled.
        SKIPPED: It was skipped.
        TIMED_OUT: It ran out of time.
        ACTION_REQUIRED: It needs someone to act.
        STALE: GitHub marked it stale.
        STARTUP_FAILURE: Its workflow could not start.
    """

    SUCCESS = "success"
    FAILURE = "failure"
    NEUTRAL = "neutral"
    CANCELLED = "cancelled"
    SKIPPED = "skipped"
    TIMED_OUT = "timed_out"
    ACTION_REQUIRED = "action_required"
    STALE = "stale"
    STARTUP_FAILURE = "startup_failure"
