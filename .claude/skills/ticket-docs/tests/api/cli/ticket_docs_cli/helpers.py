from __future__ import annotations

import io
import logging
from pathlib import Path
from typing import List, Optional, Tuple

from harness_core.terminal.human_confirmation import HumanConfirmation
from ticket_docs.api.factories.cli.cli_command_factory import CliCommandFactory
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.models.github.github_catalog import GithubCatalog


def call(
    arguments: List[str], cwd: Path, stdin: str = "", confirmation: Optional[HumanConfirmation] = None
) -> Tuple[int, str, str]:
    stdout, stderr = io.StringIO(), io.StringIO()
    factory = CliCommandFactory(
        FolderRules.SKILL_DIR / "conf" / "folder-rules.yaml",
        GithubCatalog.SKILL_DIR / "conf" / "github.yaml",
        logging.getLogger("ticket_docs.tests"),
    )
    if confirmation is None:
        cli = factory.cli(arguments, io.StringIO(stdin), stdout, stderr, cwd)
    else:
        cli = factory.cli(arguments, io.StringIO(stdin), stdout, stderr, cwd, confirmation)
    cli.execute()
    return cli.exit_code, stdout.getvalue(), stderr.getvalue()
