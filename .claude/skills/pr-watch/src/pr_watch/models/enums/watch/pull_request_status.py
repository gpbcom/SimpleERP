from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class PullRequestStatus(StrEnum):
    """Where a pull request stands.

    Attributes:
        OPEN: Open.
        MERGED: Merged.
        CLOSED: Closed without merge.
    """

    OPEN = "open"
    MERGED = "merged"
    CLOSED = "closed"
