from __future__ import annotations

from pr_watch.service.exceptions.se_pr_watch_service_error import SEPrWatchServiceError


class SEWatchNotFoundError(SEPrWatchServiceError):
    """Raised when a ticket has no watched pull request, or several and none was chosen."""
