"""No Python package of SimpleERP holds a command line: every service is a regular FastAPI application (AGENT.md)."""

from __future__ import annotations

from tests.conventions.entrypoints.command_line_scanner import CommandLineScanner
from tests.conventions.helpers import ROOT


class TestNoCommandLine:
    def test_no_package_has_a_cli_module_or_package(self) -> None:
        assert not CommandLineScanner(ROOT).command_line_modules()

    def test_no_package_declares_a_console_script(self) -> None:
        assert not CommandLineScanner(ROOT).console_scripts()

    def test_no_package_parses_command_line_arguments(self) -> None:
        assert not CommandLineScanner(ROOT).argument_parsers()
