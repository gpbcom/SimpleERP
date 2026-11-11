from __future__ import annotations

import logging
from pathlib import Path

import pytest

from harness_core.testing.git_sandbox import GitSandbox
from release_notes.models.catalogs.changelog_type_catalog import ChangelogTypeCatalog
from tests.helpers import FEATURE_BRANCH, TEMPLATES, TYPES_FILE, changelog


@pytest.fixture
def catalog() -> ChangelogTypeCatalog:
    return ChangelogTypeCatalog.load(TYPES_FILE)


@pytest.fixture
def logger() -> logging.Logger:
    return logging.getLogger("release-notes-tests")


@pytest.fixture
def sandbox(tmp_path: Path) -> GitSandbox:
    """A repository whose ``develop`` holds the changelog templates, checked out on a feature branch."""
    sandbox = GitSandbox(tmp_path / "repo")
    sandbox.create()
    sandbox.commit(
        "changelog",
        {
            "CHANGELOG.md": changelog(),
            "changelog.d/README.md": (TEMPLATES / "changelog.d-README.md").read_text(encoding="utf-8"),
        },
    )
    sandbox.git("switch", "-q", "-c", FEATURE_BRANCH)
    return sandbox


@pytest.fixture
def caller_in_sandbox(sandbox: GitSandbox, monkeypatch: pytest.MonkeyPatch) -> GitSandbox:
    """The sandbox, as the folder the command is typed in."""
    monkeypatch.setenv("RELEASE_NOTES_CALLER_CWD", str(sandbox.root))
    return sandbox
