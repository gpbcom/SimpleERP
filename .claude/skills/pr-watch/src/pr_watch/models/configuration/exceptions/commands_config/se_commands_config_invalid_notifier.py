from __future__ import annotations

from pr_watch.models.configuration.exceptions.se_invalid_commands_config_exception import (
    SEInvalidCommandsConfigException,
)


class SECommandsConfigInvalidNotifier(SEInvalidCommandsConfigException):
    """Exception raised when an invalid ``notifier`` is provided."""
