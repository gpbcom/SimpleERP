from __future__ import annotations

import json
import re
from pathlib import Path
from typing import ClassVar, Dict, List

import pytest
import yaml


class TestPnpmWorkspace:
    ROOT: ClassVar[Path] = Path(__file__).resolve().parents[2]
    WORKSPACE_PACKAGES: ClassVar[List[str]] = [
        "frontend/backoffice",
        "frontend/mobile",
        "frontend/portals/*",
        "frontend/packages/*",
    ]
    LOCK_IMPORTERS: ClassVar[List[str]] = [".", "frontend/backoffice", "frontend/mobile"]
    PACKAGE_MANAGER_PATTERN: ClassVar[str] = r"^pnpm@\d+\.\d+\.\d+$"
    NODE_MAJOR_PATTERN: ClassVar[str] = r"\d+"

    def read_json(self, relative: str) -> Dict[str, object]:
        data = json.loads((self.ROOT / relative).read_text(encoding="utf-8"))
        assert isinstance(data, dict)
        return data

    def read_yaml(self, relative: str) -> Dict[str, object]:
        data = yaml.safe_load((self.ROOT / relative).read_text(encoding="utf-8"))
        assert isinstance(data, dict)
        return data

    def test_the_root_package_is_private(self) -> None:
        assert self.read_json("package.json").get("private") is True

    def test_the_package_manager_is_an_exact_pnpm_version(self) -> None:
        package_manager = self.read_json("package.json").get("packageManager")
        assert isinstance(package_manager, str)
        assert re.match(self.PACKAGE_MANAGER_PATTERN, package_manager)

    def test_the_engines_allow_node_22_only(self) -> None:
        engines = self.read_json("package.json").get("engines")
        assert isinstance(engines, dict)
        node = engines.get("node")
        assert isinstance(node, str)
        assert "22" in node
        assert set(re.findall(self.NODE_MAJOR_PATTERN, node)) == {"22"}

    def test_the_workspace_lists_the_front_end_folders(self) -> None:
        packages = self.read_yaml("pnpm-workspace.yaml").get("packages")
        assert isinstance(packages, list)
        for expected in self.WORKSPACE_PACKAGES:
            assert expected in packages

    def test_the_lock_file_is_pinned_for_every_importer(self) -> None:
        lock = self.read_yaml("pnpm-lock.yaml")
        assert "lockfileVersion" in lock
        importers = lock.get("importers")
        assert isinstance(importers, dict)
        for expected in self.LOCK_IMPORTERS:
            assert expected in importers

    @pytest.mark.parametrize("app", ["frontend/backoffice", "frontend/mobile"])
    def test_each_app_is_a_private_named_package(self, app: str) -> None:
        package = self.read_json(f"{app}/package.json")
        assert package.get("private") is True
        name = package.get("name")
        assert isinstance(name, str)
        assert name.strip()
