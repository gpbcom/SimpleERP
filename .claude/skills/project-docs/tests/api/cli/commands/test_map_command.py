from __future__ import annotations

from pathlib import Path

import pytest

from harness_core.testing.git_sandbox import GitSandbox
from project_docs.api.cli.main import main


class TestMapCommand:
    def test_each_chapter_is_printed_with_the_paths_that_concern_it(
        self, caller_in_sandbox: GitSandbox, capsys: pytest.CaptureFixture[str]
    ) -> None:
        caller_in_sandbox.commit("code", {"src/api/cli/main.py": "x\n", "src/api/routes.py": "y\n", "LICENSE": "z\n"})
        assert main(["map", "--base", "develop"]) == 0
        assert capsys.readouterr().out.splitlines() == [
            "README.md <- LICENSE, src/api/cli/main.py, src/api/routes.py",
            "docs/technical/api.md <- src/api/cli/main.py, src/api/routes.py",
        ]

    def test_a_branch_without_documentation_impact_prints_nothing(
        self, caller_in_sandbox: GitSandbox, capsys: pytest.CaptureFixture[str]
    ) -> None:
        caller_in_sandbox.commit("changelog", {"changelog.d/GH-7.added.md": "Customers.\n"})
        assert main(["map", "--base", "develop"]) == 0
        assert capsys.readouterr().out == ""

    def test_an_unknown_base_is_a_failure_the_person_can_fix(
        self, caller_in_sandbox: GitSandbox, capsys: pytest.CaptureFixture[str]
    ) -> None:
        assert main(["map", "--base", "origin/nowhere"]) == 2
        captured = capsys.readouterr()
        assert captured.out == ""
        assert captured.err.startswith("project-docs: ")

    def test_a_folder_outside_a_repository_is_a_failure_the_person_can_fix(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        monkeypatch.setenv("PROJECT_DOCS_CALLER_CWD", str(tmp_path))
        assert main(["map"]) == 2
        assert "project-docs: " in capsys.readouterr().err
