from __future__ import annotations

from ai_cost.models.ledger.exceptions.cost_run.se_invalid_cost_run_exception import SEInvalidCostRunException


class SECostRunInvalidExitCode(SEInvalidCostRunException):
    """Exception raised when an invalid ``exit_code`` is provided."""
