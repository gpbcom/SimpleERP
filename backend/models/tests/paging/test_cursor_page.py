from __future__ import annotations

from typing import Dict, List, Optional

import pytest
from erp_models.paging.cursor_page import CursorPage
from erp_models.paging.exceptions import (
    SECursorPageInvalidItems,
    SECursorPageInvalidNextCursor,
    SEInvalidCursorPageException,
)
from pydantic import JsonValue, ValidationError


class TestCursorPage:
    def test_defaults(self) -> None:
        page = CursorPage[int]()

        assert page.items == []
        assert page.next_cursor is None
        assert page.has_more is False

    def test_full_valid_construction(self) -> None:
        page = CursorPage[int](items=[1, 2, 3], next_cursor="  abc123  ")

        assert page.items == [1, 2, 3]
        assert page.next_cursor == "abc123"
        assert page.has_more is True

    @pytest.mark.parametrize(
        ("name", "expected"),
        [("items", []), ("next_cursor", None)],
    )
    def test_none_becomes_the_default(self, name: str, expected: Optional[List[int]]) -> None:
        page = CursorPage[int].model_validate({name: None})

        assert getattr(page, name) == expected

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("items", "abc", SECursorPageInvalidItems),
            ("items", {"a": 1}, SECursorPageInvalidItems),
            ("items", 12, SECursorPageInvalidItems),
            ("next_cursor", "", SECursorPageInvalidNextCursor),
            ("next_cursor", "  ", SECursorPageInvalidNextCursor),
            ("next_cursor", 12, SECursorPageInvalidNextCursor),
            ("next_cursor", True, SECursorPageInvalidNextCursor),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            CursorPage[int].model_validate({name: value})

    @pytest.mark.parametrize(
        "error",
        [SECursorPageInvalidItems, SECursorPageInvalidNextCursor],
    )
    def test_the_exceptions_share_a_base_and_are_not_value_errors(self, error: type[Exception]) -> None:
        assert issubclass(error, SEInvalidCursorPageException)
        assert not issubclass(error, ValueError)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            CursorPage[int].model_validate({"items": [], "unknown": 1})

    def test_round_trip(self) -> None:
        page = CursorPage[int](items=[1, 2], next_cursor="abc")

        data: Dict[str, JsonValue] = page.model_dump(mode="json")

        assert data == {"items": [1, 2], "next_cursor": "abc"}
        assert CursorPage[int].model_validate(data) == page
        assert CursorPage[int].model_validate_json(page.model_dump_json()) == page

    def test_a_wrongly_typed_item_is_refused(self) -> None:
        with pytest.raises(ValidationError):
            CursorPage[int](items=["x"])  # type: ignore[list-item]

    def test_a_page_in_the_middle_of_a_list_has_a_next_cursor(self) -> None:
        page = CursorPage[int](items=[1, 2, 3], next_cursor="after-3")

        assert page.next_cursor == "after-3"
        assert page.has_more is True

    def test_the_last_page_has_no_next_cursor(self) -> None:
        page = CursorPage[int](items=[4, 5])

        assert page.next_cursor is None
        assert page.has_more is False

    def test_assignment_is_refused(self) -> None:
        page = CursorPage[int](items=[1])

        with pytest.raises(ValidationError):
            page.next_cursor = "other"  # type: ignore[misc]
