from __future__ import annotations

from pr_watch.models.configuration.exceptions.se_invalid_watch_catalog_exception import SEInvalidWatchCatalogException


class SEWatchCatalogUnreadable(SEInvalidWatchCatalogException):
    """Exception raised when the watcher's catalogue cannot be read."""
