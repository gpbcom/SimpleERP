from __future__ import annotations

# Standard library imports
import hmac
import secrets
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, Optional


class HumanConfirmation:
    """The controlling terminal of the person running a harness tool, used to confirm that a human, not Claude, acts.

    Attributes:
        TTY (Path): The controlling terminal of the process.
        CODE_LENGTH (int): How many characters the confirmation code has.
        CODE_ALPHABET (str): The characters of a confirmation code.
        tty (Path): The terminal opened, ``/dev/tty`` unless a test gives another one.
        logger (Logger): Logger instance.

    Notes:
        - **The terminal is opened directly**, not read through standard input: Claude's Bash tool runs without a
          controlling terminal, so opening ``/dev/tty`` fails there and nothing is confirmed (fail closed).
        - A random code is shown on that terminal and must be typed back on it. The ticket key on the command line
          is no proof, since whoever runs the command already knows it.
        - **This guards against accidents and a session going down the wrong path**, not against a process that
          runs as the same user and drives a pseudo-terminal on purpose.
        - Tests give a scripted subclass instead of a mock, or a pseudo-terminal.
    """

    TTY: ClassVar[Path] = Path("/dev/tty")
    CODE_LENGTH: ClassVar[int] = 6
    CODE_ALPHABET: ClassVar[str] = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"

    def __init__(self, tty: Optional[Path] = None, logger: Optional[Logger] = None) -> None:
        """Set the terminal.

        Args:
            tty (Optional[Path]): The terminal to open, ``/dev/tty`` when ``None``.
            logger (Optional[Logger]): Logger instance.
        """
        self.tty = tty if tty is not None else self.TTY
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def code(self) -> str:
        """Draw a new confirmation code.

        Returns:
            str: ``CODE_LENGTH`` random characters of ``CODE_ALPHABET``.
        """
        return "".join(secrets.choice(self.CODE_ALPHABET) for _ in range(self.CODE_LENGTH))

    def confirm(self, question: str) -> bool:
        """Ask the person at the terminal, who confirms by typing back a code shown there.

        Args:
            question (str): What is to be confirmed.

        Returns:
            bool: ``True`` when the code was typed back, ``False`` when it was not or no terminal could be opened.
        """
        code = self.code()
        try:
            with self.tty.open("r+b", buffering=0) as terminal:
                terminal.write(f"{question}\nType {code} to confirm: ".encode())
                answer = terminal.readline().decode(errors="replace").strip()
        except OSError as error:
            self.logger.warning("No terminal could be opened (%s): nothing is confirmed.", type(error).__name__)
            return False
        confirmed = hmac.compare_digest(answer.encode(), code.encode())
        self.logger.info("The person at the terminal %s.", "confirmed" if confirmed else "did not confirm")
        return confirmed
