from __future__ import annotations

# Standard library imports
import argparse
import sys
from abc import abstractmethod
from logging import Logger, getLogger
from typing import ClassVar, Optional

# First-party imports
from harness_core.lifecycle.runnable import Runnable
from progress_updates.models.exceptions import SEProgressUpdatesError
from progress_updates.service.factories.service_factory import ServiceFactory


class Command(Runnable):
    """One ``progress-updates`` command: it reads its options, calls the services and prints for the person.

    Attributes:
        FAILED (int): The exit code of a command that failed for a reason the person can fix.
        options (argparse.Namespace): The parsed command line.
        services (ServiceFactory): Builds the services.
        exit_code (int): The command's exit code, read after ``execute``.
        logger (Logger): Logger instance.
    """

    FAILED: ClassVar[int] = 2

    def __init__(self, options: argparse.Namespace, services: ServiceFactory, logger: Optional[Logger] = None) -> None:
        """Set the options and the services.

        Args:
            options (argparse.Namespace): The parsed command line.
            services (ServiceFactory): Builds the services.
            logger (Optional[Logger]): Logger instance.
        """
        self.options = options
        self.services = services
        self.exit_code = 0
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    @abstractmethod
    def _perform(self) -> None:
        """Do the command's work."""

    ############################
    # Publicly Exposed Methods #
    ############################

    def initialize(self) -> None:
        """Acquire nothing: the services open what they need."""

    def run(self) -> None:
        """Do the work, and turn a failure the person can fix into a message and exit code 2."""
        try:
            self._perform()
        except SEProgressUpdatesError as error:
            self.logger.warning("progress-updates %s failed: %s.", self.options.command, type(error).__name__)
            print(f"progress-updates: {error}", file=sys.stderr)
            self.exit_code = self.FAILED

    def close(self) -> None:
        """Release nothing."""
