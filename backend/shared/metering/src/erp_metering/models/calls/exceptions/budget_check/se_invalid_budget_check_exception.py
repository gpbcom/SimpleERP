from __future__ import annotations

# First-party imports
from erp_models.exceptions import SEInvalidModelException


class SEInvalidBudgetCheckException(SEInvalidModelException):
    """Exception raised when an invalid BudgetCheck is provided.

    Notes:
        It subclasses ``Exception`` and not ``ValueError``, so that Pydantic does not wrap it in a
        ``ValidationError``.
    """
