from __future__ import annotations

from ticket_docs.storage.github.exceptions.se_gh_error import SEGhError


class SEGhAnswerUnreadableError(SEGhError):
    """Raised when gh answers with something that is not the JSON asked for."""
