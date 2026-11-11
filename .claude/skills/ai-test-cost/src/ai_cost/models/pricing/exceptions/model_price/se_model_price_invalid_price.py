from __future__ import annotations

from ai_cost.models.pricing.exceptions.model_price.se_invalid_model_price_exception import SEInvalidModelPriceException


class SEModelPriceInvalidPrice(SEInvalidModelPriceException):
    """Exception raised when an invalid price per million tokens is provided."""
