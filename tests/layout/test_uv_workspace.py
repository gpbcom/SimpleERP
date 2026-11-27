from __future__ import annotations

# Standard library imports
import tomllib
from pathlib import Path
from typing import ClassVar, Dict, List

# Third-party imports
import pytest


class TestUvWorkspace:
    ROOT: ClassVar[Path] = Path(__file__).resolve().parents[2]
    REQUIRES_PYTHON: ClassVar[str] = ">=3.13,<3.14"
    EXPECTED_MEMBERS: ClassVar[List[str]] = [
        "backend/models",
        "backend/shared/*",
        "backend/services/*",
        "plugins/*",
        "sdk",
    ]

    def read_toml(self, path: Path) -> Dict[str, Dict[str, object]]:
        with path.open("rb") as handle:
            return tomllib.load(handle)

    def test_the_workspace_lists_every_kind_of_member(self) -> None:
        root = self.read_toml(self.ROOT / "pyproject.toml")
        members = root["tool"]["uv"]["workspace"]["members"]  # type: ignore[index]
        assert set(self.EXPECTED_MEMBERS) <= set(members)

    def test_the_root_requires_python_3_13(self) -> None:
        root = self.read_toml(self.ROOT / "pyproject.toml")
        assert root["project"]["requires-python"] == self.REQUIRES_PYTHON
        version = (self.ROOT / ".python-version").read_text(encoding="utf-8")
        assert version.strip().startswith("3.13")

    @pytest.mark.parametrize("member", ["backend/models", "sdk"])
    def test_a_member_has_a_named_project_for_python_3_13(self, member: str) -> None:
        path = self.ROOT / member / "pyproject.toml"
        assert path.is_file()
        project = self.read_toml(path)["project"]
        assert str(project["name"]).strip()
        assert project["requires-python"] == self.REQUIRES_PYTHON

    @pytest.mark.parametrize("member", ["backend/models", "sdk"])
    def test_a_member_is_pinned_in_the_one_lock(self, member: str) -> None:
        path = self.ROOT / member / "pyproject.toml"
        assert path.is_file()
        name = str(self.read_toml(path)["project"]["name"]).lower().replace("_", "-")
        lock = self.read_toml(self.ROOT / "uv.lock")
        assert name in lock["manifest"]["members"]  # type: ignore[operator]

    def test_the_shared_models_package_exists(self) -> None:
        assert (self.ROOT / "backend/models/src/erp_models/__init__.py").is_file()
