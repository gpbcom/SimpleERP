from __future__ import annotations

# First-party imports
from erp_models.exceptions import SEInvalidModelException


class SEInvalidRuleVersionException(SEInvalidModelException):
    """Exception raised when an invalid RuleVersion is provided.

    Notes:
        It does not subclass ``ValueError``, so that Pydantic does not wrap it in a ``ValidationError``.
    """
