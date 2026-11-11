from __future__ import annotations

from pr_watch.models.configuration.exceptions.se_invalid_watch_settings_exception import SEInvalidWatchSettingsException


class SEWatchSettingsInvalidCostStateDir(SEInvalidWatchSettingsException):
    """Exception raised when an invalid ``cost_state_dir`` is provided."""
