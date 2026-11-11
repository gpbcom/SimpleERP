from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class ChecksStatus(StrEnum):
    """What the checks of a head commit say as a whole.

    Attributes:
        PASSED: Every check ended well.
        FAILED: At least one check failed, was cancelled or timed out.
        RUNNING: No check failed and at least one still runs.
        NONE: No check was reported.
    """

    PASSED = "passed"
    FAILED = "failed"
    RUNNING = "running"
    NONE = "none"
