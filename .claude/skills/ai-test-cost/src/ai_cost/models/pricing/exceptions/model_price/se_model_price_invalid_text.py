from __future__ import annotations

from ai_cost.models.pricing.exceptions.model_price.se_invalid_model_price_exception import SEInvalidModelPriceException


class SEModelPriceInvalidText(SEInvalidModelPriceException):
    """Exception raised when an invalid ``name`` or ``match`` is provided."""
