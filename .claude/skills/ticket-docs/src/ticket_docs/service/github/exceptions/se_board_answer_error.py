from __future__ import annotations

from ticket_docs.service.github.exceptions.se_github_service_error import SEGithubServiceError


class SEBoardAnswerError(SEGithubServiceError):
    """Raised when GitHub's answer does not hold the issue or the board item."""
