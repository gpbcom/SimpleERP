from __future__ import annotations

from progress_updates.models.catalogs.exceptions.catalog.se_invalid_progress_catalog_exception import (
    SEInvalidProgressCatalogException,
)


class SEProgressCatalogInvalidHealthIcons(SEInvalidProgressCatalogException):
    """Exception raised when an invalid ``health_icons`` is provided."""
