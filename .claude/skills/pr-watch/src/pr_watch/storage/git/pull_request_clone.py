from __future__ import annotations

# Standard library imports
import re
import subprocess
from pathlib import Path
from typing import ClassVar, List, Tuple

# First-party imports
from harness_core.git.git_repository import GitRepository
from pr_watch.models.checks.rebase_probe_result import RebaseProbeResult
from pr_watch.storage.git.exceptions import SECloneNotOnGithubError


class PullRequestClone(GitRepository):
    """A local clone of a watched repository: where it is on GitHub, and whether a pull request still merges.

    Attributes:
        NAMESPACE (str): Where the probe fetches the remote branches to.
        GIT_TIMEOUT_S (int): The longest one git command of the probe may take.
        MESSAGE_LENGTH (int): The characters of git's error kept in a result.
        GITHUB_REMOTE (re.Pattern[str]): An ``origin`` link to GitHub, over HTTPS or SSH.

    Notes:
        - **The probe never moves ``refs/remotes/origin/*``.** It fetches into the watcher's own ``refs/pr-watch/*``,
          and ``--refmap=`` stops git from updating the remote-tracking refs of an explicit refspec. A
          ``git push --force-with-lease`` without an explicit hash leases on ``origin/<branch>``: a background fetch
          moving it would let that push overwrite commits someone else pushed.
        - ``git merge-tree --write-tree`` writes objects only: no index, no working file, no checkout. Exit 0 is a
          clean merge, 1 a conflict, anything else an error.
        - Every failure of the probe comes back in ``RebaseProbeResult.error``, never as an exception, so that one
          clone that cannot be read does not stop the run.
    """

    NAMESPACE: ClassVar[str] = "refs/pr-watch"
    GIT_TIMEOUT_S: ClassVar[int] = 180
    MESSAGE_LENGTH: ClassVar[int] = 300
    GITHUB_REMOTE: ClassVar[re.Pattern[str]] = re.compile(r"github\.com[:/](?P<slug>[\w.-]+/[\w.-]+?)(?:\.git)?/?$")

    ############################
    # Internal Helpers Methods #
    ############################

    def _attempt(self, *args: str) -> subprocess.CompletedProcess[str]:
        """Run one git command of the probe, whatever its exit code.

        Args:
            *args (str): The git arguments.

        Returns:
            subprocess.CompletedProcess[str]: What git did.
        """
        self.logger.debug("Running git %s in %s.", args[0], self.root)
        return subprocess.run(
            ["git", "-C", str(self.root), *args],
            capture_output=True,
            text=True,
            timeout=self.GIT_TIMEOUT_S,
            check=False,
        )

    def _failure(self, step: str, result: subprocess.CompletedProcess[str]) -> RebaseProbeResult:
        """Build the result of a git command of the probe that failed.

        Args:
            step (str): The command, such as ``git fetch``.
            result (subprocess.CompletedProcess[str]): What git did.

        Returns:
            RebaseProbeResult: The result, its error naming the command, its exit code and the start of its output.
        """
        error = f"{step} exited {result.returncode}: {result.stderr.strip()[: self.MESSAGE_LENGTH]}"
        self.logger.warning("The rebase probe in %s failed: %s exited %d.", self.root, step, result.returncode)
        return RebaseProbeResult(error=error)

    def _conflicts(self, output: str) -> Tuple[List[str], str]:
        """Read the output of a conflicting ``git merge-tree --write-tree --name-only --messages``.

        Args:
            output (str): The tree, the conflicting files, a blank line, then the messages.

        Returns:
            Tuple[List[str], str]: The conflicting files, each once, and the messages.
        """
        files, _, messages = output.partition("\n\n")
        return list(dict.fromkeys(line for line in files.splitlines()[1:] if line)), messages.strip()

    def _probe(self, base_ref: str, head_ref: str) -> RebaseProbeResult:
        """Fetch both branches into the watcher's namespace and merge them in memory.

        Args:
            base_ref (str): The pull request's base branch.
            head_ref (str): Its head branch.

        Returns:
            RebaseProbeResult: The conflicting files, or why the probe could not run.
        """
        base, head = f"{self.NAMESPACE}/{base_ref}", f"{self.NAMESPACE}/{head_ref}"
        fetch = self._attempt(
            "fetch", "--quiet", "--no-tags", "--refmap=", "origin",
            f"+refs/heads/{base_ref}:{base}", f"+refs/heads/{head_ref}:{head}",
        )  # fmt: skip
        if fetch.returncode:
            return self._failure("git fetch", fetch)
        heads = self._attempt("rev-parse", f"{base}^{{commit}}", f"{head}^{{commit}}")
        if heads.returncode:
            return self._failure("git rev-parse", heads)
        base_sha, head_sha = heads.stdout.split()
        merge = self._attempt("merge-tree", "--write-tree", "--name-only", "--messages", base, head)
        if merge.returncode not in {0, 1}:
            return self._failure("git merge-tree", merge).model_copy(
                update={"head_sha": head_sha, "base_sha": base_sha}
            )
        files, messages = self._conflicts(merge.stdout) if merge.returncode else ([], "")
        self.logger.debug("%s on %s: %d conflicting files.", head_ref, base_ref, len(files))
        return RebaseProbeResult(head_sha=head_sha, base_sha=base_sha, conflict_files=files, messages=messages)

    ############################
    # Publicly Exposed Methods #
    ############################

    def origin_slug(self) -> str:
        """Read the GitHub repository of the clone's ``origin``.

        Returns:
            str: ``<owner>/<name>``.

        Raises:
            SECloneNotOnGithubError: When ``origin`` is not a GitHub repository.
            SEGitCommandFailedError: When the clone has no ``origin``.
        """
        url = self._git("remote", "get-url", "origin")
        match = self.GITHUB_REMOTE.search(url)
        if match is None:
            self.logger.error("The origin of %s is not on GitHub.", self.root)
            raise SECloneNotOnGithubError(
                f"The origin of {self.root} is {url}. "  # noqa: E501
                "It must be a GitHub repository."
            )
        return match.group("slug")

    def main_root(self) -> Path:
        """Give the main working tree of the clone, the same from any of its worktrees.

        Returns:
            Path: The folder that holds the clone's ``.git``.
        """
        return Path(self._git("rev-parse", "--path-format=absolute", "--git-common-dir")).parent

    def probe(self, base_ref: str, head_ref: str) -> RebaseProbeResult:
        """Tell whether a pull request's head still merges into its base, without touching any working tree.

        Args:
            base_ref (str): The pull request's base branch, ``develop`` or ``master``.
            head_ref (str): Its head branch.

        Returns:
            RebaseProbeResult: The conflicting files, or why the probe could not run.
        """
        try:
            result = self._probe(base_ref, head_ref)
        except (OSError, subprocess.SubprocessError) as error:
            self.logger.warning("git could not run in %s: %s.", self.root, type(error).__name__)
            return RebaseProbeResult(error=f"git could not run: {type(error).__name__}")
        self.logger.info("Probed %s on %s: %d conflicting files.", head_ref, base_ref, len(result.conflict_files))
        return result
