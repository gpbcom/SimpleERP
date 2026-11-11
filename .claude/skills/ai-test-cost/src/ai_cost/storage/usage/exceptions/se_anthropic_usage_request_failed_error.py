from __future__ import annotations

from ai_cost.storage.usage.exceptions.se_anthropic_usage_error import SEAnthropicUsageError


class SEAnthropicUsageRequestFailedError(SEAnthropicUsageError):
    """Raised when the usage report request fails or its answer cannot be read."""
