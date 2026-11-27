from __future__ import annotations

import pytest
from erp_testing.plugin.testing_plugin import TestingPlugin


def pytest_configure(config: pytest.Config) -> None:
    config.pluginmanager.import_plugin("pytester")
    config.pluginmanager.register(TestingPlugin(), "erp-testing")
