from __future__ import annotations

import logging

import pytest

from release_notes.service.changelog.changelog_document import ChangelogDocument
from release_notes.service.exceptions import SEChangelogInvalidError
from tests.helpers import changelog


class TestEditing:
    SECTION = "## [0.2.0] - 2026-11-10\n\n### Added\n\n- New. ([GH-9](https://github.com/gpbcom/simple-erp/issues/9))"
    OLD = "## [0.1.0] - 2026-10-01\n\n### Fixed\n\n- Old.  \n"

    def test_a_section_goes_right_after_the_unreleased_block(self, logger: logging.Logger) -> None:
        text = ChangelogDocument(changelog(), logger).insert(self.SECTION)
        assert text == changelog().rstrip() + "\n\n" + self.SECTION + "\n"
        assert ChangelogDocument(text, logger).problems() == []

    def test_the_released_sections_stay_as_they_are_below_the_new_one(self, logger: logging.Logger) -> None:
        before = changelog(self.OLD)
        text = ChangelogDocument(before, logger).insert(self.SECTION)
        assert text.index("## [Unreleased]") < text.index("## [0.2.0]") < text.index("## [0.1.0]")
        assert text.endswith("### Fixed\n\n- Old.\n")
        assert ChangelogDocument(text, logger).versions() == ["0.2.0", "0.1.0"]

    def test_a_section_is_read_back_up_to_the_next_one(self, logger: logging.Logger) -> None:
        document = ChangelogDocument(ChangelogDocument(changelog(self.OLD), logger).insert(self.SECTION), logger)
        assert document.section("0.2.0") == self.SECTION
        assert document.section("0.1.0") == "## [0.1.0] - 2026-10-01\n\n### Fixed\n\n- Old."
        assert document.section("0.3.0") is None

    def test_a_changelog_without_its_unreleased_section_is_refused(self, logger: logging.Logger) -> None:
        with pytest.raises(SEChangelogInvalidError):
            ChangelogDocument("# Changelog\n", logger).insert(self.SECTION)
