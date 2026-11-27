"""The README's quick start installs both workspaces from their locks."""

from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import ClassVar, List


class TestReadmeQuickStart:
    README: ClassVar[Path] = Path(__file__).resolve().parents[2] / "README.md"
    HEADING: ClassVar[str] = "Development setup"
    FENCE: ClassVar[str] = "```"

    def section_lines(self) -> List[str]:
        lines = self.README.read_text(encoding="utf-8").splitlines()
        start = next(i for i, line in enumerate(lines) if line.startswith("#") and self.HEADING in line)
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("#")), len(lines))
        return lines[start + 1 : end]

    def bash_block(self) -> List[str]:
        lines = self.section_lines()
        start = next(i for i, line in enumerate(lines) if line.strip() == f"{self.FENCE}bash")
        end = next(i for i in range(start + 1, len(lines)) if lines[i].strip() == self.FENCE)
        return lines[start + 1 : end]

    def table_row(self, tool: str) -> str:
        lines = self.README.read_text(encoding="utf-8").splitlines()
        return next(line for line in lines if line.startswith("|") and tool in line.split("|")[1])

    def test_the_quick_start_installs_python_from_the_lock(self) -> None:
        assert any(line.startswith("uv sync --locked") for line in self.bash_block())

    def test_the_quick_start_installs_the_front_ends_from_the_lock(self) -> None:
        assert any(line.startswith("pnpm install --frozen-lockfile") for line in self.bash_block())

    def test_the_quick_start_no_longer_waits_for_the_front_end_folder(self) -> None:
        assert "once frontend/ exists" not in "\n".join(self.bash_block())

    def test_the_prerequisites_name_node_22(self) -> None:
        assert "22" in self.table_row("Node.js")

    def test_the_prerequisites_still_name_python_3_13(self) -> None:
        assert "3.13" in self.table_row("uv")
