from __future__ import annotations

from pathlib import Path
from typing import ClassVar, List

import pytest

from harness_core.models.catalogs.exceptions import SEYamlCatalogUnreadable
from harness_core.models.catalogs.yaml_catalog import YamlCatalog


class Colours(YamlCatalog):
    """A small catalogue for the tests."""

    UNREADABLE: ClassVar[type[Exception]] = SEYamlCatalogUnreadable

    names: List[str]


class TestYamlCatalog:
    def test_load_validates_the_file(self, tmp_path: Path) -> None:
        path = tmp_path / "colours.yaml"
        path.write_text("names:\n  - red\n  - blue\n", encoding="utf-8")
        assert Colours.load(path).names == ["red", "blue"]

    @pytest.mark.parametrize("text", [None, "names: [unclosed\n"])
    def test_a_missing_or_broken_file_is_unreadable(self, tmp_path: Path, text: str | None) -> None:
        path = tmp_path / "colours.yaml"
        if text is not None:
            path.write_text(text, encoding="utf-8")
        with pytest.raises(SEYamlCatalogUnreadable):
            Colours.load(path)
