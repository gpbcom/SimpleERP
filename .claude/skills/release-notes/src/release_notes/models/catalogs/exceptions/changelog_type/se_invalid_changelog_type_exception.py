from __future__ import annotations

from release_notes.models.exceptions import SEReleaseNotesError


class SEInvalidChangelogTypeException(SEReleaseNotesError):
    """Exception raised when an invalid ChangelogType is provided."""
