from __future__ import annotations

import subprocess
from pathlib import Path


class GitSandbox:
    """A throw-away git repository with a ``develop`` root commit and a remote-tracking ``origin/develop``."""

    def __init__(self, root: Path, branch: str = "feature/GH-1-thing") -> None:
        self.root = root
        root.mkdir(parents=True, exist_ok=True)
        self.git("init", "-q", "-b", "develop")
        self.git("config", "user.email", "sandbox@example.com")
        self.git("config", "user.name", "Sandbox")
        self.git("config", "commit.gpgsign", "false")
        self.commit("README.md", "sandbox\n", "root")
        self.git("update-ref", "refs/remotes/origin/develop", "HEAD")
        self.git("update-ref", "refs/remotes/origin/master", "HEAD")
        if branch != "develop":
            self.git("switch", "-q", "-c", branch)

    def git(self, *args: str) -> str:
        done = subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True, text=True)
        return done.stdout.strip()

    def write(self, path: str, text: str = "x = 1\n") -> Path:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return target

    def commit(self, path: str, text: str = "x = 1\n", message: str = "") -> str:
        self.write(path, text)
        self.git("add", path)
        self.git("commit", "-q", "-m", message or f"add {path}")
        return self.git("rev-parse", "HEAD")

    def head(self) -> str:
        return self.git("rev-parse", "HEAD")
