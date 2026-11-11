from __future__ import annotations

from release_notes.models.fragments.exceptions.changelog_fragment.se_invalid_changelog_fragment_exception import (
    SEInvalidChangelogFragmentException,
)


class SEChangelogFragmentInvalidTicket(SEInvalidChangelogFragmentException):
    """Exception raised when an invalid ``ticket`` is provided."""
