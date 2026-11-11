from __future__ import annotations

from release_notes.models.catalogs.exceptions.github_coordinates.se_invalid_github_coordinates_exception import (
    SEInvalidGithubCoordinatesException,
)


class SEGithubCoordinatesInvalidRepository(SEInvalidGithubCoordinatesException):
    """Exception raised when an invalid ``repository`` is provided."""
