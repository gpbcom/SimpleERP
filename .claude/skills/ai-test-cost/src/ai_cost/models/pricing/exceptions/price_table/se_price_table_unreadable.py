from __future__ import annotations

from ai_cost.models.pricing.exceptions.price_table.se_invalid_price_table_exception import SEInvalidPriceTableException


class SEPriceTableUnreadable(SEInvalidPriceTableException):
    """Exception raised when the price file cannot be read or parsed."""
