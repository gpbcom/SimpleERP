from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import ClassVar, Dict, FrozenSet, List, Optional, Set, Tuple

from tests.conventions.helpers import SOURCE_GLOBS


class ExceptionScanner:
    """The exception rules of ``AGENT.md`` ("Exceptions" and "Naming"), read from one repository tree.

    An exception is a class with the base ``Exception`` or ``BaseException``, or with the base of an exception defined
    in the scanned tree, resolved by name and transitively. Each rule returns its offenders as ``path:line`` texts, so
    that a test asserts the list is empty. The tree is a parameter, so that the rules also run on a small tree written
    by their own tests.

    Attributes:
        ROOT_EXCEPTIONS (FrozenSet[str]): The built-in bases that make a class an exception.
        PREFIX (str): What every exception name starts with.
        FOLDER (str): The name of the folder an exception lives in.
        WORD_BOUNDARY (re.Pattern[str]): Where a class name is cut to make its file name.
        root (Path): The repository tree read.
    """

    ROOT_EXCEPTIONS: ClassVar[FrozenSet[str]] = frozenset({"Exception", "BaseException"})
    PREFIX: ClassVar[str] = "SE"
    FOLDER: ClassVar[str] = "exceptions"
    WORD_BOUNDARY: ClassVar[re.Pattern[str]] = re.compile(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")

    def __init__(self, root: Path) -> None:
        self.root = root

    ############################
    # Internal Helpers Methods #
    ############################

    def _source_folders(self) -> List[Path]:
        """Return every source folder of the tree."""
        return sorted(folder for pattern in SOURCE_GLOBS for folder in self.root.glob(pattern) if folder.is_dir())

    def _files(self) -> List[Path]:
        """Return every Python file of every source folder."""
        return sorted(path for source in self._source_folders() for path in source.rglob("*.py"))

    def _base_name(self, base: ast.expr) -> Optional[str]:
        """Return the name a base class is written with, or None when it is not a plain or dotted name."""
        if isinstance(base, ast.Name):
            return base.id
        if isinstance(base, ast.Attribute):
            return base.attr
        return None

    def _exceptions(self) -> List[Tuple[Path, ast.ClassDef]]:
        """Return every exception class of the tree, with its file."""
        classes: List[Tuple[Path, ast.ClassDef]] = []
        for path in self._files():
            tree = ast.parse(path.read_text(encoding="utf-8"))
            classes.extend((path, node) for node in tree.body if isinstance(node, ast.ClassDef))
        names: Set[str] = set(self.ROOT_EXCEPTIONS)
        grown = True
        while grown:
            grown = False
            for _, node in classes:
                bases = {self._base_name(base) for base in node.bases}
                if node.name not in names and bases & names:
                    names.add(node.name)
                    grown = True
        return [(path, node) for path, node in classes if node.name in names]

    def _file_name(self, class_name: str) -> str:
        """Return the snake case file name of a class."""
        return f"{self.WORD_BOUNDARY.sub('_', class_name).lower()}.py"

    def _where(self, path: Path, line: int) -> str:
        return f"{path.relative_to(self.root).as_posix()}:{line}"

    def _exported(self, init: Path) -> Tuple[Optional[List[str]], int]:
        """Return the ``__all__`` list literal of a file with the line it starts on, or None when there is none."""
        if not init.is_file():
            return None, 1
        for node in ast.parse(init.read_text(encoding="utf-8")).body:
            targets = (
                node.targets
                if isinstance(node, ast.Assign)
                else [node.target]
                if isinstance(node, ast.AnnAssign)
                else []
            )
            if not any(isinstance(target, ast.Name) and target.id == "__all__" for target in targets):
                continue
            value = node.value if isinstance(node, (ast.Assign, ast.AnnAssign)) else None
            if isinstance(value, ast.List) and all(
                isinstance(item, ast.Constant) and isinstance(item.value, str) for item in value.elts
            ):
                return [str(item.value) for item in value.elts if isinstance(item, ast.Constant)], node.lineno
        return None, 1

    ############################
    # Publicly Exposed Methods #
    ############################

    def misnamed_exceptions(self) -> List[str]:
        """Return the exceptions whose name does not start with ``SE``."""
        return [
            self._where(path, node.lineno) for path, node in self._exceptions() if not node.name.startswith(self.PREFIX)
        ]

    def misplaced_exceptions(self) -> List[str]:
        """Return the exceptions whose file is not named after them, or that sit outside an ``exceptions`` folder."""
        offenders: List[str] = []
        for path, node in self._exceptions():
            in_folder = self.FOLDER in path.relative_to(self.root).parts[:-1]
            if path.name != self._file_name(node.name) or not in_folder:
                offenders.append(self._where(path, node.lineno))
        return offenders

    def unexported_exceptions(self) -> List[str]:
        """Return the problems of the ``__all__`` of every ``exceptions`` package: missing, unsorted or incomplete."""
        defined: Dict[Path, List[str]] = {}
        for path, node in self._exceptions():
            for folder in path.parents:
                if folder.name == self.FOLDER:
                    defined.setdefault(folder, []).append(node.name)
        offenders: List[str] = []
        for folder in sorted(defined):
            init = folder / "__init__.py"
            exported, line = self._exported(init)
            where = self._where(init if init.is_file() else folder, line)
            if exported is None:
                offenders.append(where)
                continue
            if exported != sorted(exported):
                offenders.append(where)
            offenders.extend(where for name in sorted(defined[folder]) if name not in exported)
        return offenders
