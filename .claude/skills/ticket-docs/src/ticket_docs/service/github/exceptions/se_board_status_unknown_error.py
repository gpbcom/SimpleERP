from __future__ import annotations

from ticket_docs.service.github.exceptions.se_github_service_error import SEGithubServiceError


class SEBoardStatusUnknownError(SEGithubServiceError):
    """Raised when a status is not one of the board's."""
