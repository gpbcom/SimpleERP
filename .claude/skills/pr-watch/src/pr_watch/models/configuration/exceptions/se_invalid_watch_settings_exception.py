from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidWatchSettingsException(SEPrWatchError):
    """Exception raised when an invalid WatchSettings is provided."""
