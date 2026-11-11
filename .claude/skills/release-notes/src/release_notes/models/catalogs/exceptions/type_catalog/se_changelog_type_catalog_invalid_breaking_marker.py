from __future__ import annotations

from release_notes.models.catalogs.exceptions.type_catalog.se_invalid_changelog_type_catalog_exception import (
    SEInvalidChangelogTypeCatalogException,
)


class SEChangelogTypeCatalogInvalidBreakingMarker(SEInvalidChangelogTypeCatalogException):
    """Exception raised when an invalid ``breaking_marker`` is provided."""
