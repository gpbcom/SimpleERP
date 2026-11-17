from __future__ import annotations

# Standard library imports
import sys
from datetime import datetime
from logging import Logger, getLogger
from pathlib import Path
from typing import List, Optional

# First-party imports
from progress_updates.models.catalogs.progress_catalog import ProgressCatalog
from progress_updates.models.enums import TaskSource
from progress_updates.service.factories.service_factory import ServiceFactory
from progress_updates.service.facts.declared_tasks import DeclaredTasks
from progress_updates.service.facts.fact_collector import FactCollector
from progress_updates.service.hooks.background_reminder import BackgroundReminder
from progress_updates.service.rendering.secret_mask import SecretMask
from progress_updates.service.rendering.update_renderer import UpdateRenderer
from progress_updates.service.watch.clock import Clock
from progress_updates.service.watch.progress_watch import ProgressWatch
from progress_updates.storage.actions.actions_run_reader import ActionsRunReader
from progress_updates.storage.background.task_output_reader import TaskOutputReader
from progress_updates.storage.evidence.evidence_reader import EvidenceReader
from progress_updates.storage.processes.process_reader import ProcessReader
from progress_updates.storage.task_reader import TaskReader


class DefaultServiceFactory(ServiceFactory):
    """Builds the real services on the catalogue and the repository.

    Attributes:
        catalog (ProgressCatalog): The pace and the icons.
        root (Path): The repository the command was typed in.
        logger (Logger): Logger instance.
    """

    def __init__(self, catalog: ProgressCatalog, root: Path, logger: Optional[Logger] = None) -> None:
        """Set the catalogue and the repository.

        Args:
            catalog (ProgressCatalog): The pace and the icons.
            root (Path): The repository the command was typed in.
            logger (Optional[Logger]): Logger instance.
        """
        self.catalog = catalog
        self.root = root
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _reader(
        self, source: TaskSource, tasks_dir: Optional[Path], evidence: Optional[Path], since: Optional[datetime]
    ) -> Optional[TaskReader]:
        """Build the reader of one source.

        Args:
            source (TaskSource): The source.
            tasks_dir (Optional[Path]): The session's task folder.
            evidence (Optional[Path]): The ticket's evidence folder.
            since (Optional[datetime]): When the work started.

        Returns:
            Optional[TaskReader]: The reader, ``None`` when the source lacks its folder or is not read.
        """
        limit = self.catalog.line_max_chars
        match source:
            case TaskSource.BACKGROUND if tasks_dir is not None:
                return TaskOutputReader(tasks_dir, limit, since, self.logger)
            case TaskSource.PROCESS:
                return ProcessReader(self.root, limit, self.logger)
            case TaskSource.EVIDENCE if evidence is not None:
                return EvidenceReader(evidence, self.catalog.evidence_max, limit, since, self.logger)
            case TaskSource.ACTIONS:
                return ActionsRunReader(self.root, limit, self.logger)
            case _:
                self.logger.debug("The %s source is not read.", source.value)
                return None

    ############################
    # Publicly Exposed Methods #
    ############################

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
        readers: List[TaskReader] = []
        for source in sources:
            reader = self._reader(source, tasks_dir, evidence, since)
            if reader is not None:
                readers.append(reader)
        self.logger.debug("Reading %d sources.", len(readers))
        return FactCollector(readers, DeclaredTasks(self.logger).parse(declarations), self.logger)

    def renderer(self, since: Optional[datetime]) -> UpdateRenderer:
        """Build the renderer of an update.

        Args:
            since (Optional[datetime]): When the work started.

        Returns:
            UpdateRenderer: The renderer, at the current time.
        """
        return UpdateRenderer(self.catalog, SecretMask(self.logger), datetime.now(), since, self.logger)

    def watch(self, collector: FactCollector, every_s: Optional[int], max_ticks: Optional[int]) -> ProgressWatch:
        """Build a watch printing on the standard output.

        Args:
            collector (FactCollector): Reads the tasks.
            every_s (Optional[int]): Seconds between two events, the catalogue's by default.
            max_ticks (Optional[int]): Events after which the watch stops.

        Returns:
            ProgressWatch: The watch.

        Raises:
            SEWatchIntervalError: When the interval is too short.
        """
        interval = every_s if every_s is not None else self.catalog.interval_s
        return ProgressWatch(collector, self.catalog, Clock(self.logger), sys.stdout, interval, max_ticks, self.logger)

    def reminder(self) -> BackgroundReminder:
        """Build the background reminder.

        Returns:
            BackgroundReminder: The reminder.
        """
        return BackgroundReminder(self.logger)
