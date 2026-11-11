from __future__ import annotations

# Standard library imports
import argparse
from abc import ABC, abstractmethod

# First-party imports
from pr_watch.api.cli.command import Command


class CommandFactory(ABC):
    """Builds the command that a parsed command line asks for."""

    @abstractmethod
    def __init__(self) -> None:
        """Set what the commands are built with."""

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
