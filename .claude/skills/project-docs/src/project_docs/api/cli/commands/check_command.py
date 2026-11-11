from __future__ import annotations

# Standard library imports
from typing import ClassVar

# First-party imports
from project_docs.api.cli.command import Command


class CheckCommand(Command):
    """``project-docs check``: print every problem of the documentation, one per line.

    Attributes:
        PROBLEMS (int): The exit code when the check found problems.

    Notes:
        Nothing is printed and the exit code is 0 when the documentation is complete, so CI can run it as a gate.
    """

    PROBLEMS: ClassVar[int] = 1

    ############################
    # Internal Helpers Methods #
    ############################

    def _perform(self) -> None:
        """Check the documentation and print its problems."""
        problems = self.services.documentation().check(self.options.ticket, self.options.base)
        for problem in problems:
            print(problem)
        self.exit_code = self.PROBLEMS if problems else 0
        self.logger.info("project-docs check printed %d problems.", len(problems))
