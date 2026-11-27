from __future__ import annotations

from erp_logging.models.exceptions.se_logging_setup_error import SELoggingSetupError


class SELoggingConfigInvalidError(SELoggingSetupError):
    """Raised when the logger configuration is refused.

    Notes:
        It covers a missing ``context`` filter, a blank service and a configuration that ``dictConfig`` refuses.
    """
