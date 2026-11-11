from __future__ import annotations

from ticket_docs.storage.github.exceptions.se_gh_error import SEGhError


class SEGhCommandFailedError(SEGhError):
    """Raised when a gh command exits with an error."""
