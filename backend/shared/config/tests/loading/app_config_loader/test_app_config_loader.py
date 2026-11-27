from __future__ import annotations

# Standard library imports
import logging
from pathlib import Path
from typing import ClassVar, Dict, Optional

# Third-party imports
import pytest
from erp_config.loading.app_config_loader import AppConfigLoader
from erp_config.loading.environment_overrides import EnvironmentOverrides
from erp_config.models.exceptions import (
    SEAppConfigInvalidError,
    SEAppConfigMissingDefaultError,
    SEAppConfigUnknownOverrideError,
    SEAppConfigUnreadableError,
    SEConfigSectionInvalidKey,
)

# First-party imports
from backend.shared.config.tests.loading.app_config_loader.sample_app_config import SampleAppConfig


class TestAppConfigLoader:
    NO_KEY: ClassVar[str] = "  password_key: null\n"

    def test_the_file_values_are_loaded(self, loader: AppConfigLoader[SampleAppConfig]) -> None:
        config = loader.read()
        assert config.server.host == "example.org"
        assert config.server.port == 9000
        assert config.mail.sender == "boss@example.org"
        assert config.mail.password_key == "mail/smtp-password"

    @pytest.mark.parametrize("environ", [{"ERP__SERVER__PORT": "6543"}], indirect=True)
    def test_an_environment_variable_overrides_a_default(self, loader: AppConfigLoader[SampleAppConfig]) -> None:
        config = loader.read()
        assert config.server.port == 6543
        assert config.server.host == "example.org"

    @pytest.mark.parametrize("environ", [{"ERP__MAIL__PASSWORD_KEY": "mail/other-entry"}], indirect=True)
    def test_a_key_value_never_appears_in_a_log_line(
        self, loader: AppConfigLoader[SampleAppConfig], caplog: pytest.LogCaptureFixture
    ) -> None:
        with caplog.at_level(logging.DEBUG):
            config = loader.read()
            logging.getLogger("t").info("%s %r", config, config)
        assert config.mail.password_key == "mail/other-entry"
        assert "mail/smtp-password" not in caplog.text
        assert "mail/other-entry" not in caplog.text

    @pytest.mark.parametrize("environ", [{"ERP__MAIL__PASSWORD_KEY": "not a name"}], indirect=True)
    def test_a_key_that_is_not_an_entry_name_is_refused(self, loader: AppConfigLoader[SampleAppConfig]) -> None:
        with pytest.raises(SEConfigSectionInvalidKey):
            loader.read()

    @pytest.mark.parametrize("content", [None, "server: [unclosed\n", "- server\n- mail\n"])
    def test_an_unreadable_file_is_refused(self, tmp_path: Path, content: Optional[str]) -> None:
        path = tmp_path / "app.yaml"
        if content is not None:
            path.write_text(content, encoding="utf-8")
        loader = AppConfigLoader(SampleAppConfig, path, EnvironmentOverrides("ERP", {}))
        with pytest.raises(SEAppConfigUnreadableError):
            loader.read()

    @pytest.mark.parametrize(
        "content",
        [
            "mail:\n  sender: a@b.c\n" + "  password_key: null\n",
            "server:\n  host: h\nmail:\n  sender: a@b.c\n" + "  password_key: null\n",
        ],
    )
    def test_a_missing_default_is_refused(self, tmp_path: Path, content: str) -> None:
        path = tmp_path / "app.yaml"
        path.write_text(content, encoding="utf-8")
        loader = AppConfigLoader(SampleAppConfig, path, EnvironmentOverrides("ERP", {}))
        with pytest.raises(SEAppConfigMissingDefaultError):
            loader.read()

    def test_a_missing_nested_default_is_named_by_its_dotted_path(self, tmp_path: Path) -> None:
        path = tmp_path / "app.yaml"
        path.write_text("server:\n  host: h\nmail:\n  sender: a@b.c\n" + self.NO_KEY, encoding="utf-8")
        loader = AppConfigLoader(SampleAppConfig, path, EnvironmentOverrides("ERP", {}))
        with pytest.raises(SEAppConfigMissingDefaultError, match=r"server\.port"):
            loader.read()

    @pytest.mark.parametrize(
        "server",
        ["  host: h\n  port: 1\n  extra: 1\n", "  host: h\n  port: many\n"],
    )
    def test_an_unknown_key_or_a_wrong_type_is_invalid(self, tmp_path: Path, server: str) -> None:
        path = tmp_path / "app.yaml"
        path.write_text("server:\n" + server + "mail:\n  sender: a@b.c\n" + self.NO_KEY, encoding="utf-8")
        loader = AppConfigLoader(SampleAppConfig, path, EnvironmentOverrides("ERP", {}))
        with pytest.raises(SEAppConfigInvalidError):
            loader.read()

    @pytest.mark.parametrize("environ", [{"ERP__SERVER__NOPE": "1"}], indirect=True)
    def test_an_unknown_override_is_refused(
        self, loader: AppConfigLoader[SampleAppConfig], environ: Dict[str, str]
    ) -> None:
        with pytest.raises(SEAppConfigUnknownOverrideError):
            loader.read()
