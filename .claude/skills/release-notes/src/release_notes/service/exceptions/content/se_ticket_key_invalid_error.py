from __future__ import annotations

from release_notes.service.exceptions.se_release_notes_service_error import SEReleaseNotesServiceError


class SETicketKeyInvalidError(SEReleaseNotesServiceError):
    """Raised when a ticket key is not ``GH-<n>``."""
