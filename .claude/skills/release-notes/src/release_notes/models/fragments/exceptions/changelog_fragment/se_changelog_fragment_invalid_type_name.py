from __future__ import annotations

from release_notes.models.fragments.exceptions.changelog_fragment.se_invalid_changelog_fragment_exception import (
    SEInvalidChangelogFragmentException,
)


class SEChangelogFragmentInvalidTypeName(SEInvalidChangelogFragmentException):
    """Exception raised when an invalid ``type_name`` is provided."""
