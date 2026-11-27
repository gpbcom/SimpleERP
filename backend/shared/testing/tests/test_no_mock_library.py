from __future__ import annotations

import ast
import re
import tomllib
from pathlib import Path
from typing import ClassVar, List

import pytest


class TestNoMockLibrary:
    LIBRARY: ClassVar[Path] = Path(__file__).resolve().parent.parent
    MOCK_LIBRARIES: ClassVar[List[str]] = [
        "mock",
        "pytest-mock",
        "asynctest",
        "requests-mock",
        "responses",
        "respx",
        "httpretty",
        "aioresponses",
    ]

    def _names(self) -> List[str]:
        data = tomllib.loads((self.LIBRARY / "pyproject.toml").read_text(encoding="utf-8"))
        specs: List[str] = list(data.get("project", {}).get("dependencies", []))
        for group in data.get("project", {}).get("optional-dependencies", {}).values():
            specs.extend(group)
        for group in data.get("dependency-groups", {}).values():
            specs.extend(item for item in group if isinstance(item, str))
        return [re.split(r"[\s<>=!~;\[(]", spec.strip(), maxsplit=1)[0].lower().replace("_", "-") for spec in specs]

    def _imports(self, path: Path) -> List[str]:
        names: List[str] = []
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            if isinstance(node, ast.Import):
                names.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module is not None:
                names.append(node.module)
                names.extend(f"{node.module}.{alias.name}" for alias in node.names)
        return names

    def test_no_dependency_of_the_library_is_a_mock_library(self) -> None:
        assert [name for name in self._names() if name in self.MOCK_LIBRARIES] == []

    @pytest.mark.parametrize("folder", ["src", "tests"])
    def test_no_python_file_imports_a_mock_library(self, folder: str) -> None:
        files = sorted((self.LIBRARY / folder).rglob("*.py"))
        offenders = [
            str(path)
            for path in files
            for name in self._imports(path)
            if name in ("mock", "unittest.mock") or name.startswith(("mock.", "unittest.mock."))
        ]

        assert files != []
        assert offenders == []
