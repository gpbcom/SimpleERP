from __future__ import annotations

import json
from logging import DEBUG, getLogger
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import ClassVar, Dict, List

import pytest
from erp_logging.context.log_context import LogContext
from erp_logging.models.exceptions import SELoggingConfigInvalidError, SELoggingConfigUnreadableError
from erp_logging.setup.logging_setup import LoggingSetup


class TestLoggingSetup:
    REFERENCE: ClassVar[Path] = Path(__file__).resolve().parents[2] / "conf" / "logger.yaml"
    SMALL_CONFIG: ClassVar[str] = """\
    version: 1
    filters:
      context:
        "()": erp_logging.filters.context_filter.ContextFilter
        service: written-in-the-file
    formatters:
      plain:
        format: "%(service)s|%(company)s|%(request)s|%(message)s"
    handlers:
      file:
        class: logging.FileHandler
        formatter: plain
        filters: [context]
        filename: elsewhere/small.log
        encoding: utf-8
    root:
      level: DEBUG
      handlers: [file]
    """

    def configure(self, tmp_path: Path, service: str = "platform") -> None:
        LoggingSetup(self.REFERENCE, service, tmp_path).configure()

    def json_records(self, tmp_path: Path) -> List[Dict[str, object]]:
        lines = (tmp_path / "simpleerp.jsonl").read_text(encoding="utf-8").splitlines()
        return [json.loads(line) for line in lines if line.strip()]

    @pytest.mark.parametrize("output", ["console", "text file", "json file"])
    def test_every_line_carries_the_service_the_company_and_the_request(
        self, output: str, tmp_path: Path, capsys: pytest.CaptureFixture[str]
    ) -> None:
        self.configure(tmp_path)
        LogContext.bind("c-123", "r-456")
        getLogger("tests.setup").info("a tagged line")
        match output:
            case "console":
                text = capsys.readouterr().out
            case "text file":
                text = (tmp_path / "simpleerp.log").read_text(encoding="utf-8")
            case _:
                records = self.json_records(tmp_path)
                assert records
                text = json.dumps(records)
        for tag in ("platform", "c-123", "r-456"):
            assert tag in text

    def test_an_unbound_context_writes_a_dash(self, tmp_path: Path) -> None:
        self.configure(tmp_path)
        getLogger("tests.setup").info("an untagged line")
        values = [value for record in self.json_records(tmp_path) for value in record.values()]
        assert values.count("-") >= 2

    def test_the_given_service_replaces_the_one_written_in_the_file(self, tmp_path: Path) -> None:
        config = tmp_path / "small.yaml"
        config.write_text(self.SMALL_CONFIG, encoding="utf-8")
        logs_dir = tmp_path / "logs"
        LoggingSetup(config, "platform", logs_dir).configure()
        getLogger("tests.setup").info("hello")
        text = (logs_dir / "small.log").read_text(encoding="utf-8")
        assert "platform|-|-|hello" in text
        assert "written-in-the-file" not in text

    def test_the_two_file_handlers_rotate_and_write_in_the_logs_folder(self, tmp_path: Path) -> None:
        logs_dir = tmp_path / "logs"
        LoggingSetup(self.REFERENCE, "platform", logs_dir).configure()
        handlers = [handler for handler in getLogger().handlers if isinstance(handler, RotatingFileHandler)]
        assert len(handlers) == 2
        for handler in handlers:
            assert handler.maxBytes == 10485760
            assert handler.backupCount == 5
            assert Path(handler.baseFilename).parent == logs_dir.resolve()
        assert {Path(handler.baseFilename).name for handler in handlers} == {"simpleerp.log", "simpleerp.jsonl"}

    def test_the_root_level_is_debug(self, tmp_path: Path) -> None:
        self.configure(tmp_path)
        assert getLogger().level == DEBUG

    def test_a_missing_file_is_refused(self, tmp_path: Path) -> None:
        with pytest.raises(SELoggingConfigUnreadableError):
            LoggingSetup(tmp_path / "missing.yaml", "platform", tmp_path).configure()

    def test_invalid_yaml_is_refused(self, tmp_path: Path) -> None:
        config = tmp_path / "broken.yaml"
        config.write_text("key: [unclosed", encoding="utf-8")
        with pytest.raises(SELoggingConfigUnreadableError):
            LoggingSetup(config, "platform", tmp_path).configure()

    def test_a_file_that_is_not_a_mapping_is_refused(self, tmp_path: Path) -> None:
        config = tmp_path / "list.yaml"
        config.write_text("- one\n- two\n", encoding="utf-8")
        with pytest.raises(SELoggingConfigUnreadableError):
            LoggingSetup(config, "platform", tmp_path).configure()

    def test_a_file_without_the_context_filter_is_refused(self, tmp_path: Path) -> None:
        config = tmp_path / "nofilter.yaml"
        config.write_text("version: 1\nroot:\n  level: DEBUG\n", encoding="utf-8")
        with pytest.raises(SELoggingConfigInvalidError):
            LoggingSetup(config, "platform", tmp_path).configure()

    def test_an_unknown_handler_class_is_refused(self, tmp_path: Path) -> None:
        config = tmp_path / "unknown.yaml"
        config.write_text(
            self.SMALL_CONFIG.replace("logging.FileHandler", "no_such_module.NoSuchHandler"),
            encoding="utf-8",
        )
        with pytest.raises(SELoggingConfigInvalidError):
            LoggingSetup(config, "platform", tmp_path).configure()
