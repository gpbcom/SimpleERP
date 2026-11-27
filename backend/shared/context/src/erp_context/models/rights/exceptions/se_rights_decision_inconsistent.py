from __future__ import annotations

from erp_context.models.rights.exceptions.se_invalid_rights_decision_exception import (
    SEInvalidRightsDecisionException,
)


class SERightsDecisionInconsistent(SEInvalidRightsDecisionException):
    """Exception raised when ``allowed`` and ``reason`` contradict each other."""
