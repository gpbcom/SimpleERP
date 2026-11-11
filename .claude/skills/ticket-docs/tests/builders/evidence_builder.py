from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional, Sequence


class EvidenceBuilder:
    """Writes evidence folders the way the bootstrap recorder and ``record-run`` do."""

    SHA = "a" * 40

    def __init__(self, root: Path, ticket: str = "GH-1") -> None:
        self.root = root
        self.ticket = ticket

    def readme(self, folder: str, rows: Optional[Dict[str, Optional[str]]] = None) -> str:
        values: Dict[str, Optional[str]] = {
            "What": "TEST-7 run of the storage tests",
            "Command": "`cd . && pytest -q tests --junitxml=<this folder>/report.xml`",
            "Commit": f"`{self.SHA}` on `feature/GH-1-thing`",
            "Kind": "unit",
            "Where": "local",
            "Date": "2026-11-10 10:17",
            "Result": "✅ PASS 3/3 (exit 0; 0 failures, 0 errors)",
        }
        values.update(rows or {})
        date = values["Date"] or "2026-11-10"
        lines = [f"# {self.ticket} — {values['Where']} {date[:10]}: {folder}", "", "| | |", "|---|---|"]
        lines += [f"| **{label}** | {value} |" for label, value in values.items() if value is not None]
        lines += ["", "## Artefacts", "", "| File | Holds |", "|---|---|"]
        lines += ["| [console.txt](console.txt) | The raw console output |", ""]
        return "\n".join(lines)

    def folder(
        self,
        name: str,
        rows: Optional[Dict[str, Optional[str]]] = None,
        files: Sequence[str] = ("console.txt", "report.xml"),
    ) -> Path:
        path = self.root / self.ticket / "tests-evidences" / name
        path.mkdir(parents=True, exist_ok=True)
        (path / "README.md").write_text(self.readme(name, rows), encoding="utf-8")
        for file in files:
            target = path / file
            if file.endswith("/"):
                target.mkdir(parents=True, exist_ok=True)
                (target / "index.html").write_text("<html></html>\n", encoding="utf-8")
            else:
                target.write_text(self.junit() if file == "report.xml" else "output\n", encoding="utf-8")
        return path

    def junit(self, tests: int = 3, failures: int = 0, errors: int = 0) -> str:
        return (
            '<?xml version="1.0" encoding="utf-8"?><testsuites>'
            f'<testsuite name="pytest" tests="{tests}" failures="{failures}" errors="{errors}" skipped="0"/>'
            "</testsuites>\n"
        )
