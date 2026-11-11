"""The ``release-notes`` console script."""

from __future__ import annotations

# Standard library imports
import sys
from typing import List, Optional

# Third-party imports
from pydantic import ValidationError

# First-party imports
from harness_core.logs.harness_logging import HarnessLogging
from release_notes.api.cli.command_line import CommandLine
from release_notes.api.factories.default.default_command_factory import DefaultCommandFactory
from release_notes.models.catalogs.changelog_type_catalog import ChangelogTypeCatalog
from release_notes.models.exceptions import SEReleaseNotesError
from release_notes.models.settings.release_notes_settings import ReleaseNotesSettings
from release_notes.service.factories.default.default_service_factory import DefaultServiceFactory
from release_notes.service.factories.service_factory import ServiceFactory


def main(arguments: Optional[List[str]] = None, services: Optional[ServiceFactory] = None) -> int:
    """Run one ``release-notes`` command.

    Args:
        arguments (Optional[List[str]]): The command line, by default the process's.
        services (Optional[ServiceFactory]): The services, by default the real ones built from the settings.

    Returns:
        int: The exit code: 0, 1 when ``check`` found problems, or 2 for a failure the person can fix.

    Notes:
        The logs go to the harness log file only, never to the terminal: ``release-body``'s output is the Release
        body itself.
    """
    options = CommandLine().parse(arguments)
    logger = HarnessLogging("release-notes").logger("release_notes")
    try:
        settings = ReleaseNotesSettings()
        factory = services or DefaultServiceFactory(
            settings, ChangelogTypeCatalog.load(settings.changelog_types_file), logger=logger
        )
    except (SEReleaseNotesError, ValidationError) as error:
        logger.error("release-notes could not start: %s.", type(error).__name__)
        print(f"release-notes: {error}", file=sys.stderr)
        return 2
    command = DefaultCommandFactory(factory, logger).command(options)
    command.execute()
    return command.exit_code
