from __future__ import annotations

# Standard library imports
import re
import shlex
from logging import Logger, getLogger
from typing import ClassVar, Dict, FrozenSet, List, Optional, Pattern

# First-party imports
from harness_core.shell.shell_command_splitter import ShellCommandSplitter


class PytestInvocation:
    """Decides, word by word, whether a pytest command selects the tests that call a paid AI.

    Attributes:
        PROGRAMS (FrozenSet[str]): The names pytest runs under.
        PAID_FLAG (str): The option that turns the paid tests on.
        MARK_OPTION (str): The long option of a marker expression.
        ADDOPTS_VARIABLE (str): The variable pytest reads extra options from.
        SHORT_MARK (Pattern[str]): A short option group ending in ``m``, such as ``-m``, ``-qm`` or ``-mllm``.
        NEGATED (Pattern[str]): ``not llm`` in a marker expression.
        MARKER (Pattern[str]): The ``llm`` marker as a whole word.
        logger (Logger): Logger instance.
        splitter (ShellCommandSplitter): Reads the variables a command sets before its program.

    Notes:
        - A pytest command is paid when a marker expression (``-m``, ``-m=``, ``--markexpr``) names ``llm`` other
          than as ``not llm``, or when ``--llm`` is given, on the command line or in ``PYTEST_ADDOPTS``.
        - An expression that negates ``llm`` with brackets, such as ``not (slow or llm)``, counts as paid: the gate
          errs on the safe side.
        - pytest is found as any word named ``pytest`` or ``py.test``, which covers ``uv run pytest`` and
          ``python -m pytest``.
    """

    PROGRAMS: ClassVar[FrozenSet[str]] = frozenset({"pytest", "py.test"})
    PAID_FLAG: ClassVar[str] = "--llm"
    MARK_OPTION: ClassVar[str] = "--markexpr"
    ADDOPTS_VARIABLE: ClassVar[str] = "PYTEST_ADDOPTS"
    SHORT_MARK: ClassVar[Pattern[str]] = re.compile(r"^-(?!-)[A-Za-z]*?m=?(?P<expression>.*)$", re.DOTALL)
    NEGATED: ClassVar[Pattern[str]] = re.compile(r"\bnot\s+llm\b")
    MARKER: ClassVar[Pattern[str]] = re.compile(r"\bllm\b")

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)
        self.splitter = ShellCommandSplitter(self.logger)

    ############################
    # Internal Helpers Methods #
    ############################

    def _paid_expression(self, expression: str) -> bool:
        """Tell whether a marker expression selects the ``llm`` tests.

        Args:
            expression (str): The marker expression.

        Returns:
            bool: ``True`` when ``llm`` appears other than as ``not llm``.
        """
        return bool(self.MARKER.search(self.NEGATED.sub(" ", expression)))

    def _reason_in(self, arguments: List[str]) -> Optional[str]:
        """Find what makes pytest arguments paid.

        Args:
            arguments (List[str]): pytest's arguments.

        Returns:
            Optional[str]: The option that selects the paid tests, ``None`` when none does.
        """
        for index, argument in enumerate(arguments):
            following = arguments[index + 1] if index + 1 < len(arguments) else ""
            if argument == self.PAID_FLAG:
                return f"`{self.PAID_FLAG}`"
            if argument == self.MARK_OPTION:
                expression = following
            elif argument.startswith(f"{self.MARK_OPTION}="):
                expression = argument.split("=", 1)[1]
            elif short := self.SHORT_MARK.match(argument):
                expression = short.group("expression") or following
            else:
                continue
            if self._paid_expression(expression):
                return f"the marker expression {expression!r}"
        return None

    ############################
    # Publicly Exposed Methods #
    ############################

    def reason(self, words: List[str], exported: Dict[str, str]) -> Optional[str]:
        """Find why a simple command runs the paid tests.

        Args:
            words (List[str]): The simple command.
            exported (Dict[str, str]): The variables exported earlier in the same shell command.

        Returns:
            Optional[str]: Why it is paid, ``None`` when it is not a paid pytest run.
        """
        assigned, rest = self.splitter.assignments(words)
        variables = {**exported, **assigned}
        start = next((index for index, word in enumerate(rest) if word.rsplit("/", 1)[-1] in self.PROGRAMS), None)
        if start is None:
            return None
        try:
            added = shlex.split(variables.get(self.ADDOPTS_VARIABLE, ""))
        except ValueError:
            self.logger.warning("%s has an unclosed quote: read word by word.", self.ADDOPTS_VARIABLE)
            added = variables.get(self.ADDOPTS_VARIABLE, "").split()
        reason = self._reason_in(added)
        if reason is not None:
            return f"{reason} in {self.ADDOPTS_VARIABLE}"
        reason = self._reason_in(rest[start + 1 :])
        if reason is not None:
            self.logger.info("A pytest run selects the paid tests: %s.", reason)
        return reason
