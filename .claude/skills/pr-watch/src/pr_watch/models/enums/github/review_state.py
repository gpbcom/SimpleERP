from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class ReviewState(StrEnum):
    """What a reviewer decided, as GitHub names it.

    Attributes:
        APPROVED: The reviewer approved.
        CHANGES_REQUESTED: The reviewer asked for changes.
        COMMENTED: The reviewer only commented.
        DISMISSED: The review was dismissed.
        PENDING: The review is not submitted yet.
    """

    APPROVED = "APPROVED"
    CHANGES_REQUESTED = "CHANGES_REQUESTED"
    COMMENTED = "COMMENTED"
    DISMISSED = "DISMISSED"
    PENDING = "PENDING"
