from __future__ import annotations

from pathlib import Path

import pytest
from erp_testing.models.postgres.exceptions import SEPostgresBinariesNotFoundError
from erp_testing.models.postgres.postgres_server_config import PostgresServerConfig
from erp_testing.postgres.postgres_binaries import PostgresBinaries

from tests.postgres.fake_postgres_binaries import FakePostgresBinaries


class TestPostgresBinaries:
    @pytest.fixture(autouse=True)
    def empty_path(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        empty = tmp_path / "empty_path"
        empty.mkdir()
        monkeypatch.setenv("PATH", str(empty))

    def test_a_bin_folder_with_the_four_binaries_is_accepted(self, tmp_path: Path) -> None:
        bin_dir = FakePostgresBinaries(tmp_path).write(tmp_path / "pg" / "bin")
        config = PostgresServerConfig(search_dirs=[str(bin_dir)])
        assert Path(PostgresBinaries(config).find()) == bin_dir

    def test_the_newest_version_is_preferred(self, tmp_path: Path) -> None:
        fake = FakePostgresBinaries(tmp_path / "versions")
        fake.write_version(9)
        newest = fake.write_version(16)
        fake.write_version(10)
        config = PostgresServerConfig(search_dirs=[str(tmp_path / "versions")])
        assert Path(PostgresBinaries(config).find()) == newest

    def test_a_version_missing_a_binary_is_skipped(self, tmp_path: Path) -> None:
        fake = FakePostgresBinaries(tmp_path / "versions")
        older = fake.write_version(15)
        fake.write(tmp_path / "versions" / "16" / "bin", skip="psql")
        config = PostgresServerConfig(search_dirs=[str(tmp_path / "versions")])
        assert Path(PostgresBinaries(config).find()) == older

    def test_the_path_is_searched_after_the_search_dirs(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        on_path = FakePostgresBinaries(tmp_path).write(tmp_path / "on_path")
        monkeypatch.setenv("PATH", str(on_path))
        config = PostgresServerConfig(search_dirs=[str(tmp_path / "nothing")])
        assert Path(PostgresBinaries(config).find()) == on_path

    def test_an_error_is_raised_when_no_folder_holds_the_four_binaries(self, tmp_path: Path) -> None:
        FakePostgresBinaries(tmp_path).write(tmp_path / "partial" / "bin", skip="initdb")
        config = PostgresServerConfig(search_dirs=[str(tmp_path / "partial" / "bin"), str(tmp_path / "missing")])
        with pytest.raises(SEPostgresBinariesNotFoundError):
            PostgresBinaries(config).find()
