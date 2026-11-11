from __future__ import annotations

# Standard library imports
import argparse
from logging import Logger, getLogger
from typing import Optional

# First-party imports
from progress_updates.api.cli.command import Command
from progress_updates.api.cli.commands.hook_command import HookCommand
from progress_updates.api.cli.commands.status_command import StatusCommand
from progress_updates.api.cli.commands.watch_command import WatchCommand
from progress_updates.api.factories.command_factory import CommandFactory
from progress_updates.models.enums import ProgressCommand
from progress_updates.service.factories.service_factory import ServiceFactory


class DefaultCommandFactory(CommandFactory):
    """Builds each ``progress-updates`` command on the given services.

    Attributes:
        services (ServiceFactory): Builds the services the commands call.
        logger (Logger): Logger instance.
    """

    def __init__(self, services: ServiceFactory, logger: Optional[Logger] = None) -> None:
        """Set the services.

        Args:
            services (ServiceFactory): Builds the services the commands call.
            logger (Optional[Logger]): Logger instance.
        """
        self.services = services
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def command(self, options: argparse.Namespace) -> Command:
        """Build the command of a command line.

        Args:
            options (argparse.Namespace): The parsed command line.

        Returns:
            Command: The command, ready to ``execute``.
        """
        name = ProgressCommand(options.command)
        self.logger.debug("Building progress-updates %s.", name.value)
        match name:
            case ProgressCommand.WATCH:
                return WatchCommand(options, self.services, self.logger)
            case ProgressCommand.HOOK:
                return HookCommand(options, self.services, self.logger)
            case _:
                return StatusCommand(options, self.services, self.logger)
