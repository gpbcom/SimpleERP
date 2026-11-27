from __future__ import annotations

import os
from pathlib import Path

import pytest
import yaml
from erp_config.loading.app_config_loader import AppConfigLoader
from erp_config.loading.environment_overrides import EnvironmentOverrides
from erp_platform.models.config.platform_config import PlatformConfig


class TestAppYaml:
    APP_YAML = Path(__file__).resolve().parents[2] / "conf" / "app.yaml"

    def load(self) -> PlatformConfig:
        overrides = EnvironmentOverrides("erp", dict(os.environ))
        return AppConfigLoader(PlatformConfig, self.APP_YAML, overrides).read()

    def test_the_file_exists_in_the_service_conf_folder(self) -> None:
        assert self.APP_YAML.is_file()

    def test_the_file_loads_into_the_platform_config(self) -> None:
        assert isinstance(self.load(), PlatformConfig)

    def test_every_field_is_written_in_the_file(self) -> None:
        data = yaml.safe_load(self.APP_YAML.read_text(encoding="utf-8"))
        assert set(data) == set(PlatformConfig.model_fields)

    def test_the_file_writes_every_default(self) -> None:
        assert self.load() == PlatformConfig()

    def test_the_file_holds_no_host_and_no_port(self) -> None:
        data = yaml.safe_load(self.APP_YAML.read_text(encoding="utf-8"))
        assert "host" not in data
        assert "port" not in data

    def test_the_environment_overrides_the_error_codes_path(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("ERP__ERROR_CODES_PATH", "conf/other.yaml")
        assert self.load().error_codes_path == "conf/other.yaml"
