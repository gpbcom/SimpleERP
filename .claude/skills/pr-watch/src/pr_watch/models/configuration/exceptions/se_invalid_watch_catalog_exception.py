from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidWatchCatalogException(SEPrWatchError):
    """Exception raised when an invalid WatchCatalog is provided."""
