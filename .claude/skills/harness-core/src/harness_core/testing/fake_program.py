from __future__ import annotations

# Standard library imports
import stat
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, Optional


class FakeProgram:
    """A folder of executable shell scripts that stand for programs, such as ``gh`` or ``mmdc``, in tests.

    Attributes:
        SHEBANG (str): The first line of every script.
        folder (Path): The folder that holds the scripts, put first on ``PATH`` by the test.
        logger (Logger): Logger instance.

    Notes:
        Tests use real processes rather than mocks: a script prints and exits as the real program would.
    """

    SHEBANG: ClassVar[str] = "#!/usr/bin/env bash\n"

    def __init__(self, folder: Path, logger: Optional[Logger] = None) -> None:
        """Set the folder.

        Args:
            folder (Path): The folder that holds the scripts.
            logger (Optional[Logger]): Logger instance.
        """
        self.folder = folder
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def write(self, name: str, body: str) -> Path:
        """Write one executable script.

        Args:
            name (str): The program's name.
            body (str): The bash lines it runs.

        Returns:
            Path: The script.
        """
        self.folder.mkdir(parents=True, exist_ok=True)
        path = self.folder / name
        path.write_text(self.SHEBANG + body + "\n", encoding="utf-8")
        path.chmod(path.stat().st_mode | stat.S_IXUSR)
        self.logger.debug("Wrote the stand-in program %s.", path)
        return path
