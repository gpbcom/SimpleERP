"""``plugins/`` and ``sdk/`` import only ``erp_models``, never a service, a library, another plugin or the SDK."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import pytest

from tests.conventions.convention_scanner import ConventionScanner

SERVICE = "backend/services/sales/src/erp_sales"
SHOP = "plugins/shop/src/erp_shop"
BANK = "plugins/bank/src/erp_bank"
SDK = "sdk/src/erp_sdk"
CLEAN_TREE: Dict[str, str] = {
    f"{SERVICE}/api/__init__.py": "",
    f"{SERVICE}/service/__init__.py": "",
    f"{SERVICE}/storage/__init__.py": "",
    f"{SERVICE}/models/__init__.py": "",
    "backend/shared/log/src/erp_log/__init__.py": "",
    f"{SHOP}/__init__.py": "",
    f"{BANK}/__init__.py": "",
    f"{SDK}/__init__.py": "",
}


def write(root: Path, files: Dict[str, str]) -> ConventionScanner:
    for name, text in {**CLEAN_TREE, **files}.items():
        (root / name).parent.mkdir(parents=True, exist_ok=True)
        (root / name).write_text(text, encoding="utf-8")
    return ConventionScanner(root)


class TestPluginAndSdkImports:
    def test_an_empty_tree_passes(self, tmp_path: Path) -> None:
        assert ConventionScanner(tmp_path).plugin_and_sdk_imports() == []

    def test_the_clean_tree_passes(self, tmp_path: Path) -> None:
        assert write(tmp_path, {}).plugin_and_sdk_imports() == []

    @pytest.mark.parametrize(
        ("path", "source", "own", "foreign"),
        [
            (f"{SHOP}/a.py", "from erp_sales.api import x\n", "erp_shop", "erp_sales"),
            (f"{SHOP}/a.py", "import erp_log\n", "erp_shop", "erp_log"),
            (f"{SHOP}/a.py", "import erp_bank\n", "erp_shop", "erp_bank"),
            (f"{SHOP}/a.py", "from erp_sdk import x\n", "erp_shop", "erp_sdk"),
            (f"{SDK}/a.py", "import erp_sales\n", "erp_sdk", "erp_sales"),
            (f"{SDK}/a.py", "from erp_log import x\n", "erp_sdk", "erp_log"),
        ],
    )
    def test_an_import_of_another_first_party_package_is_reported(
        self, tmp_path: Path, path: str, source: str, own: str, foreign: str
    ) -> None:
        offenders: List[str] = write(tmp_path, {path: source}).plugin_and_sdk_imports()
        assert offenders == [f"{path}:1 {own} imports {foreign}"]

    def test_imports_of_erp_models_the_own_package_and_third_parties_pass(self, tmp_path: Path) -> None:
        source = "import typing\nimport httpx\nfrom erp_models.x import y\nfrom erp_shop.b import z\n"
        assert write(tmp_path, {f"{SHOP}/a.py": source}).plugin_and_sdk_imports() == []
