from __future__ import annotations

# Standard library imports
import os
import subprocess
from logging import Logger, getLogger
from typing import ClassVar, List, Optional

# First-party imports
from harness_core.github.exceptions import SEGithubTokenMissingError


class GithubToken:
    """Finds the GitHub token a harness tool reads the API with.

    Attributes:
        ENVIRONMENT_VARIABLE (str): The variable that overrides the GitHub CLI's token.
        COMMAND (List[str]): The GitHub CLI command that prints its token.
        TIMEOUT_S (int): The longest the GitHub CLI may take.
        logger (Logger): Logger instance.

    Notes:
        - **The token is kept in memory only**: it is read when it is needed, and never logged or written.
        - ``GITHUB_TOKEN`` wins over ``gh auth token``, so that a run can use a token with fewer rights.
    """

    ENVIRONMENT_VARIABLE: ClassVar[str] = "GITHUB_TOKEN"
    COMMAND: ClassVar[List[str]] = ["gh", "auth", "token"]
    TIMEOUT_S: ClassVar[int] = 30

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def read(self) -> str:
        """Read the token.

        Returns:
            str: The token.

        Raises:
            SEGithubTokenMissingError: When neither the variable nor the GitHub CLI gives one.
        """
        token = os.environ.get(self.ENVIRONMENT_VARIABLE, "").strip()
        if token:
            self.logger.debug("The GitHub token comes from %s.", self.ENVIRONMENT_VARIABLE)
            return token
        try:
            result = subprocess.run(self.COMMAND, capture_output=True, text=True, timeout=self.TIMEOUT_S, check=False)
        except (OSError, subprocess.SubprocessError) as error:
            self.logger.error("The GitHub CLI could not run: %s.", type(error).__name__)
            raise SEGithubTokenMissingError(
                "No GitHub token was found. "  # noqa: E501
                "Set GITHUB_TOKEN or log in with gh auth login."
            ) from error
        if result.returncode or not result.stdout.strip():
            self.logger.error("gh auth token exited with code %d and printed no token.", result.returncode)
            raise SEGithubTokenMissingError(
                "No GitHub token was found. "  # noqa: E501
                "Set GITHUB_TOKEN or log in with gh auth login."
            )
        self.logger.debug("The GitHub token comes from gh auth token.")
        return result.stdout.strip()
