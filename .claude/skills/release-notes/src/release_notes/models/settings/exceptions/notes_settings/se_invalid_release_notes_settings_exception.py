from __future__ import annotations

from release_notes.models.exceptions import SEReleaseNotesError


class SEInvalidReleaseNotesSettingsException(SEReleaseNotesError):
    """Exception raised when an invalid ReleaseNotesSettings is provided."""
