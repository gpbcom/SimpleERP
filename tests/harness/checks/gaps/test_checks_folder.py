"""The clean trees of the checks are made on disk beside the repository, never in ``/tmp`` (TKT-27).

``/tmp`` is a tmpfs with a quota per user: on 2026-11-28 the clean trees and their pytest files filled it, and the
checks of two tickets stopped.
"""

from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import Dict

# First-party imports
from tests.harness.checks.helpers import call
from tests.harness.checks.test_checks import TICKET, git
from tests.harness.checks.test_checks_cleanup import a_left_tree, a_repo, gone_pid


def made_tree(repo: Path, temp: Path, where: Path) -> Dict[str, object]:
    """Make the clean tree of ``where`` with no folder given, as ``main`` does, and say where it and pytest's went."""
    setup = (
        f"repo, where, temp = Path({str(repo)!r}), Path({str(where)!r}), Path({str(temp)!r})\n"
        f"tree = checks.isolated_tree(checks.changed_files('develop', {TICKET!r}, where), where)\n"
        "made = {'tree': str(tree.parent), 'pytest': str(checks.pytest_temp(tree).parent), "
        "'in_temp': sorted(p.name for p in temp.iterdir())}\n"
        "checks.remove_tree(tree, where)"
    )
    made = call("made", setup, env={"TMPDIR": str(temp)})
    assert isinstance(made, dict)
    return made


class TestChecksFolder:
    def test_the_clean_tree_is_made_on_disk_beside_the_repository_never_in_the_temporary_folder(
        self, tmp_path: Path
    ) -> None:
        repo = a_repo(tmp_path)
        temp = tmp_path / "tmp"
        temp.mkdir()
        made = made_tree(repo, temp, repo)
        assert made["tree"] == str(tmp_path / ".repo-erp-checks")
        assert made["pytest"] == str(tmp_path / ".repo-erp-checks")
        assert made["in_temp"] == []

    def test_a_linked_worktree_makes_its_clean_tree_beside_the_main_checkout(self, tmp_path: Path) -> None:
        repo = a_repo(tmp_path)
        temp = tmp_path / "tmp"
        temp.mkdir()
        linked = tmp_path / "elsewhere" / "linked"
        git(repo, "worktree", "add", "--detach", str(linked), "HEAD")
        made = made_tree(repo, temp, linked)
        assert made["tree"] == str(tmp_path / ".repo-erp-checks")
        assert not (tmp_path / "elsewhere" / ".linked-erp-checks").exists()

    def test_the_sweep_removes_a_tree_left_in_the_folder_on_disk(self, tmp_path: Path) -> None:
        repo = a_repo(tmp_path)
        temp = tmp_path / "tmp"
        temp.mkdir()
        folder = tmp_path / ".repo-erp-checks"
        folder.mkdir()
        tree = a_left_tree(repo, folder, f"erp-checks-{gone_pid()}-abc")
        removed = call(f"[p.name for p in checks.sweep_stale_trees(Path({str(repo)!r}))]", env={"TMPDIR": str(temp)})
        assert removed == [tree.name]
        assert not tree.exists()

    def test_a_folder_given_is_still_the_one_used(self, tmp_path: Path) -> None:
        repo = a_repo(tmp_path)
        given = tmp_path / "given"
        given.mkdir()
        parent = call(
            "parent",
            f"repo = Path({str(repo)!r}); tree = checks.isolated_tree([], repo, Path({str(given)!r}))\n"
            "parent = str(tree.parent); checks.remove_tree(tree, repo)",
        )
        assert parent == str(given)
        assert not (tmp_path / ".repo-erp-checks").exists()
