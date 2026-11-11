from __future__ import annotations

from pr_watch.models.configuration.exceptions.se_invalid_commands_config_exception import (
    SEInvalidCommandsConfigException,
)


class SECommandsConfigInvalidTerminal(SEInvalidCommandsConfigException):
    """Exception raised when an invalid ``terminal`` is provided."""
