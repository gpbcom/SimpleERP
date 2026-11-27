from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import Dict

# Third-party imports
import pytest
from erp_config.loading.app_config_loader import AppConfigLoader
from erp_config.loading.environment_overrides import EnvironmentOverrides

# First-party imports
from backend.shared.config.tests.loading.app_config_loader.sample_app_config import SampleAppConfig


@pytest.fixture
def app_yaml(tmp_path: Path) -> Path:
    """Write a complete ``app.yaml`` and return its path."""
    path = tmp_path / "app.yaml"
    path.write_text(
        "server:\n"
        "  host: example.org\n"
        "  port: 9000\n"
        "mail:\n"
        "  sender: boss@example.org\n"
        "  password_key: mail/smtp-password\n",
        encoding="utf-8",
    )
    return path


@pytest.fixture
def environ(request: pytest.FixtureRequest) -> Dict[str, str]:
    """Return the environment given by ``indirect`` parametrisation, empty by default."""
    return dict(getattr(request, "param", {}))


@pytest.fixture
def loader(app_yaml: Path, environ: Dict[str, str]) -> AppConfigLoader[SampleAppConfig]:
    """Build the loader over ``app_yaml`` with ``environ``."""
    return AppConfigLoader(SampleAppConfig, app_yaml, EnvironmentOverrides("ERP", environ))
