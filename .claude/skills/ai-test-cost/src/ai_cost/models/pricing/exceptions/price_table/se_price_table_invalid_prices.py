from __future__ import annotations

from ai_cost.models.pricing.exceptions.price_table.se_invalid_price_table_exception import SEInvalidPriceTableException


class SEPriceTableInvalidPrices(SEInvalidPriceTableException):
    """Exception raised when an invalid ``prices`` is provided."""
