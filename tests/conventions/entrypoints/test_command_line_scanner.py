"""The no-command-line rule passes a clean tree, and catches each kind of command line in every Python package."""

from __future__ import annotations

from pathlib import Path
from typing import ClassVar, Dict, List

import pytest

from tests.conventions.entrypoints.command_line_scanner import CommandLineScanner


class TestCommandLineScanner:
    SERVICE: ClassVar[str] = "backend/services/sales"
    PACKAGE: ClassVar[str] = f"{SERVICE}/src/erp_sales"
    MANIFEST: ClassVar[str] = '[project]\nname = "sales"\nversion = "0.1.0"\ndependencies = ["fastapi", "uvicorn"]\n'
    CLEAN_TREE: ClassVar[Dict[str, str]] = {
        f"{SERVICE}/pyproject.toml": MANIFEST,
        f"{PACKAGE}/__init__.py": "",
        f"{PACKAGE}/api/__init__.py": "",
        f"{PACKAGE}/api/app_factory.py": "from __future__ import annotations\n\nfrom fastapi import FastAPI\n",
        f"{PACKAGE}/api/http/health_router.py": "from __future__ import annotations\n",
        f"{PACKAGE}/service/clients/client_service.py": "from __future__ import annotations\n",
        f"{PACKAGE}/storage/__init__.py": "",
        f"{PACKAGE}/models/__init__.py": "",
        f"{SERVICE}/tests/api/test_app_factory.py": "from __future__ import annotations\n",
        "sdk/pyproject.toml": '[project]\nname = "erp-sdk"\nversion = "0.1.0"\n',
        "plugins/shipping/pyproject.toml": (
            '[project]\nname = "shipping"\nversion = "0.1.0"\n\n'
            '[project.entry-points."simpleerp.plugins"]\nshipping = "erp_shipping.plugin:ShippingPlugin"\n'
        ),
    }
    RULES: ClassVar[List[str]] = ["command_line_modules", "console_scripts", "argument_parsers"]

    def write(self, root: Path, files: Dict[str, str]) -> CommandLineScanner:
        for name, text in {**self.CLEAN_TREE, **files}.items():
            (root / name).parent.mkdir(parents=True, exist_ok=True)
            (root / name).write_text(text, encoding="utf-8")
        return CommandLineScanner(root)

    @pytest.mark.parametrize("rule", RULES)
    def test_an_empty_tree_passes(self, tmp_path: Path, rule: str) -> None:
        assert getattr(CommandLineScanner(tmp_path), rule)() == []

    @pytest.mark.parametrize("rule", RULES)
    def test_a_regular_fastapi_service_passes(self, tmp_path: Path, rule: str) -> None:
        assert getattr(self.write(tmp_path, {}), rule)() == []

    @pytest.mark.parametrize(
        "name",
        [
            "backend/services/sales/src/erp_sales/api/cli.py",
            "backend/services/sales/src/erp_sales/api/cli/__init__.py",
            "backend/services/sales/src/erp_sales/api/sales_cli.py",
            "backend/services/sales/src/erp_sales/api/cli_commands.py",
            "backend/services/sales/src/erp_sales/__main__.py",
            "backend/services/sales/tests/api/cli/test_sales_cli.py",
            "backend/shared/logging/src/erp_logging/cli.py",
            "backend/models/src/erp_models/cli.py",
            "plugins/shipping/src/erp_shipping/cli.py",
            "sdk/src/erp_sdk/cli/main.py",
        ],
    )
    def test_a_cli_module_or_package_is_caught(self, tmp_path: Path, name: str) -> None:
        offenders = self.write(tmp_path, {name: "from __future__ import annotations\n"}).command_line_modules()
        assert any(name.startswith(offender) for offender in offenders)

    def test_a_name_that_only_contains_cli_passes(self, tmp_path: Path) -> None:
        files = {
            f"{self.PACKAGE}/service/clients/metering_client.py": "",
            f"{self.PACKAGE}/service/clients/client_service.py": "",
            f"{self.PACKAGE}/models/clients/clinic.py": "",
        }
        assert self.write(tmp_path, files).command_line_modules() == []

    @pytest.mark.parametrize(
        ("manifest", "table"),
        [
            ('[project.scripts]\nsales-server = "erp_sales.api.cli:main"\n', "[project.scripts] sales-server"),
            ('[project.gui-scripts]\nsales-gui = "erp_sales.api.gui:main"\n', "[project.gui-scripts] sales-gui"),
            (
                '[project.entry-points.console_scripts]\nsales-export = "erp_sales.api.export:main"\n',
                "[project.entry-points.console_scripts] sales-export",
            ),
        ],
    )
    def test_a_console_script_is_caught(self, tmp_path: Path, manifest: str, table: str) -> None:
        files = {f"{self.SERVICE}/pyproject.toml": f"{self.MANIFEST}\n{manifest}"}
        assert self.write(tmp_path, files).console_scripts() == [f"{self.SERVICE}/pyproject.toml: {table}"]

    @pytest.mark.parametrize("folder", ["sdk", "plugins/shipping", "backend/shared/logging", "backend/models"])
    def test_a_console_script_is_caught_in_every_kind_of_package(self, tmp_path: Path, folder: str) -> None:
        files = {f"{folder}/pyproject.toml": '[project]\nname = "x"\n\n[project.scripts]\nx = "x.main:main"\n'}
        assert self.write(tmp_path, files).console_scripts() == [f"{folder}/pyproject.toml: [project.scripts] x"]

    @pytest.mark.parametrize(
        ("source", "found"),
        [
            ("import argparse\n", "argparse"),
            ("from argparse import ArgumentParser\n", "argparse"),
            ("import click\n", "click"),
            ("from typer import Typer\n", "typer"),
            ("import sys\n\nARGS = sys.argv\n", "sys.argv"),
            ("from sys import argv\n", "sys.argv"),
        ],
    )
    def test_an_argument_parser_is_caught(self, tmp_path: Path, source: str, found: str) -> None:
        files = {f"{self.PACKAGE}/api/http/health_router.py": source}
        offenders = self.write(tmp_path, files).argument_parsers()
        assert len(offenders) == 1
        assert offenders[0].startswith(f"{self.PACKAGE}/api/http/health_router.py:")
        assert offenders[0].endswith(f" {found}")
