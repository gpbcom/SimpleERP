from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class HealthState(StrEnum):
    """The states a health answer can report.

    Attributes:
        OK (str): The service is up and answering.
    """

    OK = "ok"
