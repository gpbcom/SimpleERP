from __future__ import annotations

import logging
from datetime import datetime
from typing import Optional

import pytest

from ticket_docs.models.enums import Expectation
from ticket_docs.models.evidence.actions_run import ActionsRun
from ticket_docs.models.evidence.evidence_run import EvidenceRun
from ticket_docs.models.evidence.run_counts import RunCounts
from ticket_docs.service.runs.readme_renderer import ReadmeRenderer


class TestReadmeRenderer:
    @pytest.mark.parametrize(
        ("counts", "exit_code", "expectation", "line"),
        [
            (RunCounts(tests=5), 0, Expectation.GREEN, "✅ PASS 5/5 (exit 0; 0 failures, 0 errors)"),
            (RunCounts(tests=5, failures=1), 1, Expectation.GREEN, "❌ FAIL 4/5 (exit 1; 1 failures, 0 errors)"),
            (
                RunCounts(tests=3, errors=3),
                2,
                Expectation.RED,
                "❌ FAIL 0/3 (exit 2; 0 failures, 3 errors) — expected red (TDD), as expected",
            ),
            (
                RunCounts(tests=2),
                0,
                Expectation.RED,
                "✅ PASS 2/2 (exit 0; 0 failures, 0 errors) — expected red (TDD), UNEXPECTED GREEN",
            ),
            (None, 0, Expectation.GREEN, "✅ PASS (exit 0)"),
            (None, 4, Expectation.GREEN, "❌ FAIL (exit 4)"),
        ],
    )
    def test_the_result_line_follows_the_bootstrap_format(
        self, logger: logging.Logger, counts: Optional[RunCounts], exit_code: int, expectation: Expectation, line: str
    ) -> None:
        assert ReadmeRenderer(logger).result(counts, exit_code, expectation) == line

    def test_an_actions_run_result_names_the_run(self, logger: logging.Logger) -> None:
        run = ActionsRun.model_validate(
            {
                "conclusion": "failure",
                "headSha": "f" * 40,
                "headBranch": "feature/GH-1-x",
                "url": "https://github.com/o/r/actions/runs/9",
                "displayTitle": "stage dev",
                "createdAt": "2026-11-10T08:00:00Z",
            }
        )
        renderer = ReadmeRenderer(logger)
        assert renderer.actions_result(run, Expectation.GREEN) == (
            "❌ FAIL (Actions run https://github.com/o/r/actions/runs/9 concluded failure)"
        )
        assert renderer.actions_result(run, Expectation.RED).endswith("— expected red (TDD), as expected")

    def test_a_readme_reads_back_as_the_same_run(self, logger: logging.Logger) -> None:
        run = EvidenceRun(
            folder="local-2026-11-10-unit-storage",
            what="The storage tests | after the code",
            command="cd . && pytest -q 2>&1 | tail",
            commit="1" * 40,
            branch="feature/GH-1-x",
            dirty=True,
            kind="unit",
            where="local",
            date=datetime(2026, 11, 10, 11, 5),
            result="✅ PASS 3/3 (exit 0; 0 failures, 0 errors)",
        )
        text = ReadmeRenderer(logger).readme("GH-1", run, ["console.txt", "report.xml", "report.html", "notes.txt"])
        assert text.startswith("# GH-1 — local 2026-11-10: local-2026-11-10-unit-storage\n")
        assert "| **Command** | `cd . && pytest -q 2>&1 \\| tail` |" in text
        assert f"| **Commit** | `{'1' * 40}` on `feature/GH-1-x` (working tree has uncommitted changes) |" in text
        assert "| [report.xml](report.xml) | JUnit XML report |" in text
        assert "notes.txt" not in text
        assert EvidenceRun.from_readme(run.folder, text) == run

    def test_the_artefacts_table_lists_only_what_exists(self, logger: logging.Logger) -> None:
        run = EvidenceRun(folder="dev-2026-11-10-stage", result="✅ PASS (exit 0)")
        text = ReadmeRenderer(logger).readme("GH-1", run, ["actions.log", "artifacts/", "console.txt"])
        artefacts = text.split("## Artefacts", 1)[1]
        assert "[console.txt](console.txt)" in artefacts
        assert "[actions.log](actions.log)" in artefacts
        assert "[artifacts/](artifacts/)" in artefacts
        assert "report.xml" not in artefacts
