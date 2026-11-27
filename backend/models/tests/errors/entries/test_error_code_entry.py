from __future__ import annotations

from typing import Dict

import pytest
from erp_models.errors.entries.error_code_entry import ErrorCodeEntry
from erp_models.errors.entries.exceptions import (
    SEErrorCodeEntryInvalidAction,
    SEErrorCodeEntryInvalidReference,
    SEErrorCodeEntryInvalidTitle,
    SEErrorCodeEntryInvalidWhy,
    SEInvalidErrorCodeEntryException,
)
from erp_models.exceptions import SEInvalidModelException
from pydantic import JsonValue, ValidationError


class TestErrorCodeEntry:
    VALID: Dict[str, str] = {
        "title": "errors.site_close_01.title",
        "why": "errors.site_close_01.why",
        "action": "errors.site_close_01.action",
        "reference": "SITE-CLOSE-01",
    }

    ERRORS: Dict[str, type[Exception]] = {
        "title": SEErrorCodeEntryInvalidTitle,
        "why": SEErrorCodeEntryInvalidWhy,
        "action": SEErrorCodeEntryInvalidAction,
        "reference": SEErrorCodeEntryInvalidReference,
    }

    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            ErrorCodeEntry()  # type: ignore[call-arg]
        for name in self.VALID:
            partial = {key: value for key, value in self.VALID.items() if key != name}
            with pytest.raises(ValidationError):
                ErrorCodeEntry(**partial)

    def test_full_valid_construction(self) -> None:
        entry = ErrorCodeEntry(
            title="  errors.site_close_01.title  ",
            why=" errors.site_close_01.why ",
            action="errors.site_close_01.action ",
            reference="  SITE-CLOSE-01 ",
        )

        assert entry.title == "errors.site_close_01.title"
        assert entry.why == "errors.site_close_01.why"
        assert entry.action == "errors.site_close_01.action"
        assert entry.reference == "SITE-CLOSE-01"

    @pytest.mark.parametrize("name", ["title", "why", "action", "reference"])
    def test_none_becomes_the_default(self, name: str) -> None:
        values: Dict[str, JsonValue] = {**self.VALID, name: None}

        with pytest.raises(self.ERRORS[name]):
            ErrorCodeEntry(**values)  # type: ignore[arg-type]

    @pytest.mark.parametrize("name", ["title", "why", "action"])
    @pytest.mark.parametrize(
        "value",
        [
            "",
            "   ",
            12,
            True,
            ["errors.a.title"],
            "Errors.site_close_01.title",
            "errors.Site_close.title",
            "errors site.title",
            "errors.site close.title",
            "title",
            "errors.",
            ".errors.title",
            "1errors.title",
            "Close the site first.",
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue) -> None:
        values: Dict[str, JsonValue] = {**self.VALID, name: value}

        with pytest.raises(self.ERRORS[name]):
            ErrorCodeEntry(**values)  # type: ignore[arg-type]

    @pytest.mark.parametrize(
        "value",
        [
            "",
            "   ",
            12,
            True,
            ["SITE-CLOSE-01"],
            "SITE-CLOSE",
            "SITE-CLOSE-1",
            "SITE-CLOSE-001",
            "site-close-01",
            "Site-Close-01",
            "SITE CLOSE 01",
            "-SITE-01",
            "SITE--01",
            "01",
            "SITE-CLOSE-01-",
        ],
    )
    def test_rejects_bad_references(self, value: JsonValue) -> None:
        values: Dict[str, JsonValue] = {**self.VALID, "reference": value}

        with pytest.raises(SEErrorCodeEntryInvalidReference):
            ErrorCodeEntry(**values)  # type: ignore[arg-type]

    @pytest.mark.parametrize("reference", ["SITE-01", "SITE-CLOSE-01", "A1-B2-C3-99"])
    def test_accepts_good_references(self, reference: str) -> None:
        entry = ErrorCodeEntry(**{**self.VALID, "reference": reference})

        assert entry.reference == reference

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            ErrorCodeEntry(**self.VALID, other="x")  # type: ignore[call-arg]

    def test_round_trip(self) -> None:
        entry = ErrorCodeEntry(**self.VALID)

        assert entry.model_dump() == self.VALID
        assert ErrorCodeEntry.model_validate(entry.model_dump()) == entry
        assert ErrorCodeEntry.model_validate_json(entry.model_dump_json()) == entry

    def test_the_entry_is_frozen(self) -> None:
        entry = ErrorCodeEntry(**self.VALID)

        with pytest.raises(ValidationError):
            entry.title = "errors.other.title"

    @pytest.mark.parametrize("error", [*ERRORS.values()])
    def test_every_field_exception_is_a_model_exception(self, error: type[Exception]) -> None:
        assert issubclass(error, SEInvalidErrorCodeEntryException)
        assert issubclass(SEInvalidErrorCodeEntryException, SEInvalidModelException)
