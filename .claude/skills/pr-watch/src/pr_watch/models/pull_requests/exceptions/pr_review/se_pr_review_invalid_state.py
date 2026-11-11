from __future__ import annotations

from pr_watch.models.pull_requests.exceptions.se_invalid_pr_review_exception import SEInvalidPrReviewException


class SEPrReviewInvalidState(SEInvalidPrReviewException):
    """Exception raised when an invalid ``state`` is provided."""
