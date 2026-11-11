from __future__ import annotations

# First-party imports
from progress_updates.api.cli.command import Command


class StatusCommand(Command):
    """``progress-updates status``: print one update."""

    ############################
    # Internal Helpers Methods #
    ############################

    def _perform(self) -> None:
        """Gather the tasks and print the update."""
        options = self.options
        collector = self.services.collector(
            options.sources, options.tasks_dir, options.evidence, options.since, options.task
        )
        tasks = collector.collect()
        print(self.services.renderer(options.since).render(tasks))
        self.logger.info("Printed an update of %d tasks.", len(tasks))
