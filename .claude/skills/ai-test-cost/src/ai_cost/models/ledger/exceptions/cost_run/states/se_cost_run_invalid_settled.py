from __future__ import annotations

from ai_cost.models.ledger.exceptions.cost_run.se_invalid_cost_run_exception import SEInvalidCostRunException


class SECostRunInvalidSettled(SEInvalidCostRunException):
    """Exception raised when an invalid ``settled`` is provided."""
