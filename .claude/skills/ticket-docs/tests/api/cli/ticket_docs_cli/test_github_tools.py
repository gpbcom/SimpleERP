from __future__ import annotations

import json
from pathlib import Path

from tests.api.cli.ticket_docs_cli.helpers import call
from tests.builders.fake_gh import FakeGh
from tests.builders.git_sandbox import GitSandbox
from tests.builders.ticket_builder import TicketBuilder


class TestGithubTools:
    def test_history_bundle_prints_the_bundle(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        sandbox.commit("src/a.py")
        code, out, _ = call(["history-bundle", "GH-1"], sandbox.root)
        assert code == 0
        assert Path(out.strip()).is_file()
        assert Path(out.strip()).parent.name == "history"

    def test_history_bundle_without_commits_fails(self, tmp_path: Path) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        code, out, err = call(["history-bundle", "GH-1"], sandbox.root)
        assert (code, out) == (1, "")
        assert "ticket-docs:" in err

    def test_archive_prints_the_asset_link(self, tmp_path: Path, gh: FakeGh) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        TicketBuilder(sandbox.root / "docs" / "tickets").minimal()
        gh.answer(["release", "view"], stdout=json.dumps({"tagName": "evidence-GH-7", "assets": []}))
        code, out, _ = call(["archive", "GH-7"], sandbox.root)
        assert code == 0
        assert out.startswith("https://github.com/gpbcom/simple-erp/releases/download/evidence-GH-7/GH-7-")

    def test_archive_dry_run_prints_the_commands(self, tmp_path: Path, gh: FakeGh) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        TicketBuilder(sandbox.root / "docs" / "tickets").minimal()
        code, out, _ = call(["archive", "GH-7", "--dry-run"], sandbox.root)
        assert code == 0
        assert gh.calls() == []
        lines = out.splitlines()
        assert lines[0].startswith("gh release view evidence-GH-7")
        assert any(line.startswith("gh release upload evidence-GH-7") for line in lines)

    def test_archive_without_a_folder_fails(self, tmp_path: Path, gh: FakeGh) -> None:
        sandbox = GitSandbox(tmp_path / "repo")
        code, _, err = call(["archive", "GH-7"], sandbox.root)
        assert code == 1
        assert "nothing to archive" in err

    def test_board_moves_the_issue(self, tmp_path: Path, gh: FakeGh) -> None:
        issue = {"id": "I_7", "projectItems": {"nodes": [{"id": "PVTI_7", "project": {"id": "PVT_kwHOBZDE-c4Bq9-t"}}]}}
        gh.answer(["api", "graphql"], stdout=json.dumps({"data": {"repository": {"issue": issue}}}))
        assert call(["board", "GH-7", "In progress"], tmp_path) == (0, "GH-7 is In progress on the board.\n", "")

    def test_board_names_the_valid_statuses(self, tmp_path: Path, gh: FakeGh) -> None:
        code, _, err = call(["board", "GH-7", "Doing"], tmp_path)
        assert code == 2
        assert "Backlog, Ready, In progress, In review, QA, Done" in err
        assert gh.calls() == []

    def test_a_gh_failure_is_reported(self, tmp_path: Path, gh: FakeGh) -> None:
        gh.answer(["api", "graphql"], exit_code=1, stderr="HTTP 401: Bad credentials")
        code, _, err = call(["board", "GH-7", "Done"], tmp_path)
        assert code == 1
        assert "Bad credentials" in err
