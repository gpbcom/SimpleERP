from __future__ import annotations

from ai_cost.models.ledger.exceptions.cost_run.se_invalid_cost_run_exception import SEInvalidCostRunException


class SECostRunInvalidAmount(SEInvalidCostRunException):
    """Exception raised when an invalid ``estimate_usd`` or ``cost_usd`` is provided."""
