"""Every branch of the person's work is pushed with its pull request labelled automerge, nobody asked (TKT-28)."""

from __future__ import annotations

# Standard library imports
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

# Third-party imports
import pytest

# First-party imports
from tests.harness.ticket_tree.helpers import OPEN_PULL_REQUEST, environment, fake_gh, gh_calls, git, repo_root

SCRIPT = repo_root() / ".claude" / "scripts" / "github" / "publish.py"


def a_branch_with_work(tmp_path: Path, branch: str) -> Path:
    """Return a clone of a bare remote, on ``branch``, with one commit that the remote does not have."""
    remote = tmp_path / "remote.git"
    git(tmp_path, "init", "--bare", "-b", "develop", str(remote))
    clone = tmp_path / "clone"
    clone.mkdir()
    git(clone, "init", "-b", "develop")
    git(clone, "remote", "add", "origin", str(remote))
    (clone / "a.txt").write_text("a\n", encoding="utf-8")
    git(clone, "add", "-A")
    git(clone, "commit", "-m", "initial")
    git(clone, "push", "-q", "origin", "develop")
    if branch != "develop":
        git(clone, "checkout", "-q", "-b", branch)
    (clone / "b.txt").write_text("b\n", encoding="utf-8")
    git(clone, "add", "-A")
    git(clone, "commit", "-m", "the work")
    return clone


def publish(clone: Path, env: Dict[str, str]) -> subprocess.CompletedProcess[str]:
    body = clone.parent / "body.md"
    body.write_text("What and why.\n", encoding="utf-8")
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--title", "Harness: a fix", "--body-file", str(body)],
        cwd=clone,
        capture_output=True,
        text=True,
        env=env,
        check=False,
        timeout=60,
    )


def remote_branches(clone: Path) -> List[str]:
    listed = git(clone, "ls-remote", "--heads", "origin")
    return [line.split("refs/heads/")[1] for line in listed.splitlines()]


def created(calls: List[List[str]]) -> List[List[str]]:
    return [call for call in calls if call[:2] == ["pr", "create"]]


class TestPublish:
    @pytest.mark.parametrize(
        ("branch", "base"),
        [("feature/harness-cleanup", "develop"), ("bugfix/npm-glob", "develop"), ("hotfix/1.0.1-fix", "master")],
    )
    def test_a_branch_is_pushed_and_its_pull_request_opened_with_automerge(
        self, tmp_path: Path, branch: str, base: str
    ) -> None:
        clone = a_branch_with_work(tmp_path, branch)
        env = fake_gh(tmp_path / "bin", open_pull_request=False, api_fails=False)
        result = publish(clone, env)
        assert result.returncode == 0, result.stderr
        assert json.loads(result.stdout)["base"] == base
        assert branch in remote_branches(clone)
        [call] = created(gh_calls(tmp_path / "bin"))
        assert call[call.index("--base") + 1] == base
        assert call[call.index("--head") + 1] == branch
        assert call[call.index("--label") + 1] == "automerge"

    def test_an_open_pull_request_of_the_branch_gets_the_label_and_no_second_one_is_opened(
        self, tmp_path: Path
    ) -> None:
        clone = a_branch_with_work(tmp_path, "feature/harness-cleanup")
        env = fake_gh(tmp_path / "bin", open_pull_request=True, api_fails=False)
        result = publish(clone, env)
        assert result.returncode == 0, result.stderr
        assert json.loads(result.stdout)["pull_request"] == OPEN_PULL_REQUEST
        calls = gh_calls(tmp_path / "bin")
        assert created(calls) == []
        assert any(call[:1] == ["api"] and "labels[]=automerge" in call for call in calls)

    @pytest.mark.parametrize("branch", ["develop", "feature/tickets", "work-in-progress"])
    def test_a_protected_shared_or_non_gitflow_branch_is_refused_before_anything_is_pushed(
        self, tmp_path: Path, branch: str
    ) -> None:
        clone = a_branch_with_work(tmp_path, branch)
        before = remote_branches(clone)
        env = fake_gh(tmp_path / "bin", open_pull_request=False, api_fails=False)
        result = publish(clone, env)
        assert result.returncode == 1
        assert "Not published" in result.stderr
        assert remote_branches(clone) == before
        assert gh_calls(tmp_path / "bin") == []

    def test_it_says_how_to_use_it_without_a_title_or_a_body(self, tmp_path: Path) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT)], capture_output=True, text=True, env=environment(), check=False
        )
        assert result.returncode == 2
        assert "Usage" in result.stderr
