from __future__ import annotations

# Standard library imports
import re
from datetime import datetime
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, Dict, FrozenSet, List, Optional, Pattern, Tuple

# First-party imports
from harness_core.git.exceptions import SEGitError
from harness_core.git.git_repository import GitRepository
from harness_core.models.branches.branch_name import BranchName
from harness_core.models.branches.exceptions import SEInvalidBranchNameException
from harness_core.models.git.change_status import ChangeStatus
from ticket_docs.models.evidence.evidence_run import EvidenceRun
from ticket_docs.models.evidence.exceptions import SEInvalidEvidenceRunException
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.models.hooks.git_call import GitCall
from ticket_docs.service.hooks.git_invocations import GitInvocations
from ticket_docs.service.hooks.ref_guard import RefGuard
from ticket_docs.service.paths.code_paths import CodePaths
from ticket_docs.service.paths.tickets_root import TicketsRoot
from ticket_docs.service.permits.squash_permits import SquashPermits
from ticket_docs.storage.evidence.evidence_repository import EvidenceRepository
from ticket_docs.storage.evidence.exceptions import SEEvidenceStoreError


class GitGate:
    """Decides whether a git command Claude is about to run breaks GIT-8 or TEST-7.

    Attributes:
        PUSH (str): git's push command.
        COMMIT (str): git's commit command.
        PUSH_EVERYTHING (FrozenSet[str]): The push options that push every branch.
        PUSH_TAGS (str): The push option that pushes the tags.
        PUSH_VALUED (FrozenSet[str]): The push options followed by a value.
        COMMIT_WIDENING (FrozenSet[str]): The long commit options, without dashes, that commit more than the index.
        COMMIT_WIDENING_SHORT (str): The short commit options that commit more than the index, or other paths.
        INDEX_WRITERS (FrozenSet[str]): The git commands that change the index, and so what a commit records.
        PATH_WRITERS (FrozenSet[str]): The index writers whose effect is the paths they name.
        REMOVE (str): git's command that removes files.
        COMMIT_VALUED_SHORT (str): The short commit options followed by a value.
        VALUED_MARK (str): The end of a long option of ``commit_options`` that takes a value.
        END_OF_OPTIONS (str): The word after which every word is a path.
        TAGS (str): The refs of tags.
        HEADS (str): The refs of branches.
        HEAD (str): The current branch's name in a refspec.
        RED_PREFIX (str): The check name of a red run.
        GREEN_PREFIX (str): The check name of a green run.
        ALLOW_SQUASH (str): The ``ticket-docs`` command that grants a squash permit, which only the human runs.
        TOOL_MARKS (Tuple[str, ...]): The ways a command names ``ticket-docs``: its program and its module.
        PERMITS_MARK (str): The name of the squash permits folder.
        HOME_MARK (str): The start of a folder of ``guard_state_folders`` under the home folder.
        GRANT_PATTERN (Pattern[str]): A text that runs ``ticket-docs allow-squash``, the second check.
        invocations (GitInvocations): Finds the git commands of the command line.
        paths (CodePaths): Tells production code and tests apart.
        roots (TicketsRoot): Finds the tickets folder.
        catalog (GithubCatalog): The protected branches.
        permits (SquashPermits): Redeems the human's one-shot squash permits.
        guard (RefGuard): Refuses the commands that write commits or move refs past the gate.
        logger (Logger): Logger instance.

    Notes:
        - **GIT-8:** a push whose refspecs (or the current branch, when none is given) name ``master`` or ``develop``
          is refused, and so is ``--all`` or ``--mirror``. Tags pass. A commit on ``master`` or ``develop`` is refused.
        - **TEST-7:** on a ticket branch, a commit that holds production code is refused when it also adds test
          files, or when the ticket has no red run on this branch since its newest green run.
        - **The GIT-4 squash** adds tests and code together: it passes only with the human's permit
          (``ticket-docs allow-squash <KEY>`` in their own terminal), when the commit records exactly the branch,
          ``HEAD`` and staged tree of the permit, before it expires. The permit is used once. A Claude session can
          neither run ``allow-squash`` nor name the permits folder: the words of each command are read, best effort.
        - The files of a commit are the staged ones, plus every working-tree change and every path an index writer
          names when the commit takes more than the index (``-a``, ``-i``, ``-o``, ``-p``, ``--interactive``,
          ``--pathspec-from-file``, paths) or when the command line changes the index (``INDEX_WRITERS``): an upper
          bound, on the safe side. An index writer whose effect is not the paths it names (``git apply``, ``git
          stash``, ...) must run on its own line.
        - **A long option is read as git reads it**, abbreviations included, against ``commit_options`` of
          ``folder-rules.yaml``. An ambiguous or unknown one counts as taking more than the index.
        - On a ticket branch, ``RefGuard`` refuses the commands that write commits or move refs without a commit.
        - **This is a guard against mistakes, not a security boundary**: ``ticket-docs check``, CI and the review
          enforce TEST-7.
        - **The squash exemption reads the index as it is now**, so it is not granted when the commit takes more than
          the index, or when the command line runs another git command that changes the index (``INDEX_WRITERS``).
    """

    PUSH: ClassVar[str] = "push"
    COMMIT: ClassVar[str] = "commit"
    PUSH_EVERYTHING: ClassVar[FrozenSet[str]] = frozenset({"--all", "--mirror"})
    PUSH_TAGS: ClassVar[str] = "--tags"
    PUSH_VALUED: ClassVar[FrozenSet[str]] = frozenset({"-o", "--push-option", "--repo", "--receive-pack", "--exec"})
    COMMIT_WIDENING: ClassVar[FrozenSet[str]] = frozenset(
        {"all", "include", "only", "interactive", "patch", "pathspec-from-file"}
    )
    COMMIT_WIDENING_SHORT: ClassVar[str] = "aiop"
    INDEX_WRITERS: ClassVar[FrozenSet[str]] = frozenset(
        {
            "add",
            "apply",
            "read-tree",
            "restore",
            "rm",
            "mv",
            "checkout",
            "switch",
            "stash",
            "reset",
            "update-index",
            "merge",
            "cherry-pick",
            "revert",
        }
    )
    COMMIT_VALUED_SHORT: ClassVar[str] = "mFCct"
    PATH_WRITERS: ClassVar[FrozenSet[str]] = frozenset({"add", "rm", "mv", "restore", "update-index"})
    REMOVE: ClassVar[str] = "rm"
    VALUED_MARK: ClassVar[str] = "="
    END_OF_OPTIONS: ClassVar[str] = "--"
    TAGS: ClassVar[str] = "refs/tags/"
    HEADS: ClassVar[str] = "refs/heads/"
    HEAD: ClassVar[str] = "HEAD"
    RED_PREFIX: ClassVar[str] = "tdd-red-"
    GREEN_PREFIX: ClassVar[str] = "unit-"
    ALLOW_SQUASH: ClassVar[str] = "allow-squash"
    TOOL_MARKS: ClassVar[Tuple[str, ...]] = ("ticket-docs", "ticket_docs")
    PERMITS_MARK: ClassVar[str] = "squash-permits"
    HOME_MARK: ClassVar[str] = "~/"
    GRANT_PATTERN: ClassVar[Pattern[str]] = re.compile(r"ticket[-_]docs.*allow-squash", re.S)

    def __init__(
        self,
        invocations: GitInvocations,
        paths: CodePaths,
        roots: TicketsRoot,
        catalog: GithubCatalog,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the readers and the protected branches.

        Args:
            invocations (GitInvocations): Finds the git commands of the command line.
            paths (CodePaths): Tells production code and tests apart.
            roots (TicketsRoot): Finds the tickets folder.
            catalog (GithubCatalog): The protected branches.
            logger (Optional[Logger]): Logger instance.
        """
        self.invocations = invocations
        self.paths = paths
        self.roots = roots
        self.catalog = catalog
        self.logger = logger if logger else getLogger(__name__)
        self.permits = SquashPermits.default(paths.rules, self.logger)
        self.guard = RefGuard(self.logger)

    ############################
    # Internal Helpers Methods #
    ############################

    def _protected(self) -> FrozenSet[str]:
        """Give the branches that change only through a pull request.

        Returns:
            FrozenSet[str]: The production and integration branches.
        """
        return frozenset({self.catalog.production_branch, self.catalog.default_branch})

    def _push_refusal(self, call: GitCall, repository: GitRepository) -> Optional[str]:
        """Decide on a push.

        Args:
            call (GitCall): The push.
            repository (GitRepository): Its repository.

        Returns:
            Optional[str]: Why it must not run, ``None`` when it may.
        """
        words: List[str] = []
        index = 0
        while index < len(call.arguments):
            word = call.arguments[index]
            if word in self.PUSH_EVERYTHING:
                return f"GIT-8: `git push {word}` pushes every branch, master and develop included. Push your branch."
            if word in self.PUSH_VALUED:
                index += 1
            elif not word.startswith("-"):
                words.append(word)
            index += 1
        refspecs = words[1:]
        if not refspecs:
            if self.PUSH_TAGS in call.arguments:
                return None
            refspecs = [self.HEAD]
        current = repository.current_branch()
        for refspec in refspecs:
            target = refspec.lstrip("+").rsplit(":", 1)[-1] or refspec.lstrip("+").split(":", 1)[0]
            if target.startswith(self.TAGS):
                continue
            branch = current if target == self.HEAD else target.removeprefix(self.HEADS)
            if branch in self._protected():
                return (
                    f"GIT-8: pushing to {branch} is refused. "  # noqa: E501
                    "master and develop change only through a merged pull request: push your ticket branch."
                )
        return None

    def _ticket_branch(self, repository: GitRepository) -> Optional[BranchName]:
        """Give the current branch when code for a ticket is written on it.

        Args:
            repository (GitRepository): The repository.

        Returns:
            Optional[BranchName]: The branch, ``None`` when it carries no ticket work or misses its GitFlow shape.
        """
        try:
            branch = BranchName.parse(repository.current_branch() or self.HEAD)
        except SEInvalidBranchNameException:
            self.logger.debug("The branch does not follow GitFlow: no ticket work.")
            return None
        return branch if branch.carries_ticket_work and branch.ticket is not None else None

    def _long_option(self, name: str) -> Optional[str]:
        """Read a long commit option as git reads it, abbreviations included.

        Args:
            name (str): The option, without its dashes and value.

        Returns:
            Optional[str]: The option of ``commit_options`` it names, ``None`` when it is ambiguous or unknown.
        """
        options = self.paths.rules.commit_options
        exact = [option for option in options if option.removesuffix(self.VALUED_MARK) == name]
        if exact:
            return exact[0]
        prefixed = [option for option in options if name and option.startswith(name)]
        if len(prefixed) == 1:
            return prefixed[0]
        self.logger.debug("--%s is ambiguous or unknown: read as taking more than the index.", name)
        return None

    def _commit_paths(self, arguments: List[str]) -> Tuple[bool, List[str]]:
        """Read whether a commit takes more than the index, and the paths it names.

        Args:
            arguments (List[str]): The commit's arguments.

        Returns:
            Tuple[bool, List[str]]: Whether an option of ``COMMIT_WIDENING`` or ``COMMIT_WIDENING_SHORT`` is given,
            and the paths.

        Notes:
            - Short options may be combined (``-qpm``): the letters before the first one that takes a value count.
            - An ambiguous or unknown long option counts as taking more than the index.
        """
        every = False
        paths: List[str] = []
        index = 0
        while index < len(arguments):
            word = arguments[index]
            if word == self.END_OF_OPTIONS:
                paths += arguments[index + 1 :]
                break
            if word.startswith("--"):
                option = self._long_option(word[2:].split(self.VALUED_MARK, 1)[0])
                name = option.removesuffix(self.VALUED_MARK) if option else None
                every = every or name is None or name in self.COMMIT_WIDENING
                valued = option is not None and option.endswith(self.VALUED_MARK)
                index += 1 if valued and self.VALUED_MARK not in word else 0
            elif word.startswith("-") and len(word) > 1:
                for position, letter in enumerate(word[1:], start=1):
                    every = every or letter in self.COMMIT_WIDENING_SHORT
                    if letter in self.COMMIT_VALUED_SHORT:
                        index += 1 if position == len(word) - 1 else 0
                        break
            else:
                paths.append(word)
            index += 1
        return every, paths

    def _red_run_refusal(self, ticket: str, repository: GitRepository) -> Optional[str]:
        """Check that the ticket has a red run on this branch since its newest green run.

        Args:
            ticket (str): The ticket.
            repository (GitRepository): The repository.

        Returns:
            Optional[str]: Why the code must not be committed yet, ``None`` when a red run allows it.
        """
        evidence = EvidenceRepository(self.roots.of(repository), self.logger)
        runs: List[EvidenceRun] = []
        for folder in evidence.folders(ticket):
            try:
                runs.append(evidence.read(folder))
            except (SEEvidenceStoreError, SEInvalidEvidenceRunException):
                self.logger.debug("%s cannot be read: not counted.", folder.name)
        greens = [run.date for run in runs if run.check.startswith(self.GREEN_PREFIX) and run.date]
        newest_green = max(greens) if greens else datetime.min
        for run in runs:
            if not run.check.startswith(self.RED_PREFIX) or run.invalid or run.commit is None or run.date is None:
                continue
            if run.date >= newest_green and repository.is_ancestor(run.commit, self.HEAD):
                self.logger.debug("%s allows the commit.", run.folder)
                return None
        return (
            f"TEST-7: this commit holds production code but {ticket} has no red run on this branch since its last "
            "green run. "  # noqa: E501
            "Commit the tests alone, record the red run with `ticket-docs record-run --ticket "
            f"{ticket} --kind unit --where local --check tdd-red-<step> --expect red ...`, then commit the code."
        )

    def _permit_refusal(self, command: str) -> Optional[str]:
        """Refuse a command that grants a squash permit or names a folder of the guards' state.

        Args:
            command (str): The command line.

        Returns:
            Optional[str]: Why it must not run, ``None`` when it may.

        Notes:
            - Every simple command is read, inside ``sh -c`` strings too, git included (an alias, ``-c`` or a hook can
              run anything), whatever runs ``ticket-docs``: its path, ``uv run``, ``python -m ticket_docs``. The
              whole text is matched as well, as a second check.
            - The folders are those of ``guard_state_folders`` in ``folder-rules.yaml``, read relative to the home
              folder, and the permits folder by its name.
            - **A best effort against mistakes, not a security boundary.**
        """
        splitter = self.invocations.splitter
        text = splitter.without_data(command)
        marks = [folder.removeprefix(self.HOME_MARK) for folder in self.paths.rules.guard_state_folders]
        marks.append(self.PERMITS_MARK)
        grants = self.GRANT_PATTERN.search(text) is not None
        names = False
        for words in splitter.commands(text):
            tool = any(mark in word for word in words for mark in self.TOOL_MARKS)
            grants = grants or (tool and any(self.ALLOW_SQUASH in word for word in words))
            names = names or any(mark in word for word in words for mark in marks)
        if grants:
            return (
                "TEST-7: only the human grants a squash permit, in their own terminal. "  # noqa: E501
                "Ask them to run `ticket-docs allow-squash <KEY>` after `git reset --soft <base>`."
            )
        if names:
            return (
                "TEST-7: the squash permits and the AI test ledgers are written only by their own tools. "  # noqa: E501
                "This command names one of their folders."
            )
        return None

    def _named_paths(self, writer: GitCall, repository: GitRepository) -> Dict[str, ChangeStatus]:
        """Give the paths an index writer names, relative to the repository root.

        Args:
            writer (GitCall): The index writer.
            repository (GitRepository): The repository.

        Returns:
            Dict[str, ChangeStatus]: Each path, deleted for ``git rm`` and added otherwise: an upper bound.
        """
        status = ChangeStatus.DELETED if writer.subcommand == self.REMOVE else ChangeStatus.ADDED
        named: Dict[str, ChangeStatus] = {}
        for word in writer.arguments:
            if word.startswith("-"):
                continue
            target = (writer.directory / word).resolve()
            if target == repository.root or not target.is_relative_to(repository.root):
                continue
            named[target.relative_to(repository.root).as_posix()] = status
        return named

    def _commit_refusal(self, call: GitCall, repository: GitRepository, writers: List[GitCall]) -> Optional[str]:
        """Decide on a commit.

        Args:
            call (GitCall): The commit.
            repository (GitRepository): Its repository.
            writers (List[GitCall]): The git commands of the command line that change the index.

        Returns:
            Optional[str]: Why it must not run, ``None`` when it may.
        """
        name = repository.current_branch()
        if name in self._protected():
            return (
                f"GIT-8: committing on {name} is refused. "  # noqa: E501
                "Commit on a ticket branch (feature/GH-<n>-<slug>) and open a pull request."
            )
        branch = self._ticket_branch(repository)
        if branch is None or branch.ticket is None:
            return None
        blind = [writer.subcommand for writer in writers if writer.subcommand not in self.PATH_WRITERS]
        if blind:
            return (
                f"TEST-7: this commit shares its command line with `git {blind[0]}`, whose effect on the index the "
                "gate cannot compute. "  # noqa: E501
                f"Run `git {blind[0]}` and the commit as separate commands."
            )
        files: Dict[str, ChangeStatus] = {change.path: change.status for change in repository.staged_changes()}
        every, paths = self._commit_paths(call.arguments)
        widened = bool(writers) or every or bool(paths)
        if widened:
            for change in repository.working_tree_changes():
                files.setdefault(change.path, change.status)
            for writer in writers:
                for path, status in self._named_paths(writer, repository).items():
                    files.setdefault(path, status)
        production = self.paths.production(files)
        if not production:
            return None
        new_tests = self.paths.new_tests(files)
        if new_tests:
            refusal: Optional[str] = (
                f"TEST-7: this commit adds test files ({', '.join(new_tests[:5])}) together with production code "
                f"({', '.join(production[:5])}). "  # noqa: E501
                "Commit the tests alone first, record their red run, then commit the code. "
                f"For the GIT-4 squash, the human runs `ticket-docs allow-squash {branch.ticket}` after "
                "`git reset --soft <base>`."
            )
        else:
            refusal = self._red_run_refusal(branch.ticket, repository)
        if refusal is None:
            return None
        if widened:
            self.logger.debug("The commit may record more than the index: no squash permit counts.")
        elif self.permits.redeem(branch.ticket, repository):
            self.logger.info("The squash of %s holds the human's permit: allowed.", branch.ticket)
            return None
        return refusal

    ############################
    # Publicly Exposed Methods #
    ############################

    def refusal(self, command: str, cwd: Path) -> Optional[str]:
        """Decide on a Bash command line.

        Args:
            command (str): The command line.
            cwd (Path): The folder it runs in.

        Returns:
            Optional[str]: Why it must not run, ``None`` when it may.
        """
        permit_refusal = self._permit_refusal(command)
        if permit_refusal is not None:
            self.logger.warning("Refused a command about squash permits.")
            return permit_refusal
        calls = self.invocations.calls(command, cwd)
        writers = [call for call in calls if call.subcommand in self.INDEX_WRITERS]
        for call in calls:
            if call.subcommand not in {self.PUSH, self.COMMIT} | self.guard.GUARDED:
                continue
            try:
                repository = GitRepository.discover(call.directory, self.logger)
            except SEGitError:
                self.logger.debug("%s is not in a repository: nothing to guard.", call.directory)
                continue
            if call.subcommand == self.PUSH:
                refusal = self._push_refusal(call, repository)
            elif call.subcommand == self.COMMIT:
                refusal = self._commit_refusal(call, repository, writers)
            else:
                refusal = self.guard.refusal(call, repository) if self._ticket_branch(repository) else None
            if refusal is not None:
                self.logger.warning("Refused a git %s.", call.subcommand)
                return refusal
        self.logger.debug("Allowed %d git commands.", len(calls))
        return None
