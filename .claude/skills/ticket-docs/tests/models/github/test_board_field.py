from __future__ import annotations

import pytest
from pydantic import JsonValue

from ticket_docs.models.github.board_field import BoardField
from ticket_docs.models.github.exceptions import SEBoardFieldInvalidId, SEBoardFieldInvalidOptions


class TestBoardField:
    def test_defaults(self) -> None:
        assert BoardField(id="PVTSSF_1").options == {}

    def test_full_valid_construction(self) -> None:
        field = BoardField(id=" PVTSSF_1 ", options={"In progress": "63440315"})
        assert (field.id, field.options) == ("PVTSSF_1", {"In progress": "63440315"})

    @pytest.mark.parametrize("name", ["options"])
    def test_none_becomes_the_default(self, name: str) -> None:
        assert getattr(BoardField.model_validate({"id": "x", name: None}), name) == {}

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("id", "", SEBoardFieldInvalidId),
            ("id", 3, SEBoardFieldInvalidId),
            ("options", ["Done"], SEBoardFieldInvalidOptions),
            ("options", {"Done": 3}, SEBoardFieldInvalidOptions),
            ("options", {"": "x"}, SEBoardFieldInvalidOptions),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            BoardField.model_validate({"id": "x", name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            BoardField.model_validate({"id": "x", "other": 1})

    def test_round_trip(self) -> None:
        field = BoardField(id="x", options={"Done": "1"})
        assert BoardField.model_validate(field.model_dump()) == field
