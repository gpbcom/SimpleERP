from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class MergeableState(StrEnum):
    """What GitHub says of merging a pull request.

    Attributes:
        CLEAN: It merges, and every requirement is met.
        DIRTY: It conflicts with its base.
        BLOCKED: A requirement blocks it.
        BEHIND: Its head is behind its base.
        UNSTABLE: It merges, with failing checks.
        HAS_HOOKS: It merges, with pre-receive hooks.
        UNKNOWN: GitHub has not computed it yet.
        DRAFT: It is a draft.
    """

    CLEAN = "clean"
    DIRTY = "dirty"
    BLOCKED = "blocked"
    BEHIND = "behind"
    UNSTABLE = "unstable"
    HAS_HOOKS = "has_hooks"
    UNKNOWN = "unknown"
    DRAFT = "draft"
