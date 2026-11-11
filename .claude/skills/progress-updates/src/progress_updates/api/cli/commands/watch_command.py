from __future__ import annotations

# First-party imports
from progress_updates.api.cli.command import Command


class WatchCommand(Command):
    """``progress-updates watch``: one line every interval while something runs, then a final line."""

    ############################
    # Internal Helpers Methods #
    ############################

    def _perform(self) -> None:
        """Build the watch and follow the tasks until nothing runs."""
        options = self.options
        collector = self.services.collector(
            options.sources, options.tasks_dir, options.evidence, options.since, options.task
        )
        self.exit_code = self.services.watch(collector, options.every, options.max_ticks).follow()
        self.logger.info("The watch ended with exit code %d.", self.exit_code)
