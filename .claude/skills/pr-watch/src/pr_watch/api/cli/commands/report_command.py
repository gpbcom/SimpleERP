from __future__ import annotations

# First-party imports
from pr_watch.api.cli.command import Command
from pr_watch.models.enums import PrWatchCommand


class ReportCommand(Command):
    """``pr-watch status`` and ``pr-watch render``: what is watched, and the summary pages."""

    ############################
    # Internal Helpers Methods #
    ############################

    def _status(self) -> None:
        """Print every watched pull request."""
        lines = self.services.inbox().status()
        for line in lines:
            print(line)
        if not lines:
            print("No pull request is watched.")

    def _render(self) -> None:
        """Write the summary pages again."""
        with self.services.lock():
            pages = self.services.renderer().refresh()
        for page in pages:
            print(f"Wrote {page}.")

    def _perform(self) -> None:
        """Run ``status`` or ``render``."""
        match PrWatchCommand(self.options.command):
            case PrWatchCommand.STATUS:
                self._status()
            case _:
                self._render()
