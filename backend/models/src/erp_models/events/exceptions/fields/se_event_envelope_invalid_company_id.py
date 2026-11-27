from __future__ import annotations

from erp_models.events.exceptions.se_invalid_event_envelope_exception import SEInvalidEventEnvelopeException


class SEEventEnvelopeInvalidCompanyId(SEInvalidEventEnvelopeException):
    """Exception raised when an invalid ``company_id`` is provided."""
