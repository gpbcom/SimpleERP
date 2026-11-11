from __future__ import annotations

from pr_watch.models.state.exceptions.se_invalid_ci_summary_exception import SEInvalidCiSummaryException


class SECiSummaryInvalidChecks(SEInvalidCiSummaryException):
    """Exception raised when an invalid ``checks`` is provided."""
