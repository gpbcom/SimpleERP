from __future__ import annotations

# Standard library imports
import re
from logging import Logger, getLogger
from typing import ClassVar, Optional, Pattern, Tuple


class SecretMask:
    """Hides secrets in a line before it is shown to the owner.

    Attributes:
        MASK (str): What a secret becomes.
        TOKENS (Tuple[Pattern[str], ...]): Known token shapes, masked whole.
        NAMED (Pattern[str]): A secret named before its value (``DB_PASSWORD=...``, ``api_key: "..."``,
            ``Bearer ...``, ``--access-key ...``), whose value is masked.
        logger (Logger): Logger instance.

    Notes:
        **An update is shown in the terminal and kept in the transcript**: nothing that looks like a secret may reach
        it.
    """

    MASK: ClassVar[str] = "•••"
    TOKENS: ClassVar[Tuple[Pattern[str], ...]] = (
        re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
        re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
        re.compile(r"sk-[A-Za-z0-9_-]{16,}"),
        re.compile(r"eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}"),
        re.compile(r"(?:AKIA|ASIA)[A-Z0-9]{16}"),
        re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
        re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    )
    NAMED: ClassVar[Pattern[str]] = re.compile(
        r"(?i)([A-Za-z0-9_-]*(?:password|passwd|secret|token|api[_-]?key|access[_-]?key|bearer)[A-Za-z0-9_-]*)"
        r"([\"']?\s*[:=]\s*[\"']?|\s+)([^\s\"']+)"
    )

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def mask(self, text: str) -> str:
        """Mask every secret of a line.

        Args:
            text (str): The line.

        Returns:
            str: The line with each secret replaced by ``•••``.
        """
        masked = text
        for pattern in self.TOKENS:
            masked = pattern.sub(self.MASK, masked)
        masked = self.NAMED.sub(lambda found: f"{found.group(1)}{found.group(2)}{self.MASK}", masked)
        if masked != text:
            self.logger.debug("A secret was masked in an update line.")
        return masked
