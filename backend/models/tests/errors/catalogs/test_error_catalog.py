from __future__ import annotations

from pathlib import Path
from typing import Dict, Type

import pytest
from erp_models.errors.catalogs.error_catalog import ErrorCatalog
from erp_models.errors.catalogs.exceptions import (
    SEErrorCatalogInvalidCodes,
    SEErrorCatalogUnknownCode,
    SEErrorCatalogUnreadable,
    SEInvalidErrorCatalogException,
)
from erp_models.errors.entries.error_code_entry import ErrorCodeEntry
from erp_models.errors.entries.exceptions import SEErrorCodeEntryInvalidTitle
from erp_models.exceptions import SEInvalidModelException
from pydantic import JsonValue, ValidationError


class TestErrorCatalog:
    CODE = "SITE-CLOSE-01"
    OTHER_CODE = "SITE-OPEN-02"
    YAML = (
        "codes:\n"
        "  SITE-CLOSE-01:\n"
        "    title: errors.site_close_01.title\n"
        "    why: errors.site_close_01.why\n"
        "    action: errors.site_close_01.action\n"
        "    reference: SITE-CLOSE-01\n"
    )
    BAD_TITLE = {"title": "", "why": "w", "action": "a", "reference": "SITE-CLOSE-01"}

    def entry(self, code: str) -> Dict[str, str]:
        key = code.lower().replace("-", "_")
        return {
            "title": f"errors.{key}.title",
            "why": f"errors.{key}.why",
            "action": f"errors.{key}.action",
            "reference": code,
        }

    def valid(self) -> Dict[str, JsonValue]:
        return {self.CODE: self.entry(self.CODE), self.OTHER_CODE: self.entry(self.OTHER_CODE)}

    def write(self, tmp_path: Path, content: str) -> Path:
        path = tmp_path / "errors.yaml"
        path.write_text(content, encoding="utf-8")
        return path

    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            ErrorCatalog.model_validate({})

    def test_full_valid_construction(self) -> None:
        catalog = ErrorCatalog(codes=self.valid())
        assert set(catalog.codes) == {self.CODE, self.OTHER_CODE}
        assert isinstance(catalog.codes[self.CODE], ErrorCodeEntry)

    def test_none_is_refused_because_codes_has_no_default(self) -> None:
        with pytest.raises(SEErrorCatalogInvalidCodes):
            ErrorCatalog(codes=None)

    @pytest.mark.parametrize(
        ("value", "error"),
        [
            ({}, SEErrorCatalogInvalidCodes),
            ([], SEErrorCatalogInvalidCodes),
            ("SITE-CLOSE-01", SEErrorCatalogInvalidCodes),
            ({"site-close-01": {}}, SEErrorCatalogInvalidCodes),
            ({"SITE-CLOSE": {}}, SEErrorCatalogInvalidCodes),
            ({"SITE-CLOSE-1": {}}, SEErrorCatalogInvalidCodes),
            ({"SITE-CLOSE-01": BAD_TITLE}, SEErrorCodeEntryInvalidTitle),
        ],
    )
    def test_rejects_bad_values(self, value: JsonValue, error: Type[Exception]) -> None:
        with pytest.raises(error):
            ErrorCatalog(codes=value)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            ErrorCatalog.model_validate({"codes": self.valid(), "unknown": 1})

    def test_round_trip(self) -> None:
        catalog = ErrorCatalog(codes=self.valid())
        assert ErrorCatalog.model_validate(catalog.model_dump()) == catalog

    def test_the_catalog_is_frozen(self) -> None:
        catalog = ErrorCatalog(codes=self.valid())
        with pytest.raises(ValidationError):
            catalog.codes = {}

    @pytest.mark.parametrize("error", [SEErrorCatalogInvalidCodes, SEErrorCatalogUnknownCode, SEErrorCatalogUnreadable])
    def test_every_catalog_exception_is_an_invalid_model_exception(self, error: Type[Exception]) -> None:
        assert issubclass(error, SEInvalidErrorCatalogException)
        assert issubclass(error, SEInvalidModelException)

    def test_a_known_code_resolves_to_its_four_values(self) -> None:
        entry = ErrorCatalog(codes=self.valid()).resolve(self.CODE)
        assert entry.title == "errors.site_close_01.title"
        assert entry.why == "errors.site_close_01.why"
        assert entry.action == "errors.site_close_01.action"
        assert entry.reference == self.CODE

    @pytest.mark.parametrize("code", ["MISSING-CODE-01", "", "site-close-01"])
    def test_an_unknown_code_is_refused(self, code: str) -> None:
        with pytest.raises(SEErrorCatalogUnknownCode):
            ErrorCatalog(codes=self.valid()).resolve(code)

    def test_a_valid_file_loads(self, tmp_path: Path) -> None:
        catalog = ErrorCatalog.load(self.write(tmp_path, self.YAML))
        assert catalog.resolve(self.CODE).reference == self.CODE

    def test_the_unreadable_exception_is_the_catalog_one(self) -> None:
        assert ErrorCatalog.UNREADABLE is SEErrorCatalogUnreadable

    @pytest.mark.parametrize("content", ["codes: [unclosed\n", "- a\n- b\n", "just text\n"])
    def test_a_malformed_file_is_unreadable(self, tmp_path: Path, content: str) -> None:
        with pytest.raises(SEErrorCatalogUnreadable):
            ErrorCatalog.load(self.write(tmp_path, content))

    def test_a_missing_file_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SEErrorCatalogUnreadable):
            ErrorCatalog.load(tmp_path / "absent.yaml")
