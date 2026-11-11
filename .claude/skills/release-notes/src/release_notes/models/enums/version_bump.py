from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class VersionBump(StrEnum):
    """The part of a semantic version a change bumps.

    Attributes:
        MAJOR: A breaking change, ``1.4.2`` to ``2.0.0``.
        MINOR: A new feature, ``1.4.2`` to ``1.5.0``.
        PATCH: A fix, ``1.4.2`` to ``1.4.3``.
    """

    MAJOR = "major"
    MINOR = "minor"
    PATCH = "patch"
