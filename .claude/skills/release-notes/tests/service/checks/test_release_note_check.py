from __future__ import annotations

import logging

import pytest

from harness_core.testing.git_sandbox import GitSandbox
from release_notes.service.checks.release_note_check import ReleaseNoteCheck
from release_notes.service.exceptions import SETicketKeyInvalidError
from release_notes.storage.files.text_files import TextFiles
from tests.helpers import MARKER, TEMPLATES, release_note


class TestReleaseNoteCheck:
    NOTE = "docs/tickets/GH-7/RELEASE-NOTE.md"

    def check(self, sandbox: GitSandbox, logger: logging.Logger) -> ReleaseNoteCheck:
        template = (TEMPLATES / "RELEASE-NOTE.md").read_text(encoding="utf-8")
        return ReleaseNoteCheck(TextFiles(sandbox.root, logger), template, logger)

    def test_a_filled_note_passes(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        sandbox.write(self.NOTE, release_note())
        assert self.check(sandbox, logger).problems("GH-7") == []

    def test_the_marker_is_the_template_first_line(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        assert self.check(sandbox, logger).marker == MARKER

    def test_a_missing_note_is_reported(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        assert self.check(sandbox, logger).problems("GH-7") == [f"{self.NOTE}: missing."]

    def test_the_marker_and_every_heading_are_required(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        text = release_note().replace(f"{MARKER}\n", "").replace("## Known limits\n\nNone.\n\n", "")
        sandbox.write(self.NOTE, text)
        assert self.check(sandbox, logger).problems("GH-7") == [
            f"{self.NOTE}: does not start with {MARKER}.",
            f'{self.NOTE}: no "## Known limits" heading.',
        ]

    def test_a_placeholder_left_is_reported_with_its_line(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        sandbox.write(self.NOTE, release_note().replace("Customers can be archived", "<what users can now do>"))
        assert self.check(sandbox, logger).problems("GH-7") == [
            f"{self.NOTE}:8: placeholder <what users can now do> left."
        ]

    def test_the_template_itself_is_full_of_placeholders(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        sandbox.write(self.NOTE, (TEMPLATES / "RELEASE-NOTE.md").read_text(encoding="utf-8"))
        problems = self.check(sandbox, logger).problems("GH-7")
        assert f"{self.NOTE}:2: placeholder <KEY> left." in problems
        assert any(problem.endswith("placeholder <owner> left.") for problem in problems)

    @pytest.mark.parametrize("key", ["7", "GH-7/..", "gh-7"])
    def test_a_bad_ticket_key_is_refused(self, sandbox: GitSandbox, logger: logging.Logger, key: str) -> None:
        with pytest.raises(SETicketKeyInvalidError):
            self.check(sandbox, logger).problems(key)
