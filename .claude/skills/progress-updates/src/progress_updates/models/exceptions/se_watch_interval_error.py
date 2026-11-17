from __future__ import annotations

from progress_updates.models.exceptions.se_progress_updates_error import SEProgressUpdatesError


class SEWatchIntervalError(SEProgressUpdatesError):
    """Raised when a watch is asked to report more often than the catalogue allows."""
