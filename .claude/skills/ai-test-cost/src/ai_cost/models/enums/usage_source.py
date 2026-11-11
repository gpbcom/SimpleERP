from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class UsageSource(StrEnum):
    """How the guard measures what a run costs.

    Attributes:
        ANTHROPIC (str): The Anthropic Admin API usage report, read with the admin key of ``ANTHROPIC_ADMIN_KEY``.
        ESTIMATE (str): Nothing is measured: each run is charged its estimate, then ``charge`` corrects it.
    """

    ANTHROPIC = "anthropic"
    ESTIMATE = "estimate"
