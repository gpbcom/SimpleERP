from __future__ import annotations

from pr_watch.models.configuration.exceptions.se_invalid_commands_config_exception import (
    SEInvalidCommandsConfigException,
)


class SECommandsConfigInvalidClaude(SEInvalidCommandsConfigException):
    """Exception raised when an invalid ``claude`` is provided."""
