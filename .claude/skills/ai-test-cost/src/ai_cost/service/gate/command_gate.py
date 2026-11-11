from __future__ import annotations

# Standard library imports
import re
import shlex
from logging import Logger, getLogger
from typing import ClassVar, Dict, FrozenSet, List, Optional, Pattern, Tuple

# First-party imports
from ai_cost.models.commands.paid_command_catalog import PaidCommandCatalog
from ai_cost.models.ledger.exceptions import SELedgerInvalidTicket
from ai_cost.service.gate.pytest_invocation import PytestInvocation
from ai_cost.service.ledgers.exceptions import SELedgerReadFailedError
from ai_cost.service.ledgers.ledger_service import LedgerService
from harness_core.shell.shell_command_splitter import ShellCommandSplitter


class CommandGate:
    """Decides whether a shell command a Claude session is about to run may run.

    Attributes:
        RAISE_CAP (Pattern[str]): A command that raises a cap, an extra check on the text after the parsed one.
        QUOTED (Pattern[str]): A quoted string, with the shell and ``-c`` that run it when there are.
        GUARD_PROGRAM (str): The name of the guard's command line.
        GUARD_MODULE (str): The guard's Python module, run with ``python -m``.
        MODULE_OPTION (str): The Python option that runs a module.
        RUN_COMMAND (str): The guard's ``run`` command.
        RAISE_CAP_COMMAND (str): The guard's ``raise-cap`` command, which only the human runs.
        RAISE_CAP_REFUSAL (str): Why a command that raises a cap is refused.
        TICKET_OPTION (str): The option that names the ticket of a guarded run.
        END_OF_OPTIONS (str): The word after which the guarded command starts.
        GUARD_VARIABLE_PREFIX (str): The prefix of the guard's environment variables.
        HARMLESS_VARIABLES (FrozenSet[str]): The guard's variables a command may set.
        GUARDED_REMINDER (str): How to run a paid command through the guard.
        catalog (PaidCommandCatalog): The other commands that call a paid AI.
        ledgers (LedgerService): The ledgers, to refuse a blocked ticket.
        splitter (ShellCommandSplitter): Reads the command's simple commands.
        pytest (PytestInvocation): Finds the pytest runs of the paid tests.
        logger (Logger): Logger instance.

    Notes:
        - It refuses, in order: a command that raises a cap, found in the parsed words wherever the guard is called
          (after variables, ``env``, ``uv run``, ``python -m``, inside ``sh -c`` strings and inside ``ai-cost run``),
          and also by a regular expression on the text as a second check; a command that sets an ``AI_COST_``
          variable other than ``AI_COST_CALLER_CWD``; ``ai-cost run`` without ``--ticket``, with a key that is not a
          ticket, or for a blocked ticket; a pytest run of the paid tests not run through the guard; a command of
          ``conf/paid-commands.yaml`` when nothing is run through the guard.
        - pytest is read word by word, quotes kept, so quoting a marker does not hide it. The catalogue's regular
          expressions are searched in the text without its quoted strings, so that a mention (a ``grep`` pattern, a
          commit message) runs nothing.
        - **It never raises on a command it cannot read**: a ledger that cannot be read refuses the run.
    """

    RAISE_CAP: ClassVar[Pattern[str]] = re.compile(
        r"(?:^|[;&|(\n]|\$\()\s*(?:\S*/)?ai-cost\s+(?:-\S+\s+)*raise-cap\b|-m\s+ai_cost\s+(?:-\S+\s+)*raise-cap\b"
    )
    QUOTED: ClassVar[Pattern[str]] = re.compile(
        r"(?P<run>\b(?:bash|sh|zsh|dash|ksh)\s+(?:-\w+\s+)*-\w*c\s+)?(?:'[^']*'|\"(?:[^\"\\]|\\.)*\")"
    )
    GUARD_PROGRAM: ClassVar[str] = "ai-cost"
    GUARD_MODULE: ClassVar[str] = "ai_cost"
    MODULE_OPTION: ClassVar[str] = "-m"
    RUN_COMMAND: ClassVar[str] = "run"
    RAISE_CAP_COMMAND: ClassVar[str] = "raise-cap"
    RAISE_CAP_REFUSAL: ClassVar[str] = (
        "Only the human raises a ticket's AI test cap, in their own terminal, by typing the ticket back. "
        "Ask them to run `ai-cost raise-cap <KEY> <usd>`."
    )
    TICKET_OPTION: ClassVar[str] = "--ticket"
    END_OF_OPTIONS: ClassVar[str] = "--"
    GUARD_VARIABLE_PREFIX: ClassVar[str] = "AI_COST_"
    HARMLESS_VARIABLES: ClassVar[FrozenSet[str]] = frozenset({"AI_COST_CALLER_CWD"})
    GUARDED_REMINDER: ClassVar[str] = (
        'Run it through the cost guard: `ai-cost run --ticket <KEY> --estimate-usd <n> --label "<what>" -- <command>`.'
    )

    def __init__(
        self,
        catalog: PaidCommandCatalog,
        ledgers: LedgerService,
        splitter: ShellCommandSplitter,
        pytest: PytestInvocation,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the paid commands, the ledgers and the readers of a command.

        Args:
            catalog (PaidCommandCatalog): The other commands that call a paid AI.
            ledgers (LedgerService): The ledgers, to refuse a blocked ticket.
            splitter (ShellCommandSplitter): Reads the command's simple commands.
            pytest (PytestInvocation): Finds the pytest runs of the paid tests.
            logger (Optional[Logger]): Logger instance.
        """
        self.catalog = catalog
        self.ledgers = ledgers
        self.splitter = splitter
        self.pytest = pytest
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _quoted(self, match: re.Match[str]) -> str:
        """Keep a quoted string a shell runs, drop any other.

        Args:
            match (re.Match[str]): The quoted string.

        Returns:
            str: The string when a shell runs it (``bash -c '...'``), else a space.
        """
        return match.group(0) if match.group("run") else " "

    def _guard_call(self, words: List[str]) -> Optional[Tuple[str, List[str]]]:
        """Find a call of the guard in a simple command, wherever it stands in it.

        Args:
            words (List[str]): The simple command.

        Returns:
            Optional[Tuple[str, List[str]]]: The guard's command, such as ``run``, and the words after it, ``None``
            when the command does not call the guard.

        Notes:
            The guard may follow variables, ``env``, ``uv run [options]`` or ``python -m ai_cost``, so every word is
            looked at, and the command is the first word after it that is not an option.
        """
        for index, word in enumerate(words):
            start: Optional[int] = None
            if word.rsplit("/", 1)[-1] == self.GUARD_PROGRAM:
                start = index + 1
            elif word == self.MODULE_OPTION and words[index + 1 : index + 2] == [self.GUARD_MODULE]:
                start = index + 2
            if start is None:
                continue
            for position in range(start, len(words)):
                if not words[position].startswith("-"):
                    return words[position], words[position + 1 :]
        return None

    def _raises_cap(self, words: List[str]) -> bool:
        """Tell whether a simple command raises a cap, also through the command an ``ai-cost run`` starts.

        Args:
            words (List[str]): The simple command.

        Returns:
            bool: ``True`` when it calls ``ai-cost raise-cap``.
        """
        call = self._guard_call(words)
        if call is None:
            return False
        command, arguments = call
        if command == self.RAISE_CAP_COMMAND:
            return True
        if command != self.RUN_COMMAND or self.END_OF_OPTIONS not in arguments:
            return False
        started = arguments[arguments.index(self.END_OF_OPTIONS) + 1 :]
        return any(self._raises_cap(inner) for inner in self.splitter.commands(shlex.join(started)))

    def _ticket(self, arguments: List[str]) -> Optional[str]:
        """Read the ticket of a guarded run.

        Args:
            arguments (List[str]): The words after ``run``.

        Returns:
            Optional[str]: The ticket given with ``--ticket``, ``None`` when there is none.
        """
        options = arguments[: arguments.index(self.END_OF_OPTIONS)] if self.END_OF_OPTIONS in arguments else arguments
        for index, argument in enumerate(options):
            if argument == self.TICKET_OPTION and index + 1 < len(options):
                return options[index + 1]
            if argument.startswith(f"{self.TICKET_OPTION}="):
                return argument.split("=", 1)[1]
        return None

    def _guarded_refusal(self, arguments: List[str]) -> Optional[str]:
        """Decide on a guarded run.

        Args:
            arguments (List[str]): The words after ``run``.

        Returns:
            Optional[str]: Why it must not run, ``None`` when it may.
        """
        ticket = self._ticket(arguments)
        if ticket is None:
            return "`ai-cost run` needs `--ticket <KEY>`: the cost is charged to that ticket."
        try:
            ledger = self.ledgers.ledger(ticket)
        except SELedgerInvalidTicket:
            return f"`ai-cost run` needs a ticket key such as GH-12, not {ticket!r}."
        except SELedgerReadFailedError as error:
            return (
                f"The ledger of {ticket} cannot be read, so the cap cannot be checked: {error} "  # noqa: E501
                "Ask the human to look at it."
            )
        if ledger.block_reason is not None:
            return (
                f"{ledger.ticket}'s paid AI tests are blocked: {ledger.block_reason}. "  # noqa: E501
                f"Only the human raises the cap, with `ai-cost raise-cap {ledger.ticket} <usd>` in their own terminal."
            )
        return None

    def _variable_refusal(self, words: List[str]) -> Optional[str]:
        """Refuse a simple command that sets one of the guard's variables.

        Args:
            words (List[str]): The simple command.

        Returns:
            Optional[str]: Why it must not run, ``None`` when it sets none.
        """
        assigned, _rest = self.splitter.assignments(words)
        names = sorted({*assigned, *self.splitter.exports(words)})
        guarded = [
            name
            for name in names
            if name.startswith(self.GUARD_VARIABLE_PREFIX) and name not in self.HARMLESS_VARIABLES
        ]
        if not guarded:
            return None
        return (
            f"This command sets {guarded[0]}, a variable of the AI test cost guard. "  # noqa: E501
            "Only AI_COST_CALLER_CWD may be set: the guard's settings live in its versioned conf/settings.yaml."
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    def refusal(self, command: str) -> Optional[str]:
        """Decide on a shell command.

        Args:
            command (str): The shell command.

        Returns:
            Optional[str]: Why it must not run, ``None`` when it may.
        """
        text = self.splitter.without_data(command)
        visible = self.QUOTED.sub(self._quoted, text)
        commands = self.splitter.commands(text)
        if self.RAISE_CAP.search(visible) or any(self._raises_cap(words) for words in commands):
            self.logger.warning("Refused a command that raises a cap.")
            return self.RAISE_CAP_REFUSAL
        exported: Dict[str, str] = {}
        guarded_any = False
        for words in commands:
            refusal = self._variable_refusal(words)
            if refusal is None:
                call = self._guard_call(words)
                if call is not None and call[0] == self.RUN_COMMAND:
                    guarded_any = True
                    refusal = self._guarded_refusal(call[1])
                else:
                    reason = self.pytest.reason(words, exported)
                    if reason is not None:
                        refusal = f"This pytest run calls a paid AI ({reason}). {self.GUARDED_REMINDER}"
            if refusal is not None:
                self.logger.warning("Refused a command: %s", refusal)
                return refusal
            exported.update(self.splitter.exports(words))
        if not guarded_any:
            for paid in self.catalog.paid_commands:
                if re.search(paid.pattern, visible):
                    self.logger.warning("Refused a paid command: %s.", paid.name)
                    return f"This command calls a paid AI ({paid.name}). {self.GUARDED_REMINDER}"
        self.logger.debug("Allowed a command.")
        return None
