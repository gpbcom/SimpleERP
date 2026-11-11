from __future__ import annotations

# Standard library imports
import json
import shlex
import subprocess
from datetime import datetime
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, Dict, List, Optional, Union

# Third-party imports
from pydantic import JsonValue

# First-party imports
from ticket_docs.models.evidence.actions_run import ActionsRun
from ticket_docs.storage.github.exceptions import SEGhAnswerUnreadableError, SEGhCommandFailedError


class GhClient:
    """Talks to GitHub through the ``gh`` command line, logged in as the person at the keyboard.

    Attributes:
        RUN_FIELDS (str): The fields of an Actions run that are read.
        RELEASE_FIELDS (str): The fields of a release that are read.
        repository (str): The repository, ``owner/name``.
        dry_run (bool): Whether to list the commands instead of running them.
        executable (str): The gh program.
        logger (Logger): Logger instance.
        planned (List[str]): The commands a dry run would have run, in order.

    Notes:
        - Every call names the repository, so the folder ``gh`` runs from does not matter.
        - **A dry run asks nothing**, not even a read: the release is then taken as missing and no asset has a link.
        - The token stays with ``gh``: it is never read, passed or logged here.
    """

    RUN_FIELDS: ClassVar[str] = "conclusion,headSha,headBranch,url,displayTitle,createdAt"
    RELEASE_FIELDS: ClassVar[str] = "tagName,assets"

    def __init__(
        self, repository: str, dry_run: bool = False, executable: str = "gh", logger: Optional[Logger] = None
    ) -> None:
        """Set the repository and how gh is called.

        Args:
            repository (str): The repository, ``owner/name``.
            dry_run (bool): Whether to list the commands instead of running them.
            executable (str): The gh program.
            logger (Optional[Logger]): Logger instance.
        """
        self.repository = repository
        self.dry_run = dry_run
        self.executable = executable
        self.logger = logger if logger else getLogger(__name__)
        self.planned: List[str] = []

    ############################
    # Internal Helpers Methods #
    ############################

    def _gh(self, *args: str) -> str:
        """Run one gh command.

        Args:
            *args (str): The gh arguments.

        Returns:
            str: Its standard output, empty in a dry run.

        Raises:
            SEGhCommandFailedError: When gh exits with an error or cannot start.
        """
        if self.dry_run:
            self.planned.append(shlex.join([self.executable, *args]))
            self.logger.debug("Dry run: gh %s %s not run.", args[0], args[1] if len(args) > 1 else "")
            return ""
        self.logger.debug("Running gh %s %s.", args[0], args[1] if len(args) > 1 else "")
        try:
            done = subprocess.run([self.executable, *args], capture_output=True, text=True, check=False)
        except OSError as error:
            self.logger.error("gh cannot start: %s.", type(error).__name__)
            raise SEGhCommandFailedError(
                f"gh cannot start: {error}. "  # noqa: E501
                "Install the GitHub command line and log in with gh auth login."
            ) from error
        if done.returncode:
            self.logger.error("gh %s failed with exit code %d.", args[0], done.returncode)
            raise SEGhCommandFailedError(
                f"gh {' '.join(args[:2])} failed with exit code {done.returncode}. "  # noqa: E501
                f"It said: {done.stderr.strip()[-300:]}"
            )
        return done.stdout

    def _json(self, *args: str) -> JsonValue:
        """Run one gh command that answers in JSON.

        Args:
            *args (str): The gh arguments.

        Returns:
            JsonValue: The parsed answer, ``None`` in a dry run.

        Raises:
            SEGhAnswerUnreadableError: When the answer is not JSON.
        """
        text = self._gh(*args)
        if self.dry_run:
            return None
        try:
            answer: JsonValue = json.loads(text)
        except ValueError as error:
            self.logger.error("gh %s answered with something that is not JSON.", args[0])
            raise SEGhAnswerUnreadableError(f"gh {' '.join(args[:2])} did not answer with JSON.") from error
        return answer

    def _release(self, tag: str) -> Optional[Dict[str, JsonValue]]:
        """Read a release.

        Args:
            tag (str): The release's tag.

        Returns:
            Optional[Dict[str, JsonValue]]: Its tag and assets, ``None`` when it does not exist or in a dry run.
        """
        try:
            answer = self._json("release", "view", tag, "--repo", self.repository, "--json", self.RELEASE_FIELDS)
        except SEGhCommandFailedError:
            self.logger.info("The release %s does not exist.", tag)
            return None
        return answer if isinstance(answer, dict) else None

    def _assets(self, tag: str) -> Optional[List[Dict[str, JsonValue]]]:
        """Read a release's assets.

        Args:
            tag (str): The release's tag.

        Returns:
            Optional[List[Dict[str, JsonValue]]]: Its assets, ``None`` when the release does not exist.
        """
        release = self._release(tag)
        if release is None:
            return None
        assets = release.get("assets")
        return [asset for asset in assets if isinstance(asset, dict)] if isinstance(assets, list) else []

    ############################
    # Publicly Exposed Methods #
    ############################

    def run_view(self, run_id: str) -> ActionsRun:
        """Read an Actions run.

        Args:
            run_id (str): The run's id.

        Returns:
            ActionsRun: Its conclusion, commit, branch, link, title and start.
        """
        answer = self._json("run", "view", run_id, "--repo", self.repository, "--json", self.RUN_FIELDS)
        return ActionsRun.model_validate(answer)

    def run_download(self, run_id: str, directory: Path) -> str:
        """Download every artifact of an Actions run.

        Args:
            run_id (str): The run's id.
            directory (Path): Where the artifacts go, one folder each.

        Returns:
            str: What gh said.
        """
        said = self._gh("run", "download", run_id, "--repo", self.repository, "--dir", str(directory))
        self.logger.info("Downloaded the artifacts of run %s.", run_id)
        return said

    def run_log(self, run_id: str) -> str:
        """Read the full log of an Actions run.

        Args:
            run_id (str): The run's id.

        Returns:
            str: The log of every job and step.
        """
        return self._gh("run", "view", run_id, "--repo", self.repository, "--log")

    def release_exists(self, tag: str) -> bool:
        """Tell whether a release exists.

        Args:
            tag (str): The release's tag.

        Returns:
            bool: ``True`` when it exists. Always ``False`` in a dry run.
        """
        return self._release(tag) is not None

    def release_asset_times(self, tag: str) -> Optional[List[datetime]]:
        """Read when each asset of a release was uploaded.

        Args:
            tag (str): The release's tag.

        Returns:
            Optional[List[datetime]]: The upload moments, ``None`` when the release does not exist.
        """
        assets = self._assets(tag)
        if assets is None:
            return None
        moments = [asset.get("createdAt") for asset in assets]
        return [datetime.fromisoformat(moment.replace("Z", "+00:00")) for moment in moments if isinstance(moment, str)]

    def release_asset_url(self, tag: str, name: str) -> Optional[str]:
        """Give the download link of one asset of a release.

        Args:
            tag (str): The release's tag.
            name (str): The asset's file name.

        Returns:
            Optional[str]: The link, ``None`` when there is no such asset.
        """
        for asset in self._assets(tag) or []:
            url = asset.get("url")
            if asset.get("name") == name and isinstance(url, str):
                return url
        return None

    def release_create(self, tag: str, target: str, title: str, notes: str) -> None:
        """Create a pre-release.

        Args:
            tag (str): Its tag.
            target (str): The commit the tag points at.
            title (str): Its title.
            notes (str): Its description.
        """
        self._gh(
            "release", "create", tag, "--repo", self.repository, "--prerelease",
            "--target", target, "--title", title, "--notes", notes,
        )  # fmt: skip
        self.logger.info("Created the pre-release %s.", tag)

    def release_upload(self, tag: str, path: Path) -> None:
        """Upload a file to a release, never replacing an asset of the same name.

        Args:
            tag (str): The release's tag.
            path (Path): The file.
        """
        self._gh("release", "upload", tag, str(path), "--repo", self.repository)
        self.logger.info("Uploaded %s to %s.", path.name, tag)

    def issue_comment(self, number: int, body: str) -> None:
        """Comment on an issue.

        Args:
            number (int): The issue's number.
            body (str): The comment.
        """
        self._gh("issue", "comment", str(number), "--repo", self.repository, "--body", body)
        self.logger.info("Commented on issue %d.", number)

    def graphql(self, query: str, variables: Dict[str, Union[str, int]]) -> JsonValue:
        """Run a GraphQL query or mutation.

        Args:
            query (str): The query.
            variables (Dict[str, Union[str, int]]): Its variables. Numbers are passed typed, the rest as text.

        Returns:
            JsonValue: The answer, ``None`` in a dry run.
        """
        arguments = ["api", "graphql", "-f", f"query={query}"]
        for name, value in variables.items():
            arguments += ["-F" if isinstance(value, int) else "-f", f"{name}={value}"]
        return self._json(*arguments)
