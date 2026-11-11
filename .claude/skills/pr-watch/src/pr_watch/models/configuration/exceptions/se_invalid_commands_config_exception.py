from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidCommandsConfigException(SEPrWatchError):
    """Exception raised when an invalid CommandsConfig is provided."""
