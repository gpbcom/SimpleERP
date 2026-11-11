from __future__ import annotations

from ai_cost.models.ledger.exceptions.cost_run.se_invalid_cost_run_exception import SEInvalidCostRunException


class SECostRunInvalidMoment(SEInvalidCostRunException):
    """Exception raised when an invalid ``started_on`` or ``finished_on`` is provided."""
