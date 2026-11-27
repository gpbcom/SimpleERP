from __future__ import annotations

from erp_outbox.models.exceptions.se_outbox_error import SEOutboxError


class SEOutboxStoreError(SEOutboxError):
    """Raised when the outbox table cannot be read or written."""
