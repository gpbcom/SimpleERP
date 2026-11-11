from __future__ import annotations

from ticket_docs.models.hooks.exceptions.hook_payload.se_invalid_hook_payload_exception import (
    SEInvalidHookPayloadException,
)


class SEHookPayloadInvalidCwd(SEInvalidHookPayloadException):
    """Exception raised when an invalid ``cwd`` is provided."""
