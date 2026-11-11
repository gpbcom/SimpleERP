from __future__ import annotations

from project_docs.service.exceptions.se_project_docs_service_error import SEProjectDocsServiceError


class SETicketKeyInvalidError(SEProjectDocsServiceError):
    """Raised when a ticket key is not ``GH-<n>``."""
