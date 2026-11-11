from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class RunPlace(StrEnum):
    """Where an evidence run ran.

    Attributes:
        LOCAL (str): On the developer's machine.
        CI (str): In the CI workflow on GitHub Actions.
        DEV (str): On the ephemeral dev stage.
        QA (str): On the ephemeral QA stage.
    """

    LOCAL = "local"
    CI = "ci"
    DEV = "dev"
    QA = "qa"
