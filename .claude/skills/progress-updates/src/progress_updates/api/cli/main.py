"""The ``progress-updates`` console script."""

from __future__ import annotations

# Standard library imports
import os
import sys
from pathlib import Path
from typing import List, Optional

# Third-party imports
from pydantic import ValidationError

# First-party imports
from harness_core.logs.harness_logging import HarnessLogging
from progress_updates.api.cli.command_line import CommandLine
from progress_updates.api.factories.default.default_command_factory import DefaultCommandFactory
from progress_updates.models.catalogs.exceptions import SEInvalidProgressCatalogException, SEProgressCatalogUnreadable
from progress_updates.models.catalogs.progress_catalog import ProgressCatalog
from progress_updates.service.factories.default.default_service_factory import DefaultServiceFactory
from progress_updates.service.factories.service_factory import ServiceFactory


def main(arguments: Optional[List[str]] = None, services: Optional[ServiceFactory] = None) -> int:
    """Run one ``progress-updates`` command.

    Args:
        arguments (Optional[List[str]]): The command line, by default the process's.
        services (Optional[ServiceFactory]): The services, by default the real ones built from the catalogue.

    Returns:
        int: The exit code: 0, or 2 for a failure the person can fix.

    Notes:
        - The catalogue is the skill's ``conf/progress-updates.yaml``; the repository is the folder the command was
          typed in (``PROGRESS_UPDATES_CALLER_CWD``, set by ``bin/progress-updates``).
        - The logs go to the harness log file only: the output is the update itself.
    """
    options = CommandLine().parse(arguments)
    logger = HarnessLogging("progress-updates").logger("progress_updates")
    catalog_file = Path(__file__).resolve().parents[4] / "conf" / "progress-updates.yaml"
    root = Path(os.environ.get("PROGRESS_UPDATES_CALLER_CWD", os.getcwd()))
    try:
        factory = services or DefaultServiceFactory(ProgressCatalog.load(catalog_file), root, logger)
    except (SEProgressCatalogUnreadable, SEInvalidProgressCatalogException, ValidationError) as error:
        logger.error("progress-updates could not start: %s.", type(error).__name__)
        print(f"progress-updates: {error}", file=sys.stderr)
        return 2
    command = DefaultCommandFactory(factory, logger).command(options)
    command.execute()
    return command.exit_code
