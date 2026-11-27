"""A shared library imports ``erp_models`` and other libraries, never a service, a plugin or the SDK."""

from __future__ import annotations

from pathlib import Path
from typing import Dict

import pytest

from tests.conventions.convention_scanner import ConventionScanner

SERVICE = "backend/services/sales/src/erp_sales"
LIBRARY = "backend/shared/log/src/erp_log"
OFFENDER = f"{LIBRARY}/a.py"
CLEAN_TREE: Dict[str, str] = {
    f"{SERVICE}/api/__init__.py": "",
    f"{SERVICE}/service/__init__.py": "",
    f"{SERVICE}/storage/__init__.py": "",
    f"{SERVICE}/models/__init__.py": "",
    f"{LIBRARY}/__init__.py": "",
    "backend/shared/conf/src/erp_conf/__init__.py": "",
    "backend/shared/conf/src/erp_conf/x.py": "",
    "plugins/shop/src/erp_shop/__init__.py": "",
    "sdk/src/erp_sdk/__init__.py": "",
}


def write(root: Path, files: Dict[str, str]) -> ConventionScanner:
    for name, text in {**CLEAN_TREE, **files}.items():
        (root / name).parent.mkdir(parents=True, exist_ok=True)
        (root / name).write_text(text, encoding="utf-8")
    return ConventionScanner(root)


class TestSharedLibraryImports:
    def test_an_empty_tree_passes(self, tmp_path: Path) -> None:
        assert ConventionScanner(tmp_path).shared_library_imports() == []

    def test_a_clean_tree_passes(self, tmp_path: Path) -> None:
        assert write(tmp_path, {}).shared_library_imports() == []

    @pytest.mark.parametrize(
        ("source", "package"),
        [
            ("import erp_sales\n", "erp_sales"),
            ("from erp_sales.service.quotes import QuoteService\n", "erp_sales"),
            ("import erp_shop\n", "erp_shop"),
            ("from erp_sdk import x\n", "erp_sdk"),
        ],
    )
    def test_a_library_importing_a_service_plugin_or_sdk_is_reported(
        self, tmp_path: Path, source: str, package: str
    ) -> None:
        scanner = write(tmp_path, {OFFENDER: source})
        assert scanner.shared_library_imports() == [f"{OFFENDER}:1 erp_log imports {package}"]

    def test_imports_of_models_other_libraries_itself_and_third_parties_pass(self, tmp_path: Path) -> None:
        source = (
            "import erp_models\n"
            "from erp_models.x import Y\n"
            "from erp_conf.x import z\n"
            "from erp_log.y import w\n"
            "import logging\n"
            "import yaml\n"
        )
        assert write(tmp_path, {OFFENDER: source}).shared_library_imports() == []
