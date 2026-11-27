from __future__ import annotations

from erp_context.models.rights.exceptions.se_invalid_rights_decision_exception import (
    SEInvalidRightsDecisionException,
)


class SERightsDecisionInvalidReason(SEInvalidRightsDecisionException):
    """Exception raised when an invalid ``reason`` is provided."""
