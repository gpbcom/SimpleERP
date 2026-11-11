from __future__ import annotations

# Standard library imports
from datetime import datetime
from logging import Logger
from typing import Dict, Optional

# First-party imports
from ai_cost.models.ledger.model_usage import ModelUsage
from ai_cost.service.pricing.price_book import PriceBook
from ai_cost.service.usage.exceptions import SEUsageMeasureFailedError
from ai_cost.service.usage.usage_meter import UsageMeter
from ai_cost.storage.usage.anthropic_usage_client import AnthropicUsageClient
from ai_cost.storage.usage.exceptions import SEAnthropicUsageError


class AnthropicUsageMeter(UsageMeter):
    """Measures a run from the Anthropic Admin API usage report, priced with ``conf/prices.yaml``.

    Attributes:
        client (AnthropicUsageClient): Reads the usage report.
        prices (PriceBook): Prices the tokens.
        logger (Logger): Logger instance.

    Notes:
        The report counts every call of the organisation, or of the API key named by ``AI_COST_API_KEY_ID``, in the
        run's minutes: other calls made at the same time are counted too, so the cap errs on the safe side.
    """

    def __init__(self, client: AnthropicUsageClient, prices: PriceBook, logger: Optional[Logger] = None) -> None:
        """Set the report client and the prices.

        Args:
            client (AnthropicUsageClient): Reads the usage report.
            prices (PriceBook): Prices the tokens.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.client = client
        self.prices = prices

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def measurable(self) -> bool:
        """Always ``True``: the usage report measures every run."""
        return True

    def ready(self) -> bool:
        """Tell whether the admin key is set.

        Returns:
            bool: ``True`` when the usage report can be read.
        """
        return self.client.configured

    def measure(self, start: datetime, end: datetime) -> Dict[str, ModelUsage]:
        """Measure and price the calls between two moments.

        Args:
            start (datetime): The start of the window.
            end (datetime): The end of the window.

        Returns:
            Dict[str, ModelUsage]: The tokens and cost of each model.

        Raises:
            SEUsageMeasureFailedError: When the usage report cannot be read.
        """
        try:
            tokens = self.client.usage(start, end)
        except SEAnthropicUsageError as error:
            self.logger.error("The run's usage could not be measured: %s.", type(error).__name__)
            raise SEUsageMeasureFailedError(f"The usage report could not be read: {error}") from error
        priced = {model: self.prices.priced(model, usage) for model, usage in tokens.items()}
        self.logger.info("Measured %d models from %s to %s.", len(priced), start, end)
        return priced
