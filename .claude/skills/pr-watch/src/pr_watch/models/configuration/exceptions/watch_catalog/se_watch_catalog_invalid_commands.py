from __future__ import annotations

from pr_watch.models.configuration.exceptions.se_invalid_watch_catalog_exception import SEInvalidWatchCatalogException


class SEWatchCatalogInvalidCommands(SEInvalidWatchCatalogException):
    """Exception raised when an invalid ``commands`` is provided."""
