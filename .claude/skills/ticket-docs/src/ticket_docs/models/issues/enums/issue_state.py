from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class IssueState(StrEnum):
    """The state of a GitHub issue, as the REST API writes it.

    Attributes:
        OPEN (str): The issue is open: every rule of GIT-10 applies to it.
        CLOSED (str): The issue is closed: only its labels and its parent are checked.
    """

    OPEN = "open"
    CLOSED = "closed"
