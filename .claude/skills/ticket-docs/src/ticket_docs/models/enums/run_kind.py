from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class RunKind(StrEnum):
    """What an evidence run tested.

    Attributes:
        UNIT (str): Unit tests, kept with their JUnit and HTML reports.
        GUI (str): Playwright tests of a front end.
        E2E (str): End-to-end tests, such as a stage run.
        CHECK (str): A check that is not a test, such as a linter or a rule check.
    """

    UNIT = "unit"
    GUI = "gui"
    E2E = "e2e"
    CHECK = "check"
