from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidPullRequestStateException(SEPrWatchError):
    """Exception raised when an invalid PullRequestState is provided."""
