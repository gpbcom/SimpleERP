from __future__ import annotations

from pathlib import Path
from typing import Optional

import pytest
from erp_models.catalogs.yaml_catalog import YamlCatalog
from erp_testing.models.synthetic.exceptions import (
    SEInvalidSyntheticCatalogException,
    SESyntheticCatalogInvalidCompanyWords,
    SESyntheticCatalogInvalidEmailDomain,
    SESyntheticCatalogInvalidFirstNames,
    SESyntheticCatalogInvalidLastNames,
    SESyntheticCatalogInvalidSectors,
    SESyntheticCatalogUnreadable,
)
from erp_testing.models.synthetic.synthetic_catalog import SyntheticCatalog
from pydantic import JsonValue, ValidationError


class TestSyntheticCatalog:
    def valid(self) -> dict[str, JsonValue]:
        return {
            "sectors": ["sc01", "sc02"],
            "company_words": ["Acme", "Globex"],
            "first_names": ["Ada", "Grace"],
            "last_names": ["Martin", "Keller"],
            "email_domain": "example.com",
        }

    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            SyntheticCatalog()  # type: ignore[call-arg]

    def test_full_valid_construction(self) -> None:
        values = self.valid()
        values["company_words"] = ["  Acme  ", "Globex"]

        catalog = SyntheticCatalog(**values)  # type: ignore[arg-type]

        assert catalog.sectors == ["sc01", "sc02"]
        assert catalog.company_words == ["Acme", "Globex"]
        assert catalog.first_names == ["Ada", "Grace"]
        assert catalog.last_names == ["Martin", "Keller"]
        assert catalog.email_domain == "example.com"
        assert isinstance(catalog, YamlCatalog)
        assert SyntheticCatalog.UNREADABLE is SESyntheticCatalogUnreadable

    def test_the_reserved_domains_follow_the_rfcs(self) -> None:
        assert SyntheticCatalog.RESERVED_DOMAINS == ("example.com", "example.net", "example.org")
        assert SyntheticCatalog.RESERVED_SUFFIXES == (".test", ".example", ".invalid", ".localhost")

    def test_the_default_path_is_the_shipped_catalogue(self) -> None:
        assert SyntheticCatalog.DEFAULT_PATH.name == "synthetic.yaml"
        assert SyntheticCatalog.DEFAULT_PATH.parent.parts[-3:] == ("testing", "conf", "catalogs")

    @pytest.mark.parametrize(
        ("name", "error"),
        [
            ("sectors", SESyntheticCatalogInvalidSectors),
            ("company_words", SESyntheticCatalogInvalidCompanyWords),
            ("first_names", SESyntheticCatalogInvalidFirstNames),
            ("last_names", SESyntheticCatalogInvalidLastNames),
            ("email_domain", SESyntheticCatalogInvalidEmailDomain),
        ],
    )
    def test_none_becomes_the_default(self, name: str, error: type[Exception]) -> None:
        values = self.valid()
        values[name] = None

        with pytest.raises(error):
            SyntheticCatalog(**values)  # type: ignore[arg-type]

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("sectors", [], SESyntheticCatalogInvalidSectors),
            ("sectors", "sc01", SESyntheticCatalogInvalidSectors),
            ("sectors", ["sc01", "sc01"], SESyntheticCatalogInvalidSectors),
            ("sectors", ["sc1"], SESyntheticCatalogInvalidSectors),
            ("sectors", ["SC01"], SESyntheticCatalogInvalidSectors),
            ("sectors", ["sc001"], SESyntheticCatalogInvalidSectors),
            ("sectors", [1], SESyntheticCatalogInvalidSectors),
            ("company_words", [], SESyntheticCatalogInvalidCompanyWords),
            ("company_words", "Acme", SESyntheticCatalogInvalidCompanyWords),
            ("company_words", [""], SESyntheticCatalogInvalidCompanyWords),
            ("company_words", ["  "], SESyntheticCatalogInvalidCompanyWords),
            ("company_words", [1], SESyntheticCatalogInvalidCompanyWords),
            ("first_names", [], SESyntheticCatalogInvalidFirstNames),
            ("first_names", "Ada", SESyntheticCatalogInvalidFirstNames),
            ("first_names", [""], SESyntheticCatalogInvalidFirstNames),
            ("first_names", [True], SESyntheticCatalogInvalidFirstNames),
            ("last_names", [], SESyntheticCatalogInvalidLastNames),
            ("last_names", "Martin", SESyntheticCatalogInvalidLastNames),
            ("last_names", ["  "], SESyntheticCatalogInvalidLastNames),
            ("last_names", [None], SESyntheticCatalogInvalidLastNames),
            ("email_domain", "", SESyntheticCatalogInvalidEmailDomain),
            ("email_domain", "gmail.com", SESyntheticCatalogInvalidEmailDomain),
            ("email_domain", "example.com.evil.io", SESyntheticCatalogInvalidEmailDomain),
            ("email_domain", 12, SESyntheticCatalogInvalidEmailDomain),
            ("email_domain", True, SESyntheticCatalogInvalidEmailDomain),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        values = self.valid()
        values[name] = value

        with pytest.raises(error) as raised:
            SyntheticCatalog(**values)  # type: ignore[arg-type]

        assert isinstance(raised.value, SEInvalidSyntheticCatalogException)

    @pytest.mark.parametrize("domain", ["example.com", "example.net", "example.org", "mail.test", "erp.example"])
    def test_a_reserved_email_domain_is_accepted(self, domain: str) -> None:
        values = self.valid()
        values["email_domain"] = domain

        assert SyntheticCatalog(**values).email_domain == domain  # type: ignore[arg-type]

    def test_rejects_unknown_keys(self) -> None:
        values = self.valid()
        values["other"] = "x"

        with pytest.raises(ValidationError):
            SyntheticCatalog(**values)  # type: ignore[arg-type]

    def test_a_catalogue_loads_from_a_yaml_file(self, tmp_path: Path) -> None:
        path = tmp_path / "synthetic.yaml"
        path.write_text(
            "sectors: [sc01, sc02]\n"
            "company_words: [Acme, Globex]\n"
            "first_names: [Ada, Grace]\n"
            "last_names: [Martin, Keller]\n"
            "email_domain: example.org\n",
            encoding="utf-8",
        )

        catalog = SyntheticCatalog.load(path)

        assert catalog.sectors == ["sc01", "sc02"]
        assert catalog.email_domain == "example.org"

    @pytest.mark.parametrize("content", [None, "sectors: [unclosed\n", "- a\n- b\n", "plain text\n"])
    def test_an_unreadable_file_raises_the_catalogue_exception(self, tmp_path: Path, content: Optional[str]) -> None:
        path = tmp_path / "synthetic.yaml"
        if content is not None:
            path.write_text(content, encoding="utf-8")

        with pytest.raises(SESyntheticCatalogUnreadable):
            SyntheticCatalog.load(path)

    def test_round_trip(self) -> None:
        catalog = SyntheticCatalog(**self.valid())  # type: ignore[arg-type]

        assert catalog.model_dump(mode="json") == self.valid()
        assert SyntheticCatalog.model_validate(catalog.model_dump(mode="json")) == catalog
        assert SyntheticCatalog.model_validate_json(catalog.model_dump_json()) == catalog
