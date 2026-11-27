from __future__ import annotations

# First-party imports
from erp_models.exceptions import SEInvalidModelException


class SEInvalidRightsDecisionException(SEInvalidModelException):
    """Exception raised when an invalid RightsDecision is provided.

    Notes:
        It is not a ``ValueError``, so that Pydantic does not wrap it in a ``ValidationError``.
    """
