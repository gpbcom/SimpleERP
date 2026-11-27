from __future__ import annotations

from erp_context.models.refusals.exceptions.problems.se_invalid_problem_exception import SEInvalidProblemException


class SEProblemInvalidDetail(SEInvalidProblemException):
    """Exception raised when an invalid ``detail`` is provided."""
