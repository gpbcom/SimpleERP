from __future__ import annotations

from erp_platform.service.problems.exceptions.se_problem_error import SEProblemError


class SEProblemUnknownCodeError(SEProblemError):
    """Raised when a problem is asked for a code that is not in the error catalogue."""
