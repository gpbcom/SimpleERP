from __future__ import annotations

from pathlib import Path
from typing import Dict

import pytest
from pydantic import JsonValue

from ticket_docs.models.checks.exceptions import (
    SEFolderRulesInvalidHeadings,
    SEFolderRulesInvalidList,
    SEFolderRulesInvalidMinutes,
    SEFolderRulesUnreadable,
)
from ticket_docs.models.checks.folder_rules import FolderRules


class TestFolderRules:
    CONF = Path(__file__).resolve().parents[3] / "conf" / "folder-rules.yaml"
    LISTS = (
        "required_files",
        "handover_files",
        "placeholders",
        "finished_files",
        "status_icons",
        "stage_icons",
        "result_sections",
        "run_steps",
        "production_paths",
        "test_paths",
        "marker_files",
        "commit_options",
        "guard_state_folders",
    )

    def valid(self) -> Dict[str, JsonValue]:
        fields: Dict[str, JsonValue] = {name: ["x"] for name in self.LISTS}
        fields["headings"] = {"PLAN.md": ["## Files modified"]}
        return fields

    def test_defaults(self) -> None:
        rules = FolderRules.model_validate({**self.valid(), "handover_files": None, "headings": None})
        assert (rules.handover_files, rules.headings, rules.squash_permit_minutes) == ([], {}, 30)

    def test_full_valid_construction(self) -> None:
        rules = FolderRules.load(self.CONF)
        assert "PROGRESS.md" in rules.required_files
        assert rules.handover_files == ["RELEASE-NOTE.md"]
        assert "## Stage validation" in rules.headings["PROGRESS.md"]
        assert rules.stage_icons == ["💻", "🟦", "🟪"]
        assert ".claude/skills/*/src/" in rules.production_paths
        assert rules.marker_files == ["__init__.py"]
        assert {"include", "message=", "pathspec-from-file=", "no-verify"} <= set(rules.commit_options)
        assert rules.squash_permit_minutes == 30
        assert rules.guard_state_folders == [
            "~/.local/state/claude-harness/squash-permits",
            "~/.local/state/ai-test-cost",
        ]

    @pytest.mark.parametrize(
        "name", ["handover_files", "headings", "marker_files", "commit_options", "guard_state_folders"]
    )
    def test_none_becomes_the_default(self, name: str) -> None:
        rules = FolderRules.model_validate({**self.valid(), name: None})
        assert not getattr(rules, name)

    def test_no_permit_lifetime_becomes_thirty_minutes(self) -> None:
        assert FolderRules.model_validate({**self.valid(), "squash_permit_minutes": None}).squash_permit_minutes == 30

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("required_files", "PLAN.md", SEFolderRulesInvalidList),
            ("status_icons", ["✅", ""], SEFolderRulesInvalidList),
            ("run_steps", [3], SEFolderRulesInvalidList),
            ("commit_options", ["include", " "], SEFolderRulesInvalidList),
            ("squash_permit_minutes", 0, SEFolderRulesInvalidMinutes),
            ("squash_permit_minutes", True, SEFolderRulesInvalidMinutes),
            ("squash_permit_minutes", "30", SEFolderRulesInvalidMinutes),
            ("squash_permit_minutes", 241, SEFolderRulesInvalidMinutes),
            ("headings", ["## Status"], SEFolderRulesInvalidHeadings),
            ("headings", {"PLAN.md": "## Files modified"}, SEFolderRulesInvalidHeadings),
            ("headings", {"PLAN.md": [""]}, SEFolderRulesInvalidHeadings),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            FolderRules.model_validate({**self.valid(), name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            FolderRules.model_validate({**self.valid(), "other": []})

    def test_round_trip(self) -> None:
        rules = FolderRules.load(self.CONF)
        assert FolderRules.model_validate(rules.model_dump()) == rules

    def test_a_missing_file_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SEFolderRulesUnreadable):
            FolderRules.load(tmp_path / "none.yaml")
