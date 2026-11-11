from __future__ import annotations

# Standard library imports
import os
import subprocess
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, Dict, Optional


class GitSandbox:
    """A real git repository in a temporary folder, for the tests of the harness tools.

    Attributes:
        IDENTITY (Dict[str, str]): The author and committer of the sandbox's commits.
        root (Path): The repository's folder.
        branch (str): The branch it starts on.
        logger (Logger): Logger instance.

    Notes:
        - Signing is turned off in the repository itself, so a person's global ``commit.gpgsign`` or
          ``tag.gpgsign`` never stops a test.
        - The tools read the sandbox with their own ``GitRepository``, exactly as they read the real repository.
    """

    IDENTITY: ClassVar[Dict[str, str]] = {
        "GIT_AUTHOR_NAME": "Sandbox",
        "GIT_AUTHOR_EMAIL": "sandbox@example.com",
        "GIT_COMMITTER_NAME": "Sandbox",
        "GIT_COMMITTER_EMAIL": "sandbox@example.com",
    }

    def __init__(self, root: Path, branch: str = "develop", logger: Optional[Logger] = None) -> None:
        """Set the folder and the first branch.

        Args:
            root (Path): The repository's folder, created by ``create``.
            branch (str): The branch it starts on.
            logger (Optional[Logger]): Logger instance.
        """
        self.root = root.resolve()
        self.branch = branch
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def git(self, *args: str) -> str:
        """Run one git command in the sandbox.

        Args:
            *args (str): The git arguments.

        Returns:
            str: The standard output, stripped.

        Raises:
            subprocess.CalledProcessError: When git fails.
        """
        self.logger.debug("Sandbox git %s.", " ".join(args))
        return subprocess.run(
            ["git", "-C", str(self.root), *args],
            check=True,
            capture_output=True,
            text=True,
            env={**os.environ, **self.IDENTITY},
        ).stdout.strip()

    def create(self) -> Path:
        """Create the repository with one empty commit on its branch.

        Returns:
            Path: The repository's folder.
        """
        self.root.mkdir(parents=True, exist_ok=True)
        self.git("init", "-q", "-b", self.branch)
        self.git("config", "commit.gpgsign", "false")
        self.git("config", "tag.gpgsign", "false")
        self.git("commit", "-q", "--allow-empty", "-m", "root")
        self.logger.info("Created the sandbox %s on %s.", self.root, self.branch)
        return self.root

    def write(self, path: str, text: str) -> Path:
        """Write one file without committing it.

        Args:
            path (str): The path relative to the repository.
            text (str): The content.

        Returns:
            Path: The file.
        """
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return target

    def commit(self, message: str, files: Optional[Dict[str, Optional[str]]] = None) -> str:
        """Write or delete files, then commit everything.

        Args:
            message (str): The commit message.
            files (Optional[Dict[str, Optional[str]]]): Each path and its content, ``None`` to delete it.

        Returns:
            str: The new commit's hash.
        """
        for path, text in (files or {}).items():
            if text is None:
                (self.root / path).unlink()
            else:
                self.write(path, text)
        self.git("add", "-A")
        self.git("commit", "-q", "--allow-empty", "-m", message)
        commit = self.git("rev-parse", "HEAD")
        self.logger.info("Committed %s in the sandbox.", commit[:8])
        return commit
