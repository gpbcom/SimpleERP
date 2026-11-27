from __future__ import annotations

import logging
from pathlib import Path

import pytest
from erp_models.errors.catalogs.error_catalog import ErrorCatalog
from erp_platform.storage.catalogs.error_code_repository import ErrorCodeRepository
from erp_platform.storage.catalogs.exceptions import SEErrorCodeCatalogUnreadableError, SEErrorCodeStorageError


class TestErrorCodeRepository:
    CODES = ["PLATFORM-ROUTE-01", "PLATFORM-METHOD-01", "PLATFORM-REQUEST-01", "PLATFORM-INTERNAL-01"]

    def real_path(self) -> Path:
        return Path(__file__).resolve().parents[3] / "conf" / "catalogs" / "error_codes.yaml"

    def test_the_real_catalogue_loads_as_the_error_catalogue_model(self) -> None:
        catalog = ErrorCodeRepository(self.real_path()).load()

        assert isinstance(catalog, ErrorCatalog)

    def test_the_real_catalogue_holds_the_four_platform_codes(self) -> None:
        catalog = ErrorCodeRepository(self.real_path()).load()

        assert set(catalog.codes) == set(self.CODES)

    @pytest.mark.parametrize("code", CODES)
    def test_each_platform_code_has_its_keys_and_reference(self, code: str) -> None:
        entry = ErrorCodeRepository(self.real_path()).load().resolve(code)

        assert entry.title
        assert entry.why
        assert entry.action
        assert entry.reference

    def test_a_missing_file_is_refused(self, tmp_path: Path) -> None:
        with pytest.raises(SEErrorCodeCatalogUnreadableError):
            ErrorCodeRepository(tmp_path / "missing.yaml").load()

    @pytest.mark.parametrize(
        "content",
        ["codes: [unclosed", "- just\n- a list\n", "", "codes: {}\n", "codes:\n  not a code:\n    title: x\n"],
    )
    def test_an_unreadable_file_is_refused(self, tmp_path: Path, content: str) -> None:
        path = tmp_path / "error_codes.yaml"
        path.write_text(content, encoding="utf-8")

        with pytest.raises(SEErrorCodeCatalogUnreadableError):
            ErrorCodeRepository(path).load()

    def test_the_unreadable_error_is_a_storage_error(self, tmp_path: Path) -> None:
        with pytest.raises(SEErrorCodeStorageError):
            ErrorCodeRepository(tmp_path / "missing.yaml").load()

    def test_the_unreadable_error_keeps_its_cause(self, tmp_path: Path) -> None:
        with pytest.raises(SEErrorCodeCatalogUnreadableError) as raised:
            ErrorCodeRepository(tmp_path / "missing.yaml").load()

        assert raised.value.__cause__ is not None

    def test_a_refusal_writes_an_error_log_line(self, tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
        with caplog.at_level(logging.DEBUG), pytest.raises(SEErrorCodeCatalogUnreadableError):
            ErrorCodeRepository(tmp_path / "missing.yaml").load()

        assert [record for record in caplog.records if record.levelno == logging.ERROR]

    def test_a_given_logger_receives_the_error_line(self, tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
        logger = logging.getLogger("tests.error_code_repository")

        with caplog.at_level(logging.DEBUG), pytest.raises(SEErrorCodeCatalogUnreadableError):
            ErrorCodeRepository(tmp_path / "missing.yaml", logger).load()

        assert any(record.name == "tests.error_code_repository" for record in caplog.records)
