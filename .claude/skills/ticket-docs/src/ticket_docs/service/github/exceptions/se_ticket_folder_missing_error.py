from __future__ import annotations

from ticket_docs.service.github.exceptions.se_github_service_error import SEGithubServiceError


class SETicketFolderMissingError(SEGithubServiceError):
    """Raised when the ticket has no folder to archive."""
