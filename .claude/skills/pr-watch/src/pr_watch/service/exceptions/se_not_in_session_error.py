from __future__ import annotations

from pr_watch.service.exceptions.se_pr_watch_service_error import SEPrWatchServiceError


class SENotInSessionError(SEPrWatchServiceError):
    """Raised when a command needs a Claude Code session and none is known."""
