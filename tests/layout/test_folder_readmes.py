from __future__ import annotations

from pathlib import Path
from typing import ClassVar, List

import pytest


class TestFolderReadmes:
    ROOT: ClassVar[Path] = Path(__file__).resolve().parents[2]
    D438: ClassVar[Path] = ROOT / "docs" / "specs" / "06-decisions" / "technical" / "d438-repository-layout.md"
    FOLDERS: ClassVar[List[str]] = [
        "backend",
        "backend/models",
        "backend/shared",
        "backend/services",
        "frontend",
        "frontend/backoffice",
        "frontend/mobile",
        "frontend/packages",
        "plugins",
        "sdk",
        "infra",
        "infra/compose",
        "infra/helm",
        "infra/terraform",
        "packs",
        "packs/countries",
        "packs/sectors",
    ]

    def readme_lines(self, folder: str) -> List[str]:
        path = self.ROOT / folder / "README.md"
        assert path.is_file(), f"{folder}/README.md is missing."
        return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

    @pytest.mark.parametrize("folder", FOLDERS, ids=lambda folder: folder)
    def test_the_folder_has_a_readme(self, folder: str) -> None:
        assert (self.ROOT / folder / "README.md").is_file()

    @pytest.mark.parametrize("folder", FOLDERS, ids=lambda folder: folder)
    def test_the_readme_starts_with_a_title(self, folder: str) -> None:
        lines = self.readme_lines(folder)
        assert lines
        assert lines[0].startswith("# ")
        assert lines[0][2:].strip()

    @pytest.mark.parametrize("folder", FOLDERS, ids=lambda folder: folder)
    def test_the_readme_says_what_the_folder_holds(self, folder: str) -> None:
        lines = self.readme_lines(folder)
        assert len(lines) > 1
        assert any(not line.startswith("#") for line in lines[1:])

    @pytest.mark.parametrize("folder", FOLDERS, ids=lambda folder: folder)
    def test_the_readme_links_d438(self, folder: str) -> None:
        text = "\n".join(self.readme_lines(folder))
        targets = [part.split(")", 1)[0] for part in text.split("](")[1:]]
        resolved = [
            (self.ROOT / folder / target.split("#", 1)[0]).resolve()
            for target in targets
            if target.split("#", 1)[0].endswith("d438-repository-layout.md")
        ]
        assert self.D438.resolve() in resolved
