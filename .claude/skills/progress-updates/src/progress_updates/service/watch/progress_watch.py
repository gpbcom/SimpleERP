from __future__ import annotations

# Standard library imports
from collections import Counter
from logging import Logger, getLogger
from typing import ClassVar, List, Optional, TextIO

# First-party imports
from progress_updates.models.catalogs.progress_catalog import ProgressCatalog
from progress_updates.models.enums import TaskState
from progress_updates.models.exceptions import SEWatchIntervalError
from progress_updates.models.tasks.running_task import RunningTask
from progress_updates.models.watch.watch_marker import WatchMarker
from progress_updates.service.facts.fact_collector import FactCollector
from progress_updates.service.watch.clock import Clock


class ProgressWatch:
    """Prints one line every interval while something runs, then a final line, for Claude Code's Monitor tool.

    Attributes:
        CLOCK (str): The icon of an event.
        FINISH (str): The icon of the final event.
        TIME_FORMAT (str): How the time is written.
        ACTIVE (List[TaskState]): The states that keep the watch going.
        COUNTED (List[TaskState]): The states an event counts, in order.
        collector (FactCollector): Reads the tasks.
        catalog (ProgressCatalog): The icons and the shortest interval.
        clock (Clock): The time and the waits.
        out (TextIO): Where the events are printed.
        interval_s (int): Seconds between two events.
        max_ticks (Optional[int]): Events after which the watch stops, ``None`` for no limit.
        logger (Logger): Logger instance.

    Notes:
        - The Monitor tool wakes Claude once per printed line, so each event is exactly one line.
        - A declared task (a subagent) stays running for the watch: Claude stops the Monitor when it knows it ended.
    """

    CLOCK: ClassVar[str] = "⏱️"
    FINISH: ClassVar[str] = "🏁"
    TIME_FORMAT: ClassVar[str] = "%H:%M"
    ACTIVE: ClassVar[List[TaskState]] = [TaskState.RUNNING, TaskState.WAITING]
    COUNTED: ClassVar[List[TaskState]] = [
        TaskState.RUNNING,
        TaskState.WAITING,
        TaskState.FAILED,
        TaskState.WARNING,
        TaskState.DONE,
    ]

    def __init__(
        self,
        collector: FactCollector,
        catalog: ProgressCatalog,
        clock: Clock,
        out: TextIO,
        interval_s: int,
        max_ticks: Optional[int] = None,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the sources, the pace and the output.

        Args:
            collector (FactCollector): Reads the tasks.
            catalog (ProgressCatalog): The icons and the shortest interval.
            clock (Clock): The time and the waits.
            out (TextIO): Where the events are printed.
            interval_s (int): Seconds between two events.
            max_ticks (Optional[int]): Events after which the watch stops, ``None`` for no limit.
            logger (Optional[Logger]): Logger instance.

        Raises:
            SEWatchIntervalError: When the interval is shorter than the catalogue's shortest.
        """
        self.logger = logger if logger else getLogger(__name__)
        if interval_s < catalog.INTERVAL_S_MIN:
            self.logger.error("A watch every %d s was refused.", interval_s)
            raise SEWatchIntervalError(
                f"Invalid interval: {interval_s} s. "  # noqa: E501
                f"Must be at least {catalog.INTERVAL_S_MIN} s."
            )
        self.collector = collector
        self.catalog = catalog
        self.clock = clock
        self.out = out
        self.interval_s = interval_s
        self.max_ticks = max_ticks

    ############################
    # Internal Helpers Methods #
    ############################

    def _active(self, tasks: List[RunningTask]) -> bool:
        """Tell whether something still runs or waits.

        Args:
            tasks (List[RunningTask]): The tasks.

        Returns:
            bool: ``True`` while a task runs or waits.
        """
        return any(task.state in self.ACTIVE for task in tasks)

    def _event(self, tasks: List[RunningTask]) -> str:
        """Draw one event.

        Args:
            tasks (List[RunningTask]): The tasks.

        Returns:
            str: The time, the count per state, and what to do.
        """
        counts = Counter(task.state for task in tasks)
        parts = [f"{self.CLOCK} {self.clock.now():{self.TIME_FORMAT}}"]
        parts += [
            f"{self.catalog.state_icons[state.value]} {counts[state]} {state.value}"
            for state in self.COUNTED
            if counts[state]
        ]
        return " · ".join([*parts, WatchMarker.TICK.value])

    def _final(self) -> str:
        """Draw the final event.

        Returns:
            str: The time and what to do.
        """
        return f"{self.FINISH} {self.clock.now():{self.TIME_FORMAT}} · {WatchMarker.FINAL.value}"

    def _print(self, line: str) -> None:
        """Print one event and flush it, so that the Monitor sees it at once.

        Args:
            line (str): The event.
        """
        print(line, file=self.out, flush=True)

    ############################
    # Publicly Exposed Methods #
    ############################

    def follow(self) -> int:
        """Watch until nothing runs, or until ``max_ticks`` events.

        Returns:
            int: The exit code, 0.
        """
        ticks = 0
        tasks = self.collector.collect()
        while self._active(tasks):
            if self.max_ticks is not None and ticks >= self.max_ticks:
                self.logger.info("The watch stopped after %d events.", ticks)
                return 0
            self.clock.sleep(self.interval_s)
            tasks = self.collector.collect()
            if not self._active(tasks):
                break
            self._print(self._event(tasks))
            ticks += 1
        self._print(self._final())
        self.logger.info("The watch ended after %d events: nothing runs any more.", ticks)
        return 0
