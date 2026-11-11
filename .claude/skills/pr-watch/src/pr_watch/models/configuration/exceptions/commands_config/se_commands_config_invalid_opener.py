from __future__ import annotations

from pr_watch.models.configuration.exceptions.se_invalid_commands_config_exception import (
    SEInvalidCommandsConfigException,
)


class SECommandsConfigInvalidOpener(SEInvalidCommandsConfigException):
    """Exception raised when an invalid ``opener`` is provided."""
