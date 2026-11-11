from __future__ import annotations

# Standard library imports
import subprocess
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, List, Optional

# First-party imports
from harness_core.git.exceptions import SEGitCommandFailedError
from harness_core.models.git.change_status import ChangeStatus
from harness_core.models.git.file_change import FileChange


class GitRepository:
    """Read access to a git working tree, and its history saved in bundles.

    Attributes:
        PORCELAIN_UNTRACKED (str): The two-letter code of an untracked file in ``git status --porcelain``.
        root (Path): The repository's top-level folder.
        logger (Logger): Logger instance.

    Notes:
        - **Nothing here changes the working tree, the index or the branches**: no checkout, commit or reset. The
          harness's checks read, and only Claude or the person at the keyboard changes the tree.
        - The two writes are a bundle file outside the object store (``create_bundle``) and the refs of a private
          namespace the caller names (``fetch_bundle``), so that commits saved before a squash stay readable.
        - Each call runs ``git -C <root>``, so the caller's current folder does not matter.
    """

    PORCELAIN_UNTRACKED: ClassVar[str] = "??"

    def __init__(self, root: Path, logger: Optional[Logger] = None) -> None:
        """Set the repository folder.

        Args:
            root (Path): The repository's top-level folder.
            logger (Optional[Logger]): Logger instance.
        """
        self.root = root.resolve()
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _raw(self, *args: str) -> str:
        """Run one git command in the repository and keep its output as it is.

        Args:
            *args (str): The git arguments.

        Returns:
            str: The command's standard output, unstripped.

        Raises:
            SEGitCommandFailedError: When git exits with an error.
        """
        self.logger.debug("Running git %s in %s.", " ".join(args), self.root)
        result = subprocess.run(["git", "-C", str(self.root), *args], capture_output=True, text=True, check=False)
        if result.returncode:
            self.logger.error("git %s failed with exit code %d.", args[0], result.returncode)
            raise SEGitCommandFailedError(
                f"git {' '.join(args)} failed with exit code {result.returncode}. "  # noqa: E501
                f"It said: {result.stderr.strip()[-300:]}"
            )
        return result.stdout

    def _git(self, *args: str) -> str:
        """Run one git command in the repository.

        Args:
            *args (str): The git arguments.

        Returns:
            str: The command's standard output, stripped.

        Raises:
            SEGitCommandFailedError: When git exits with an error.
        """
        return self._raw(*args).strip()

    def _lines(self, *args: str) -> List[str]:
        """Run one git command and split its output into non-empty lines.

        Args:
            *args (str): The git arguments.

        Returns:
            List[str]: The output lines.
        """
        return [line for line in self._git(*args).splitlines() if line.strip()]

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def discover(cls, start: Path, logger: Optional[Logger] = None) -> GitRepository:
        """Find the repository that holds a folder.

        Args:
            start (Path): Any folder inside the working tree.
            logger (Optional[Logger]): Logger instance.

        Returns:
            GitRepository: The repository at the working tree's top level.

        Raises:
            SEGitCommandFailedError: When the folder is not inside a git working tree.
        """
        return cls(Path(cls(start, logger)._git("rev-parse", "--show-toplevel")), logger)

    def current_branch(self) -> str:
        """Give the branch checked out, or an empty string on a detached head."""
        return self._git("branch", "--show-current")

    def head(self) -> str:
        """Give the full hash of the commit checked out."""
        return self._git("rev-parse", "HEAD")

    def staged_changes(self) -> List[FileChange]:
        """List the files staged for the next commit.

        Returns:
            List[FileChange]: Each staged file with its status. A rename or a copy is listed as the file it adds, and a
            rename also as the file it deletes.

        Notes:
            Renames are not detected, so that a file moved into a test folder counts as a new test file (TEST-7).
        """
        changes = []
        for line in self._lines("diff", "--cached", "--no-renames", "--name-status"):
            fields = line.split("\t")
            changes.append(FileChange(path=fields[-1], status=fields[0]))
        self.logger.debug("Found %d staged files.", len(changes))
        return changes

    def changed_files(self, base: str) -> List[str]:
        """List the files the branch changed since it left a base.

        Args:
            base (str): The base branch or commit, such as ``origin/develop``.

        Returns:
            List[str]: The paths, sorted, compared with the merge base (``base...HEAD``).
        """
        return sorted(self._lines("diff", "--name-only", f"{base}...HEAD"))

    def uncommitted_files(self) -> List[str]:
        """List the files changed in the working tree and not committed yet.

        Returns:
            List[str]: The staged, unstaged and untracked paths, sorted and unique. A rename is listed under its new
            path.

        Notes:
            The paths of ``working_tree_changes``, so that the porcelain output is read in one place only (CS-1).
        """
        paths = sorted({change.path for change in self.working_tree_changes()})
        self.logger.debug("Found %d uncommitted files.", len(paths))
        return paths

    def tags(self, pattern: str) -> List[str]:
        """List the tags whose name matches a pattern.

        Args:
            pattern (str): A ``git tag --list`` pattern, such as ``v*``.

        Returns:
            List[str]: The tag names, in git's order.
        """
        return self._lines("tag", "--list", pattern)

    def commits_between(self, base: str, head: str) -> List[str]:
        """List the commits reachable from ``head`` and not from ``base``.

        Args:
            base (str): The base branch or commit.
            head (str): The tip.

        Returns:
            List[str]: The full hashes, oldest first.
        """
        return self._lines("rev-list", "--reverse", f"{base}..{head}")

    def files_in_commit(self, commit: str) -> List[str]:
        """List the files a commit changed.

        Args:
            commit (str): The commit.

        Returns:
            List[str]: The paths, sorted.
        """
        return sorted(self._lines("show", "--format=", "--name-only", commit))

    def is_ancestor(self, ancestor: str, descendant: str) -> bool:
        """Tell whether a commit is an ancestor of another one, or the same.

        Args:
            ancestor (str): The older commit.
            descendant (str): The newer commit.

        Returns:
            bool: ``True`` when ``ancestor`` is in the history of ``descendant``.
        """
        result = subprocess.run(
            ["git", "-C", str(self.root), "merge-base", "--is-ancestor", ancestor, descendant],
            capture_output=True,
            check=False,
        )
        return result.returncode == 0

    def commit_exists(self, commit: str) -> bool:
        """Tell whether a commit is in the repository's object store.

        Args:
            commit (str): The commit hash.

        Returns:
            bool: ``True`` when the commit can be read.
        """
        result = subprocess.run(
            ["git", "-C", str(self.root), "cat-file", "-e", f"{commit}^{{commit}}"], capture_output=True, check=False
        )
        return result.returncode == 0

    def has_uncommitted_changes(self) -> bool:
        """Tell whether a tracked file differs from the commit checked out.

        Returns:
            bool: ``True`` when a tracked file is changed, staged or not. Untracked files do not count.
        """
        return bool(self._git("status", "--porcelain", "--untracked-files=no"))

    def working_tree_changes(self) -> List[FileChange]:
        """List every file that differs from the commit checked out, staged or not, untracked files included.

        Returns:
            List[FileChange]: Each file with its status. A rename is listed under its new path.

        Notes:
            - The status is the index's letter when the file is staged, else the working tree's.
            - git's unmerged states have no ``ChangeStatus``: they are listed as modified.
        """
        letters = {status.value for status in ChangeStatus}
        entries = self._raw("status", "--porcelain", "-z", "--untracked-files=all").split("\0")
        changes: List[FileChange] = []
        index = 0
        while index < len(entries):
            entry = entries[index]
            index += 1
            if len(entry) < 4:
                continue
            code, path = entry[:2], entry[3:]
            letter = ChangeStatus.UNTRACKED.value if code == self.PORCELAIN_UNTRACKED else code.strip()[:1]
            if letter in {ChangeStatus.RENAMED.value, ChangeStatus.COPIED.value}:
                index += 1
            changes.append(FileChange(path=path, status=letter if letter in letters else ChangeStatus.MODIFIED.value))
        self.logger.debug("Found %d changed files in the working tree.", len(changes))
        return changes

    def commit_subjects(self, base: str, head: str) -> List[str]:
        """List the commits reachable from ``head`` and not from ``base``, with their subject.

        Args:
            base (str): The base branch or commit.
            head (str): The tip.

        Returns:
            List[str]: One ``<full hash> <subject>`` line per commit, oldest first.
        """
        return self._lines("log", "--reverse", "--format=%H %s", f"{base}..{head}")

    def create_bundle(self, path: Path, base: str, head: str) -> None:
        """Save the commits reachable from ``head`` and not from ``base`` in a bundle file.

        Args:
            path (Path): The bundle file to write. Its folder is created when missing.
            base (str): The base branch or commit.
            head (str): The tip.

        Raises:
            SEGitCommandFailedError: When git cannot write it, such as for an empty range.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        self._git("bundle", "create", str(path), f"{base}..{head}")
        self.logger.info("Saved %s..%s in %s.", base, head, path)

    def fetch_bundle(self, bundle: Path, namespace: str) -> None:
        """Fetch every head of a bundle into a private namespace of refs, so that its commits can be read.

        Args:
            bundle (Path): The bundle file.
            namespace (str): The refs prefix, such as ``refs/ticket-history/GH-12``.

        Raises:
            SEGitCommandFailedError: When the bundle cannot be read or its base commits are missing.
        """
        heads = [line.split(" ", 1)[1] for line in self._lines("bundle", "list-heads", str(bundle)) if " " in line]
        refspecs = [f"+{ref}:{namespace}/{bundle.stem}/{ref}" for ref in heads]
        self._git("fetch", "-q", str(bundle), *refspecs)
        self.logger.info("Fetched %d heads of %s into %s.", len(refspecs), bundle.name, namespace)

    def index_tree(self) -> str:
        """Give the hash of the tree the next commit would record.

        Returns:
            str: The tree hash of the index.

        Notes:
            ``git write-tree`` stores the tree object, which a commit would store anyway; no ref moves.
        """
        return self._git("write-tree")

    def merge_base(self, first: str, second: str) -> str:
        """Give the newest commit two histories share.

        Args:
            first (str): A branch or commit.
            second (str): Another branch or commit.

        Returns:
            str: The full hash of their best common ancestor.

        Raises:
            SEGitCommandFailedError: When the two histories share no commit.
        """
        return self._git("merge-base", first, second)

    def last_commit(self, path: str, refs: List[str]) -> Optional[str]:
        """Give the newest commit, on some refs, that adds or changes a path.

        Args:
            path (str): The file or folder, relative to the repository root.
            refs (List[str]): The refs to search, such as ``origin/develop``, or ``--remotes`` for every
                remote-tracking branch.

        Returns:
            Optional[str]: The full hash, ``None`` when no commit of those refs adds or changes the path.

        Notes:
            - A commit that only deletes the path is skipped, so the path exists at the commit returned.
            - The history is read in topological order, so a child comes before its parent even when both were
              made in the same second.
        """
        found = self._git("log", "-1", "--topo-order", "--format=%H", "--diff-filter=ACMRT", *refs, "--", path)
        self.logger.debug("The last commit of %s on %s is %s.", path, " ".join(refs), found or "none")
        return found or None

    def path_exists(self, commit: str, path: str) -> bool:
        """Tell whether a file or folder exists at a commit.

        Args:
            commit (str): The commit hash.
            path (str): The file or folder, relative to the repository root.

        Returns:
            bool: ``True`` when the commit holds the path. ``False`` too when the commit is unknown.
        """
        result = subprocess.run(
            ["git", "-C", str(self.root), "cat-file", "-e", f"{commit}:{path}"], capture_output=True, check=False
        )
        return result.returncode == 0

    def main_root(self) -> Path:
        """Give the top-level folder of the main checkout, the same as ``root`` unless this is a linked worktree.

        Returns:
            Path: The main checkout's folder.
        """
        return Path(self._git("rev-parse", "--path-format=absolute", "--git-common-dir")).parent.resolve()
