from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class PolicyEffect(StrEnum):
    """The effect of one policy on an action.

    Attributes:
        ALLOW: The policy allows the action.
        DENY: The policy denies the action.
        ABSTAIN: The policy has no opinion on the action.
    """

    ALLOW = "allow"
    DENY = "deny"
    ABSTAIN = "abstain"
