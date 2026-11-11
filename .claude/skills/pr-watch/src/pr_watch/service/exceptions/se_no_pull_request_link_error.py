from __future__ import annotations

from pr_watch.service.exceptions.se_pr_watch_service_error import SEPrWatchServiceError


class SENoPullRequestLinkError(SEPrWatchServiceError):
    """Raised when a ticket has no pull request link to watch."""
