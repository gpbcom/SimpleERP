"""An empty new library, plugin or front-end package needs no change to the conventions."""

from __future__ import annotations

from pathlib import Path
from typing import Dict

import pytest

from tests.conventions.convention_scanner import ConventionScanner

SERVICE = "backend/services/sales/src/erp_sales"
CLEAN: Dict[str, str] = {
    f"{SERVICE}/api/__init__.py": "",
    f"{SERVICE}/service/__init__.py": "",
    f"{SERVICE}/storage/__init__.py": "",
    f"{SERVICE}/models/__init__.py": "",
    "backend/models/src/erp_models/__init__.py": "",
}


def write(root: Path, files: Dict[str, str]) -> ConventionScanner:
    for name, text in {**CLEAN, **files}.items():
        (root / name).parent.mkdir(parents=True, exist_ok=True)
        (root / name).write_text(text, encoding="utf-8")
    return ConventionScanner(root)


class TestNewPackages:
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
        "async_before_sync",
        "npm_scope_offenders",
        "shared_models_imports",
        "shared_library_imports",
        "plugin_and_sdk_imports",
    )
    ADDITIONS = (
        {"backend/shared/newlib/src/erp_newlib/__init__.py": ""},
        {"plugins/newplugin/src/erp_newplugin/__init__.py": ""},
        {"frontend/packages/newpkg/package.json": '{"name": "@simpleerp/newpkg", "private": true}'},
    )

    @pytest.mark.parametrize("rule", RULES)
    @pytest.mark.parametrize("addition", ADDITIONS, ids=["library", "plugin", "front-end package"])
    def test_an_empty_new_package_passes_every_rule(self, tmp_path: Path, rule: str, addition: Dict[str, str]) -> None:
        assert getattr(write(tmp_path, addition), rule)() == []

    def test_a_shared_model_importing_a_new_library_is_caught_without_any_list_of_names(self, tmp_path: Path) -> None:
        scanner = write(
            tmp_path,
            {
                "backend/shared/newlib/src/erp_newlib/__init__.py": "",
                "backend/models/src/erp_models/a.py": "import erp_newlib\n",
            },
        )
        assert len(scanner.shared_models_imports()) == 1

    def test_a_plugin_importing_a_new_library_is_caught_without_any_list_of_names(self, tmp_path: Path) -> None:
        scanner = write(
            tmp_path,
            {
                "backend/shared/newlib/src/erp_newlib/__init__.py": "",
                "plugins/newplugin/src/erp_newplugin/__init__.py": "",
                "plugins/newplugin/src/erp_newplugin/a.py": "import erp_newlib\n",
            },
        )
        assert len(scanner.plugin_and_sdk_imports()) == 1

    @pytest.mark.parametrize("rule", RULES)
    def test_a_service_importing_a_new_library_breaks_no_rule(self, tmp_path: Path, rule: str) -> None:
        scanner = write(
            tmp_path,
            {
                "backend/shared/newlib/src/erp_newlib/__init__.py": "",
                f"{SERVICE}/service/a.py": "import erp_newlib\n",
            },
        )
        assert getattr(scanner, rule)() == []
