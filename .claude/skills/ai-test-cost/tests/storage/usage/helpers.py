from __future__ import annotations

from typing import Dict, Optional

from pydantic import JsonValue

ADMIN_SECRET = "sk-ant-admin01-test-secret-never-logged"


def usage_result(model: Optional[str], uncached: int, output: int, cache_read: int = 0) -> Dict[str, JsonValue]:
    return {
        "account_id": None,
        "api_key_id": None,
        "cache_creation": {"ephemeral_1h_input_tokens": 0, "ephemeral_5m_input_tokens": 100},
        "cache_read_input_tokens": cache_read,
        "context_window": None,
        "inference_geo": None,
        "model": model,
        "output_tokens": output,
        "server_tool_use": {"web_search_requests": 0},
        "service_account_id": None,
        "service_tier": None,
        "speed": None,
        "uncached_input_tokens": uncached,
        "workspace_id": None,
    }


def usage_page(results: JsonValue, next_page: Optional[str] = None) -> Dict[str, JsonValue]:
    return {
        "data": [
            {"starting_at": "2026-11-10T09:00:00Z", "ending_at": "2026-11-10T09:01:00Z", "results": results},
            {"starting_at": "2026-11-10T09:01:00Z", "ending_at": "2026-11-10T09:02:00Z", "results": []},
        ],
        "has_more": next_page is not None,
        "next_page": next_page,
    }
