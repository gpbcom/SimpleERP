from __future__ import annotations

# Standard library imports
from logging import Logger
from typing import List, Optional

# First-party imports
from harness_core.terminal.human_confirmation import HumanConfirmation


class ScriptedConfirmation(HumanConfirmation):
    """A confirmation whose answer follows a script, for the tests of the harness tools.

    Attributes:
        confirmed (bool): Whether the scripted human types the code back.
        questions (List[str]): Each question asked.
    """

    def __init__(self, confirmed: bool, logger: Optional[Logger] = None) -> None:
        """Set the script.

        Args:
            confirmed (bool): Whether the scripted human types the code back.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(None, logger)
        self.confirmed = confirmed
        self.questions: List[str] = []

    ############################
    # Publicly Exposed Methods #
    ############################

    def confirm(self, question: str) -> bool:
        """Record the question and give the scripted answer.

        Args:
            question (str): What is to be confirmed.

        Returns:
            bool: The scripted answer.
        """
        self.questions.append(question)
        self.logger.debug("Asked a scripted question.")
        return self.confirmed
