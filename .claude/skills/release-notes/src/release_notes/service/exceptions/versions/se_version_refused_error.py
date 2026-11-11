from __future__ import annotations

from release_notes.service.exceptions.se_release_notes_service_error import SEReleaseNotesServiceError


class SEVersionRefusedError(SEReleaseNotesServiceError):
    """Raised when a version cannot be released: unparsable, already released or not newer than the last one."""
