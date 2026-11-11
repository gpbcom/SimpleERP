from __future__ import annotations

from ai_cost.models.settings.exceptions.caller_environment.se_invalid_caller_environment_exception import (
    SEInvalidCallerEnvironmentException,
)


class SECallerEnvironmentInvalidCallerCwd(SEInvalidCallerEnvironmentException):
    """Exception raised when an invalid ``caller_cwd`` is provided."""
