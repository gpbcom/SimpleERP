from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from pathlib import Path
from string import Template
from typing import ClassVar, List, Optional

# First-party imports
from harness_core.git.git_repository import GitRepository
from pr_watch.storage.files.text_files import TextFiles
from pr_watch.storage.git.pull_request_clone import PullRequestClone


class UnitInstaller:
    """Copies the watcher's systemd user units, their paths filled in, to the user's systemd folder.

    Attributes:
        UNITS (List[str]): The unit files.
        units_dir (Path): The folder of the unit templates.
        skill_dir (Path): The skill's folder.
        files (TextFiles): Writes the units.
        logger (Logger): Logger instance.

    Notes:
        - The templates hold ``${skill_dir}`` and ``${repository_root}``, filled with the **main** working tree of
          the repository, so that units installed from a worktree still work once the worktree is removed.
        - Nothing is enabled here: ``systemctl --user enable --now claude-pr-watch.timer`` stays a decision of the
          person at the keyboard.
    """

    UNITS: ClassVar[List[str]] = ["claude-pr-watch.service", "claude-pr-watch.timer"]

    def __init__(
        self,
        units_dir: Path,
        skill_dir: Path,
        files: TextFiles,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the templates and what fills them.

        Args:
            units_dir (Path): The folder of the unit templates.
            skill_dir (Path): The skill's folder.
            files (TextFiles): Writes the units.
            logger (Optional[Logger]): Logger instance.
        """
        self.units_dir = units_dir
        self.skill_dir = skill_dir
        self.files = files
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def install(self, target_dir: Path) -> List[Path]:
        """Write the units to a folder.

        Args:
            target_dir (Path): The folder, usually ``~/.config/systemd/user``.

        Returns:
            List[Path]: The units written.

        Raises:
            SEGitCommandFailedError: When the skill's folder is not inside a git working tree.
        """
        top = GitRepository.discover(self.skill_dir, self.logger).root
        repository_root = PullRequestClone(self.skill_dir, self.logger).main_root()
        skill_dir = repository_root / self.skill_dir.resolve().relative_to(top)
        self.logger.debug("The units run %s from %s.", skill_dir, repository_root)
        written = []
        for name in self.UNITS:
            template = Template(self.files.read(self.units_dir / name) or "")
            content = template.substitute(skill_dir=skill_dir, repository_root=repository_root)
            self.files.write(target_dir / name, content)
            written.append(target_dir / name)
        self.logger.info("Installed %d systemd units in %s.", len(written), target_dir)
        return written
