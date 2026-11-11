from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEWatchStoreError(SEPrWatchError):
    """Base class for every error raised while reading or writing the watcher's state."""
