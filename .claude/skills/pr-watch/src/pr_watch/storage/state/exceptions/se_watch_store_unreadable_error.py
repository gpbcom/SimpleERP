from __future__ import annotations

from pr_watch.storage.state.exceptions.se_watch_store_error import SEWatchStoreError


class SEWatchStoreUnreadableError(SEWatchStoreError):
    """Raised when a state file cannot be read back."""
