from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class RefusalReason(StrEnum):
    """Why a request was refused.

    Attributes:
        NO_COMPANY: The request names no company.
        NO_USER: The request has no authenticated user.
        NO_POLICY: No policy covers the action.
        POLICY_DENIED: A policy denied the action.
        OTHER_COMPANY: The record belongs to another company.
    """

    NO_COMPANY = "no-company"
    NO_USER = "no-user"
    NO_POLICY = "no-policy"
    POLICY_DENIED = "policy-denied"
    OTHER_COMPANY = "other-company"
