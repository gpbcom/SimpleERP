from __future__ import annotations

from erp_outbox.models.exceptions.se_outbox_error import SEOutboxError


class SEOutboxPublishError(SEOutboxError):
    """Raised when the publisher refuses an event."""
