from __future__ import annotations

from ai_cost.models.pricing.exceptions.price_table.se_invalid_price_table_exception import SEInvalidPriceTableException


class SEPriceTableInvalidReadOn(SEInvalidPriceTableException):
    """Exception raised when an invalid ``read_on`` is provided."""
