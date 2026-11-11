from __future__ import annotations

# Standard library imports
import argparse
from logging import Logger, getLogger
from typing import Optional

# First-party imports
from pr_watch.api.cli.command import Command
from pr_watch.api.cli.commands.inbox_command import InboxCommand
from pr_watch.api.cli.commands.report_command import ReportCommand
from pr_watch.api.cli.commands.session_command import SessionCommand
from pr_watch.api.cli.commands.setup_command import SetupCommand
from pr_watch.api.cli.commands.watch_command import WatchCommand
from pr_watch.api.factories.command_factory import CommandFactory
from pr_watch.models.enums import PrWatchCommand
from pr_watch.service.factories.service_factory import ServiceFactory


class DefaultCommandFactory(CommandFactory):
    """Builds each ``pr-watch`` command on the given services.

    Attributes:
        services (ServiceFactory): Builds the services the commands call.
        logger (Logger): Logger instance.

    Notes:
        ``hook-inbox`` never reaches this factory: ``main`` hands it to the hook's light entry point, so the last
        case is ``install-units``.
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
        name = PrWatchCommand(options.command)
        self.logger.debug("Building pr-watch %s.", name.value)
        match name:
            case PrWatchCommand.ONCE:
                return WatchCommand(options, self.services, self.logger)
            case PrWatchCommand.REGISTER | PrWatchCommand.BACKFILL:
                return SessionCommand(options, self.services, self.logger)
            case PrWatchCommand.SHOW | PrWatchCommand.ACK | PrWatchCommand.LOG:
                return InboxCommand(options, self.services, self.logger)
            case PrWatchCommand.STATUS | PrWatchCommand.RENDER:
                return ReportCommand(options, self.services, self.logger)
            case _:
                return SetupCommand(options, self.services, self.logger)
