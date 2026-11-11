from __future__ import annotations

from release_notes.models.exceptions import SEReleaseNotesError


class SEInvalidSemanticVersionException(SEReleaseNotesError):
    """Exception raised when an invalid SemanticVersion is provided."""
