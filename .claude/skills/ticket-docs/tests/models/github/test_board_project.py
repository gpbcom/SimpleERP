from __future__ import annotations

from typing import Dict

import pytest
from pydantic import JsonValue

from ticket_docs.models.github.board_field import BoardField
from ticket_docs.models.github.board_project import BoardProject
from ticket_docs.models.github.exceptions import (
    SEBoardProjectInvalidFields,
    SEBoardProjectInvalidNumber,
    SEBoardProjectInvalidText,
)


class TestBoardProject:
    VALID: Dict[str, JsonValue] = {
        "number": 6,
        "url": "https://github.com/users/gpbcom/projects/6",
        "id": "PVT_kwHOBZDE-c4Bq9-t",
        "fields": {"status": {"id": "PVTSSF_1", "options": {"Done": "436b8e2a"}}},
    }

    def test_defaults(self) -> None:
        assert BoardProject.model_validate({**self.VALID, "fields": None}).fields == {}

    def test_full_valid_construction(self) -> None:
        project = BoardProject.model_validate(self.VALID)
        assert project.fields["status"] == BoardField(id="PVTSSF_1", options={"Done": "436b8e2a"})

    @pytest.mark.parametrize("name", ["fields"])
    def test_none_becomes_the_default(self, name: str) -> None:
        assert getattr(BoardProject.model_validate({**self.VALID, name: None}), name) == {}

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("number", 0, SEBoardProjectInvalidNumber),
            ("number", True, SEBoardProjectInvalidNumber),
            ("url", "", SEBoardProjectInvalidText),
            ("id", None, SEBoardProjectInvalidText),
            ("fields", ["status"], SEBoardProjectInvalidFields),
            ("fields", {"": {"id": "x"}}, SEBoardProjectInvalidFields),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            BoardProject.model_validate({**self.VALID, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            BoardProject.model_validate({**self.VALID, "other": 1})

    def test_round_trip(self) -> None:
        project = BoardProject.model_validate(self.VALID)
        assert BoardProject.model_validate(project.model_dump()) == project
