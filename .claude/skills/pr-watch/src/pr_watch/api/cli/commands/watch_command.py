from __future__ import annotations

# Standard library imports
import asyncio

# First-party imports
from pr_watch.api.cli.command import Command


class WatchCommand(Command):
    """``pr-watch once``: one run of the watcher, the timer's command.

    Notes:
        It reopens sessions and shows notifications: it is meant for the systemd timer, not to be typed on real
        tickets without the person's go.
    """

    ############################
    # Internal Helpers Methods #
    ############################

    def _perform(self) -> None:
        """Run the watcher once and print what it did."""
        job = self.services.watch_job()
        asyncio.run(job.execute())
        self.logger.info("pr-watch once checked %d pull requests.", job.checked)
        print(f"Checked {job.checked} open pull requests: {job.found} events found.")
