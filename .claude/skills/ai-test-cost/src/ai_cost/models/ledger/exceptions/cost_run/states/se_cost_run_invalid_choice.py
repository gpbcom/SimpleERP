from __future__ import annotations

from ai_cost.models.ledger.exceptions.cost_run.se_invalid_cost_run_exception import SEInvalidCostRunException


class SECostRunInvalidChoice(SEInvalidCostRunException):
    """Exception raised when an invalid ``status`` or ``source`` is provided."""
