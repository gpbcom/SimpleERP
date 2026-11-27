from __future__ import annotations

# Standard library imports
from typing import Iterator

# Third-party imports
import pytest

# First-party imports
from erp_logging.context.log_context import LogContext


@pytest.fixture(autouse=True)
def clean_log_context() -> Iterator[None]:
    LogContext.clear()
    yield
    LogContext.clear()
