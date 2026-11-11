from __future__ import annotations

from ai_cost.models.settings.exceptions.caller_environment.se_invalid_caller_environment_exception import (
    SEInvalidCallerEnvironmentException,
)


class SECallerEnvironmentInvalidApiKeyId(SEInvalidCallerEnvironmentException):
    """Exception raised when an invalid ``api_key_id`` is provided."""
