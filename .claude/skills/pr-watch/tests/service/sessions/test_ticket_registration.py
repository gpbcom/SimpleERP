from __future__ import annotations

import json
from pathlib import Path

import pytest

from pr_watch.models.configuration.commands_config import CommandsConfig
from pr_watch.models.enums import OperationKind
from pr_watch.models.watch.session_ref import SessionRef
from pr_watch.service.exceptions import SENoPullRequestLinkError, SEPullRequestLinkInvalidError
from pr_watch.service.sessions.ticket_registration import TicketRegistration
from pr_watch.storage.desktop.command_runner import CommandRunner
from pr_watch.storage.files.text_files import TextFiles
from pr_watch.storage.sessions.session_directory import SessionDirectory
from pr_watch.storage.state.watch_store import WatchStore
from tests.stand_ins.git_sandbox import GitSandbox
from tests.stand_ins.helpers import NOW, PR_URL, SESSION_ID


class TestTicketRegistration:
    @pytest.fixture
    def clone(self, tmp_path: Path) -> Path:
        clone = GitSandbox(tmp_path).build(conflict=False)
        folder = clone / "docs" / "tickets" / "GH-12"
        folder.mkdir(parents=True)
        (folder / "PROGRESS.md").write_text(f"# GH-12\n\n## Pull request\n\n- {PR_URL}\n", encoding="utf-8")
        (clone / "docs" / "tickets" / "GH-13").mkdir()
        return clone

    @pytest.fixture
    def store(self, tmp_path: Path) -> WatchStore:
        return WatchStore(tmp_path / "state", TextFiles())

    def registration(
        self, store: WatchStore, commands: CommandsConfig, tmp_path: Path, cwd: Path
    ) -> TicketRegistration:
        return TicketRegistration(store, SessionDirectory(tmp_path / "claude", commands.claude, CommandRunner()), cwd)

    def test_the_link_comes_from_progress_in_the_main_working_tree(
        self, store: WatchStore, commands: CommandsConfig, tmp_path: Path, clone: Path, calls_log: Path
    ) -> None:
        GitSandbox(tmp_path).git(clone, "worktree", "add", "-q", str(tmp_path / "tree"), "HEAD")
        registration = self.registration(store, commands, tmp_path, tmp_path / "tree")
        session = registration.session_for(SESSION_ID)
        watches = registration.register("GH-12", [], session, NOW)
        assert [watch.id for watch in watches] == ["GH-12:gpbcom/simple-erp#7"]
        assert watches[0].pull_request.root == str(clone.resolve())
        assert session.cwd == str(tmp_path / "tree")
        assert [operation.kind for operation in store.operations()] == [OperationKind.REGISTERED]

    def test_registering_again_changes_the_owner_and_keeps_the_history(
        self, store: WatchStore, commands: CommandsConfig, tmp_path: Path, clone: Path
    ) -> None:
        registration = self.registration(store, commands, tmp_path, clone)
        first = registration.register("GH-12", [], None, NOW)[0]
        second = registration.register("GH-12", [PR_URL], SessionRef(session_id="other-session"), NOW.replace(hour=11))[
            0
        ]
        assert second.history == first.history
        assert store.registry().pull_requests[first.id].session == SessionRef(session_id="other-session")

    def test_a_ticket_without_link_is_refused(
        self, store: WatchStore, commands: CommandsConfig, tmp_path: Path, clone: Path
    ) -> None:
        with pytest.raises(SENoPullRequestLinkError):
            self.registration(store, commands, tmp_path, clone).register("GH-13", [], None, NOW)

    def test_a_link_off_github_is_refused(
        self, store: WatchStore, commands: CommandsConfig, tmp_path: Path, clone: Path
    ) -> None:
        with pytest.raises(SEPullRequestLinkInvalidError):
            self.registration(store, commands, tmp_path, clone).register(
                "GH-12", ["https://bitbucket.org/x/y/pull-requests/1"], None, NOW
            )

    def test_proposals_list_the_unwatched_pull_requests_with_their_candidate_sessions(
        self, store: WatchStore, commands: CommandsConfig, tmp_path: Path, clone: Path
    ) -> None:
        project = tmp_path / "claude" / "projects" / "-repo"
        project.mkdir(parents=True)
        lines = [{"cwd": "/repo", "message": PR_URL}, {"type": "ai-title", "aiTitle": "GH-12 customers"}]
        (project / "sess-1.jsonl").write_text("\n".join(json.dumps(line) for line in lines), encoding="utf-8")
        registration = self.registration(store, commands, tmp_path, clone)
        proposals = registration.proposals()
        assert [(key, link, [item.session_id for item in found]) for key, link, found in proposals] == [
            ("GH-12", PR_URL, ["sess-1"])
        ]
        registration.register("GH-12", [], None, NOW)
        assert registration.proposals() == []
