from __future__ import annotations

from ai_cost.models.ledger.exceptions.cost_run.se_invalid_cost_run_exception import SEInvalidCostRunException


class SECostRunInvalidText(SEInvalidCostRunException):
    """Exception raised when an invalid ``id``, ``label``, ``command`` or ``note`` is provided."""
