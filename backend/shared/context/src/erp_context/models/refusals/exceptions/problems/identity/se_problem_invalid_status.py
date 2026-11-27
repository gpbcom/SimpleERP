from __future__ import annotations

from erp_context.models.refusals.exceptions.problems.se_invalid_problem_exception import SEInvalidProblemException


class SEProblemInvalidStatus(SEInvalidProblemException):
    """Exception raised when an invalid ``status`` is provided."""
