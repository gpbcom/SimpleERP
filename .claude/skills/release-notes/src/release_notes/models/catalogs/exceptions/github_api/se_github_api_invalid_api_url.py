from __future__ import annotations

from release_notes.models.catalogs.exceptions.github_api.se_invalid_github_api_exception import (
    SEInvalidGithubApiException,
)


class SEGithubApiInvalidApiUrl(SEInvalidGithubApiException):
    """Exception raised when an invalid ``api_url`` is provided."""
