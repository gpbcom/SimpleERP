from __future__ import annotations

# Standard library imports
import argparse
from typing import List, Optional

# First-party imports
from release_notes.models.enums import ReleaseNotesCommand


class CommandLine:
    """The ``release-notes`` command line.

    Attributes:
        parser (argparse.ArgumentParser): The parser of every command.
    """

    def __init__(self) -> None:
        """Describe the commands."""
        self.parser = argparse.ArgumentParser(
            prog="release-notes",
            description="Check the changelog fragments and release notes, and assemble a release (DOC-3).",
        )
        commands = self.parser.add_subparsers(dest="command", required=True)
        check = commands.add_parser(
            ReleaseNotesCommand.CHECK.value, help="print every problem of the changelog, nothing when DOC-3 holds"
        )
        check.add_argument("--branch", help="the branch whose rules apply, by default the one checked out")
        check.add_argument("--ticket", help="also check the ticket's RELEASE-NOTE.md, such as GH-12")
        commands.add_parser(
            ReleaseNotesCommand.NEXT_VERSION.value, help="suggest the next version from the last tag and the fragments"
        )
        build = commands.add_parser(
            ReleaseNotesCommand.BUILD.value, help="add the version's section to CHANGELOG.md and delete its fragments"
        )
        build.add_argument("version", help="the version, such as 1.4.0")
        body = commands.add_parser(
            ReleaseNotesCommand.RELEASE_BODY.value, help="print the GitHub Release body of a version"
        )
        body.add_argument("version", help="the released version, such as 1.4.0")

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
