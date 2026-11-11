from __future__ import annotations

from ticket_docs.models.evidence.exceptions.run_request.se_invalid_run_request_exception import (
    SEInvalidRunRequestException,
)


class SERunRequestInvalidTicket(SEInvalidRunRequestException):
    """Exception raised when an invalid ``ticket`` is provided."""
