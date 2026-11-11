from __future__ import annotations

import logging

import pytest

from harness_core.git.git_repository import GitRepository
from harness_core.testing.git_sandbox import GitSandbox
from release_notes.models.catalogs.changelog_type_catalog import ChangelogTypeCatalog
from release_notes.service.checks.branch_check import BranchCheck
from release_notes.service.fragments.fragment_reader import FragmentReader
from release_notes.storage.files.text_files import TextFiles
from tests.helpers import changelog


class TestBranchCheck:
    RELEASED = "## [0.1.0] - 2026-11-10\n\n### Added\n\n- Customers. ([GH-7](https://x))"

    def check(self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger) -> BranchCheck:
        files = TextFiles(sandbox.root, logger)
        return BranchCheck(GitRepository(sandbox.root, logger), files, FragmentReader(files, catalog, logger), logger)

    @pytest.mark.parametrize("branch", ["feature/GH-7-add-customers", "bugfix/GH-7-fix-customers"])
    def test_a_ticket_branch_with_its_one_fragment_passes(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger, branch: str
    ) -> None:
        sandbox.write("changelog.d/GH-7.added.md", "Customers can be archived.\n")
        sandbox.write("changelog.d/GH-70.oops.md", "Another ticket's problem.\n")
        assert self.check(sandbox, catalog, logger).problems(branch) == []

    def test_the_current_branch_is_the_default(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        sandbox.write("changelog.d/GH-70.added.md", "Another ticket.\n")
        assert self.check(sandbox, catalog, logger).problems(None) == [
            "changelog.d/: no fragment GH-7.<type>.md for GH-7."
        ]

    def test_several_fragments_for_the_ticket_are_reported(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        sandbox.write("changelog.d/GH-7.added.md", "A.\n")
        sandbox.write("changelog.d/GH-7.fixed.md", "B.\n")
        assert self.check(sandbox, catalog, logger).problems("feature/GH-7-add-customers") == [
            "changelog.d/: 2 fragments for GH-7 (GH-7.added.md, GH-7.fixed.md), exactly one expected."
        ]

    @pytest.mark.parametrize(
        ("name", "text", "start"),
        [
            ("GH-7.feature.md", "A.\n", "changelog.d/GH-7.feature.md: unknown type feature"),
            ("GH-7.added.md", "a\nb\nc\nd\n", "changelog.d/GH-7.added.md: 4 non-empty lines"),
        ],
    )
    def test_the_ticket_fragment_must_be_valid(
        self,
        sandbox: GitSandbox,
        catalog: ChangelogTypeCatalog,
        logger: logging.Logger,
        name: str,
        text: str,
        start: str,
    ) -> None:
        sandbox.write(f"changelog.d/{name}", text)
        problems = self.check(sandbox, catalog, logger).problems("feature/GH-7-add-customers")
        assert len(problems) == 1
        assert problems[0].startswith(start)

    def test_a_release_branch_needs_its_section_and_no_fragment_left(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        check = self.check(sandbox, catalog, logger)
        sandbox.write("changelog.d/GH-7.added.md", "A.\n")
        assert check.problems("release/0.1.0") == [
            "CHANGELOG.md: no section ## [0.1.0] - YYYY-MM-DD.",
            "changelog.d/GH-7.added.md: left over, release-notes build 0.1.0 moves it into CHANGELOG.md.",
        ]
        sandbox.write("CHANGELOG.md", changelog(self.RELEASED))
        (sandbox.root / "changelog.d/GH-7.added.md").unlink()
        assert check.problems("release/0.1.0") == []

    def test_a_hotfix_branch_has_its_fragment_or_its_built_section(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        check = self.check(sandbox, catalog, logger)
        assert check.problems("hotfix/0.1.0-GH-7-fix-login") == ["changelog.d/: no fragment GH-7.<type>.md for GH-7."]
        sandbox.write("changelog.d/GH-7.fixed.md", "Login works again.\n")
        assert check.problems("hotfix/0.1.0-GH-7-fix-login") == []
        sandbox.write("CHANGELOG.md", changelog(self.RELEASED))
        assert check.problems("hotfix/0.1.0-GH-7-fix-login") == [
            "changelog.d/GH-7.fixed.md: left over, release-notes build 0.1.0 moves it into CHANGELOG.md."
        ]

    @pytest.mark.parametrize("branch", ["develop", "master", "dependabot/pip/httpx-0.28.1"])
    def test_other_branches_only_need_a_valid_changelog(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger, branch: str
    ) -> None:
        sandbox.write("changelog.d/GH-7.oops.md", "x\n")
        check = self.check(sandbox, catalog, logger)
        assert check.problems(branch) == []
        sandbox.write("CHANGELOG.md", "# Changelog\n")
        assert check.problems(branch) == ["CHANGELOG.md: no ## [Unreleased] section."]

    def test_a_branch_that_misses_its_gitflow_shape_is_reported(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        problems = self.check(sandbox, catalog, logger).problems("feature/add-customers")
        assert len(problems) == 1
        assert problems[0].startswith("feature/add-customers: not a GitFlow branch name.")
