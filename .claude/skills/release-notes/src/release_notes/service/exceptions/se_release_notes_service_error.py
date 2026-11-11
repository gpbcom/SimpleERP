from __future__ import annotations

from release_notes.models.exceptions import SEReleaseNotesError


class SEReleaseNotesServiceError(SEReleaseNotesError):
    """Base class for every error raised while checking or building the changelog and the release notes."""
