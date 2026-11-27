from __future__ import annotations

from erp_logging.models.exceptions.se_logging_setup_error import SELoggingSetupError


class SELoggingConfigUnreadableError(SELoggingSetupError):
    """Raised when the logger configuration file cannot be read, is not YAML or is not a mapping."""
