from __future__ import annotations

# Standard library imports
import sys
from pathlib import Path
from typing import Optional

# Third-party imports
import pytest

# First-party imports
from tests.harness.check_ticket.helpers import (
    DECISION,
    ENTITY,
    FLOW,
    LIST_SCREEN,
    MOCKUP,
    OLD_DECISION,
    REQUIREMENT,
    RULE,
    SCREEN,
    SECTOR_USE_CASE,
    USE_CASE,
    build_root,
    repo_root,
)

sys.path.insert(0, str(repo_root() / ".claude" / "skills" / "ticket" / "scripts"))

from spec_ids import SPEC_ID, id_of, normalise, resolve  # noqa: E402


class TestSpecIds:
    @pytest.mark.parametrize(
        ("spec_id", "page"),
        [
            ("UC-F6-01", USE_CASE),
            ("UC-F06-01", USE_CASE),
            ("BR-F6-01", RULE),
            ("E-F6-01", ENTITY),
            ("FL-F6-01", FLOW),
            ("S-F6-01", SCREEN),
            ("S-F6-L01", LIST_SCREEN),
            ("REQ-T01-01", REQUIREMENT),
            ("D438", DECISION),
            ("D9", OLD_DECISION),
            ("UC-SC01-01", SECTOR_USE_CASE),
        ],
    )
    def test_an_id_resolves_to_its_page(self, tmp_path: Path, spec_id: str, page: str) -> None:
        root = build_root(tmp_path)
        assert resolve(spec_id, root) == (root / page).resolve()

    @pytest.mark.parametrize("spec_id", ["UC-F6-99", "D999", "REQ-T09-01", "UC-F6-77", "T0.03", "not an id"])
    def test_an_id_without_a_page_resolves_to_nothing(self, tmp_path: Path, spec_id: str) -> None:
        assert resolve(spec_id, build_root(tmp_path)) is None

    @pytest.mark.parametrize(
        ("page", "expected"),
        [
            (USE_CASE, "UC-F6-01"),
            (LIST_SCREEN, "S-F6-L01"),
            (OLD_DECISION, "D9"),
            (MOCKUP, "UC-F6-77"),
            ("README.md", None),
        ],
    )
    def test_a_page_gives_the_id_its_title_writes(self, page: str, expected: Optional[str]) -> None:
        assert id_of(Path(page)) == expected

    @pytest.mark.parametrize("text", ["T1.07", "ticket T0.03", "UC-F6-01x", "the D-day", "mUC-F6-01"])
    def test_ticket_ids_and_words_are_no_specification_ids(self, text: str) -> None:
        assert SPEC_ID.search(text) is None

    def test_a_padded_feature_number_gives_the_unpadded_id(self) -> None:
        assert normalise("BR-F06-01") == "BR-F6-01"
