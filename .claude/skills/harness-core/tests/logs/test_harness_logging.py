from __future__ import annotations

from pathlib import Path

import pytest

from harness_core.logs.harness_logging import HarnessLogging


class TestHarnessLogging:
    def test_logs_go_to_the_tool_file_and_never_to_the_console(
        self, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        logger = HarnessLogging("demo-tool", state_dir=tmp_path).logger("demo")
        logger.info("Hello %s.", "file")
        for handler in logger.handlers:
            handler.flush()
        assert "Hello file." in (tmp_path / "demo-tool.log").read_text(encoding="utf-8")
        captured = capsys.readouterr()
        assert captured.out == ""
        assert captured.err == ""

    def test_the_same_logger_is_not_given_two_file_handlers(self, tmp_path: Path) -> None:
        logging = HarnessLogging("demo-tool", state_dir=tmp_path)
        assert len(logging.logger("again").handlers) == len(logging.logger("again").handlers) == 1
