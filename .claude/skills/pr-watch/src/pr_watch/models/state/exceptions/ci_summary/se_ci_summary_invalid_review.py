from __future__ import annotations

from pr_watch.models.state.exceptions.se_invalid_ci_summary_exception import SEInvalidCiSummaryException


class SECiSummaryInvalidReview(SEInvalidCiSummaryException):
    """Exception raised when an invalid ``review`` is provided."""
