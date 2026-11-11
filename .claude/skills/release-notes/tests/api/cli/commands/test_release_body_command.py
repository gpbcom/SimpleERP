from __future__ import annotations

import logging

import pytest

from harness_core.testing.git_sandbox import GitSandbox
from harness_core.testing.github_fake import GithubFake
from release_notes.api.cli.main import main
from release_notes.models.catalogs.changelog_type_catalog import ChangelogTypeCatalog
from release_notes.models.settings.release_notes_settings import ReleaseNotesSettings
from release_notes.service.factories.default.default_service_factory import DefaultServiceFactory
from tests.helpers import ISSUES, MARKER, changelog, release_note


class TestReleaseBodyCommand:
    SECTION = f"## [0.1.0] - 2026-11-10\n\n### Added\n\n- Customers can be archived. ([GH-7]({ISSUES}/7))"

    def services(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, fake: GithubFake, logger: logging.Logger
    ) -> DefaultServiceFactory:
        return DefaultServiceFactory(ReleaseNotesSettings(caller_cwd=sandbox.root), catalog, fake.transport(), logger)

    def test_the_body_is_printed_from_the_changelog_and_the_issue_note(
        self,
        caller_in_sandbox: GitSandbox,
        catalog: ChangelogTypeCatalog,
        logger: logging.Logger,
        monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        monkeypatch.setenv("GITHUB_TOKEN", "secret-token")
        caller_in_sandbox.write("CHANGELOG.md", changelog(self.SECTION))
        fake = GithubFake()
        fake.routes["/repos/gpbcom/simple-erp/issues/7/comments"] = [{"body": release_note()}]
        assert main(["release-body", "0.1.0"], self.services(caller_in_sandbox, catalog, fake, logger)) == 0
        output = capsys.readouterr().out
        assert output.startswith(f"{self.SECTION}\n\n## Release notes\n\n# GH-7: Customers\n")
        assert MARKER not in output
        assert output.endswith("## Upgrade notes\n\nNothing to do.\n")
        assert fake.requests[0].headers["Authorization"] == "Bearer secret-token"

    def test_an_unreleased_version_is_a_failure_the_person_can_fix(
        self,
        caller_in_sandbox: GitSandbox,
        catalog: ChangelogTypeCatalog,
        logger: logging.Logger,
        capsys: pytest.CaptureFixture[str],
    ) -> None:
        fake = GithubFake()
        assert main(["release-body", "0.1.0"], self.services(caller_in_sandbox, catalog, fake, logger)) == 2
        assert capsys.readouterr().err.startswith("release-notes: ")
        assert fake.requests == []
