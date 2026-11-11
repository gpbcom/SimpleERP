from __future__ import annotations

from ticket_docs.models.evidence.exceptions.run_request.se_invalid_run_request_exception import (
    SEInvalidRunRequestException,
)


class SERunRequestInvalidCheck(SEInvalidRunRequestException):
    """Exception raised when an invalid ``check`` is provided."""
