from __future__ import annotations

from progress_updates.models.catalogs.exceptions.catalog.se_invalid_progress_catalog_exception import (
    SEInvalidProgressCatalogException,
)


class SEProgressCatalogInvalidLineMaxChars(SEInvalidProgressCatalogException):
    """Exception raised when an invalid ``line_max_chars`` is provided."""
