from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

import pytest
from pydantic import JsonValue

from tests.builders.evidence_builder import EvidenceBuilder
from ticket_docs.models.enums import RunKind, RunPlace
from ticket_docs.models.evidence.evidence_run import EvidenceRun
from ticket_docs.models.evidence.exceptions import (
    SEEvidenceRunInvalidCommit,
    SEEvidenceRunInvalidDate,
    SEEvidenceRunInvalidDirty,
    SEEvidenceRunInvalidFolder,
    SEEvidenceRunInvalidKind,
    SEEvidenceRunInvalidText,
    SEEvidenceRunInvalidWhere,
)


class TestEvidenceRun:
    BOOTSTRAP = (
        "# GH-1 — local 2026-11-10: local-2026-11-10-tdd-red-ai-test-cost-cli\n\n| | |\n|---|---|\n"
        "| **What** | TEST-7 red run: ai-test-cost command line before the code |\n"
        "| **Command** | `cd .claude/skills/ai-test-cost && ../.venv/bin/pytest -q tests/api "
        "--junitxml=<this folder>/report.xml` |\n"
        "| **Commit** | `ef0211fe52275e7c4bd7b9ee41ef02355e3d51ca` on `worktree-agent-aa805b65c29436053` |\n"
        "| **Kind** | unit |\n"
        "| **Where** | local |\n"
        "| **Date** | 2026-11-10 10:17 |\n"
        "| **Result** | ❌ FAIL 0/3 (exit 2; 0 failures, 3 errors) — expected red (TDD), as expected |\n\n"
        "## Artefacts\n\n| File | Holds |\n|---|---|\n| [console.txt](console.txt) | The raw console output |\n"
    )

    def test_defaults(self) -> None:
        run = EvidenceRun(folder="local-2026-11-10-unit-x")
        assert (run.commit, run.kind, run.where, run.date, run.result) == (None, None, None, None, None)
        assert not run.dirty

    def test_full_valid_construction(self) -> None:
        run = EvidenceRun(
            folder=" local-2026-11-10-unit-x ",
            what="What it proves",
            command="pytest -q",
            commit="A" * 40,
            branch="feature/GH-1-x",
            dirty=True,
            kind="unit",
            where="ci",
            date="2026-11-10 10:17",
            result="✅ PASS 1/1 (exit 0; 0 failures, 0 errors)",
        )
        assert run.folder == "local-2026-11-10-unit-x"
        assert run.commit == "a" * 40
        assert (run.kind, run.where) == (RunKind.UNIT, RunPlace.CI)
        assert run.date == datetime(2026, 11, 10, 10, 17)

    @pytest.mark.parametrize(
        "name", ["what", "command", "commit", "branch", "kind", "where", "date", "result", "dirty"]
    )
    def test_none_becomes_the_default(self, name: str) -> None:
        run = EvidenceRun.model_validate({"folder": "local-2026-11-10-unit-x", name: None})
        assert getattr(run, name) == EvidenceRun.model_fields[name].get_default()

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("folder", "", SEEvidenceRunInvalidFolder),
            ("folder", 3, SEEvidenceRunInvalidFolder),
            ("what", "  ", SEEvidenceRunInvalidText),
            ("command", 1, SEEvidenceRunInvalidText),
            ("commit", "ef0211f", SEEvidenceRunInvalidCommit),
            ("commit", "<40-character commit hash>", SEEvidenceRunInvalidCommit),
            ("kind", "<unit | gui | e2e | check>", SEEvidenceRunInvalidKind),
            ("where", "laptop", SEEvidenceRunInvalidWhere),
            ("date", "10/11/2026", SEEvidenceRunInvalidDate),
            ("date", 5, SEEvidenceRunInvalidDate),
            ("dirty", "yes", SEEvidenceRunInvalidDirty),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        fields: Dict[str, JsonValue] = {"folder": "local-2026-11-10-unit-x", name: value}
        with pytest.raises(error):
            EvidenceRun.model_validate(fields)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            EvidenceRun.model_validate({"folder": "local-2026-11-10-unit-x", "other": 1})

    def test_round_trip(self) -> None:
        run = EvidenceRun.from_readme("local-2026-11-10-tdd-red-ai-test-cost-cli", self.BOOTSTRAP)
        assert EvidenceRun.model_validate(run.model_dump()) == run

    def test_a_bootstrap_readme_is_read_unchanged(self) -> None:
        run = EvidenceRun.from_readme("local-2026-11-10-tdd-red-ai-test-cost-cli", self.BOOTSTRAP)
        assert run.what == "TEST-7 red run: ai-test-cost command line before the code"
        assert str(run.command).startswith("cd .claude/skills/ai-test-cost && ")
        assert (run.commit, run.branch, run.dirty) == (
            "ef0211fe52275e7c4bd7b9ee41ef02355e3d51ca",
            "worktree-agent-aa805b65c29436053",
            False,
        )
        assert (run.kind, run.where, run.date) == (RunKind.UNIT, RunPlace.LOCAL, datetime(2026, 11, 10, 10, 17))
        assert run.check == "tdd-red-ai-test-cost-cli"
        assert (run.icon, run.counts) == ("❌", "0/3")
        assert run.expected_red
        assert not run.passed
        assert not run.invalid

    def test_a_dirty_tree_and_an_escaped_pipe_are_read(self) -> None:
        text = EvidenceBuilder(Path(".")).readme(
            "ci-2026-11-11-checks",
            {
                "Commit": f"`{'b' * 40}` on `develop` (working tree has uncommitted changes)",
                "Command": "`pytest -q 2>&1 \\| tail`",
                "Where": "ci",
            },
        )
        run = EvidenceRun.from_readme("ci-2026-11-11-checks", text)
        assert (run.commit, run.branch, run.dirty, run.where) == ("b" * 40, "develop", True, RunPlace.CI)
        assert run.command == "pytest -q 2>&1 | tail"
        assert run.check == "checks"
        assert run.passed

    @pytest.mark.parametrize(
        ("result", "invalid", "expected_red", "counts"),
        [
            ("⚠️ INVALID: pytest-html was missing. Re-run in [x](../x/README.md)", True, False, None),
            ("❌ FAIL 2/3 (exit 1; 1 failures, 0 errors) — expected red (TDD), UNEXPECTED GREEN", False, False, "2/3"),
            ("🔴 RED 3 failed (expected, TEST-7)", False, False, None),
        ],
    )
    def test_the_result_says_how_the_run_ended(
        self, result: str, invalid: bool, expected_red: bool, counts: Optional[str]
    ) -> None:
        run = EvidenceRun(folder="local-2026-11-10-tdd-red-x", result=result)
        assert (run.invalid, run.expected_red, run.counts) == (invalid, expected_red, counts)

    def test_missing_rows_stay_empty(self) -> None:
        run = EvidenceRun.from_readme("dev-2026-11-10-stage", "# Nothing here\n")
        assert (run.command, run.commit, run.kind, run.result, run.icon) == (None, None, None, None, "")
