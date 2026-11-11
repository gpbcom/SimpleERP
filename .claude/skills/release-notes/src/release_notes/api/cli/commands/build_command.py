from __future__ import annotations

# Standard library imports
from datetime import date

# First-party imports
from release_notes.api.cli.command import Command


class BuildCommand(Command):
    """``release-notes build <x.y.z>``: add the version's section to CHANGELOG.md and delete its fragments.

    Notes:
        It prints the section added and each fragment deleted, so the person stages exactly those with
        ``git add CHANGELOG.md`` and ``git rm``.
    """

    ############################
    # Internal Helpers Methods #
    ############################

    def _perform(self) -> None:
        """Build the section and print what changed."""
        today = date.today()
        deleted = self.services.changelog_builder().build(self.options.version, today)
        print(f"CHANGELOG.md: added ## [{self.options.version.strip()}] - {today.isoformat()}.")
        for path in deleted:
            print(f"{path}: deleted.")
        self.logger.info("release-notes build %s deleted %d fragments.", self.options.version, len(deleted))
