from __future__ import annotations

from erp_models.exceptions import SEError


class SEOutboxError(SEError):
    """Base class for every error raised while storing or publishing an outbox event."""
