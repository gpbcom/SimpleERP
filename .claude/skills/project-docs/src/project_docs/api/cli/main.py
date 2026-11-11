"""The ``project-docs`` console script."""

from __future__ import annotations

# Standard library imports
import sys
from typing import List, Optional

# Third-party imports
from pydantic import ValidationError

# First-party imports
from harness_core.logs.harness_logging import HarnessLogging
from project_docs.api.cli.command_line import CommandLine
from project_docs.api.factories.default.default_command_factory import DefaultCommandFactory
from project_docs.models.catalogs.doc_map import DocMap
from project_docs.models.exceptions import SEProjectDocsError
from project_docs.models.settings.project_docs_settings import ProjectDocsSettings
from project_docs.service.factories.default.default_service_factory import DefaultServiceFactory
from project_docs.service.factories.service_factory import ServiceFactory


def main(arguments: Optional[List[str]] = None, services: Optional[ServiceFactory] = None) -> int:
    """Run one ``project-docs`` command.

    Args:
        arguments (Optional[List[str]]): The command line, by default the process's.
        services (Optional[ServiceFactory]): The services, by default the real ones built from the settings.

    Returns:
        int: The exit code: 0, 1 when ``check`` found problems, or 2 for a failure the person can fix.

    Notes:
        The logs go to the harness log file only, never to the terminal: the output is what the person or CI reads.
    """
    options = CommandLine().parse(arguments)
    logger = HarnessLogging("project-docs").logger("project_docs")
    try:
        settings = ProjectDocsSettings()
        factory = services or DefaultServiceFactory(settings, DocMap.load(settings.doc_map_file), logger)
    except (SEProjectDocsError, ValidationError) as error:
        logger.error("project-docs could not start: %s.", type(error).__name__)
        print(f"project-docs: {error}", file=sys.stderr)
        return 2
    command = DefaultCommandFactory(factory, logger).command(options)
    command.execute()
    return command.exit_code
