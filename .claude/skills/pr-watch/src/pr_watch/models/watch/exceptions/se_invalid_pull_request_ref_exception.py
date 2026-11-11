from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidPullRequestRefException(SEPrWatchError):
    """Exception raised when an invalid PullRequestRef is provided."""
