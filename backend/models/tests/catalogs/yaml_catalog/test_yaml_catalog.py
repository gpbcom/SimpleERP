from __future__ import annotations

from pathlib import Path
from typing import Type

import pytest
import yaml
from erp_models.catalogs.exceptions import SEInvalidYamlCatalogException, SEYamlCatalogUnreadable
from erp_models.catalogs.yaml_catalog import YamlCatalog
from pydantic import JsonValue, ValidationError, create_model

from tests.catalogs.yaml_catalog.sample_catalog import SampleCatalog
from tests.catalogs.yaml_catalog.se_sample_catalog_invalid_names import SESampleCatalogInvalidNames
from tests.catalogs.yaml_catalog.se_sample_catalog_unreadable import SESampleCatalogUnreadable


class TestYamlCatalog:
    def write(self, tmp_path: Path, content: str) -> Path:
        path = tmp_path / "catalog.yaml"
        path.write_text(content, encoding="utf-8")
        return path

    def test_defaults(self) -> None:
        assert SampleCatalog().names == []

    def test_full_valid_construction(self) -> None:
        assert SampleCatalog(names=["Café", "Tea"]).names == ["Café", "Tea"]

    def test_none_becomes_the_default(self) -> None:
        assert SampleCatalog(names=None).names == []

    @pytest.mark.parametrize(
        ("value", "error"),
        [
            ("Café", SESampleCatalogInvalidNames),
            ({"a": 1}, SESampleCatalogInvalidNames),
            ([1], SESampleCatalogInvalidNames),
            ([True], SESampleCatalogInvalidNames),
            ([""], SESampleCatalogInvalidNames),
            (["   "], SESampleCatalogInvalidNames),
        ],
    )
    def test_rejects_bad_values(self, value: JsonValue, error: Type[Exception]) -> None:
        with pytest.raises(error):
            SampleCatalog(names=value)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            SampleCatalog.model_validate({"unknown": 1})

    def test_round_trip(self) -> None:
        catalog = SampleCatalog(names=["Café", "Tea"])
        assert SampleCatalog.model_validate(catalog.model_dump()) == catalog

    def test_names_are_stripped(self) -> None:
        assert SampleCatalog(names=["  Café "]).names == ["Café"]

    def test_a_valid_file_loads_into_a_frozen_catalog(self, tmp_path: Path) -> None:
        catalog = SampleCatalog.load(self.write(tmp_path, "names:\n  - Café\n  - Tea\n"))
        assert isinstance(catalog, SampleCatalog)
        assert catalog.names == ["Café", "Tea"]
        with pytest.raises(ValidationError):
            catalog.names = []

    def test_a_missing_file_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SESampleCatalogUnreadable) as caught:
            SampleCatalog.load(tmp_path / "missing.yaml")
        assert isinstance(caught.value.__cause__, OSError)

    def test_invalid_yaml_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SESampleCatalogUnreadable) as caught:
            SampleCatalog.load(self.write(tmp_path, "names: [unclosed\n"))
        assert isinstance(caught.value.__cause__, yaml.YAMLError)

    @pytest.mark.parametrize("content", ["", "- a\n- b\n", "just text\n"])
    def test_a_file_that_is_not_a_mapping_is_unreadable(self, tmp_path: Path, content: str) -> None:
        with pytest.raises(SESampleCatalogUnreadable):
            SampleCatalog.load(self.write(tmp_path, content))

    def test_an_unknown_key_in_the_file_is_refused(self, tmp_path: Path) -> None:
        with pytest.raises(ValidationError):
            SampleCatalog.load(self.write(tmp_path, "unknown: 1\n"))

    @pytest.mark.parametrize("content", ["names: Café\n", "names:\n  - 1\n", 'names:\n  - ""\n'])
    def test_bad_names_in_the_file_raise_the_field_exception(self, tmp_path: Path, content: str) -> None:
        with pytest.raises(SESampleCatalogInvalidNames):
            SampleCatalog.load(self.write(tmp_path, content))

    def test_a_catalog_with_the_base_default_raises_the_base_exception(self, tmp_path: Path) -> None:
        plain = create_model("PlainCatalog", __base__=YamlCatalog)
        with pytest.raises(SEYamlCatalogUnreadable):
            plain.load(tmp_path / "missing.yaml")

    def test_the_base_unreadable_exception_is_the_default(self) -> None:
        assert YamlCatalog.UNREADABLE is SEYamlCatalogUnreadable

    def test_the_exceptions_hierarchy(self) -> None:
        assert issubclass(SEYamlCatalogUnreadable, SEInvalidYamlCatalogException)
        assert not issubclass(SEInvalidYamlCatalogException, ValueError)
        assert not issubclass(SEYamlCatalogUnreadable, ValueError)
