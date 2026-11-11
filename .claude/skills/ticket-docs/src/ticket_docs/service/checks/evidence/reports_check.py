from __future__ import annotations

# Standard library imports
import re
from logging import Logger
from operator import attrgetter
from typing import ClassVar, FrozenSet, List, Optional, Tuple

# First-party imports
from ticket_docs.models.enums import RunKind, RunPlace
from ticket_docs.models.evidence.evidence_run import EvidenceRun
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.checks.ticket_check import TicketCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder
from ticket_docs.service.index.report_index import ReportIndex
from ticket_docs.storage.evidence.evidence_repository import EvidenceRepository
from ticket_docs.storage.github.gh_client import GhClient
from ticket_docs.storage.tickets.ticket_repository import TicketRepository


class ReportsCheck(TicketCheck):
    """Checks that every report is kept (TEST-9): per run, its size, the index, and the archive once handed over.

    Attributes:
        MAX_BYTES (int): The largest evidence file allowed.
        MEGABYTE (int): Bytes in a megabyte, for the messages.
        INDEX_LABEL (str): How the index is named in a problem line.
        BRUNO_PREFIX (str): The start of a Bruno report's name.
        UNIT_REPORTS (Tuple[str, ...]): The files a unit run keeps.
        CONSOLE (str): The only file a run that pytest stopped before its tests can keep.
        STOPPED_EXIT_CODES (FrozenSet[int]): pytest's exit codes when it ran no test: interrupted, usage error, no
            test collected.
        EXIT_PATTERN (re.Pattern[str]): Reads the exit code from a run's result line.
        index (ReportIndex): Writes what the index should hold.
        tickets (TicketRepository): Reads the index as it is.
        evidence (EvidenceRepository): The evidence folders.
        gh (GhClient): Reads the evidence pre-release.
        catalog (GithubCatalog): Names the pre-release.
        offline (bool): Whether to leave GitHub out.
        logger (Logger): Logger instance.

    Notes:
        - A run marked ⚠️ invalid is kept but not asked for reports: its environment failed before it wrote them.
        - A unit run that pytest stopped before its tests (exit 2, 4 or 5, such as a red run whose conftest imports
          a module the step has not written yet) wrote no JUnit report: its console is its evidence.
        - The archive must hold an asset uploaded after the newest evidence folder's run, so that the archive on
          GitHub has every run.
    """

    MAX_BYTES: ClassVar[int] = 5 * 1024 * 1024
    MEGABYTE: ClassVar[int] = 1024 * 1024
    INDEX_LABEL: ClassVar[str] = "docs/tickets/README.md"
    BRUNO_PREFIX: ClassVar[str] = "bruno"
    UNIT_REPORTS: ClassVar[Tuple[str, ...]] = ("report.xml", "console.txt")
    CONSOLE: ClassVar[str] = "console.txt"
    STOPPED_EXIT_CODES: ClassVar[FrozenSet[int]] = frozenset({2, 4, 5})
    EXIT_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"\(exit (\d+);")

    def __init__(
        self,
        index: ReportIndex,
        tickets: TicketRepository,
        evidence: EvidenceRepository,
        gh: GhClient,
        catalog: GithubCatalog,
        offline: bool,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set where the reports, the index and the archive are read.

        Args:
            index (ReportIndex): Writes what the index should hold.
            tickets (TicketRepository): Reads the index as it is.
            evidence (EvidenceRepository): The evidence folders.
            gh (GhClient): Reads the evidence pre-release.
            catalog (GithubCatalog): Names the pre-release.
            offline (bool): Whether to leave GitHub out.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.index = index
        self.tickets = tickets
        self.evidence = evidence
        self.gh = gh
        self.catalog = catalog
        self.offline = offline

    ############################
    # Internal Helpers Methods #
    ############################

    def _stopped_before_tests(self, run: EvidenceRun) -> bool:
        """Tell whether pytest stopped the run before running any test.

        Args:
            run (EvidenceRun): The run.

        Returns:
            bool: ``True`` when its result line shows exit code 2, 4 or 5.
        """
        match = self.EXIT_PATTERN.search(run.result or "")
        stopped = match is not None and int(match.group(1)) in self.STOPPED_EXIT_CODES
        if stopped:
            self.logger.debug("Run %s stopped before its tests: only its console is asked for.", run.folder)
        return stopped

    def _run_problems(self, folder: TicketFolder, run: EvidenceRun) -> List[str]:
        """List the reports a run lacks for its kind and place.

        Args:
            folder (TicketFolder): The ticket folder.
            run (EvidenceRun): The run.

        Returns:
            List[str]: Its problems.
        """
        label = folder.label(f"tests-evidences/{run.folder}")
        files = set(self.evidence.files(folder.run_folder(run.folder)))
        problems: List[str] = []
        match run.kind:
            case RunKind.UNIT:
                expected = (self.CONSOLE,) if self._stopped_before_tests(run) else self.UNIT_REPORTS
                missing = [name for name in expected if name not in files]
                problems += [f"{label}: unit run without {name} (TEST-9)" for name in missing]
            case RunKind.GUI | RunKind.E2E:
                bruno = any(name.startswith(self.BRUNO_PREFIX) for name in files)
                if not ({"playwright-report/", "artifacts/"} & files or bruno):
                    problems.append(
                        f"{label}: {run.kind.value} run without a Playwright report, a Bruno report or artifacts/ "
                        "(TEST-9)"
                    )
            case _:
                pass
        if run.where is not None and run.where is not RunPlace.LOCAL and not {"actions.log", "artifacts/"} & files:
            problems.append(f"{label}: {run.where.value} run without actions.log or artifacts/ (TEST-9)")
        return problems

    def _archive_problems(self, folder: TicketFolder, runs: List[EvidenceRun]) -> List[str]:
        """Check that the evidence pre-release has an asset newer than the newest run.

        Args:
            folder (TicketFolder): The ticket folder.
            runs (List[EvidenceRun]): Its runs.

        Returns:
            List[str]: The problem, if any.
        """
        tag = self.catalog.release_tag(folder.key)
        uploads = self.gh.release_asset_times(tag)
        if uploads is None:
            return [f"{tag}: no pre-release, run ticket-docs archive {folder.key} (TEST-9)"]
        dated = [run for run in runs if run.date is not None]
        if not dated:
            return []
        newest = max(dated, key=attrgetter("date"))
        local = [upload.astimezone().replace(tzinfo=None) for upload in uploads]
        if newest.date is not None and not any(upload > newest.date for upload in local):
            return [
                f"{tag}: no asset newer than the evidence folder {newest.folder}, "
                f"run ticket-docs archive {folder.key} (TEST-9)"
            ]
        return []

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, folder: TicketFolder) -> List[str]:
        """List the missing reports, the files over 5 MB, a stale index and a stale archive.

        Args:
            folder (TicketFolder): The ticket folder.

        Returns:
            List[str]: One line per problem.
        """
        runs = folder.runs()
        problems: List[str] = []
        for run in runs:
            if not run.invalid:
                problems += self._run_problems(folder, run)
        for path in self.evidence.large_files(folder.key, self.MAX_BYTES):
            size = path.stat().st_size / self.MEGABYTE
            relative = path.relative_to(folder.path)
            problems.append(f"{folder.label(str(relative))}: {size:.1f} MB, over the 5 MB limit (TEST-9)")
        if self.tickets.index() != self.index.text():
            problems.append(f"{self.INDEX_LABEL}: out of date, run ticket-docs report-index (TEST-9)")
        if not self.offline and folder.handed_over():
            problems += self._archive_problems(folder, runs)
        self.logger.debug("%s has %d report problems.", folder.key, len(problems))
        return problems
