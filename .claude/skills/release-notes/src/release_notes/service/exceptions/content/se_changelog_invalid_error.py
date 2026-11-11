from __future__ import annotations

from release_notes.service.exceptions.se_release_notes_service_error import SEReleaseNotesServiceError


class SEChangelogInvalidError(SEReleaseNotesServiceError):
    """Raised when CHANGELOG.md lacks the structure a release needs."""
