from __future__ import annotations

# Standard library imports
import re
from logging import Logger
from pathlib import Path
from typing import ClassVar, List, Optional, Pattern, Tuple

# First-party imports
from harness_core.git.exceptions import SEGitCommandFailedError
from harness_core.git.git_repository import GitRepository
from ticket_docs.models.evidence.evidence_run import EvidenceRun
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.ticket_check import TicketCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder
from ticket_docs.service.paths.code_paths import CodePaths


class TddCheck(TicketCheck):
    """Checks that each code step was tested first (TEST-7): a red run on a tests-only commit, then the code on top.

    Attributes:
        RED_PREFIX (str): The check name of a red run, before its step.
        GREEN_PREFIX (str): The check name of a green run, before its step.
        RETRY_SUFFIX (Pattern[str]): The ``-2`` a second folder of the same check gets.
        RED_ICONS (Tuple[str, ...]): The icons of a run that failed.
        UNEXPECTED_GREEN (str): The mark of a red run that passed.
        HISTORY (str): The folder of the history bundles, inside the evidence folder.
        BUNDLE_GLOB (str): A history bundle's file name.
        REFS (str): The refs namespace the bundles are fetched into, followed by the ticket.
        PROGRESS (str): The progress file.
        LOG_SECTION (str): PROGRESS.md's Log heading.
        SUB_STEPS (str): The line of a step's sub-steps.
        DONE (str): The icon of a sub-step that is done.
        RED_RUN (str): The words of the red-run sub-step.
        LINK (Pattern[str]): A Markdown link.
        SHORT_SHA (int): How many characters of a hash the messages show.
        repository (Optional[GitRepository]): The repository the commits are read in, ``None`` outside one.
        paths (CodePaths): Tells production code apart.
        tables (MarkdownTables): Reads PROGRESS.md's Log.
        logger (Logger): Logger instance.
        fetched (bool): Whether the history bundles were fetched already.

    Notes:
        - A red folder marked ⚠️ invalid is kept but not counted: it was run again.
        - **A commit that is not in the repository** (squashed away) is looked for in
          ``tests-evidences/history/*.bundle``, fetched into ``refs/ticket-history/<KEY>/``.
        - The green run of a red ``tdd-red-<step>`` is ``unit-<step>``. A retry suffix (``-2``) is ignored on both.
    """

    RED_PREFIX: ClassVar[str] = "tdd-red-"
    GREEN_PREFIX: ClassVar[str] = "unit-"
    RETRY_SUFFIX: ClassVar[Pattern[str]] = re.compile(r"-\d+$")
    RED_ICONS: ClassVar[Tuple[str, ...]] = ("❌", "🔴")
    UNEXPECTED_GREEN: ClassVar[str] = "UNEXPECTED GREEN"
    HISTORY: ClassVar[str] = "history"
    BUNDLE_GLOB: ClassVar[str] = "*.bundle"
    REFS: ClassVar[str] = "refs/ticket-history"
    PROGRESS: ClassVar[str] = "PROGRESS.md"
    LOG_SECTION: ClassVar[str] = "## Log"
    SUB_STEPS: ClassVar[str] = "**Sub-steps:**"
    DONE: ClassVar[str] = "✅"
    RED_RUN: ClassVar[str] = "red run"
    LINK: ClassVar[Pattern[str]] = re.compile(r"\]\(([^)\s]+)\)")
    SHORT_SHA: ClassVar[int] = 7

    def __init__(
        self,
        repository: Optional[GitRepository],
        paths: CodePaths,
        tables: MarkdownTables,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the repository and the readers.

        Args:
            repository (Optional[GitRepository]): The repository the commits are read in, ``None`` outside one.
            paths (CodePaths): Tells production code apart.
            tables (MarkdownTables): Reads PROGRESS.md's Log.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.repository = repository
        self.paths = paths
        self.tables = tables
        self.fetched = False

    ############################
    # Internal Helpers Methods #
    ############################

    def _step(self, check: str, prefix: str) -> str:
        """Give the step a check name is about, retry suffix left out.

        Args:
            check (str): The check name.
            prefix (str): Its prefix, red or green.

        Returns:
            str: The step.
        """
        return self.RETRY_SUFFIX.sub("", check[len(prefix) :])

    def _known(self, repository: GitRepository, folder: TicketFolder, commit: str) -> bool:
        """Tell whether a commit can be read, fetching the history bundles the first time one cannot.

        Args:
            repository (GitRepository): The repository.
            folder (TicketFolder): The ticket folder, which holds the bundles.
            commit (str): The commit.

        Returns:
            bool: ``True`` when the commit is in the repository, after the bundles were fetched if needed.
        """
        if repository.commit_exists(commit):
            return True
        if not self.fetched:
            self.fetched = True
            history = folder.evidence.evidence_dir(folder.key) / self.HISTORY
            for bundle in sorted(history.glob(self.BUNDLE_GLOB)) if history.is_dir() else []:
                try:
                    repository.fetch_bundle(bundle, f"{self.REFS}/{folder.key}")
                except SEGitCommandFailedError:
                    self.logger.warning("The history bundle %s cannot be fetched.", bundle.name)
        return repository.commit_exists(commit)

    def _red_problems(
        self, repository: GitRepository, folder: TicketFolder, red: EvidenceRun, runs: List[EvidenceRun]
    ) -> List[str]:
        """Check one red run and the green runs of its step.

        Args:
            repository (GitRepository): The repository.
            folder (TicketFolder): The ticket folder.
            red (EvidenceRun): The red run.
            runs (List[EvidenceRun]): Every run of the ticket.

        Returns:
            List[str]: Its problems.
        """
        label = folder.label(f"tests-evidences/{red.folder}")
        problems: List[str] = []
        if not red.icon.startswith(self.RED_ICONS) or self.UNEXPECTED_GREEN in (red.result or ""):
            problems.append(f"{label}: the red run did not fail (TEST-7)")
        if red.commit is None:
            return problems
        red_known = self._known(repository, folder, red.commit)
        if not red_known:
            problems.append(self._missing(label, red.commit))
        else:
            touched = self.paths.production(repository.files_in_commit(red.commit))
            if touched:
                problems.append(
                    f"{label}: the red commit {red.commit[: self.SHORT_SHA]} touches production code: "
                    f"{', '.join(touched)} (TEST-7)"
                )
        step = self._step(red.check, self.RED_PREFIX)
        for green in runs:
            if not green.check.startswith(self.GREEN_PREFIX) or green.commit is None:
                continue
            if self._step(green.check, self.GREEN_PREFIX) != step:
                continue
            green_label = folder.label(f"tests-evidences/{green.folder}")
            if not self._known(repository, folder, green.commit):
                problems.append(self._missing(green_label, green.commit))
            elif red_known and not repository.is_ancestor(red.commit, green.commit):
                problems.append(
                    f"{green_label}: its commit {green.commit[: self.SHORT_SHA]} does not descend from the red "
                    f"run's commit {red.commit[: self.SHORT_SHA]} (TEST-7)"
                )
        return problems

    def _missing(self, label: str, commit: str) -> str:
        """Name a commit that cannot be found.

        Args:
            label (str): The run folder that names it.
            commit (str): The commit.

        Returns:
            str: The problem line.
        """
        return (
            f"{label}: commit {commit[: self.SHORT_SHA]} is neither in the repository nor in "
            "tests-evidences/history (TEST-7)"
        )

    def _log_problems(self, folder: TicketFolder) -> List[str]:
        """List the Log steps that claim a red run without a link to its folder.

        Args:
            folder (TicketFolder): The ticket folder.

        Returns:
            List[str]: One line per such step.
        """
        text = self.tables.without_blocks(folder.text(self.PROGRESS) or "")
        log = self.tables.section(text, self.LOG_SECTION, nested=True) or ""
        problems: List[str] = []
        for entry in re.split(r"^### ", log, flags=re.M)[1:]:
            heading = entry.splitlines()[0].strip()
            for line in entry.splitlines():
                if self.SUB_STEPS not in line:
                    continue
                claimed = any(self.DONE in item and self.RED_RUN in item for item in line.split(" · "))
                if claimed and not self._links_red_folder(folder.path, line):
                    problems.append(
                        f"{folder.label(self.PROGRESS)}: step '{heading}' claims a red run without a link to its "
                        "tdd-red folder (TEST-7)"
                    )
        return problems

    def _links_red_folder(self, base: Path, line: str) -> bool:
        """Tell whether a line links an existing red-run folder.

        Args:
            base (Path): The ticket folder.
            line (str): The line.

        Returns:
            bool: ``True`` when one of its links leads into a ``tdd-red`` folder that exists.
        """
        for link in self.LINK.findall(line):
            target = Path(link.split("#", 1)[0])
            parts = target.parts
            red = [part for part in parts if self.RED_PREFIX in part]
            if red and (base / Path(*parts[: parts.index(red[0]) + 1])).is_dir():
                return True
        return False

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, folder: TicketFolder) -> List[str]:
        """List the red runs that do not prove the tests came first, and the Log's unproven red runs.

        Args:
            folder (TicketFolder): The ticket folder.

        Returns:
            List[str]: One line per problem.
        """
        runs = folder.runs()
        reds = [run for run in runs if run.check.startswith(self.RED_PREFIX) and not run.invalid]
        problems: List[str] = []
        if self.repository is None:
            if any(run.commit for run in runs):
                problems.append(
                    f"{folder.key}: the tickets folder is not in a git repository, so the TDD commits cannot be "
                    "checked (TEST-7)"
                )
        else:
            for red in reds:
                problems += self._red_problems(self.repository, folder, red, runs)
        problems += self._log_problems(folder)
        self.logger.debug("%s has %d TDD problems over %d red runs.", folder.key, len(problems), len(reds))
        return problems
