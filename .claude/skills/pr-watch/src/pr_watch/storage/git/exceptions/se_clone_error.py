from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SECloneError(SEPrWatchError):
    """Base class for every error raised while reading the local clone."""
