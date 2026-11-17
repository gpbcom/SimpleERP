from __future__ import annotations

from progress_updates.models.catalogs.exceptions.catalog.se_invalid_progress_catalog_exception import (
    SEInvalidProgressCatalogException,
)


class SEProgressCatalogInvalidEvidenceMax(SEInvalidProgressCatalogException):
    """Exception raised when an invalid ``evidence_max`` is provided."""
