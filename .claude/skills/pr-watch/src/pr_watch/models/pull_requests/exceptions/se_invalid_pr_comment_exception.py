from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidPrCommentException(SEPrWatchError):
    """Exception raised when an invalid PrComment is provided."""
