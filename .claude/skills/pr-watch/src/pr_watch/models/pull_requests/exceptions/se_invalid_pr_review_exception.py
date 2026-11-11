from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidPrReviewException(SEPrWatchError):
    """Exception raised when an invalid PrReview is provided."""
