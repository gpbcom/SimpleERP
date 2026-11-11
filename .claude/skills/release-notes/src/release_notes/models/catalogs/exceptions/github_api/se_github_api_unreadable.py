from __future__ import annotations

from release_notes.models.catalogs.exceptions.github_api.se_invalid_github_api_exception import (
    SEInvalidGithubApiException,
)


class SEGithubApiUnreadable(SEInvalidGithubApiException):
    """Exception raised when the GitHub API file cannot be read or parsed."""
