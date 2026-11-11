from __future__ import annotations

import logging

import pytest


@pytest.fixture
def logger() -> logging.Logger:
    return logging.getLogger("harness_core.tests")
