from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class WatchMarker(StrEnum):
    """The phrases that end the watch's events, so that its own output is recognised and never listed as a task.

    Attributes:
        TICK (str): The end of an event while something runs.
        FINAL (str): The end of the final event.
    """

    TICK = "post an update (progress-updates status)"
    FINAL = "nothing runs any more · post the final update"
