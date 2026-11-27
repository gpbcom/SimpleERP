from __future__ import annotations

from erp_models.events.exceptions.se_invalid_event_envelope_exception import SEInvalidEventEnvelopeException


class SEEventEnvelopeInvalidEventId(SEInvalidEventEnvelopeException):
    """Exception raised when an invalid ``event_id`` is provided."""
