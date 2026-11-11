from __future__ import annotations

# Standard library imports
import argparse
from logging import Logger, getLogger
from typing import Optional

# First-party imports
from release_notes.api.cli.command import Command
from release_notes.api.cli.commands.build_command import BuildCommand
from release_notes.api.cli.commands.check_command import CheckCommand
from release_notes.api.cli.commands.next_version_command import NextVersionCommand
from release_notes.api.cli.commands.release_body_command import ReleaseBodyCommand
from release_notes.api.factories.command_factory import CommandFactory
from release_notes.models.enums import ReleaseNotesCommand
from release_notes.service.factories.service_factory import ServiceFactory


class DefaultCommandFactory(CommandFactory):
    """Builds each ``release-notes`` command on the given services.

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
        name = ReleaseNotesCommand(options.command)
        self.logger.debug("Building release-notes %s.", name.value)
        match name:
            case ReleaseNotesCommand.NEXT_VERSION:
                return NextVersionCommand(options, self.services, self.logger)
            case ReleaseNotesCommand.BUILD:
                return BuildCommand(options, self.services, self.logger)
            case ReleaseNotesCommand.RELEASE_BODY:
                return ReleaseBodyCommand(options, self.services, self.logger)
            case _:
                return CheckCommand(options, self.services, self.logger)
