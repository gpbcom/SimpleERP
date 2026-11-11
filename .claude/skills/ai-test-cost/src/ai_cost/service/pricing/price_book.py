from __future__ import annotations

# Standard library imports
from decimal import ROUND_CEILING, Decimal
from logging import Logger, getLogger
from typing import ClassVar, Optional

# First-party imports
from ai_cost.models.ledger.model_usage import ModelUsage
from ai_cost.models.pricing.model_price import ModelPrice
from ai_cost.models.pricing.price_table import PriceTable


class PriceBook:
    """Prices the tokens a run used on each model.

    Attributes:
        MILLION (Decimal): Tokens per priced unit.
        CENT_FRACTION (Decimal): The precision a cost is kept to: a millionth of a dollar.
        table (PriceTable): The prices.
        logger (Logger): Logger instance.

    Notes:
        A model the table does not know is priced as the most expensive one (the highest output price, then input
        price), so that the cap is never reached later than it should be.
    """

    MILLION: ClassVar[Decimal] = Decimal(1_000_000)
    CENT_FRACTION: ClassVar[Decimal] = Decimal("0.000001")

    def __init__(self, table: PriceTable, logger: Optional[Logger] = None) -> None:
        """Set the prices.

        Args:
            table (PriceTable): The prices.
            logger (Optional[Logger]): Logger instance.
        """
        self.table = table
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def most_expensive(self) -> ModelPrice:
        """The price of the most expensive model, used for a model the table does not know."""
        return max(self.table.prices, key=lambda price: (price.output_per_mtok, price.input_per_mtok))

    @property
    def source(self) -> str:
        """Where the prices come from and when they were read, for ``COST.md``."""
        return f"{self.table.source}, read {self.table.read_on.isoformat()}"

    def price_of(self, model_id: str) -> ModelPrice:
        """Find the price of a model.

        Args:
            model_id (str): The model id the usage report gives.

        Returns:
            ModelPrice: The first price whose ``match`` the id contains, else the most expensive one.
        """
        price = next((price for price in self.table.prices if price.match in model_id), None)
        if price is None:
            self.logger.warning("No price for %s: priced as %s.", model_id, self.most_expensive.name)
            return self.most_expensive
        return price

    def priced(self, model_id: str, usage: ModelUsage) -> ModelUsage:
        """Set what the tokens of one model cost.

        Args:
            model_id (str): The model id.
            usage (ModelUsage): The tokens.

        Returns:
            ModelUsage: The same tokens with their cost, rounded up to the millionth of a dollar.
        """
        price = self.price_of(model_id)
        cost = (
            usage.input_tokens * price.input_per_mtok
            + usage.output_tokens * price.output_per_mtok
            + usage.cache_read_tokens * price.cache_read_per_mtok
            + usage.cache_write_5m_tokens * price.cache_write_5m_per_mtok
            + usage.cache_write_1h_tokens * price.cache_write_1h_per_mtok
        ) / self.MILLION
        priced = usage.model_copy(update={"cost_usd": cost.quantize(self.CENT_FRACTION, rounding=ROUND_CEILING)})
        self.logger.debug("Priced %s at $%s.", model_id, priced.cost_usd)
        return priced
