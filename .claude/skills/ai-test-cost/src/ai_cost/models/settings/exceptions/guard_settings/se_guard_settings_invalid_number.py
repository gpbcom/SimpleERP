from __future__ import annotations

from ai_cost.models.settings.exceptions.guard_settings.se_invalid_guard_settings_exception import (
    SEInvalidGuardSettingsException,
)


class SEGuardSettingsInvalidNumber(SEInvalidGuardSettingsException):
    """Exception raised when an invalid number setting, such as ``kill_ratio``, is provided."""
