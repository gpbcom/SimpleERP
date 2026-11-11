from __future__ import annotations

from pr_watch.models.configuration.exceptions.se_invalid_watch_settings_exception import SEInvalidWatchSettingsException


class SEWatchSettingsInvalidCallerCwd(SEInvalidWatchSettingsException):
    """Exception raised when an invalid ``caller_cwd`` is provided."""
