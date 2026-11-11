from __future__ import annotations

from ai_cost.models.settings.exceptions.guard_settings.se_invalid_guard_settings_exception import (
    SEInvalidGuardSettingsException,
)


class SEGuardSettingsInvalidUsageSource(SEInvalidGuardSettingsException):
    """Exception raised when an invalid ``usage_source`` is provided."""
