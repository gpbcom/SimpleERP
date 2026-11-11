from __future__ import annotations

from release_notes.models.exceptions import SEReleaseNotesError


class SEInvalidGithubCoordinatesException(SEReleaseNotesError):
    """Exception raised when an invalid GithubCoordinates is provided."""
