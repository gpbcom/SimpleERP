from __future__ import annotations

# Standard library imports
from typing import ClassVar

# First-party imports
from release_notes.api.cli.command import Command


class CheckCommand(Command):
    """``release-notes check``: print every problem of the changelog, the fragments and the release note.

    Attributes:
        PROBLEMS (int): The exit code when the check found problems.

    Notes:
        Nothing is printed and the exit code is 0 when DOC-3 holds, so CI can run it as a gate.
    """

    PROBLEMS: ClassVar[int] = 1

    ############################
    # Internal Helpers Methods #
    ############################

    def _perform(self) -> None:
        """Check the branch, and the ticket's release note when asked, and print the problems."""
        problems = self.services.branch_check().problems(self.options.branch)
        if self.options.ticket is not None:
            problems.extend(self.services.release_note_check().problems(self.options.ticket))
        for problem in problems:
            print(problem)
        self.exit_code = self.PROBLEMS if problems else 0
        self.logger.info("release-notes check printed %d problems.", len(problems))
