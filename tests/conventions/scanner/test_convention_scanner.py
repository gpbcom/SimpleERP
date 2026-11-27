"""The convention rules pass on an empty tree and catch each violation in the layout of decision D438."""

from __future__ import annotations

from pathlib import Path
from typing import Dict

import pytest

from tests.conventions.convention_scanner import ConventionScanner

SERVICE = "backend/services/sales/src/erp_sales"
CLEAN_SERVICE: Dict[str, str] = {
    f"{SERVICE}/api/__init__.py": "",
    f"{SERVICE}/service/__init__.py": "",
    f"{SERVICE}/storage/__init__.py": "",
    f"{SERVICE}/models/__init__.py": "",
}


def write(root: Path, files: Dict[str, str]) -> ConventionScanner:
    for name, text in {**CLEAN_SERVICE, **files}.items():
        (root / name).parent.mkdir(parents=True, exist_ok=True)
        (root / name).write_text(text, encoding="utf-8")
    return ConventionScanner(root)


class TestConventionScanner:
    RULES = (
        "nested_functions",
        "staticmethods",
        "files_with_several_classes",
        "crowded_folders",
        "any_imports",
        "underscore_instance_attributes",
        "underscore_class_attributes",
        "layer_imports",
        "foreign_service_imports",
        "top_level_layer_packages",
        "services_missing_layers",
        "lifecycle_offenders",
        "node_offenders",
        "models_outside_models",
    )

    @pytest.mark.parametrize("rule", RULES)
    def test_an_empty_tree_passes_every_rule(self, tmp_path: Path, rule: str) -> None:
        assert getattr(ConventionScanner(tmp_path), rule)() == []

    @pytest.mark.parametrize("rule", RULES)
    def test_a_clean_service_passes_every_rule(self, tmp_path: Path, rule: str) -> None:
        assert getattr(write(tmp_path, {}), rule)() == []

    @pytest.mark.parametrize(
        ("rule", "name", "text"),
        [
            ("nested_functions", "tests/test_a.py", "def a() -> None:\n    def b() -> None: ...\n"),
            ("nested_functions", f"{SERVICE}/service/a.py", "def a() -> None:\n    def b() -> None: ...\n"),
            ("staticmethods", "plugins/shop/src/erp_shop/a.py", "class A:\n    @staticmethod\n    def b(): ...\n"),
            ("files_with_several_classes", "backend/services/sales/tests/test_a.py", "class A: ...\nclass B: ...\n"),
            ("any_imports", "sdk/src/erp_sdk/a.py", "from typing import Any\n"),
            (
                "underscore_instance_attributes",
                "backend/models/tests/test_a.py",
                "class A:\n    def f(self):\n        self._x = 1\n",
            ),
            ("underscore_class_attributes", "backend/shared/log/src/erp_log/a.py", "class A:\n    _X = 1\n"),
            ("layer_imports", f"{SERVICE}/storage/a.py", "from erp_sales.service.quotes import QuoteService\n"),
            ("layer_imports", f"{SERVICE}/models/a.py", "import erp_sales.storage.quotes\n"),
            ("layer_imports", f"{SERVICE}/api/a.py", "from erp_sales.storage import x\n"),
            (
                "foreign_service_imports",
                "backend/services/stock/src/erp_stock/service/a.py",
                "import erp_sales.models\n",
            ),
            ("foreign_service_imports", "backend/models/src/erp_models/a.py", "from erp_sales.api import x\n"),
            ("top_level_layer_packages", "backend/services/sales/src/service/a.py", ""),
            ("services_missing_layers", "backend/services/stock/src/erp_stock/api/a.py", ""),
            ("lifecycle_offenders", f"{SERVICE}/service/a.py", "class A:\n    def run(self) -> None: ...\n"),
            ("lifecycle_offenders", "backend/shared/x/src/erp_x/a.py", "class A:\n    def start(self) -> None: ...\n"),
            ("node_offenders", f"{SERVICE}/service/a.py", "class CheckNode:\n    async def run(self) -> None: ...\n"),
            ("models_outside_models", f"{SERVICE}/api/a.py", "class A(BaseModel): ...\n"),
            ("models_outside_models", "backend/shared/x/src/erp_x/a.py", "class A(BaseModel): ...\n"),
        ],
    )
    def test_each_rule_catches_its_violation(self, tmp_path: Path, rule: str, name: str, text: str) -> None:
        assert getattr(write(tmp_path, {name: text}), rule)()

    def test_a_sixth_file_in_a_folder_is_caught(self, tmp_path: Path) -> None:
        files = {f"backend/services/sales/tests/service/test_{n}.py": "" for n in range(6)}
        files["backend/services/sales/tests/service/conftest.py"] = ""
        assert write(tmp_path, files).crowded_folders() == ["backend/services/sales/tests/service holds 6"]

    @pytest.mark.parametrize(
        ("name", "text"),
        [
            (f"{SERVICE}/api/a.py", "from erp_sales.service.quotes import QuoteService\nimport erp_models\n"),
            (f"{SERVICE}/service/a.py", "from erp_sales.storage import x\nfrom erp_sales.models import y\n"),
            (f"{SERVICE}/models/quote.py", "class Quote(BaseModel): ...\n"),
            ("backend/models/src/erp_models/sales/quote.py", "class Quote(BaseModel): ...\n"),
            ("backend/shared/x/src/erp_x/runner.py", "class Job(Runnable):\n    def run(self) -> None: ...\n"),
        ],
    )
    def test_what_the_layout_allows_passes(self, tmp_path: Path, name: str, text: str) -> None:
        scanner = write(tmp_path, {name: text})
        assert scanner.layer_imports() == []
        assert scanner.models_outside_models() == []
        assert scanner.lifecycle_offenders() == []
        assert scanner.foreign_service_imports() == []
