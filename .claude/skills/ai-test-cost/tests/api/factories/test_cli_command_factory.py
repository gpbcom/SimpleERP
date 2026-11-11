from __future__ import annotations

import io
import logging
from pathlib import Path

from ai_cost.api.cli.ai_cost_cli import AiCostCli
from ai_cost.api.factories.cli.cli_command_factory import CliCommandFactory


class TestCliCommandFactory:
    def test_the_factory_builds_the_command_line(self, tmp_path: Path, logger: logging.Logger) -> None:
        cli = CliCommandFactory(tmp_path / "settings.yaml", logger).cli(
            ["status", "GH-1"], io.StringIO(), io.StringIO(), io.StringIO()
        )
        assert isinstance(cli, AiCostCli)
        assert (cli.arguments, cli.settings_file, cli.exit_code) == (["status", "GH-1"], tmp_path / "settings.yaml", 0)
