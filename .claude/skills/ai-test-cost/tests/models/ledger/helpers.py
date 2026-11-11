from __future__ import annotations

from datetime import UTC, datetime
from typing import Dict

from pydantic import JsonValue

STARTED_ON = datetime(2026, 11, 10, 9, 0, tzinfo=UTC)
FINISHED_ON = datetime(2026, 11, 10, 9, 5, tzinfo=UTC)


def usage_fields() -> Dict[str, JsonValue]:
    return {
        "input_tokens": 1000,
        "output_tokens": 200,
        "cache_read_tokens": 50,
        "cache_write_5m_tokens": 10,
        "cache_write_1h_tokens": 5,
        "cost_usd": "0.0123",
    }


def run_fields() -> Dict[str, JsonValue]:
    return {
        "id": "20261110-090000-ab12cd",
        "label": "invoice summary on Haiku",
        "command": "pytest tests -m llm",
        "started_on": STARTED_ON.isoformat(),
        "finished_on": FINISHED_ON.isoformat(),
        "estimate_usd": "0.50",
        "cost_usd": "0.25",
        "status": "done",
        "source": "usage_report",
        "usage": {"claude-haiku-5-5": usage_fields()},
        "settled": True,
        "exit_code": 0,
        "note": "measured by the usage report",
    }
