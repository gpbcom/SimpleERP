from __future__ import annotations

from erp_context.models.rights.exceptions.se_invalid_rights_decision_exception import (
    SEInvalidRightsDecisionException,
)


class SERightsDecisionInvalidAllowed(SEInvalidRightsDecisionException):
    """Exception raised when an invalid ``allowed`` is provided."""
