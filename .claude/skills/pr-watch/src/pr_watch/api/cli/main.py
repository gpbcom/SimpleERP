"""The ``pr-watch`` console script."""

from __future__ import annotations

# Standard library imports
import sys
from typing import List, Optional

# Third-party imports
from pydantic import ValidationError

# First-party imports
from harness_core.logs.harness_logging import HarnessLogging
from pr_watch.api.cli import hook_main
from pr_watch.api.cli.command_line import CommandLine
from pr_watch.api.factories.default.default_command_factory import DefaultCommandFactory
from pr_watch.models.configuration.watch_catalog import WatchCatalog
from pr_watch.models.configuration.watch_settings import WatchSettings
from pr_watch.models.enums import PrWatchCommand
from pr_watch.models.exceptions import SEPrWatchError
from pr_watch.service.factories.default.default_service_factory import DefaultServiceFactory
from pr_watch.service.factories.service_factory import ServiceFactory


def main(arguments: Optional[List[str]] = None, services: Optional[ServiceFactory] = None) -> int:
    """Run one ``pr-watch`` command.

    Args:
        arguments (Optional[List[str]]): The command line, by default the process's.
        services (Optional[ServiceFactory]): The services, by default the real ones built from the settings.

    Returns:
        int: The exit code: 0, or 2 for a failure the person can fix.

    Notes:
        - The logs go to ``<state dir>/pr-watch.log`` only, never to the terminal: the prompt hook's output is
          read by Claude Code.
        - ``hook-inbox`` goes to the hook's light entry point, which exits 0 whatever happens.
    """
    options = CommandLine().parse(arguments)
    if PrWatchCommand(options.command) == PrWatchCommand.HOOK_INBOX:
        return hook_main.main()
    try:
        settings = WatchSettings()
        logger = HarnessLogging("pr-watch", settings.state_dir).logger("pr_watch")
        factory = services or DefaultServiceFactory(settings, WatchCatalog.load(settings.catalog_file), logger=logger)
    except (SEPrWatchError, ValidationError, OSError) as error:
        print(f"pr-watch: {error}", file=sys.stderr)
        return 2
    command = DefaultCommandFactory(factory, logger).command(options)
    command.execute()
    return command.exit_code
