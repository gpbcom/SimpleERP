from __future__ import annotations

# Standard library imports
import shutil
import subprocess
import tempfile
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, Optional


class MermaidRenderer:
    """Renders a Mermaid diagram with mermaid-cli (``mmdc``), to tell whether it is valid.

    Attributes:
        EXECUTABLE (str): The mermaid-cli program.
        TIMEOUT_S (int): The longest one rendering may take.
        ERROR_MAX (int): The most characters of an error kept.
        logger (Logger): Logger instance.

    Notes:
        - Each block is written to a temporary file and rendered to SVG in the same temporary folder, which is
          removed afterwards: nothing is written in the repository.
        - A failure is returned as its message rather than raised, so that every block of every chapter is checked.
    """

    EXECUTABLE: ClassVar[str] = "mmdc"
    TIMEOUT_S: ClassVar[int] = 120
    ERROR_MAX: ClassVar[int] = 300

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def available(self) -> bool:
        """Tell whether ``mmdc`` is on the ``PATH``."""
        return shutil.which(self.EXECUTABLE) is not None

    def render(self, source: str) -> Optional[str]:
        """Render one diagram.

        Args:
            source (str): The Mermaid source, without its fences.

        Returns:
            Optional[str]: ``None`` when it renders, otherwise the last line ``mmdc`` printed, or its exit code.
        """
        with tempfile.TemporaryDirectory(prefix="project-docs-mermaid-") as folder:
            source_file = Path(folder) / "diagram.mmd"
            source_file.write_text(source, encoding="utf-8")
            command = [self.EXECUTABLE, "-q", "-i", str(source_file), "-o", str(Path(folder) / "diagram.svg")]
            try:
                result = subprocess.run(command, capture_output=True, text=True, timeout=self.TIMEOUT_S, check=False)
            except (OSError, subprocess.SubprocessError) as error:
                self.logger.warning("mmdc could not run: %s.", type(error).__name__)
                return f"mmdc could not run: {type(error).__name__}."
        if result.returncode == 0:
            self.logger.debug("A Mermaid block rendered.")
            return None
        printed = [line.strip() for line in result.stderr.splitlines() if line.strip()] or [
            line.strip() for line in result.stdout.splitlines() if line.strip()
        ]
        message = printed[-1] if printed else f"mmdc exited with code {result.returncode}."
        self.logger.warning("A Mermaid block does not render: mmdc exited with code %d.", result.returncode)
        return message[: self.ERROR_MAX]
