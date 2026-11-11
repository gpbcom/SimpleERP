from __future__ import annotations

# Standard library imports
import re
import shlex
from logging import Logger, getLogger
from typing import ClassVar, Dict, FrozenSet, List, Optional, Pattern, Tuple


class ShellCommandSplitter:
    """Reads a shell command the way the shell will: its simple commands, each one a list of words.

    Attributes:
        HEREDOC (Pattern[str]): A here-document: the line feeding it, and its body.
        SHELLS (FrozenSet[str]): The programs that run a here-document's body or a ``-c`` string as commands.
        PUNCTUATION (str): The characters that end a word.
        SEPARATOR_CHARACTERS (FrozenSet[str]): The characters of an operator that ends a simple command.
        MAX_DEPTH (int): How many ``sh -c`` strings inside each other are read.
        ASSIGNMENT (Pattern[str]): A ``NAME=value`` word.
        NAME (Pattern[str]): A variable name.
        ENV_PROGRAM (str): The program that sets variables before another one.
        ENV_UNSET_OPTIONS (FrozenSet[str]): The options of ``env`` followed by a variable name.
        EXPORTERS (FrozenSet[str]): The builtins that export or declare variables.
        logger (Logger): Logger instance.

    Notes:
        - Quoted words keep their content, so ``pytest -m "llm"`` gives the word ``llm``.
        - A backslash before a new line joins the two lines, as the shell does.
        - The body of a here-document fed to a program that is not a shell (``python3 - <<'PY'``,
          ``cat > notes.md <<EOF``) is data, not commands, and is dropped first.
        - A command the shell would reject, such as one with an unclosed quote, is split on white space line by line,
          so that the gate still reads its words.
    """

    HEREDOC: ClassVar[Pattern[str]] = re.compile(
        r"(?P<head>[^\n]*?)<<-?\s*(?P<quote>['\"]?)(?P<tag>\w+)(?P=quote)[^\n]*\n"
        r"(?P<body>.*?\n)?[ \t]*(?P=tag)[ \t]*(?=\n|$)",
        re.DOTALL,
    )
    SHELLS: ClassVar[FrozenSet[str]] = frozenset({"bash", "sh", "zsh", "dash", "ksh"})
    PUNCTUATION: ClassVar[str] = ";&|()<>\n"
    SEPARATOR_CHARACTERS: ClassVar[FrozenSet[str]] = frozenset(";&|()\n")
    MAX_DEPTH: ClassVar[int] = 5
    ASSIGNMENT: ClassVar[Pattern[str]] = re.compile(r"^(?P<name>[A-Za-z_][A-Za-z0-9_]*)=(?P<value>.*)$", re.DOTALL)
    NAME: ClassVar[Pattern[str]] = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
    ENV_PROGRAM: ClassVar[str] = "env"
    ENV_UNSET_OPTIONS: ClassVar[FrozenSet[str]] = frozenset({"-u", "--unset"})
    EXPORTERS: ClassVar[FrozenSet[str]] = frozenset({"export", "declare", "typeset", "readonly", "local"})

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _heredoc(self, match: re.Match[str]) -> str:
        """Keep a here-document fed to a shell, or drop the body of one fed to another program.

        Args:
            match (re.Match[str]): The here-document.

        Returns:
            str: The whole here-document for a shell, else its feeding line only.
        """
        words = re.split(r"[;&|(]", match.group("head"))[-1].split()
        program = words[0].rsplit("/", 1)[-1] if words else ""
        return match.group(0) if program in self.SHELLS else match.group("head")

    def _tokens(self, text: str) -> List[str]:
        """Split a text into words and operators.

        Args:
            text (str): The shell text.

        Returns:
            List[str]: The words, quotes removed, and the operators, new lines included.

        Raises:
            ValueError: When a quote is not closed.
        """
        lexer = shlex.shlex(text.replace("\\\n", ""), posix=True, punctuation_chars=self.PUNCTUATION)
        lexer.whitespace = " \t\r"
        lexer.whitespace_split = True
        lexer.commenters = ""
        return list(lexer)

    def _separator(self, token: str) -> bool:
        """Tell whether a token ends a simple command.

        Args:
            token (str): The token.

        Returns:
            bool: ``True`` for ``;``, ``&&``, ``||``, ``|``, ``&``, brackets and new lines, not for redirections.
        """
        return bool(token) and set(token) <= self.SEPARATOR_CHARACTERS

    def _script(self, words: List[str]) -> Optional[str]:
        """Find the string a shell runs with ``-c``.

        Args:
            words (List[str]): A simple command.

        Returns:
            Optional[str]: The script, ``None`` when no shell of the command runs a ``-c`` string.

        Notes:
            The shell may come after another program, as in ``env A=1 bash -c`` or ``nohup sh -c``, so every word
            is looked at: reading too much only makes the gate stricter.
        """
        for start, program in enumerate(words):
            if program.rsplit("/", 1)[-1] not in self.SHELLS:
                continue
            for index in range(start + 1, len(words) - 1):
                word = words[index]
                if word.startswith("-") and not word.startswith("--") and "c" in word:
                    return words[index + 1]
        return None

    def _split(self, text: str, depth: int) -> List[List[str]]:
        """Split a text into simple commands, reading inside ``sh -c`` strings.

        Args:
            text (str): The shell text.
            depth (int): How deep inside ``sh -c`` strings the text is.

        Returns:
            List[List[str]]: The simple commands, those of each ``sh -c`` string right after it.
        """
        try:
            tokens = self._tokens(text)
        except ValueError:
            self.logger.warning("The command has an unclosed quote: split on white space.")
            return [line.split() for line in text.replace("\\\n", "").splitlines() if line.split()]
        commands: List[List[str]] = []
        words: List[str] = []
        for token in [*tokens, "\n"]:
            if not self._separator(token):
                words.append(token)
                continue
            if words:
                commands.append(words)
                script = self._script(words)
                if script is not None and depth < self.MAX_DEPTH:
                    commands.extend(self._split(script, depth + 1))
            words = []
        return commands

    ############################
    # Publicly Exposed Methods #
    ############################

    def without_data(self, command: str) -> str:
        """Drop the bodies of the here-documents fed to programs that are not shells.

        Args:
            command (str): The shell command.

        Returns:
            str: The command, quotes kept.
        """
        return self.HEREDOC.sub(self._heredoc, command)

    def commands(self, command: str) -> List[List[str]]:
        """Split a shell command into its simple commands.

        Args:
            command (str): The shell command, here-documents of data already dropped.

        Returns:
            List[List[str]]: Each simple command as its words, in order.
        """
        commands = self._split(command, 0)
        self.logger.debug("Split the command into %d simple commands.", len(commands))
        return commands

    def assignments(self, words: List[str]) -> Tuple[Dict[str, str], List[str]]:
        """Read the variables a simple command sets for its program.

        Args:
            words (List[str]): The simple command.

        Returns:
            Tuple[Dict[str, str], List[str]]: The variables set by ``NAME=value`` words, before the program or after
            ``env`` and its options, and the words from the program on.
        """
        variables: Dict[str, str] = {}
        index = 0
        after_env = False
        while index < len(words):
            word = words[index]
            assignment = self.ASSIGNMENT.match(word)
            if assignment:
                variables[assignment.group("name")] = assignment.group("value")
            elif word.rsplit("/", 1)[-1] == self.ENV_PROGRAM and not after_env:
                after_env = True
            elif after_env and word in self.ENV_UNSET_OPTIONS:
                index += 1
            elif not (after_env and word.startswith("-")):
                break
            index += 1
        return variables, words[index:]

    def exports(self, words: List[str]) -> Dict[str, str]:
        """Read the variables an ``export``-like builtin sets for the rest of the shell command.

        Args:
            words (List[str]): The simple command.

        Returns:
            Dict[str, str]: Each variable named, with its value or an empty string, empty when the command is not
            ``export``, ``declare``, ``typeset``, ``readonly`` or ``local``.
        """
        if not words or words[0] not in self.EXPORTERS:
            return {}
        variables: Dict[str, str] = {}
        for word in words[1:]:
            assignment = self.ASSIGNMENT.match(word)
            if assignment:
                variables[assignment.group("name")] = assignment.group("value")
            elif self.NAME.match(word):
                variables[word] = ""
        return variables
