from __future__ import annotations

from pr_watch.models.configuration.exceptions.se_invalid_commands_config_exception import (
    SEInvalidCommandsConfigException,
)


class SECommandsConfigInvalidVscode(SEInvalidCommandsConfigException):
    """Exception raised when an invalid ``vscode`` is provided."""
