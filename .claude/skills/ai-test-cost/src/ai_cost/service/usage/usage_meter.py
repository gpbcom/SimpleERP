from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod
from datetime import datetime
from logging import Logger, getLogger
from typing import Dict, Optional

# First-party imports
from ai_cost.models.ledger.model_usage import ModelUsage


class UsageMeter(ABC):
    """Measures what the paid AI calls of a time window cost, model by model.

    Attributes:
        logger (Logger): Logger instance.

    Notes:
        Each ``UsageSource`` has its meter. A meter that is not ``measurable`` makes every run soft: the run is
        charged its estimate.
    """

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    @abstractmethod
    def measurable(self) -> bool:
        """Whether this meter measures anything at all."""

    @abstractmethod
    def ready(self) -> bool:
        """Tell whether a measure can be taken now.

        Returns:
            bool: ``False`` when something the measure needs, such as a key, is missing.
        """

    @abstractmethod
    def measure(self, start: datetime, end: datetime) -> Dict[str, ModelUsage]:
        """Measure the paid AI calls between two moments.

        Args:
            start (datetime): The start of the window.
            end (datetime): The end of the window.

        Returns:
            Dict[str, ModelUsage]: The tokens and cost of each model.

        Raises:
            SEUsageMeasureFailedError: When the measure cannot be taken.
        """
