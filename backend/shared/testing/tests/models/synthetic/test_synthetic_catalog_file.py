from __future__ import annotations

from pathlib import Path
from typing import ClassVar

import pytest
from erp_testing.models.synthetic.exceptions import SESyntheticCatalogUnreadable
from erp_testing.models.synthetic.synthetic_catalog import SyntheticCatalog


class TestSyntheticCatalogFile:
    SECTORS_DIR: ClassVar[Path] = Path(__file__).resolve().parents[6] / "docs" / "specs" / "08-sectors"

    def test_the_shipped_catalogue_loads(self) -> None:
        catalog = SyntheticCatalog.load(SyntheticCatalog.DEFAULT_PATH)

        assert catalog.company_words
        assert catalog.first_names
        assert catalog.last_names

    def test_the_sectors_are_exactly_the_sector_folders_of_the_specifications(self) -> None:
        folders = self.SECTORS_DIR.glob("sc[0-9][0-9]-*")
        codes = sorted(folder.name.split("-", 1)[0] for folder in folders if folder.is_dir())

        catalog = SyntheticCatalog.load(SyntheticCatalog.DEFAULT_PATH)

        assert len(codes) == 20
        assert sorted(catalog.sectors) == codes

    def test_the_email_domain_is_reserved(self) -> None:
        domain = SyntheticCatalog.load(SyntheticCatalog.DEFAULT_PATH).email_domain

        assert domain in SyntheticCatalog.RESERVED_DOMAINS or domain.endswith(SyntheticCatalog.RESERVED_SUFFIXES)

    @pytest.mark.parametrize("name", ["missing.yaml", "directory"])
    def test_an_unreadable_file_raises_the_catalogue_exception(self, tmp_path: Path, name: str) -> None:
        path = tmp_path / name
        if name == "directory":
            path.mkdir()

        with pytest.raises(SESyntheticCatalogUnreadable):
            SyntheticCatalog.load(path)

    def test_a_malformed_file_raises_the_catalogue_exception(self, tmp_path: Path) -> None:
        path = tmp_path / "synthetic.yaml"
        path.write_text("sectors: [unclosed\n", encoding="utf-8")

        with pytest.raises(SESyntheticCatalogUnreadable):
            SyntheticCatalog.load(path)
