from __future__ import annotations

# First-party imports
from erp_metering.models.calls.exceptions.budget_check.se_invalid_budget_check_exception import (
    SEInvalidBudgetCheckException,
)


class SEBudgetCheckInvalidWithinBudget(SEInvalidBudgetCheckException):
    """Exception raised when an invalid ``within_budget`` is provided."""
