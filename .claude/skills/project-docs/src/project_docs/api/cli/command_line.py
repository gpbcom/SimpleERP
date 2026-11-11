from __future__ import annotations

# Standard library imports
import argparse
from typing import ClassVar, List, Optional

# First-party imports
from project_docs.models.enums import ProjectDocsCommand


class CommandLine:
    """The ``project-docs`` command line.

    Attributes:
        DEFAULT_BASE (str): The branch the changes are compared with, by default.
        parser (argparse.ArgumentParser): The parser of every command.
    """

    DEFAULT_BASE: ClassVar[str] = "origin/develop"

    def __init__(self) -> None:
        """Describe the commands."""
        self.parser = argparse.ArgumentParser(
            prog="project-docs",
            description="Map a branch's changes to the project documentation and check that it is complete (DOC-2).",
        )
        commands = self.parser.add_subparsers(dest="command", required=True)
        mapping = commands.add_parser(
            ProjectDocsCommand.MAP.value, help="list the chapters the branch's changed files concern"
        )
        mapping.add_argument(
            "--base", default=self.DEFAULT_BASE, help=f"the base branch, by default {self.DEFAULT_BASE}"
        )
        check = commands.add_parser(
            ProjectDocsCommand.CHECK.value, help="print every problem of the documentation, nothing when complete"
        )
        check.add_argument("--ticket", help="also check that the ticket handled every chapter its branch concerns")
        check.add_argument(
            "--base", default=self.DEFAULT_BASE, help=f"the base branch of --ticket, by default {self.DEFAULT_BASE}"
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    def parse(self, arguments: Optional[List[str]]) -> argparse.Namespace:
        """Read a command line.

        Args:
            arguments (Optional[List[str]]): The arguments, by default the process's.

        Returns:
            argparse.Namespace: The options.
        """
        return self.parser.parse_args(arguments)
