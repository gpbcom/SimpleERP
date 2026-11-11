from __future__ import annotations

from ai_cost.models.pricing.exceptions.price_table.se_invalid_price_table_exception import SEInvalidPriceTableException


class SEPriceTableInvalidSource(SEInvalidPriceTableException):
    """Exception raised when an invalid ``source`` is provided."""
