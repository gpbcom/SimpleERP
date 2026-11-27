from __future__ import annotations

from typing import Iterator

import pytest
from erp_logging.context.log_context import LogContext


@pytest.fixture(autouse=True)
def clear_log_context() -> Iterator[None]:
    LogContext.clear()
    yield
    LogContext.clear()
