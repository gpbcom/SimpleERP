from __future__ import annotations

from ticket_docs.models.hooks.exceptions.file_hook_payload.se_invalid_file_hook_payload_exception import (
    SEInvalidFileHookPayloadException,
)


class SEFileHookPayloadInvalidPath(SEInvalidFileHookPayloadException):
    """Exception raised when an invalid ``path`` is provided."""
