from __future__ import annotations

import pytest
from pydantic import JsonValue

from harness_core.models.git.change_status import ChangeStatus
from harness_core.models.git.exceptions import SEFileChangeInvalidPath, SEFileChangeInvalidStatus
from harness_core.models.git.file_change import FileChange


class TestFileChange:
    def test_full_valid_construction(self) -> None:
        change = FileChange(path=" src/a.py ", status="A")
        assert change.path == "src/a.py"
        assert change.status is ChangeStatus.ADDED

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("path", "", SEFileChangeInvalidPath),
            ("path", 3, SEFileChangeInvalidPath),
            ("status", "Z", SEFileChangeInvalidStatus),
            ("status", None, SEFileChangeInvalidStatus),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        fields: dict[str, JsonValue] = {"path": "a.py", "status": "M"}
        fields[name] = value
        with pytest.raises(error):
            FileChange.model_validate(fields)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            FileChange.model_validate({"path": "a.py", "status": "M", "other": 1})

    def test_an_untracked_file_has_its_own_status(self) -> None:
        assert FileChange(path="new.py", status="??").status is ChangeStatus.UNTRACKED

    def test_renames_and_copies_keep_their_letter_only(self) -> None:
        assert FileChange(path="b.py", status="R100").status is ChangeStatus.RENAMED

    def test_round_trip(self) -> None:
        change = FileChange(path="a.py", status="D")
        assert FileChange.model_validate(change.model_dump()) == change
