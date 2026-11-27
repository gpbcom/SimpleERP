"""The clean tree of the checks never downloads the Git LFS files: no check reads an image (TKT-6)."""

from __future__ import annotations

# Standard library imports
from pathlib import Path

# First-party imports
from tests.harness.checks.test_checks import TICKET, clean_tree, git, two_tickets_at_work

POINTER = "version https://git-lfs.github.com/spec/v1\noid sha256:0\nsize 1\n"


def repository_with_an_lfs_image(tmp_path: Path) -> Path:
    """Return two tickets at work in a repository whose PNG files go through an LFS filter that always fails."""
    repo = two_tickets_at_work(tmp_path, ["backend/services/mine/", f"docs/tickets/{TICKET}/"])
    # A machine with git-lfs installed (CI) would turn the pointer into a new one on ``git add``: store it as it is.
    git(repo, "config", "filter.lfs.clean", "cat")
    git(repo, "config", "filter.lfs.process", "")
    (repo / ".gitattributes").write_text("*.png filter=lfs diff=lfs merge=lfs -text\n", encoding="utf-8")
    (repo / "docs" / "image.png").parent.mkdir(parents=True, exist_ok=True)
    (repo / "docs" / "image.png").write_text(POINTER, encoding="utf-8")
    git(repo, "add", ".gitattributes", "docs/image.png")
    git(repo, "commit", "-m", "an image stored in LFS")
    git(repo, "config", "filter.lfs.smudge", "false")
    git(repo, "config", "filter.lfs.process", "false")
    git(repo, "config", "filter.lfs.required", "true")
    return repo


class TestChecksLfs:
    def test_the_clean_tree_is_made_without_running_the_lfs_filter(self, tmp_path: Path) -> None:
        tree = clean_tree(repository_with_an_lfs_image(tmp_path))
        assert tree["gone"] is True
        assert "docs/image.png" in tree["files"]  # type: ignore[operator]

    def test_an_lfs_file_stays_a_pointer_in_the_clean_tree(self, tmp_path: Path) -> None:
        tree = clean_tree(repository_with_an_lfs_image(tmp_path))
        assert tree["texts"]["docs/image.png"] == POINTER  # type: ignore[index]
