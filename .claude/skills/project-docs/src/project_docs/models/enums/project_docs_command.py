from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class ProjectDocsCommand(StrEnum):
    """The commands of ``project-docs``.

    Attributes:
        MAP: List the chapters the branch's changed files concern.
        CHECK: Print every problem of the documentation, nothing when it is complete.
    """

    MAP = "map"
    CHECK = "check"
