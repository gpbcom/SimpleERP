from __future__ import annotations

from pr_watch.models.checks.exceptions.se_invalid_check_run_exception import SEInvalidCheckRunException


class SECheckRunInvalidConclusion(SEInvalidCheckRunException):
    """Exception raised when an invalid ``conclusion`` is provided."""
