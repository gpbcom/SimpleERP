from __future__ import annotations

# Standard library imports
import shlex
from datetime import datetime
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, List, Optional

# First-party imports
from harness_core.git.git_repository import GitRepository
from harness_core.lifecycle.runnable import Runnable
from ticket_docs.models.evidence.actions_run import ActionsRun
from ticket_docs.models.evidence.evidence_run import EvidenceRun
from ticket_docs.models.evidence.run_counts import RunCounts
from ticket_docs.models.evidence.run_request import RunRequest
from ticket_docs.service.runs.command_shape import CommandShape
from ticket_docs.service.runs.readme_renderer import ReadmeRenderer
from ticket_docs.storage.evidence.evidence_repository import EvidenceRepository
from ticket_docs.storage.evidence.report_reader import ReportReader
from ticket_docs.storage.github.exceptions import SEGhCommandFailedError
from ticket_docs.storage.github.gh_client import GhClient
from ticket_docs.storage.processes.command_runner import CommandRunner


class RunRecorder(Runnable):
    """Runs a test command, or reads an Actions run, and keeps it in a new evidence folder.

    Attributes:
        CONSOLE (str): The raw output file.
        README (str): The folder's description.
        ACTIONS_LOG (str): The Actions run's log file.
        ARTIFACTS (str): The folder of the Actions run's artifacts.
        PLAYWRIGHT_REPORT (str): Playwright's HTML report folder, in the command's folder and in the evidence.
        PLAYWRIGHT_RESULTS (str): Playwright's JSON results, in the command's folder.
        RESULTS (str): Playwright's JSON results, in the evidence.
        FAILED_EXIT_CODE (int): The exit code of a failed Actions run.
        request (RunRequest): What to record.
        repository (GitRepository): The caller's repository, for the commit.
        cwd (Path): The folder the command runs in.
        evidence (EvidenceRepository): The evidence folders.
        runner (CommandRunner): Runs the command.
        reports (ReportReader): Reads the reports' counts.
        gh (GhClient): Reads the Actions run.
        shape (CommandShape): Tells pytest and Playwright apart, and adds pytest's report options.
        renderer (ReadmeRenderer): Writes the README and the verdict.
        logger (Logger): Logger instance.
        folder (Optional[Path]): The evidence folder, once created.
        verdict (str): The Result line.
        exit_code (int): The command's exit code, 0 or 1 for an Actions run.
        actions_run (Optional[ActionsRun]): The Actions run, once read.
        started (datetime): When the run started, to the minute.

    Notes:
        - **The folder is created before the command runs**, so that pytest writes its reports straight into it.
        - An Actions run is dated by its start, in local time. A command by the moment it starts.
        - A failed artifact download or log read is kept in ``console.txt``: the run is still recorded.
    """

    CONSOLE: ClassVar[str] = "console.txt"
    README: ClassVar[str] = "README.md"
    ACTIONS_LOG: ClassVar[str] = "actions.log"
    ARTIFACTS: ClassVar[str] = "artifacts"
    PLAYWRIGHT_REPORT: ClassVar[str] = "playwright-report"
    PLAYWRIGHT_RESULTS: ClassVar[str] = "test-results/results.json"
    RESULTS: ClassVar[str] = "results.json"
    FAILED_EXIT_CODE: ClassVar[int] = 1

    def __init__(
        self,
        request: RunRequest,
        repository: GitRepository,
        cwd: Path,
        evidence: EvidenceRepository,
        runner: CommandRunner,
        reports: ReportReader,
        gh: GhClient,
        shape: CommandShape,
        renderer: ReadmeRenderer,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set what to record and the tools it needs.

        Args:
            request (RunRequest): What to record.
            repository (GitRepository): The caller's repository, for the commit.
            cwd (Path): The folder the command runs in.
            evidence (EvidenceRepository): The evidence folders.
            runner (CommandRunner): Runs the command.
            reports (ReportReader): Reads the reports' counts.
            gh (GhClient): Reads the Actions run.
            shape (CommandShape): Tells pytest and Playwright apart.
            renderer (ReadmeRenderer): Writes the README and the verdict.
            logger (Optional[Logger]): Logger instance.
        """
        self.request = request
        self.repository = repository
        self.cwd = cwd.resolve()
        self.evidence = evidence
        self.runner = runner
        self.reports = reports
        self.gh = gh
        self.shape = shape
        self.renderer = renderer
        self.logger = logger if logger else getLogger(__name__)
        self.folder: Optional[Path] = None
        self.verdict = ""
        self.exit_code = 0
        self.actions_run: Optional[ActionsRun] = None
        self.started = datetime.now().replace(second=0, microsecond=0)

    ############################
    # Internal Helpers Methods #
    ############################

    def _relative_cwd(self) -> str:
        """Give the command's folder relative to the repository.

        Returns:
            str: The relative folder, ``.`` at the top level.
        """
        try:
            relative = self.cwd.relative_to(self.repository.root)
        except ValueError:
            return str(self.cwd)
        return str(relative) if relative.parts else "."

    def _artefacts(self, folder: Path) -> List[str]:
        """List what the folder holds, empty folders left out.

        Args:
            folder (Path): The evidence folder.

        Returns:
            List[str]: The names, folders ending with a slash.
        """
        return [
            name for name in self.evidence.files(folder) if not name.endswith("/") or any((folder / name).iterdir())
        ]

    def _record_command(self, folder: Path) -> EvidenceRun:
        """Run the command and describe the run.

        Args:
            folder (Path): The evidence folder.

        Returns:
            EvidenceRun: The run, for the README.
        """
        command = self.shape.with_reports(self.request.command, folder)
        outcome = self.runner.run(command, self.cwd)
        self.evidence.write(folder, self.CONSOLE, outcome.output)
        counts: Optional[RunCounts] = None
        if self.shape.is_pytest(self.request.command):
            counts = self.reports.junit(folder / "report.xml") or RunCounts()
        elif self.shape.is_playwright(self.request.command):
            self.evidence.copy_in(self.cwd / self.PLAYWRIGHT_REPORT, folder, self.PLAYWRIGHT_REPORT)
            self.evidence.copy_in(self.cwd / self.PLAYWRIGHT_RESULTS, folder, self.RESULTS)
            counts = self.reports.playwright(folder / self.RESULTS)
        self.exit_code = outcome.exit_code
        self.verdict = self.renderer.result(counts, outcome.exit_code, self.request.expectation)
        return EvidenceRun(
            folder=folder.name,
            what=self.request.what,
            command=self.shape.display(command, folder, self._relative_cwd()),
            commit=self.repository.head(),
            branch=self.repository.current_branch() or "HEAD",
            dirty=self.repository.has_uncommitted_changes(),
            kind=self.request.kind,
            where=self.request.where,
            date=self.started,
            result=self.verdict,
        )

    def _record_actions(self, folder: Path, run: ActionsRun, run_id: str) -> EvidenceRun:
        """Download an Actions run's artifacts and log, and describe the run.

        Args:
            folder (Path): The evidence folder.
            run (ActionsRun): The run.
            run_id (str): Its id.

        Returns:
            EvidenceRun: The run, for the README.
        """
        console = [run.model_dump_json(by_alias=True, indent=2)]
        try:
            console.append(self.gh.run_download(run_id, folder / self.ARTIFACTS))
        except SEGhCommandFailedError as error:
            self.logger.warning("The artifacts of run %s could not be downloaded.", run_id)
            console.append(str(error))
        try:
            self.evidence.write(folder, self.ACTIONS_LOG, self.gh.run_log(run_id))
        except SEGhCommandFailedError as error:
            self.logger.warning("The log of run %s could not be read.", run_id)
            console.append(str(error))
        self.evidence.write(folder, self.CONSOLE, "\n".join(part for part in console if part) + "\n")
        self.exit_code = 0 if run.succeeded else self.FAILED_EXIT_CODE
        self.verdict = self.renderer.actions_result(run, self.request.expectation)
        repository = ["--repo", self.gh.repository]
        commands = [
            shlex.join(["gh", "run", "view", run_id, *repository, "--json", self.gh.RUN_FIELDS]),
            shlex.join(["gh", "run", "download", run_id, *repository, "--dir", f"{folder}/{self.ARTIFACTS}"]),
            f"{shlex.join(['gh', 'run', 'view', run_id, *repository, '--log'])} > {folder}/{self.ACTIONS_LOG}",
        ]
        return EvidenceRun(
            folder=folder.name,
            what=self.request.what,
            command=" && ".join(commands).replace(str(folder), self.shape.FOLDER_MARK),
            commit=run.head_sha,
            branch=run.head_branch,
            kind=self.request.kind,
            where=self.request.where,
            date=self.started,
            result=self.verdict,
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    def initialize(self) -> None:
        """Read the Actions run when there is one, and create the evidence folder."""
        if self.request.run_id is not None:
            self.actions_run = self.gh.run_view(self.request.run_id)
            self.started = self.actions_run.created_at.astimezone().replace(tzinfo=None, second=0, microsecond=0)
        name = f"{self.request.where.value}-{self.started:%Y-%m-%d}-{self.request.check}"
        self.folder = self.evidence.create(self.request.ticket, name)
        self.logger.debug("Recording %s into %s.", self.request.check, self.folder.name)

    def run(self) -> None:
        """Run the command or read the Actions run, then write the README."""
        if self.folder is None:
            return
        if self.actions_run is not None and self.request.run_id is not None:
            run = self._record_actions(self.folder, self.actions_run, self.request.run_id)
        else:
            run = self._record_command(self.folder)
        readme = self.renderer.readme(self.request.ticket, run, self._artefacts(self.folder))
        self.evidence.write(self.folder, self.README, readme)
        self.logger.info("Recorded %s: %s.", self.folder.name, self.verdict)

    def close(self) -> None:
        """Release nothing: the folder stays, whatever happened."""
        self.logger.debug("The recorder is closed.")
