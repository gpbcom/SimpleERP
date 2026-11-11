from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import ClassVar, FrozenSet, List, Optional

# First-party imports
from harness_core.git.git_repository import GitRepository
from ticket_docs.models.hooks.git_call import GitCall


class RefGuard:
    """Refuses, on a ticket branch, the git commands that write commits or move refs without a ``git commit``.

    Attributes:
        COMMIT_TREE (str): git's command that writes a commit object.
        UPDATE_REF (str): git's command that moves any ref.
        REPLACE (str): git's command that makes one object stand for another.
        HASH_OBJECT (str): git's command that writes any object with ``-w``.
        BRANCH (str): git's branch command.
        RESET (str): git's reset command.
        GUARDED (FrozenSet[str]): The commands this guard decides on.
        HELP (FrozenSet[str]): The options that only print help.
        REPLACE_LIST (FrozenSet[str]): The options that make ``git replace`` list.
        REPLACE_WRITES (FrozenSet[str]): The options of ``git replace`` that write.
        HASH_WRITE (str): The short option of ``git hash-object`` that writes the object.
        BRANCH_FORCE_LONG (str): The long option of ``git branch`` that moves an existing branch.
        BRANCH_FORCE_SHORT (str): The short options of ``git branch`` that move or overwrite an existing branch.
        END_OF_OPTIONS (str): The word after which every word is a path.
        EXPANSIONS (str): The characters of a shell expansion the hook sees unexpanded.
        HEAD (str): What git calls the commit checked out.
        logger (Logger): Logger instance.

    Notes:
        - ``commit-tree``, ``update-ref``, ``replace`` and ``hash-object -w`` write commits, objects or refs that never
          go through ``git-gate``, so they are refused but for their help and reading forms.
        - ``git branch -f``, ``-C`` or ``-M`` naming the current branch, and ``git reset`` onto a commit that is not an
          ancestor of ``HEAD``, move the branch onto history the gate never saw.
        - A reset whose commit is a shell expansion (``$(...)``, backquotes) cannot be read: it is refused, and the
          commit must be given as it is.
        - **This is a guard against mistakes, not a security boundary**: ``ticket-docs check``, CI and the review
          enforce TEST-7.
    """

    COMMIT_TREE: ClassVar[str] = "commit-tree"
    UPDATE_REF: ClassVar[str] = "update-ref"
    REPLACE: ClassVar[str] = "replace"
    HASH_OBJECT: ClassVar[str] = "hash-object"
    BRANCH: ClassVar[str] = "branch"
    RESET: ClassVar[str] = "reset"
    GUARDED: ClassVar[FrozenSet[str]] = frozenset({COMMIT_TREE, UPDATE_REF, REPLACE, HASH_OBJECT, BRANCH, RESET})
    HELP: ClassVar[FrozenSet[str]] = frozenset({"-h", "--help"})
    REPLACE_LIST: ClassVar[FrozenSet[str]] = frozenset({"-l", "--list"})
    REPLACE_WRITES: ClassVar[FrozenSet[str]] = frozenset(
        {"-d", "--delete", "-f", "--force", "-e", "--edit", "-g", "--graft", "--convert-graft-file"}
    )
    HASH_WRITE: ClassVar[str] = "w"
    BRANCH_FORCE_LONG: ClassVar[str] = "--force"
    BRANCH_FORCE_SHORT: ClassVar[str] = "fCM"
    END_OF_OPTIONS: ClassVar[str] = "--"
    EXPANSIONS: ClassVar[str] = "$`"
    HEAD: ClassVar[str] = "HEAD"

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _writes(self, call: GitCall) -> bool:
        """Tell whether a plumbing command writes a commit, an object or a ref.

        Args:
            call (GitCall): A ``commit-tree``, ``update-ref``, ``replace`` or ``hash-object`` call.

        Returns:
            bool: ``True`` unless it only prints help, lists or hashes.
        """
        words = call.arguments
        if any(word in self.HELP for word in words):
            return False
        match call.subcommand:
            case self.REPLACE:
                lists = not words or any(word in self.REPLACE_LIST for word in words)
                return not lists or any(word.split("=", 1)[0] in self.REPLACE_WRITES for word in words)
            case self.HASH_OBJECT:
                short = [word for word in words if word.startswith("-") and not word.startswith("--")]
                return any(self.HASH_WRITE in word for word in short)
            case _:
                return True

    def _moves_current_branch(self, call: GitCall, repository: GitRepository) -> bool:
        """Tell whether a ``git branch`` forces the current branch onto another commit.

        Args:
            call (GitCall): The branch call.
            repository (GitRepository): Its repository.

        Returns:
            bool: ``True`` when a force option is given and the current branch is named.
        """
        words = call.arguments
        force = any(
            word == self.BRANCH_FORCE_LONG
            or (word.startswith("-") and not word.startswith("--") and any(c in self.BRANCH_FORCE_SHORT for c in word))
            for word in words
        )
        return force and repository.current_branch() in words

    def _reset_refusal(self, call: GitCall, repository: GitRepository) -> Optional[str]:
        """Decide on a ``git reset``.

        Args:
            call (GitCall): The reset call.
            repository (GitRepository): Its repository.

        Returns:
            Optional[str]: Why it must not run, ``None`` when it moves the branch within its own history or not at all.
        """
        positional: List[str] = []
        for word in call.arguments:
            if word == self.END_OF_OPTIONS:
                break
            if not word.startswith("-"):
                positional.append(word)
        if not positional:
            return None
        target = positional[0]
        if any(character in target for character in self.EXPANSIONS):
            return (
                f"TEST-7: `git reset {target}` names its commit through a shell expansion the gate cannot read. "  # noqa: E501
                "Run the inner command first, then reset to the commit it printed."
            )
        if not repository.commit_exists(target) or repository.is_ancestor(target, self.HEAD):
            return None
        return (
            f"TEST-7: `git reset {target}` moves the branch onto a commit outside its history, which never went "
            "through git-gate. "  # noqa: E501
            "Reset only to an ancestor of HEAD, such as the merge base of a GIT-4 squash."
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    def refusal(self, call: GitCall, repository: GitRepository) -> Optional[str]:
        """Decide on one git command run on a ticket branch.

        Args:
            call (GitCall): The command.
            repository (GitRepository): Its repository.

        Returns:
            Optional[str]: Why it must not run, ``None`` when it may.
        """
        reason: Optional[str] = None
        match call.subcommand:
            case self.BRANCH:
                if self._moves_current_branch(call, repository):
                    reason = (
                        "TEST-7: forcing the current branch onto another commit moves it onto history git-gate never "
                        "saw. "  # noqa: E501
                        "Commit on the branch, or reset it to an ancestor of HEAD."
                    )
            case self.RESET:
                reason = self._reset_refusal(call, repository)
            case _:
                if call.subcommand in self.GUARDED and self._writes(call):
                    reason = (
                        f"TEST-7: `git {call.subcommand}` writes commits, objects or refs without going through "
                        "git-gate. "  # noqa: E501
                        "Commit with `git commit`, tests first."
                    )
        if reason is not None:
            self.logger.warning("Refused a git %s.", call.subcommand)
        else:
            self.logger.debug("git %s keeps the branch's history.", call.subcommand)
        return reason
