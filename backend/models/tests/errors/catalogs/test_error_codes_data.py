from __future__ import annotations

import re
from pathlib import Path
from typing import ClassVar

import pytest
from erp_models.errors.catalogs.error_catalog import ErrorCatalog
from erp_models.exceptions import SEError, SEException, SEInvalidModelException


class TestErrorCodesData:
    PATH: ClassVar[Path] = Path(__file__).resolve().parents[3] / "conf" / "catalogs" / "error_codes.yaml"
    KEY_PATTERN: ClassVar[str] = r"^[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)+$"

    @pytest.fixture
    def catalog(self) -> ErrorCatalog:
        return ErrorCatalog.load(self.PATH)

    def test_the_file_loads(self, catalog: ErrorCatalog) -> None:
        assert catalog.codes

    def test_every_code_has_a_title_a_why_an_action_and_a_reference(self, catalog: ErrorCatalog) -> None:
        for code in catalog.codes:
            entry = catalog.resolve(code)
            assert entry.title.strip(), code
            assert entry.why.strip(), code
            assert entry.action.strip(), code
            assert entry.reference.strip(), code

    @pytest.mark.parametrize("base", [SEException, SEError, SEInvalidModelException])
    def test_the_code_of_each_base_resolves(self, catalog: ErrorCatalog, base: type[SEException]) -> None:
        assert catalog.resolve(base.CODE).reference

    def test_the_d122_sample_code_is_present(self, catalog: ErrorCatalog) -> None:
        assert catalog.resolve("SITE-CLOSE-01").reference == "SITE-CLOSE-01"

    def test_every_message_key_is_a_lower_case_dotted_key(self, catalog: ErrorCatalog) -> None:
        for code in catalog.codes:
            entry = catalog.resolve(code)
            for key in (entry.title, entry.why, entry.action):
                assert re.match(self.KEY_PATTERN, key), f"{code}: {key}"

    @pytest.mark.parametrize("word", ["secret", "password", "passwd", "token", "credential", "private", "api_key"])
    def test_no_key_or_reference_holds_a_secret_word(self, catalog: ErrorCatalog, word: str) -> None:
        for code in catalog.codes:
            entry = catalog.resolve(code)
            for text in (entry.title, entry.why, entry.action, entry.reference):
                assert word not in text.lower(), f"{code}: {text}"

    def test_the_file_holds_no_placeholder(self) -> None:
        assert "{" not in self.PATH.read_text(encoding="utf-8")
