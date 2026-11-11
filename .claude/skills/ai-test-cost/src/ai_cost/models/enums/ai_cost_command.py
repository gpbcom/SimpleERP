from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class AiCostCommand(StrEnum):
    """The commands of the ``ai-cost`` command line.

    Attributes:
        RUN (str): Run a paid AI test within its ticket's cap.
        STATUS (str): Print a ticket's spend and runs.
        REMAINING (str): Print what a ticket may still spend.
        CHARGE (str): Charge a cost measured elsewhere.
        RAISE_CAP (str): Set a ticket's cap, for the human only.
        GATE (str): Answer the PreToolUse hook on Bash.
    """

    RUN = "run"
    STATUS = "status"
    REMAINING = "remaining"
    CHARGE = "charge"
    RAISE_CAP = "raise-cap"
    GATE = "gate"
