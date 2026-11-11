from __future__ import annotations

from pathlib import Path

import pytest

from harness_core.git.exceptions import SEGitCommandFailedError
from harness_core.git.git_repository import GitRepository
from harness_core.models.git.change_status import ChangeStatus
from tests.git.helpers import git


def commit_file(root: Path, name: str, text: str = "x\n") -> str:
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    git(root, "add", name)
    git(root, "commit", "-q", "-m", f"add {name}")
    return git(root, "rev-parse", "HEAD")


class TestGitRepository:
    def test_discover_finds_the_top_level_from_a_sub_folder(self, sandbox: Path) -> None:
        (sandbox / "deep" / "er").mkdir(parents=True)
        repository = GitRepository.discover(sandbox / "deep" / "er")
        assert repository.root == sandbox.resolve()

    def test_discover_outside_a_repository_is_refused(self, tmp_path: Path) -> None:
        with pytest.raises(SEGitCommandFailedError):
            GitRepository.discover(tmp_path)

    def test_current_branch_and_head(self, sandbox: Path) -> None:
        git(sandbox, "switch", "-q", "-c", "feature/GH-3-thing")
        repository = GitRepository(sandbox)
        assert repository.current_branch() == "feature/GH-3-thing"
        assert repository.head() == git(sandbox, "rev-parse", "HEAD")

    def test_staged_changes_carry_their_status(self, sandbox: Path) -> None:
        (sandbox / "README.md").write_text("changed\n", encoding="utf-8")
        (sandbox / "new.py").write_text("x = 1\n", encoding="utf-8")
        git(sandbox, "add", "README.md", "new.py")
        changes = {change.path: change.status for change in GitRepository(sandbox).staged_changes()}
        assert changes == {"README.md": ChangeStatus.MODIFIED, "new.py": ChangeStatus.ADDED}

    def test_a_staged_rename_is_a_deleted_file_and_an_added_one(self, sandbox: Path) -> None:
        commit_file(sandbox, "src/helpers.py", "x = 1\ny = 2\nz = 3\n")
        (sandbox / "tests").mkdir()
        git(sandbox, "mv", "src/helpers.py", "tests/test_helpers.py")
        changes = {change.path: change.status for change in GitRepository(sandbox).staged_changes()}
        assert changes == {"src/helpers.py": ChangeStatus.DELETED, "tests/test_helpers.py": ChangeStatus.ADDED}

    def test_changed_files_since_the_merge_base(self, sandbox: Path) -> None:
        git(sandbox, "switch", "-q", "-c", "feature/GH-3-thing")
        commit_file(sandbox, "src/a.py")
        commit_file(sandbox, "tests/test_a.py")
        assert GitRepository(sandbox).changed_files("develop") == ["src/a.py", "tests/test_a.py"]

    def test_commits_between_are_oldest_first_with_their_files(self, sandbox: Path) -> None:
        git(sandbox, "switch", "-q", "-c", "feature/GH-3-thing")
        first = commit_file(sandbox, "tests/test_a.py")
        second = commit_file(sandbox, "src/a.py")
        repository = GitRepository(sandbox)
        assert repository.commits_between("develop", "HEAD") == [first, second]
        assert repository.files_in_commit(second) == ["src/a.py"]

    def test_ancestry_and_existence(self, sandbox: Path) -> None:
        first = commit_file(sandbox, "a.txt")
        second = commit_file(sandbox, "b.txt")
        repository = GitRepository(sandbox)
        assert repository.is_ancestor(first, second)
        assert not repository.is_ancestor(second, first)
        assert repository.commit_exists(first)
        assert not repository.commit_exists("0" * 40)

    def test_uncommitted_files_list_staged_unstaged_untracked_and_renamed_paths(self, sandbox: Path) -> None:
        commit_file(sandbox, "docs/old name.md")
        commit_file(sandbox, "src/kept.py")
        (sandbox / "README.md").write_text("changed\n", encoding="utf-8")
        (sandbox / "notes").mkdir()
        (sandbox / "notes" / "draft.md").write_text("draft\n", encoding="utf-8")
        git(sandbox, "mv", "docs/old name.md", "docs/new name.md")
        assert GitRepository(sandbox).uncommitted_files() == ["README.md", "docs/new name.md", "notes/draft.md"]

    def test_a_clean_tree_has_no_uncommitted_file(self, sandbox: Path) -> None:
        assert GitRepository(sandbox).uncommitted_files() == []

    def test_tags_are_listed_by_pattern(self, sandbox: Path) -> None:
        git(sandbox, "config", "tag.gpgsign", "false")
        git(sandbox, "tag", "v0.1.0")
        commit_file(sandbox, "a.txt")
        git(sandbox, "tag", "-a", "v0.10.0", "-m", "simple-erp 0.10.0")
        git(sandbox, "tag", "evidence-GH-1")
        repository = GitRepository(sandbox)
        assert sorted(repository.tags("v*")) == ["v0.1.0", "v0.10.0"]
        assert repository.tags("nothing-*") == []

    def test_uncommitted_changes_ignore_untracked_files(self, sandbox: Path) -> None:
        repository = GitRepository(sandbox)
        (sandbox / "new.txt").write_text("x\n", encoding="utf-8")
        assert not repository.has_uncommitted_changes()
        (sandbox / "README.md").write_text("changed\n", encoding="utf-8")
        assert repository.has_uncommitted_changes()

    def test_working_tree_changes_list_staged_unstaged_and_untracked_files(self, sandbox: Path) -> None:
        commit_file(sandbox, "src/old name.py")
        (sandbox / "README.md").write_text("changed\n", encoding="utf-8")
        (sandbox / "tests").mkdir()
        (sandbox / "tests" / "test_new.py").write_text("x = 1\n", encoding="utf-8")
        (sandbox / "staged.py").write_text("x = 1\n", encoding="utf-8")
        git(sandbox, "add", "staged.py")
        git(sandbox, "mv", "src/old name.py", "src/new name.py")
        changes = {change.path: change.status for change in GitRepository(sandbox).working_tree_changes()}
        assert changes == {
            "README.md": ChangeStatus.MODIFIED,
            "tests/test_new.py": ChangeStatus.UNTRACKED,
            "staged.py": ChangeStatus.ADDED,
            "src/new name.py": ChangeStatus.RENAMED,
        }

    def test_commit_subjects_are_oldest_first(self, sandbox: Path) -> None:
        git(sandbox, "switch", "-q", "-c", "feature/GH-3-thing")
        first = commit_file(sandbox, "a.txt")
        second = commit_file(sandbox, "b.txt")
        subjects = GitRepository(sandbox).commit_subjects("develop", "HEAD")
        assert subjects == [f"{first} add a.txt", f"{second} add b.txt"]

    def test_a_bundle_keeps_the_commits_and_can_be_fetched_back(self, sandbox: Path, tmp_path: Path) -> None:
        clone = tmp_path / "clone"
        git(tmp_path, "clone", "-q", str(sandbox), str(clone))
        git(sandbox, "switch", "-q", "-c", "feature/GH-3-thing")
        kept = commit_file(sandbox, "a.txt")
        bundle = tmp_path / "out" / "history.bundle"
        repository = GitRepository(sandbox)
        repository.create_bundle(bundle, "develop", "HEAD")
        assert bundle.is_file()
        other = GitRepository(clone)
        assert not other.commit_exists(kept)
        other.fetch_bundle(bundle, "refs/ticket-history/GH-3")
        assert other.commit_exists(kept)
        assert git(clone, "for-each-ref", "--format=%(refname)", "refs/ticket-history/GH-3") != ""

    def test_an_empty_range_cannot_be_bundled(self, sandbox: Path, tmp_path: Path) -> None:
        with pytest.raises(SEGitCommandFailedError):
            GitRepository(sandbox).create_bundle(tmp_path / "empty.bundle", "HEAD", "HEAD")

    def test_the_main_root_of_a_linked_worktree_is_the_main_checkout(self, sandbox: Path, tmp_path: Path) -> None:
        linked = tmp_path / "linked"
        git(sandbox, "worktree", "add", "-q", "-b", "other", str(linked))
        assert GitRepository(linked).main_root() == sandbox.resolve()
        assert GitRepository(sandbox).main_root() == sandbox.resolve()

    def test_the_tree_of_the_index_follows_what_is_staged(self, sandbox: Path) -> None:
        git(sandbox, "switch", "-q", "-c", "feature/GH-3-thing")
        commit_file(sandbox, "a.txt")
        repository = GitRepository(sandbox)
        assert repository.index_tree() == git(sandbox, "rev-parse", "HEAD^{tree}")
        (sandbox / "b.txt").write_text("b\n", encoding="utf-8")
        git(sandbox, "add", "b.txt")
        assert repository.index_tree() != git(sandbox, "rev-parse", "HEAD^{tree}")

    def test_the_merge_base_is_where_two_branches_parted(self, sandbox: Path) -> None:
        parted = commit_file(sandbox, "a.txt")
        git(sandbox, "switch", "-q", "-c", "feature/GH-3-thing")
        tip = commit_file(sandbox, "b.txt")
        git(sandbox, "switch", "-q", "develop")
        commit_file(sandbox, "c.txt")
        repository = GitRepository(sandbox)
        assert repository.merge_base("develop", tip) == parted
        assert repository.merge_base(tip, "develop") == parted

    def test_two_unrelated_histories_have_no_merge_base(self, sandbox: Path) -> None:
        git(sandbox, "switch", "-q", "--orphan", "alone")
        alone = commit_file(sandbox, "a.txt")
        with pytest.raises(SEGitCommandFailedError):
            GitRepository(sandbox).merge_base("develop", alone)
