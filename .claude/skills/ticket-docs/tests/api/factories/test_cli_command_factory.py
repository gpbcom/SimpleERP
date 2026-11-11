from __future__ import annotations

import io
import logging
from pathlib import Path

from ticket_docs.api.cli.ticket_docs_cli import TicketDocsCli
from ticket_docs.api.factories.cli.cli_command_factory import CliCommandFactory


class TestCliCommandFactory:
    def test_the_factory_builds_the_command_line(self, tmp_path: Path, logger: logging.Logger) -> None:
        rules, catalog = tmp_path / "rules.yaml", tmp_path / "github.yaml"
        cli = CliCommandFactory(rules, catalog, logger).cli(
            ["check", "GH-1"], io.StringIO(), io.StringIO(), io.StringIO(), tmp_path
        )
        assert isinstance(cli, TicketDocsCli)
        assert (cli.arguments, cli.rules_file, cli.catalog_file, cli.caller_cwd, cli.exit_code) == (
            ["check", "GH-1"],
            rules,
            catalog,
            tmp_path,
            0,
        )
