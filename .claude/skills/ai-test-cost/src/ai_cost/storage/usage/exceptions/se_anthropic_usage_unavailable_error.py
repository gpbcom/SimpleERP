from __future__ import annotations

from ai_cost.storage.usage.exceptions.se_anthropic_usage_error import SEAnthropicUsageError


class SEAnthropicUsageUnavailableError(SEAnthropicUsageError):
    """Raised when the usage report cannot be read because no admin key is set."""
