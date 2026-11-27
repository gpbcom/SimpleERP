from __future__ import annotations

# Standard library imports
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REPORTS = ROOT / ".claude" / "scripts" / "reports"
GIT_ENV = {
    "GIT_AUTHOR_NAME": "T",
    "GIT_AUTHOR_EMAIL": "t@example.com",
    "GIT_COMMITTER_NAME": "T",
    "GIT_COMMITTER_EMAIL": "t@example.com",
}


def git(cwd: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, env={**os.environ, **GIT_ENV})


def develop_ref(repo: Path) -> str:
    code = (
        f"import sys; sys.path.insert(0, {str(REPORTS)!r}); import roadmap_gantt; "
        f"print(roadmap_gantt.develop_ref({str(repo)!r}))"
    )
    return subprocess.run(
        [sys.executable, "-c", code], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.strip()


class TestDevelopRef:
    def test_the_local_develop_comes_first(self, tmp_path: Path) -> None:
        git(tmp_path, "init", "-b", "develop")
        git(tmp_path, "commit", "--allow-empty", "-m", "one")
        assert develop_ref(tmp_path) == "develop"

    def test_a_checkout_without_develop_uses_origin_develop(self, tmp_path: Path) -> None:
        origin = tmp_path / "origin"
        origin.mkdir()
        git(origin, "init", "-b", "develop")
        git(origin, "commit", "--allow-empty", "-m", "one")
        git(tmp_path, "clone", "--quiet", str(origin), "clone")
        clone = tmp_path / "clone"
        git(clone, "checkout", "--quiet", "--detach")
        git(clone, "branch", "-D", "develop")
        assert develop_ref(clone) == "origin/develop"

    def test_a_ci_checkout_of_a_pull_request_uses_its_own_commit(self, tmp_path: Path) -> None:
        git(tmp_path, "init", "-b", "pull-request")
        git(tmp_path, "commit", "--allow-empty", "-m", "one")
        assert develop_ref(tmp_path) == "HEAD"
