from __future__ import annotations

import os
import time
from pathlib import Path

import pytest

from progress_updates.models.enums import TaskSource, TaskState
from progress_updates.models.exceptions import SESourceUnreadableError
from progress_updates.storage.evidence.evidence_reader import EvidenceReader


class TestEvidenceReader:
    def _run(self, root: Path, name: str, result: str, age_s: int) -> None:
        folder = root / name
        folder.mkdir(parents=True)
        (folder / "README.md").write_text(f"| **Result** | {result} |\n", encoding="utf-8")
        stamp = time.time() - age_s
        os.utime(folder, (stamp, stamp))

    def test_the_newest_runs_are_reported_with_their_result(self, tmp_path: Path) -> None:
        self._run(tmp_path, "local-2026-11-11-unit-skill", "✅ PASS 43/43 (exit 0)", 30)
        self._run(tmp_path, "local-2026-11-11-tdd-red-skill", "❌ FAIL 0/5 (exit 1)", 60)
        self._run(tmp_path, "local-2026-11-10-old", "⚠️ invalid", 90)
        tasks = EvidenceReader(tmp_path, 2, 160).tasks()
        assert [(task.name, task.state) for task in tasks] == [
            ("local-2026-11-11-unit-skill", TaskState.DONE),
            ("local-2026-11-11-tdd-red-skill", TaskState.FAILED),
        ]
        assert tasks[0].source is TaskSource.EVIDENCE
        assert tasks[0].detail == "✅ PASS 43/43 (exit 0)"

    def test_an_invalid_run_is_a_warning(self, tmp_path: Path) -> None:
        self._run(tmp_path, "local-2026-11-11-x", "⚠️ invalid: stopped", 10)
        assert EvidenceReader(tmp_path, 5, 160).tasks()[0].state is TaskState.WARNING

    def test_an_expected_red_run_counts_as_done(self, tmp_path: Path) -> None:
        self._run(tmp_path, "local-2026-11-11-tdd-red-x", "❌ FAIL 0/5 (exit 1) — expected red (TDD), as expected", 10)
        assert EvidenceReader(tmp_path, 5, 160).tasks()[0].state is TaskState.DONE

    def test_a_red_run_that_was_not_expected_still_fails(self, tmp_path: Path) -> None:
        self._run(tmp_path, "local-2026-11-11-tdd-red-y", "✅ PASS 5/5 — expected red (TDD), NOT as expected", 10)
        assert EvidenceReader(tmp_path, 5, 160).tasks()[0].state is TaskState.FAILED

    def test_a_missing_folder_cannot_be_read(self, tmp_path: Path) -> None:
        with pytest.raises(SESourceUnreadableError):
            EvidenceReader(tmp_path / "missing", 5, 160).tasks()
