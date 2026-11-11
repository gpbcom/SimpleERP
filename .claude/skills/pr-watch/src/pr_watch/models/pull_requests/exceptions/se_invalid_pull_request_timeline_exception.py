from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidPullRequestTimelineException(SEPrWatchError):
    """Exception raised when an invalid PullRequestTimeline is provided."""
