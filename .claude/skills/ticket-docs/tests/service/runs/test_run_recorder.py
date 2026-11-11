from __future__ import annotations

import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

import pytest
from pydantic import JsonValue

from harness_core.git.git_repository import GitRepository
from harness_core.shell.shell_command_splitter import ShellCommandSplitter
from tests.builders.fake_gh import FakeGh
from tests.builders.git_sandbox import GitSandbox
from ticket_docs.models.enums import RunKind, RunPlace
from ticket_docs.models.evidence.evidence_run import EvidenceRun
from ticket_docs.models.evidence.run_request import RunRequest
from ticket_docs.service.runs.command_shape import CommandShape
from ticket_docs.service.runs.readme_renderer import ReadmeRenderer
from ticket_docs.service.runs.run_recorder import RunRecorder
from ticket_docs.storage.evidence.evidence_repository import EvidenceRepository
from ticket_docs.storage.evidence.report_reader import ReportReader
from ticket_docs.storage.github.gh_client import GhClient
from ticket_docs.storage.processes.command_runner import CommandRunner


class TestRunRecorder:
    PASSING = "def test_ok():\n    assert True\n"
    FAILING = "def test_not_yet():\n    assert False\n"

    def record(
        self,
        sandbox: GitSandbox,
        logger: logging.Logger,
        fields: Dict[str, JsonValue],
        cwd: Optional[Path] = None,
    ) -> RunRecorder:
        request = RunRequest.model_validate(
            {"ticket": "GH-1", "kind": "unit", "where": "local", "check": "unit-x", "what": "It works", **fields}
        )
        recorder = RunRecorder(
            request,
            GitRepository(sandbox.root, logger),
            cwd or sandbox.root,
            EvidenceRepository(sandbox.root / "docs" / "tickets", logger),
            CommandRunner(logger),
            ReportReader(logger),
            GhClient("gpbcom/simple-erp", logger=logger),
            CommandShape(logger, ShellCommandSplitter(logger)),
            ReadmeRenderer(logger),
            logger,
        )
        recorder.execute()
        return recorder

    def pytest_command(self, test: str) -> JsonValue:
        return [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", test]

    def read(self, folder: Optional[Path]) -> EvidenceRun:
        assert folder is not None
        return EvidenceRun.from_readme(folder.name, (folder / "README.md").read_text(encoding="utf-8"))

    def test_a_green_pytest_run_keeps_its_reports(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.commit("tests/test_ok.py", self.PASSING)
        recorder = self.record(sandbox, logger, {"command": self.pytest_command("tests/test_ok.py")})
        today = datetime.now().strftime("%Y-%m-%d")
        assert (
            recorder.folder == sandbox.root / "docs" / "tickets" / "GH-1" / "tests-evidences" / f"local-{today}-unit-x"
        )
        assert recorder.exit_code == 0
        assert recorder.verdict == "✅ PASS 1/1 (exit 0; 0 failures, 0 errors)"
        run = self.read(recorder.folder)
        assert (run.commit, run.branch, run.dirty) == (sandbox.head(), "feature/GH-1-thing", False)
        assert (run.kind, run.where, run.what, run.result) == (
            RunKind.UNIT,
            RunPlace.LOCAL,
            "It works",
            recorder.verdict,
        )
        assert str(run.command).startswith("cd . && ")
        assert "--junitxml=<this folder>/report.xml" in str(run.command)
        assert {"console.txt", "report.xml", "report.html"} <= {path.name for path in recorder.folder.iterdir()}
        assert "1 passed" in (recorder.folder / "console.txt").read_text(encoding="utf-8")

    def test_a_red_run_is_recorded_as_expected(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.commit("tests/test_red.py", self.FAILING)
        recorder = self.record(
            sandbox, logger, {"command": self.pytest_command("tests/test_red.py"), "expectation": "red"}
        )
        assert recorder.exit_code == 1
        assert recorder.verdict == "❌ FAIL 0/1 (exit 1; 1 failures, 0 errors) — expected red (TDD), as expected"
        assert self.read(recorder.folder).expected_red

    def test_a_red_run_that_passes_is_flagged(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.commit("tests/test_ok.py", self.PASSING)
        recorder = self.record(
            sandbox, logger, {"command": self.pytest_command("tests/test_ok.py"), "expectation": "red"}
        )
        assert recorder.verdict.endswith("UNEXPECTED GREEN")
        assert recorder.exit_code == 0

    def test_any_command_is_kept_with_its_console_and_dirty_tree(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.write("README.md", "changed\n")
        (sandbox.root / "sub").mkdir()
        command: JsonValue = [sys.executable, "-c", "print('checked')"]
        recorder = self.record(sandbox, logger, {"command": command, "kind": "check"}, cwd=sandbox.root / "sub")
        assert recorder.verdict == "✅ PASS (exit 0)"
        run = self.read(recorder.folder)
        assert run.dirty
        assert str(run.command).startswith("cd sub && ")
        assert recorder.folder is not None
        assert sorted(path.name for path in recorder.folder.iterdir()) == ["README.md", "console.txt"]
        assert "report.xml" not in (recorder.folder / "README.md").read_text(encoding="utf-8")

    def test_the_same_check_twice_gets_a_second_folder(self, tmp_path: Path, logger: logging.Logger) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        command: JsonValue = [sys.executable, "-c", "raise SystemExit(3)"]
        first = self.record(sandbox, logger, {"command": command})
        second = self.record(sandbox, logger, {"command": command})
        assert first.folder is not None
        assert second.folder is not None
        assert second.folder.name == f"{first.folder.name}-2"
        assert (second.exit_code, second.verdict) == (3, "❌ FAIL (exit 3)")

    def test_a_playwright_run_keeps_its_report_and_results(
        self, tmp_path: Path, logger: logging.Logger, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        tools = tmp_path / "tools"
        tools.mkdir()
        results = json.dumps({"stats": {"expected": 4, "unexpected": 1, "flaky": 0, "skipped": 0}})
        (tools / "npx").write_text(
            "#!/bin/sh\nmkdir -p playwright-report test-results\n"
            "echo '<html/>' > playwright-report/index.html\n"
            f"echo '{results}' > test-results/results.json\nexit 1\n",
            encoding="utf-8",
        )
        (tools / "npx").chmod(0o755)
        monkeypatch.setenv("PATH", f"{tools}{os.pathsep}{os.environ['PATH']}")
        recorder = self.record(sandbox, logger, {"command": ["npx", "playwright", "test"], "kind": "gui"})
        assert recorder.folder is not None
        assert (recorder.folder / "playwright-report" / "index.html").is_file()
        assert (recorder.folder / "results.json").is_file()
        assert recorder.verdict == "❌ FAIL 4/5 (exit 1; 1 failures, 0 errors)"
        readme = (recorder.folder / "README.md").read_text(encoding="utf-8")
        assert "[playwright-report/index.html](playwright-report/index.html)" in readme

    def test_an_actions_run_is_recorded_from_github(self, tmp_path: Path, logger: logging.Logger, gh: FakeGh) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        gh.answer(
            ["run", "view", "42", "--repo", "gpbcom/simple-erp", "--json"],
            stdout=json.dumps(
                {
                    "conclusion": "success",
                    "headSha": "9" * 40,
                    "headBranch": "feature/GH-1-thing",
                    "url": "https://github.com/gpbcom/simple-erp/actions/runs/42",
                    "displayTitle": "stage dev",
                    "createdAt": "2026-11-09T22:30:00Z",
                }
            ),
        )
        gh.answer(["run", "download", "42"], files={"playwright-report/index.html": "<html/>"})
        gh.answer(["run", "view", "42", "--repo", "gpbcom/simple-erp", "--log"], stdout="smoke\tok\n")
        recorder = self.record(
            sandbox, logger, {"command": None, "run_id": "42", "kind": "e2e", "where": "dev", "check": "stage"}
        )
        assert recorder.exit_code == 0
        assert recorder.folder is not None
        run = self.read(recorder.folder)
        local = datetime.fromisoformat("2026-11-09T22:30:00+00:00").astimezone()
        assert recorder.folder.name == f"dev-{local:%Y-%m-%d}-stage"
        assert (run.commit, run.branch, run.where, run.kind) == (
            "9" * 40,
            "feature/GH-1-thing",
            RunPlace.DEV,
            RunKind.E2E,
        )
        assert run.date == local.replace(tzinfo=None, second=0, microsecond=0)
        assert run.passed
        assert "actions/runs/42" in str(run.result)
        assert str(run.command).startswith("gh run view 42 --repo gpbcom/simple-erp --json ")
        assert (recorder.folder / "actions.log").read_text(encoding="utf-8") == "smoke\tok\n"
        assert (recorder.folder / "artifacts" / "playwright-report" / "index.html").is_file()
        assert (recorder.folder / "console.txt").is_file()

    def test_a_failed_actions_run_without_artifacts_is_still_recorded(
        self, tmp_path: Path, logger: logging.Logger, gh: FakeGh
    ) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        gh.answer(
            ["run", "view", "43", "--repo", "gpbcom/simple-erp", "--json"],
            stdout=json.dumps(
                {
                    "conclusion": "failure",
                    "headSha": "8" * 40,
                    "headBranch": "feature/GH-1-thing",
                    "url": "https://github.com/gpbcom/simple-erp/actions/runs/43",
                    "displayTitle": "ci",
                    "createdAt": "2026-11-10T09:00:00Z",
                }
            ),
        )
        gh.answer(["run", "download", "43"], exit_code=1, stderr="no valid artifacts found to download")
        recorder = self.record(
            sandbox, logger, {"command": None, "run_id": "43", "kind": "check", "where": "ci", "check": "checks"}
        )
        assert recorder.exit_code == 1
        assert recorder.verdict.startswith("❌ FAIL (Actions run ")
        assert recorder.folder is not None
        assert "no valid artifacts" in (recorder.folder / "console.txt").read_text(encoding="utf-8")
        assert not (recorder.folder / "artifacts").exists() or not any((recorder.folder / "artifacts").iterdir())
        assert "[artifacts/]" not in (recorder.folder / "README.md").read_text(encoding="utf-8")
