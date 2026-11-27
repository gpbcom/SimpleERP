from __future__ import annotations

from logging import Filter, Handler, Logger, getLogger
from typing import Iterator, List

import pytest
from erp_logging.context.log_context import LogContext


@pytest.fixture(autouse=True)
def restore_root_logger() -> Iterator[Logger]:
    root = getLogger()
    handlers: List[Handler] = list(root.handlers)
    level = root.level
    filters: List[Filter] = list(root.filters)
    LogContext.clear()
    yield root
    for handler in list(root.handlers):
        if handler not in handlers:
            handler.close()
    root.handlers[:] = handlers
    root.filters[:] = filters
    root.setLevel(level)
    LogContext.clear()
