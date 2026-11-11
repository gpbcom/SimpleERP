from __future__ import annotations

from release_notes.service.exceptions.se_release_notes_service_error import SEReleaseNotesServiceError


class SEFragmentsRefusedError(SEReleaseNotesServiceError):
    """Raised when the changelog fragments cannot be released: none, or some invalid."""
