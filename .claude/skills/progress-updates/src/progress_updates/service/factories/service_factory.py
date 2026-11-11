from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import List, Optional

# First-party imports
from progress_updates.models.enums import TaskSource
from progress_updates.service.facts.fact_collector import FactCollector
from progress_updates.service.hooks.background_reminder import BackgroundReminder
from progress_updates.service.rendering.update_renderer import UpdateRenderer
from progress_updates.service.watch.progress_watch import ProgressWatch


class ServiceFactory(ABC):
    """Builds the services the commands call."""

    @abstractmethod
    def __init__(self) -> None:
        """Set what the services need."""

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def collector(
        self,
        sources: List[TaskSource],
        tasks_dir: Optional[Path],
        evidence: Optional[Path],
        since: Optional[datetime],
        declarations: List[str],
    ) -> FactCollector:
        """Build the collector of an update.

        Args:
            sources (List[TaskSource]): The sources to read.
            tasks_dir (Optional[Path]): The session's task folder.
            evidence (Optional[Path]): The ticket's evidence folder.
            since (Optional[datetime]): When the work started.
            declarations (List[str]): The tasks Claude declares.

        Returns:
            FactCollector: The collector.
        """

    @abstractmethod
    def renderer(self, since: Optional[datetime]) -> UpdateRenderer:
        """Build the renderer of an update.

        Args:
            since (Optional[datetime]): When the work started.

        Returns:
            UpdateRenderer: The renderer, at the current time.
        """

    @abstractmethod
    def watch(self, collector: FactCollector, every_s: Optional[int], max_ticks: Optional[int]) -> ProgressWatch:
        """Build a watch.

        Args:
            collector (FactCollector): Reads the tasks.
            every_s (Optional[int]): Seconds between two events, the catalogue's by default.
            max_ticks (Optional[int]): Events after which the watch stops.

        Returns:
            ProgressWatch: The watch.

        Raises:
            SEWatchIntervalError: When the interval is too short.
        """

    @abstractmethod
    def reminder(self) -> BackgroundReminder:
        """Build the background reminder.

        Returns:
            BackgroundReminder: The reminder.
        """
