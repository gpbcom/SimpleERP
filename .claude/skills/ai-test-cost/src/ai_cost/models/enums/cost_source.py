from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class CostSource(StrEnum):
    """Where the cost of a run comes from.

    Attributes:
        USAGE_REPORT (str): Measured from the Anthropic Admin API usage report.
        ESTIMATE (str): The run's own estimate, charged because nothing measures it.
        CHARGED (str): A cost measured elsewhere and charged by hand.
    """

    USAGE_REPORT = "usage_report"
    ESTIMATE = "estimate"
    CHARGED = "charged"
