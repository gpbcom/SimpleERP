from __future__ import annotations

# First-party imports
from release_notes.api.cli.command import Command


class NextVersionCommand(Command):
    """``release-notes next-version``: print the suggested version, then the reason for it.

    Notes:
        The version comes alone on the first line, so a script can read it with ``head -1``.
    """

    ############################
    # Internal Helpers Methods #
    ############################

    def _perform(self) -> None:
        """Suggest the next version and print it with its reason."""
        version, reason = self.services.version_advisor().suggest()
        print(version)
        print(reason)
        self.logger.info("release-notes next-version printed %s.", version)
