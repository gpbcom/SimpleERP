from __future__ import annotations

import logging
from pathlib import Path

import pytest

from harness_core.testing.git_sandbox import GitSandbox
from project_docs.models.catalogs.doc_map import DocMap
from tests.helpers import DOC_MAP_FILE, FEATURE_BRANCH, documentation


@pytest.fixture
def doc_map() -> DocMap:
    return DocMap.load(DOC_MAP_FILE)


@pytest.fixture
def logger() -> logging.Logger:
    return logging.getLogger("project-docs-tests")


@pytest.fixture
def sandbox(tmp_path: Path) -> GitSandbox:
    """A repository whose ``develop`` holds a complete documentation, checked out on a feature branch."""
    sandbox = GitSandbox(tmp_path / "repo")
    sandbox.create()
    sandbox.commit("documentation", documentation())
    sandbox.git("switch", "-q", "-c", FEATURE_BRANCH)
    return sandbox


@pytest.fixture
def caller_in_sandbox(sandbox: GitSandbox, monkeypatch: pytest.MonkeyPatch) -> GitSandbox:
    """The sandbox, as the folder the command is typed in, with no ``mmdc`` on the ``PATH``."""
    monkeypatch.setenv("PROJECT_DOCS_CALLER_CWD", str(sandbox.root))
    monkeypatch.setenv("PATH", "/usr/bin:/bin")
    return sandbox
