from __future__ import annotations

from ai_cost.models.settings.exceptions.guard_settings.se_invalid_guard_settings_exception import (
    SEInvalidGuardSettingsException,
)


class SEGuardSettingsUnreadable(SEInvalidGuardSettingsException):
    """Exception raised when the settings file cannot be read or parsed."""
