from __future__ import annotations

from erp_models.events.exceptions.se_invalid_event_envelope_exception import SEInvalidEventEnvelopeException


class SEEventEnvelopeInvalidOccurredAt(SEInvalidEventEnvelopeException):
    """Exception raised when an invalid ``occurred_at`` is provided."""
