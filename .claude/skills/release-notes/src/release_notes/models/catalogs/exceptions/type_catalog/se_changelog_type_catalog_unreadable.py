from __future__ import annotations

from release_notes.models.catalogs.exceptions.type_catalog.se_invalid_changelog_type_catalog_exception import (
    SEInvalidChangelogTypeCatalogException,
)


class SEChangelogTypeCatalogUnreadable(SEInvalidChangelogTypeCatalogException):
    """Exception raised when the changelog types file cannot be read or parsed."""
