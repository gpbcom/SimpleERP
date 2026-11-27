from __future__ import annotations

import logging
from pathlib import Path
from typing import ClassVar, Optional

import pytest
from erp_country_rules.models.config.country_rules_config import CountryRulesConfig
from erp_country_rules.models.exceptions import SECountryPackNotFoundError, SECountryPackUnreadable
from erp_country_rules.storage.packs.country_pack_repository import CountryPackRepository


class TestCountryPackRepository:
    PACK_TEXT: ClassVar[str] = (
        'country: ZZ\nversion: "2026.11"\n'
        "rules:\n"
        "  - rule: standard-rate\n"
        "    versions:\n"
        '      - {valid_from: "2024-01-01", valid_to: "2025-12-31", value: "19.6"}\n'
        '      - {valid_from: "2026-01-01", value: "20"}\n'
    )

    def write_pack(self, packs_dir: Path, text: str = PACK_TEXT) -> Path:
        path = packs_dir / "zz" / "rules.yaml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def repository(self, packs_dir: Path, logger: Optional[logging.Logger] = None) -> CountryPackRepository:
        return CountryPackRepository(CountryRulesConfig(packs_dir=packs_dir), logger)

    @pytest.mark.parametrize("country", ["ZZ", "zz", " ZZ ", "Zz"])
    def test_a_country_is_found_whatever_its_case_and_spaces(self, tmp_path: Path, country: str) -> None:
        self.write_pack(tmp_path)
        pack = self.repository(tmp_path).get(country)
        assert pack.country == "ZZ"
        assert pack.version == "2026.11"
        assert len(pack.rules) == 1
        assert len(pack.rules[0].versions) == 2

    def test_the_second_get_returns_the_same_object(self, tmp_path: Path) -> None:
        self.write_pack(tmp_path)
        repository = self.repository(tmp_path)
        assert repository.get("ZZ") is repository.get("zz")

    def test_the_second_get_does_not_read_the_file_again(self, tmp_path: Path) -> None:
        path = self.write_pack(tmp_path)
        repository = self.repository(tmp_path)
        first = repository.get("ZZ")
        path.unlink()
        assert repository.get(" zz ") is first

    def test_a_country_without_a_pack_file_is_not_found(self, tmp_path: Path) -> None:
        with pytest.raises(SECountryPackNotFoundError):
            self.repository(tmp_path).get("QQ")

    @pytest.mark.parametrize("country", ["ZZZ", "../zz", "", "z1", " ", "Z", "é", "z/", "..", "zz/../zz"])
    def test_a_country_that_is_not_two_ascii_letters_is_not_found(self, tmp_path: Path, country: str) -> None:
        self.write_pack(tmp_path)
        with pytest.raises(SECountryPackNotFoundError):
            self.repository(tmp_path).get(country)

    def test_a_malformed_yaml_file_is_unreadable(self, tmp_path: Path) -> None:
        self.write_pack(tmp_path, "country: [ZZ\nversion: : :\n")
        with pytest.raises(SECountryPackUnreadable):
            self.repository(tmp_path).get("ZZ")

    def test_a_failed_get_is_not_kept(self, tmp_path: Path) -> None:
        path = self.write_pack(tmp_path, "country: [ZZ\n")
        repository = self.repository(tmp_path)
        with pytest.raises(SECountryPackUnreadable):
            repository.get("ZZ")
        path.write_text(self.PACK_TEXT, encoding="utf-8")
        assert repository.get("ZZ").version == "2026.11"

    def test_the_given_logger_receives_the_log(self, tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
        self.write_pack(tmp_path)
        logger = logging.getLogger("test.country_pack_repository")
        with caplog.at_level(logging.DEBUG, logger=logger.name):
            self.repository(tmp_path, logger).get("ZZ")
        assert any(record.name == logger.name for record in caplog.records)

    def test_a_missing_pack_is_logged_as_an_error_before_it_is_raised(
        self, tmp_path: Path, caplog: pytest.LogCaptureFixture
    ) -> None:
        logger = logging.getLogger("test.country_pack_repository")
        with caplog.at_level(logging.DEBUG, logger=logger.name), pytest.raises(SECountryPackNotFoundError):
            self.repository(tmp_path, logger).get("QQ")
        assert any(record.name == logger.name and record.levelno == logging.ERROR for record in caplog.records)
