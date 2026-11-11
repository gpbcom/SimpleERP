from __future__ import annotations

import logging
from datetime import date

import pytest

from harness_core.git.git_repository import GitRepository
from harness_core.testing.git_sandbox import GitSandbox
from release_notes.models.catalogs.changelog_type_catalog import ChangelogTypeCatalog
from release_notes.models.catalogs.github_coordinates import GithubCoordinates
from release_notes.service.changelog.changelog_builder import ChangelogBuilder
from release_notes.service.changelog.changelog_document import ChangelogDocument
from release_notes.service.exceptions import SEChangelogInvalidError, SEFragmentsRefusedError, SEVersionRefusedError
from release_notes.service.fragments.fragment_reader import FragmentReader
from release_notes.storage.files.text_files import TextFiles
from tests.helpers import ISSUES, changelog


class TestChangelogBuilder:
    TODAY = date(2026, 11, 10)

    def builder(self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger) -> ChangelogBuilder:
        files = TextFiles(sandbox.root, logger)
        return ChangelogBuilder(
            GitRepository(sandbox.root, logger),
            files,
            FragmentReader(files, catalog, logger),
            catalog,
            GithubCoordinates(owner="gpbcom", repository="simple-erp"),
            logger,
        )

    def fragments(self, sandbox: GitSandbox) -> None:
        sandbox.write("changelog.d/GH-7.added.md", "Customers can be archived.\n- Their invoices stay.\n")
        sandbox.write("changelog.d/GH-12.fixed.md", "Login works again after a password change.\n")
        sandbox.write("changelog.d/GH-3.added.md", "**Breaking:** Customers have a code.\n")

    def test_the_section_groups_the_fragments_by_type_and_links_their_issues(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        self.fragments(sandbox)
        deleted = self.builder(sandbox, catalog, logger).build("0.1.0", self.TODAY)
        assert deleted == ["changelog.d/GH-12.fixed.md", "changelog.d/GH-3.added.md", "changelog.d/GH-7.added.md"]
        document = ChangelogDocument((sandbox.root / "CHANGELOG.md").read_text(encoding="utf-8"), logger)
        assert document.problems() == []
        assert document.section("0.1.0") == (
            "## [0.1.0] - 2026-11-10\n\n### Added\n\n"
            f"- **Breaking:** Customers have a code. ([GH-3]({ISSUES}/3))\n"
            f"- Customers can be archived. ([GH-7]({ISSUES}/7))\n"
            f"- Their invoices stay. ([GH-7]({ISSUES}/7))\n\n"
            f"### Fixed\n\n- Login works again after a password change. ([GH-12]({ISSUES}/12))"
        )
        assert sorted(path.name for path in (sandbox.root / "changelog.d").iterdir()) == ["README.md"]

    @pytest.mark.parametrize(
        ("version", "released", "tag"),
        [
            ("1.0", "", ""),
            ("0.1.0", "## [0.1.0] - 2026-10-01", ""),
            ("0.1.0", "", "v0.1.0"),
            ("0.0.9", "## [0.1.0] - 2026-10-01", ""),
        ],
    )
    def test_a_version_that_cannot_be_released_is_refused_and_nothing_changes(
        self,
        sandbox: GitSandbox,
        catalog: ChangelogTypeCatalog,
        logger: logging.Logger,
        version: str,
        released: str,
        tag: str,
    ) -> None:
        self.fragments(sandbox)
        sandbox.write("CHANGELOG.md", changelog(released) if released else changelog())
        if tag:
            sandbox.git("tag", tag)
        before = (sandbox.root / "CHANGELOG.md").read_text(encoding="utf-8")
        with pytest.raises(SEVersionRefusedError):
            self.builder(sandbox, catalog, logger).build(version, self.TODAY)
        assert (sandbox.root / "CHANGELOG.md").read_text(encoding="utf-8") == before
        assert (sandbox.root / "changelog.d/GH-7.added.md").exists()

    def test_no_fragment_is_refused(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        with pytest.raises(SEFragmentsRefusedError, match="nothing to release"):
            self.builder(sandbox, catalog, logger).build("0.1.0", self.TODAY)

    def test_an_invalid_fragment_is_refused_and_nothing_changes(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        self.fragments(sandbox)
        sandbox.write("changelog.d/GH-8.added.md", "a\nb\nc\nd\n")
        with pytest.raises(SEFragmentsRefusedError, match="4 non-empty lines"):
            self.builder(sandbox, catalog, logger).build("0.1.0", self.TODAY)
        assert (sandbox.root / "changelog.d/GH-7.added.md").exists()
        assert "## [0.1.0]" not in (sandbox.root / "CHANGELOG.md").read_text(encoding="utf-8")

    def test_a_changelog_without_its_unreleased_section_is_refused(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        self.fragments(sandbox)
        sandbox.write("CHANGELOG.md", "# Changelog\n")
        with pytest.raises(SEChangelogInvalidError):
            self.builder(sandbox, catalog, logger).build("0.1.0", self.TODAY)
        assert (sandbox.root / "changelog.d/GH-7.added.md").exists()
