from __future__ import annotations

import asyncio
import logging
from pathlib import Path

import pytest

from harness_core.github.github_token import GithubToken
from harness_core.testing.git_sandbox import GitSandbox
from harness_core.testing.github_fake import GithubFake
from release_notes.models.catalogs.github_api import GithubApi
from release_notes.models.catalogs.github_coordinates import GithubCoordinates
from release_notes.service.exceptions import SEVersionNotFoundError
from release_notes.service.notes.release_body import ReleaseBody
from release_notes.storage.files.text_files import TextFiles
from tests.helpers import GITHUB_API_FILE, ISSUES, MARKER, changelog, release_note


class TestReleaseBody:
    SECTION = (
        "## [0.2.0] - 2026-11-10\n\n### Added\n\n"
        f"- Customers can be archived. ([GH-7]({ISSUES}/7))\n- Their invoices stay. ([GH-7]({ISSUES}/7))\n\n"
        f"### Fixed\n\n- Login works again. ([GH-9]({ISSUES}/9))"
    )
    OLD = f"## [0.1.0] - 2026-10-01\n\n### Added\n\n- A harness. ([GH-3]({ISSUES}/3))"
    COMMENTS = "/repos/gpbcom/simple-erp/issues/{number}/comments"

    @pytest.fixture(autouse=True)
    def token(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("GITHUB_TOKEN", "secret-token")

    def body(self, sandbox: GitSandbox, fake: GithubFake, logger: logging.Logger, version: str = "0.2.0") -> str:
        sandbox.write("CHANGELOG.md", changelog(self.SECTION, self.OLD))
        service = ReleaseBody(
            TextFiles(sandbox.root, logger),
            GithubCoordinates(owner="gpbcom", repository="simple-erp"),
            GithubApi.load(GITHUB_API_FILE),
            GithubToken(logger),
            MARKER,
            fake.transport(),
            logger,
        )
        return asyncio.run(service.text(version))

    def test_the_section_then_each_issue_note_then_the_upgrade_notes(
        self, sandbox: GitSandbox, logger: logging.Logger
    ) -> None:
        note = release_note("GH-7", upgrade="Run the `migrate` command once.")
        fake = GithubFake()
        fake.routes[self.COMMENTS.format(number=7)] = [
            {"body": "Looks good."},
            {"body": release_note("GH-7", upgrade="An older note.")},
            {"body": note},
        ]
        fake.routes[self.COMMENTS.format(number=9)] = [{"body": release_note("GH-9")}]
        body = self.body(sandbox, fake, logger)
        assert body == (
            f"{self.SECTION}\n\n## Release notes\n\n{note.removeprefix(MARKER).strip()}\n\n"
            f"{release_note('GH-9').removeprefix(MARKER).strip()}\n\n"
            "## Upgrade notes\n\n### GH-7\n\nRun the `migrate` command once.\n"
        )
        assert sorted(set(fake.paths())) == [self.COMMENTS.format(number=7), self.COMMENTS.format(number=9)]

    def test_a_missing_or_unreadable_note_is_a_line_not_a_crash(
        self, sandbox: GitSandbox, logger: logging.Logger
    ) -> None:
        fake = GithubFake()
        fake.routes[self.COMMENTS.format(number=7)] = [{"body": "No marker here."}]
        fake.failures[self.COMMENTS.format(number=9)] = 502
        body = self.body(sandbox, fake, logger)
        assert body == (
            f"{self.SECTION}\n\n## Release notes\n\nNo release note was found on issue #7.\n\n"
            "The release note of issue #9 could not be read (SEGithubRequestFailedError).\n\n"
            "## Upgrade notes\n\nNothing to do.\n"
        )

    def test_without_a_token_no_note_is_read(
        self, sandbox: GitSandbox, logger: logging.Logger, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        monkeypatch.delenv("GITHUB_TOKEN")
        monkeypatch.setenv("PATH", str(tmp_path / "empty"))
        fake = GithubFake()
        body = self.body(sandbox, fake, logger)
        assert "The release note of issue #7 could not be read (SEGithubTokenMissingError)." in body
        assert "The release note of issue #9 could not be read (SEGithubTokenMissingError)." in body
        assert fake.requests == []

    def test_a_version_without_its_section_is_refused(self, sandbox: GitSandbox, logger: logging.Logger) -> None:
        with pytest.raises(SEVersionNotFoundError):
            self.body(sandbox, GithubFake(), logger, version="0.3.0")
