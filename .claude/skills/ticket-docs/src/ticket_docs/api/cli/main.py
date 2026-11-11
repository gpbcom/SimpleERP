from __future__ import annotations

# Standard library imports
import os
import sys
from pathlib import Path

# First-party imports
from harness_core.logs.harness_logging import HarnessLogging
from ticket_docs.api.factories.cli.cli_command_factory import CliCommandFactory
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.models.github.github_catalog import GithubCatalog


def main() -> int:
    """Run the ``ticket-docs`` command line.

    Returns:
        int: The exit code: the recorded command's for ``record-run``, 1 for problems or failures, 2 for a usage
        error, 0 for the hooks.

    Notes:
        - The logs go to the harness log file only, because a hook's standard output is its answer.
        - ``bin/ticket-docs`` passes the caller's folder in ``TICKET_DOCS_CALLER_CWD``, because ``uv run --project``
          may start the tool from another folder.
    """
    logger = HarnessLogging("ticket-docs").logger("ticket_docs")
    caller_cwd = Path(os.environ.get("TICKET_DOCS_CALLER_CWD") or os.getcwd())
    factory = CliCommandFactory(
        FolderRules.SKILL_DIR / "conf" / "folder-rules.yaml", GithubCatalog.SKILL_DIR / "conf" / "github.yaml", logger
    )
    cli = factory.cli(sys.argv[1:], sys.stdin, sys.stdout, sys.stderr, caller_cwd)
    cli.execute()
    return cli.exit_code
