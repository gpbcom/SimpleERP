from __future__ import annotations

from erp_platform.models.problems.exceptions.se_invalid_problem_details_exception import (
    SEInvalidProblemDetailsException,
)


class SEProblemDetailsInvalidDetail(SEInvalidProblemDetailsException):
    """Exception raised when an invalid ``detail`` is provided."""
