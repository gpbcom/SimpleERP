from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from pathlib import Path
from typing import Optional

# First-party imports
from pr_watch.api.cli.hooks.hook_command import HookCommand
from pr_watch.api.factories.hook_factory import HookFactory
from pr_watch.service.inbox.inbox_service import InboxService


class DefaultHookFactory(HookFactory):
    """Builds the prompt hook on the watcher's state folder.

    Attributes:
        state_dir (Path): The watcher's state folder.
        logger (Logger): Logger instance.
    """

    def __init__(self, state_dir: Path, logger: Optional[Logger] = None) -> None:
        """Set the state folder.

        Args:
            state_dir (Path): The watcher's state folder.
            logger (Optional[Logger]): Logger instance.
        """
        self.state_dir = state_dir
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def hook(self) -> HookCommand:
        """Build the prompt hook.

        Returns:
            HookCommand: The hook, reading the inboxes of the state folder.
        """
        return HookCommand(InboxService.at(self.state_dir, self.logger), self.logger)
