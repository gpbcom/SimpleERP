from __future__ import annotations

from pathlib import Path

import pytest

from tests.git.helpers import git


@pytest.fixture
def sandbox(tmp_path: Path) -> Path:
    git(tmp_path, "init", "-q", "-b", "develop")
    git(tmp_path, "config", "user.email", "sandbox@example.com")
    git(tmp_path, "config", "user.name", "Sandbox")
    git(tmp_path, "config", "commit.gpgsign", "false")
    (tmp_path / "README.md").write_text("sandbox\n", encoding="utf-8")
    git(tmp_path, "add", "README.md")
    git(tmp_path, "commit", "-q", "-m", "root")
    return tmp_path
