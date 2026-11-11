from __future__ import annotations

from ticket_docs.models.evidence.exceptions.run_request.se_invalid_run_request_exception import (
    SEInvalidRunRequestException,
)


class SERunRequestNoCommand(SEInvalidRunRequestException):
    """Exception raised when neither or both of ``command`` and ``run_id`` are provided."""
