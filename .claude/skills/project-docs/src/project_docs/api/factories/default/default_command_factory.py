from __future__ import annotations

# Standard library imports
import argparse
from logging import Logger, getLogger
from typing import Optional

# First-party imports
from project_docs.api.cli.command import Command
from project_docs.api.cli.commands.check_command import CheckCommand
from project_docs.api.cli.commands.map_command import MapCommand
from project_docs.api.factories.command_factory import CommandFactory
from project_docs.models.enums import ProjectDocsCommand
from project_docs.service.factories.service_factory import ServiceFactory


class DefaultCommandFactory(CommandFactory):
    """Builds each ``project-docs`` command on the given services.

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
        name = ProjectDocsCommand(options.command)
        self.logger.debug("Building project-docs %s.", name.value)
        match name:
            case ProjectDocsCommand.MAP:
                return MapCommand(options, self.services, self.logger)
            case _:
                return CheckCommand(options, self.services, self.logger)
