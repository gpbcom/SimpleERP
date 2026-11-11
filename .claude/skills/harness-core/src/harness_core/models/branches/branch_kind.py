from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class BranchKind(StrEnum):
    """The GitFlow role of a branch.

    Attributes:
        MASTER: ``master``, what is released.
        DEVELOP: ``develop``, the integration branch.
        FEATURE: ``feature/GH-<n>-<slug>``, new work for one issue.
        BUGFIX: ``bugfix/GH-<n>-<slug>``, a fix for one issue, made on ``develop``.
        RELEASE: ``release/<x.y.z>``, a version being stabilised.
        HOTFIX: ``hotfix/<x.y.z>-GH-<n>-<slug>``, an urgent fix made on ``main``.
        OTHER: Any other branch, such as a Dependabot one.
    """

    MASTER = "master"
    DEVELOP = "develop"
    FEATURE = "feature"
    BUGFIX = "bugfix"
    RELEASE = "release"
    HOTFIX = "hotfix"
    OTHER = "other"
