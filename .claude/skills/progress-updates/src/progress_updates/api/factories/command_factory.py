from __future__ import annotations

# Standard library imports
import argparse
from abc import ABC, abstractmethod

# First-party imports
from progress_updates.api.cli.command import Command


class CommandFactory(ABC):
    """Builds the command of a command line."""

    @abstractmethod
    def __init__(self) -> None:
        """Set what the commands need."""

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def command(self, options: argparse.Namespace) -> Command:
        """Build the command of a command line.

        Args:
            options (argparse.Namespace): The parsed command line.

        Returns:
            Command: The command, ready to ``execute``.
        """
