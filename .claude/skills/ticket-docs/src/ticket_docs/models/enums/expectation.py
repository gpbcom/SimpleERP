from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class Expectation(StrEnum):
    """How a recorded run is expected to end.

    Attributes:
        RED (str): The tests are written before the code, so the run must fail.
        GREEN (str): The run must pass.
    """

    RED = "red"
    GREEN = "green"
