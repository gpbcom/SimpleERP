from __future__ import annotations

from release_notes.models.exceptions import SEReleaseNotesError


class SEInvalidGithubApiException(SEReleaseNotesError):
    """Exception raised when an invalid GithubApi is provided."""
