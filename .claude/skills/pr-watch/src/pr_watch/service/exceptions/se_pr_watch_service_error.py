from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEPrWatchServiceError(SEPrWatchError):
    """Base class for every error raised while handling a watched pull request."""
