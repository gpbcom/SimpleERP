from __future__ import annotations

# Standard library imports
from datetime import datetime
from typing import Dict

# First-party imports
from ai_cost.models.ledger.model_usage import ModelUsage
from ai_cost.service.usage.usage_meter import UsageMeter


class EstimateUsageMeter(UsageMeter):
    """The meter of the ``estimate`` usage source: it measures nothing, so each run is charged its estimate.

    Attributes:
        logger (Logger): Logger instance.

    Notes:
        ``ai-cost charge`` then corrects a run's cost with the figure read where the calls are billed.
    """

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def measurable(self) -> bool:
        """Always ``False``: nothing is measured."""
        return False

    def ready(self) -> bool:
        """Tell that the meter needs nothing.

        Returns:
            bool: Always ``True``.
        """
        return True

    def measure(self, start: datetime, end: datetime) -> Dict[str, ModelUsage]:
        """Measure nothing.

        Args:
            start (datetime): The start of the window.
            end (datetime): The end of the window.

        Returns:
            Dict[str, ModelUsage]: Always empty.
        """
        self.logger.debug("Nothing measured from %s to %s: runs are charged their estimate.", start, end)
        return {}
