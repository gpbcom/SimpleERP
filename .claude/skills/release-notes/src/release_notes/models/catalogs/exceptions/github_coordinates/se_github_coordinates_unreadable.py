from __future__ import annotations

from release_notes.models.catalogs.exceptions.github_coordinates.se_invalid_github_coordinates_exception import (
    SEInvalidGithubCoordinatesException,
)


class SEGithubCoordinatesUnreadable(SEInvalidGithubCoordinatesException):
    """Exception raised when the GitHub coordinates file cannot be read or parsed."""
