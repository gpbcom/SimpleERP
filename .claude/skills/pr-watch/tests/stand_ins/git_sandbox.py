from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Dict

from tests.stand_ins.helpers import HEAD_REF


class GitSandbox:
    """A real origin and its clone: ``develop``, and a ticket branch that conflicts with it or not."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.environment: Dict[str, str] = {
            "GIT_AUTHOR_NAME": "Sandbox",
            "GIT_AUTHOR_EMAIL": "sandbox@example.com",
            "GIT_COMMITTER_NAME": "Sandbox",
            "GIT_COMMITTER_EMAIL": "sandbox@example.com",
            "GIT_CONFIG_GLOBAL": "/dev/null",
            "GIT_CONFIG_NOSYSTEM": "1",
            "HOME": str(root),
            "PATH": "/usr/bin:/bin",
        }

    def git(self, folder: Path, *args: str) -> str:
        return subprocess.run(
            ["git", "-C", str(folder), *args], check=True, capture_output=True, text=True, env=self.environment
        ).stdout.strip()

    def build(self, conflict: bool) -> Path:
        work = self.root / "work"
        work.mkdir()
        self.git(work, "init", "-q", "-b", "develop")
        (work / "a.txt").write_text("one\n", encoding="utf-8")
        self.git(work, "add", ".")
        self.git(work, "commit", "-q", "-m", "base")
        self.git(work, "checkout", "-q", "-b", HEAD_REF)
        (work / "a.txt").write_text("branch\n", encoding="utf-8")
        self.git(work, "commit", "-q", "-am", "branch")
        self.git(work, "checkout", "-q", "develop")
        (work / ("a.txt" if conflict else "b.txt")).write_text("develop\n", encoding="utf-8")
        self.git(work, "add", ".")
        self.git(work, "commit", "-q", "-m", "develop moved")
        origin = self.root / "origin.git"
        self.git(self.root, "clone", "-q", "--bare", str(work), str(origin))
        clone = self.root / "clone"
        self.git(self.root, "clone", "-q", str(origin), str(clone))
        return clone
