from __future__ import annotations

# First-party imports
from project_docs.api.cli.command import Command


class MapCommand(Command):
    """``project-docs map``: print each chapter the branch's changes concern, with the paths that concern it.

    Notes:
        One line per chapter, ``<chapter> <- <path>, <path>``, and nothing when the branch has no documentation
        impact.
    """

    ############################
    # Internal Helpers Methods #
    ############################

    def _perform(self) -> None:
        """Map the branch's changes and print the chapters."""
        mapping = self.services.documentation().map(self.options.base)
        for chapter, paths in mapping.items():
            print(f"{chapter} <- {', '.join(paths)}")
        self.logger.info("Printed %d chapters for the changes since %s.", len(mapping), self.options.base)
