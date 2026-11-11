from __future__ import annotations

from ai_cost.models.settings.exceptions.guard_settings.se_invalid_guard_settings_exception import (
    SEInvalidGuardSettingsException,
)


class SEGuardSettingsInvalidPath(SEInvalidGuardSettingsException):
    """Exception raised when an invalid path setting, such as ``state_dir``, is provided."""
