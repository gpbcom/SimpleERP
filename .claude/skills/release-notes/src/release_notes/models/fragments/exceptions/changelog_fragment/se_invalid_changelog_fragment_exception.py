from __future__ import annotations

from release_notes.models.exceptions import SEReleaseNotesError


class SEInvalidChangelogFragmentException(SEReleaseNotesError):
    """Exception raised when an invalid ChangelogFragment is provided."""
