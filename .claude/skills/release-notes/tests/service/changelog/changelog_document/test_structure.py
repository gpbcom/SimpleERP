from __future__ import annotations

import logging

from release_notes.service.changelog.changelog_document import ChangelogDocument
from tests.helpers import changelog


class TestStructure:
    def line(self, text: str, heading: str) -> int:
        return text.splitlines().index(heading) + 1

    def test_the_template_is_a_valid_changelog(self, logger: logging.Logger) -> None:
        document = ChangelogDocument(changelog(), logger)
        assert document.problems() == []
        assert document.versions() == []

    def test_released_sections_in_descending_order_are_valid(self, logger: logging.Logger) -> None:
        document = ChangelogDocument(
            changelog("## [0.10.0] - 2026-11-10\n\n### Added\n\n- A.", "## [0.9.0] - 2026-10-01\n\n### Fixed\n\n- B."),
            logger,
        )
        assert document.problems() == []
        assert document.versions() == ["0.10.0", "0.9.0"]
        assert document.has("0.9.0")
        assert not document.has("0.9.1")

    def test_a_missing_changelog_is_reported(self, logger: logging.Logger) -> None:
        assert ChangelogDocument("", logger).problems() == ["CHANGELOG.md: missing."]

    def test_the_title_and_the_unreleased_section_are_required(self, logger: logging.Logger) -> None:
        text = "# Changes\n\nNothing.\n"
        assert ChangelogDocument(text, logger).problems() == [
            'CHANGELOG.md: does not start with "# Changelog".',
            "CHANGELOG.md: no ## [Unreleased] section.",
        ]

    def test_the_unreleased_section_comes_first(self, logger: logging.Logger) -> None:
        text = "# Changelog\n\n## [0.1.0] - 2026-11-10\n\n- A.\n\n## [Unreleased]\n"
        assert ChangelogDocument(text, logger).problems() == [
            "CHANGELOG.md:3: the first section must be ## [Unreleased]."
        ]

    def test_a_bad_heading_is_reported_with_its_line(self, logger: logging.Logger) -> None:
        text = changelog("## [0.3] - 2026-11-10", "## [0.2.0] - 2026-02-30", "## [0.1.0]")
        assert ChangelogDocument(text, logger).problems() == [
            f'CHANGELOG.md:{self.line(text, heading)}: invalid heading "{heading}", expected ## [x.y.z] - YYYY-MM-DD.'
            for heading in ["## [0.3] - 2026-11-10", "## [0.2.0] - 2026-02-30", "## [0.1.0]"]
        ]

    def test_versions_go_in_descending_order(self, logger: logging.Logger) -> None:
        text = changelog("## [0.1.0] - 2026-10-01", "## [0.2.0] - 2026-11-10", "## [0.2.0] - 2026-11-11")
        assert ChangelogDocument(text, logger).problems() == [
            f"CHANGELOG.md:{self.line(text, '## [0.2.0] - 2026-11-10')}: [0.2.0] comes after [0.1.0], versions"
            " must be in descending order.",
            f"CHANGELOG.md:{self.line(text, '## [0.2.0] - 2026-11-11')}: [0.2.0] comes after [0.2.0], versions"
            " must be in descending order.",
        ]
