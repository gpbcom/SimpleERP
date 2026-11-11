from __future__ import annotations

from ai_cost.models.ledger.exceptions.model_usage.se_invalid_model_usage_exception import SEInvalidModelUsageException


class SEModelUsageInvalidCostUsd(SEInvalidModelUsageException):
    """Exception raised when an invalid ``cost_usd`` is provided."""
