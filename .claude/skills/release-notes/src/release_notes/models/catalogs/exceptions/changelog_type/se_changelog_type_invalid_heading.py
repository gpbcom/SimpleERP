from __future__ import annotations

from release_notes.models.catalogs.exceptions.changelog_type.se_invalid_changelog_type_exception import (
    SEInvalidChangelogTypeException,
)


class SEChangelogTypeInvalidHeading(SEInvalidChangelogTypeException):
    """Exception raised when an invalid ``heading`` is provided."""
