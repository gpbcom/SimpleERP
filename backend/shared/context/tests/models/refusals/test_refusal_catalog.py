from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List

import pytest
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.refusals.exceptions import SERefusalCatalogInvalidEntries, SERefusalCatalogUnreadable
from erp_context.models.refusals.refusal_catalog import RefusalCatalog
from erp_context.models.refusals.refusal_code import RefusalCode
from erp_models.catalogs.yaml_catalog import YamlCatalog
from erp_models.exceptions import SEInvalidModelException
from pydantic import JsonValue, ValidationError


class TestRefusalCatalog:
    SHIPPED: Path = Path(__file__).resolve().parents[3] / "conf" / "catalogs" / "refusal_codes.yaml"
    KEY_PATTERN = r"[a-z0-9_.]+"
    CODE_PATTERN = r"[A-Z]+(-[A-Z]+)*-[0-9]{2}"
    STATUSES: Dict[RefusalReason, int] = {
        RefusalReason.NO_POLICY: 403,
        RefusalReason.POLICY_DENIED: 403,
        RefusalReason.OTHER_COMPANY: 403,
    }

    def entry(self, reason: RefusalReason, number: int, status: int = 403) -> Dict[str, JsonValue]:
        code = f"ACCESS-{reason.name.replace('_', '-')}-{number:02d}"
        key = code.lower().replace("-", "_")
        return {
            "reason": reason.value,
            "code": code,
            "status": status,
            "title_key": f"errors.{key}.title",
            "why_key": f"errors.{key}.why",
            "action_key": f"errors.{key}.action",
            "reference": code,
        }

    def entries(self) -> List[Dict[str, JsonValue]]:
        return [self.entry(reason, number) for number, reason in enumerate(RefusalReason, start=1)]

    def shipped(self) -> RefusalCatalog:
        return RefusalCatalog.load(self.SHIPPED)

    def write(self, tmp_path: Path, content: str) -> Path:
        path = tmp_path / "refusal_codes.yaml"
        path.write_text(content, encoding="utf-8")
        return path

    def test_it_is_a_yaml_catalog(self) -> None:
        assert issubclass(RefusalCatalog, YamlCatalog)
        assert RefusalCatalog.UNREADABLE is SERefusalCatalogUnreadable

    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            RefusalCatalog.model_validate({})

    def test_full_valid_construction(self) -> None:
        catalog = RefusalCatalog.model_validate({"entries": self.entries()})

        assert len(catalog.entries) == len(RefusalReason)
        assert all(isinstance(entry, RefusalCode) for entry in catalog.entries)

    def test_none_is_refused_because_entries_has_no_default(self) -> None:
        with pytest.raises(ValidationError):
            RefusalCatalog.model_validate({"entries": None})

    def test_a_catalog_that_misses_a_reason_is_refused(self) -> None:
        with pytest.raises(SERefusalCatalogInvalidEntries):
            RefusalCatalog.model_validate({"entries": self.entries()[:-1]})

    def test_an_empty_catalog_is_refused(self) -> None:
        with pytest.raises(SERefusalCatalogInvalidEntries):
            RefusalCatalog.model_validate({"entries": []})

    def test_a_catalog_that_holds_a_reason_twice_is_refused(self) -> None:
        entries = [*self.entries(), self.entry(RefusalReason.NO_USER, 9)]

        with pytest.raises(SERefusalCatalogInvalidEntries):
            RefusalCatalog.model_validate({"entries": entries})

    def test_a_catalog_that_repeats_a_code_is_refused(self) -> None:
        entries = self.entries()
        entries[-1] = {**self.entry(RefusalReason.OTHER_COMPANY, 5), "code": entries[0]["code"]}

        with pytest.raises(SERefusalCatalogInvalidEntries):
            RefusalCatalog.model_validate({"entries": entries})

    @pytest.mark.parametrize("value", ["text", 3, {"a": 1}, True])
    def test_a_non_list_is_refused(self, value: JsonValue) -> None:
        with pytest.raises(ValidationError):
            RefusalCatalog.model_validate({"entries": value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            RefusalCatalog.model_validate({"entries": self.entries(), "unknown": 1})

    def test_round_trip(self) -> None:
        catalog = RefusalCatalog.model_validate({"entries": self.entries()})

        assert RefusalCatalog.model_validate(catalog.model_dump()) == catalog

    def test_the_catalog_is_frozen(self) -> None:
        catalog = RefusalCatalog.model_validate({"entries": self.entries()})

        with pytest.raises(ValidationError):
            catalog.entries = []

    def test_the_catalog_exceptions_are_invalid_model_exceptions(self) -> None:
        assert issubclass(SERefusalCatalogInvalidEntries, SEInvalidModelException)
        assert issubclass(SERefusalCatalogUnreadable, SEInvalidModelException)

    @pytest.mark.parametrize("reason", list(RefusalReason))
    def test_code_for_returns_the_code_of_the_reason(self, reason: RefusalReason) -> None:
        catalog = RefusalCatalog.model_validate({"entries": self.entries()})

        assert catalog.code_for(reason).reason is reason

    @pytest.mark.parametrize("content", ["entries: [unclosed\n", "- a\n- b\n", "just text\n"])
    def test_a_malformed_file_is_unreadable(self, tmp_path: Path, content: str) -> None:
        with pytest.raises(SERefusalCatalogUnreadable):
            RefusalCatalog.load(self.write(tmp_path, content))

    def test_a_missing_file_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SERefusalCatalogUnreadable):
            RefusalCatalog.load(tmp_path / "absent.yaml")

    def test_the_shipped_catalog_loads(self) -> None:
        assert len(self.shipped().entries) == len(RefusalReason)

    @pytest.mark.parametrize("reason", list(RefusalReason))
    def test_every_reason_resolves_to_exactly_one_code(self, reason: RefusalReason) -> None:
        catalog = self.shipped()

        assert [entry for entry in catalog.entries if entry.reason is reason] == [catalog.code_for(reason)]

    def test_the_codes_of_the_shipped_catalog_are_distinct(self) -> None:
        codes = [entry.code for entry in self.shipped().entries]

        assert len(codes) == len(set(codes))

    @pytest.mark.parametrize("reason", [RefusalReason.NO_COMPANY, RefusalReason.NO_USER])
    def test_a_missing_context_is_a_client_error(self, reason: RefusalReason) -> None:
        assert 400 <= self.shipped().code_for(reason).status <= 499

    @pytest.mark.parametrize("reason", list(STATUSES))
    def test_a_policy_refusal_is_forbidden(self, reason: RefusalReason) -> None:
        assert self.shipped().code_for(reason).status == self.STATUSES[reason]

    @pytest.mark.parametrize("reason", list(RefusalReason))
    def test_the_shipped_entries_hold_only_keys_and_codes(self, reason: RefusalReason) -> None:
        entry = self.shipped().code_for(reason)

        for key in (entry.title_key, entry.why_key, entry.action_key):
            assert re.fullmatch(self.KEY_PATTERN, key)
        for code in (entry.code, entry.reference):
            assert re.fullmatch(self.CODE_PATTERN, code)
