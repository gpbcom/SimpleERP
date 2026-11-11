from __future__ import annotations

from release_notes.models.exceptions import SEReleaseNotesError


class SEInvalidChangelogTypeCatalogException(SEReleaseNotesError):
    """Exception raised when an invalid ChangelogTypeCatalog is provided."""
