from __future__ import annotations

from pr_watch.service.exceptions.se_pr_watch_service_error import SEPrWatchServiceError


class SEPullRequestLinkInvalidError(SEPrWatchServiceError):
    """Raised when a link is not a GitHub pull request link."""
