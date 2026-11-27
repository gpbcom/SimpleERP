from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import pytest

from tests.conventions.convention_scanner import ConventionScanner

SERVICE = "backend/services/sales/src/erp_sales"
MODEL = "backend/models/src/erp_models/a.py"
CLEAN_TREE: Dict[str, str] = {
    f"{SERVICE}/api/__init__.py": "",
    f"{SERVICE}/service/__init__.py": "",
    f"{SERVICE}/storage/__init__.py": "",
    f"{SERVICE}/models/__init__.py": "",
    "backend/shared/log/src/erp_log/__init__.py": "",
    "plugins/shop/src/erp_shop/__init__.py": "",
    "sdk/src/erp_sdk/__init__.py": "",
    "backend/models/src/erp_models/__init__.py": "",
}


def write(root: Path, files: Dict[str, str]) -> ConventionScanner:
    for name, text in {**CLEAN_TREE, **files}.items():
        (root / name).parent.mkdir(parents=True, exist_ok=True)
        (root / name).write_text(text, encoding="utf-8")
    return ConventionScanner(root)


class TestSharedModelsImports:
    def test_an_empty_tree_passes(self, tmp_path: Path) -> None:
        assert ConventionScanner(tmp_path).shared_models_imports() == []

    def test_the_clean_tree_passes(self, tmp_path: Path) -> None:
        assert write(tmp_path, {}).shared_models_imports() == []

    @pytest.mark.parametrize(
        ("source", "package"),
        [
            ("import erp_log\n", "erp_log"),
            ("from erp_log.x import y\n", "erp_log"),
            ("import erp_sales.models\n", "erp_sales"),
            ("from erp_shop import z\n", "erp_shop"),
            ("import erp_sdk\n", "erp_sdk"),
        ],
    )
    def test_an_import_of_a_first_party_package_is_reported(self, tmp_path: Path, source: str, package: str) -> None:
        offenders = write(tmp_path, {MODEL: source}).shared_models_imports()
        assert offenders == [f"{MODEL}:1 erp_models imports {package}"]

    @pytest.mark.parametrize(
        "source",
        [
            "import erp_models.money\n",
            "from erp_models.money import Money\n",
            "import typing\n",
            "from pydantic import BaseModel\n",
            "from . import x\n",
        ],
    )
    def test_imports_of_erp_models_the_library_and_relative_imports_pass(self, tmp_path: Path, source: str) -> None:
        offenders: List[str] = write(tmp_path, {MODEL: source}).shared_models_imports()
        assert offenders == []
