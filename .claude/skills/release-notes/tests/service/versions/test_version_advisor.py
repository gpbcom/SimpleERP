from __future__ import annotations

import logging
from typing import Dict, List

import pytest

from harness_core.git.git_repository import GitRepository
from harness_core.testing.git_sandbox import GitSandbox
from release_notes.models.catalogs.changelog_type_catalog import ChangelogTypeCatalog
from release_notes.service.exceptions import SEFragmentsRefusedError
from release_notes.service.fragments.fragment_reader import FragmentReader
from release_notes.service.versions.version_advisor import VersionAdvisor
from release_notes.storage.files.text_files import TextFiles


class TestVersionAdvisor:
    def advisor(self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger) -> VersionAdvisor:
        files = TextFiles(sandbox.root, logger)
        return VersionAdvisor(GitRepository(sandbox.root, logger), FragmentReader(files, catalog, logger), logger)

    def prepare(self, sandbox: GitSandbox, tags: List[str], fragments: Dict[str, str]) -> None:
        for tag in tags:
            sandbox.git("tag", tag)
        for name, text in fragments.items():
            sandbox.write(f"changelog.d/{name}", text)

    def test_without_a_tag_the_first_version_starts_from_0_0_0(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        self.prepare(sandbox, [], {"GH-1.added.md": "A harness.\n"})
        version, reason = self.advisor(sandbox, catalog, logger).suggest()
        assert str(version) == "0.1.0"
        assert reason == "minor bump from 0.0.0 (no v<x.y.z> tag yet): GH-1.added.md (minor)."

    @pytest.mark.parametrize(
        ("tags", "fragments", "expected"),
        [
            (["v0.1.0", "v0.10.0", "v0.9.0", "v1.2", "evidence-GH-1"], {"GH-4.fixed.md": "Fix.\n"}, "0.10.1"),
            (["v1.2.3"], {"GH-4.fixed.md": "Fix.\n", "GH-5.security.md": "Patch.\n"}, "1.2.4"),
            (["v1.2.3"], {"GH-4.fixed.md": "Fix.\n", "GH-5.deprecated.md": "Old.\n"}, "1.3.0"),
            (["v1.2.3"], {"GH-4.removed.md": "Gone.\n", "GH-5.added.md": "New.\n"}, "2.0.0"),
            (["v1.2.3"], {"GH-4.added.md": "**Breaking:** The API moved.\n"}, "2.0.0"),
        ],
    )
    def test_the_highest_bump_of_the_fragments_wins(
        self,
        sandbox: GitSandbox,
        catalog: ChangelogTypeCatalog,
        logger: logging.Logger,
        tags: List[str],
        fragments: Dict[str, str],
        expected: str,
    ) -> None:
        self.prepare(sandbox, tags, fragments)
        assert str(self.advisor(sandbox, catalog, logger).suggest()[0]) == expected

    def test_a_breaking_fragment_is_named_as_such(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        self.prepare(sandbox, ["v1.2.3"], {"GH-4.changed.md": "**Breaking:** The API moved.\n"})
        assert self.advisor(sandbox, catalog, logger).suggest()[1] == (
            "major bump from v1.2.3: GH-4.changed.md (breaking)."
        )

    def test_while_the_major_version_is_0_a_major_bump_bumps_the_minor_version(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        self.prepare(sandbox, ["v0.3.2"], {"GH-4.removed.md": "Gone.\n"})
        version, reason = self.advisor(sandbox, catalog, logger).suggest()
        assert str(version) == "0.4.0"
        assert reason == (
            "major bump from v0.3.2: GH-4.removed.md (major). While the major version is 0, a major bump bumps the"
            " minor version instead (semver 0.x)."
        )

    def test_no_fragment_is_refused(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        with pytest.raises(SEFragmentsRefusedError, match="nothing to release"):
            self.advisor(sandbox, catalog, logger).suggest()

    def test_an_invalid_fragment_is_refused(
        self, sandbox: GitSandbox, catalog: ChangelogTypeCatalog, logger: logging.Logger
    ) -> None:
        self.prepare(sandbox, [], {"GH-1.added.md": "A.\n", "GH-2.feature.md": "B.\n"})
        with pytest.raises(SEFragmentsRefusedError, match="unknown type feature"):
            self.advisor(sandbox, catalog, logger).suggest()
