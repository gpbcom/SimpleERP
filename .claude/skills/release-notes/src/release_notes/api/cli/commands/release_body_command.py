from __future__ import annotations

# Standard library imports
import asyncio

# First-party imports
from release_notes.api.cli.command import Command


class ReleaseBodyCommand(Command):
    """``release-notes release-body <x.y.z>``: print the GitHub Release body of a version.

    Notes:
        ``release.yml`` writes the output to ``release-body.md`` and publishes it, so nothing else is printed on
        the standard output.
    """

    ############################
    # Internal Helpers Methods #
    ############################

    def _perform(self) -> None:
        """Write the body and print it."""
        body = asyncio.run(self.services.release_body().text(self.options.version.strip()))
        print(body, end="")
        self.logger.info("release-notes release-body printed %d characters.", len(body))
