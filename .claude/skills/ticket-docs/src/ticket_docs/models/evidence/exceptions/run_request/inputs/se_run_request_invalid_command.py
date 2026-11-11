from __future__ import annotations

from ticket_docs.models.evidence.exceptions.run_request.se_invalid_run_request_exception import (
    SEInvalidRunRequestException,
)


class SERunRequestInvalidCommand(SEInvalidRunRequestException):
    """Exception raised when an invalid ``command`` is provided."""
