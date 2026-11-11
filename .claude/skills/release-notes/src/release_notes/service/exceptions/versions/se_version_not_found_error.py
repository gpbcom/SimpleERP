from __future__ import annotations

from release_notes.service.exceptions.se_release_notes_service_error import SEReleaseNotesServiceError


class SEVersionNotFoundError(SEReleaseNotesServiceError):
    """Raised when a version has no section in CHANGELOG.md."""
