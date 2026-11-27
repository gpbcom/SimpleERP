from __future__ import annotations

import ast
import tomllib
from pathlib import Path
from typing import ClassVar, Dict, FrozenSet, List, Tuple

from tests.conventions.helpers import SOURCE_GLOBS


class CommandLineScanner:
    """The rule of ``AGENT.md`` that no Python package of SimpleERP holds a command line, read from one repository tree.

    Every service is a regular FastAPI application served by uvicorn, so no package of ``backend/``, ``plugins/`` or
    ``sdk/`` has a ``cli`` module or package, a ``__main__.py``, a console script, an argument parser or a read of
    ``sys.argv``. Each rule returns its offenders as texts naming the file, so that a test asserts the list is empty.
    The tree is a parameter, so that the rules also run on a small tree written by their own tests.

    Attributes:
        COMMAND_LINE_NAMES (FrozenSet[str]): The module or package names that are a command line.
        COMMAND_LINE_SUFFIX (str): The end of a module or package name that is a command line.
        COMMAND_LINE_PREFIX (str): The start of a module or package name that is a command line.
        ENTRY_MODULE (str): The module that ``python -m`` runs.
        SCRIPT_TABLES (Tuple[str, ...]): The ``[project]`` tables of a ``pyproject.toml`` that declare scripts.
        SCRIPT_GROUPS (Tuple[str, ...]): The ``[project.entry-points]`` groups that declare scripts.
        PARSER_MODULES (FrozenSet[str]): The modules that parse command-line arguments.
        root (Path): The repository tree read.
    """

    COMMAND_LINE_NAMES: ClassVar[FrozenSet[str]] = frozenset({"cli"})
    COMMAND_LINE_SUFFIX: ClassVar[str] = "_cli"
    COMMAND_LINE_PREFIX: ClassVar[str] = "cli_"
    ENTRY_MODULE: ClassVar[str] = "__main__.py"
    SCRIPT_TABLES: ClassVar[Tuple[str, ...]] = ("scripts", "gui-scripts")
    SCRIPT_GROUPS: ClassVar[Tuple[str, ...]] = ("console_scripts", "gui_scripts")
    PARSER_MODULES: ClassVar[FrozenSet[str]] = frozenset({"argparse", "click", "fire", "getopt", "optparse", "typer"})

    def __init__(self, root: Path) -> None:
        self.root = root

    ############################
    # Internal Helpers Methods #
    ############################

    def _packages(self) -> List[Path]:
        """Return the folder of every Python package: the folder that holds, or will hold, its ``src/``."""
        patterns = [pattern.removesuffix("/src") for pattern in SOURCE_GLOBS]
        return sorted({folder for pattern in patterns for folder in self.root.glob(pattern) if folder.is_dir()})

    def _code_folders(self) -> List[Path]:
        """Return the ``src/`` and ``tests/`` folders of every package."""
        return [
            folder for package in self._packages() for name in ("src", "tests") if (folder := package / name).is_dir()
        ]

    def _is_command_line_name(self, name: str) -> bool:
        return (
            name in self.COMMAND_LINE_NAMES
            or name.endswith(self.COMMAND_LINE_SUFFIX)
            or name.startswith(self.COMMAND_LINE_PREFIX)
        )

    def _parser_imports(self, node: ast.AST) -> List[str]:
        """Return what a node imports or reads that parses the command line."""
        if isinstance(node, ast.Import):
            return [alias.name for alias in node.names if alias.name.split(".")[0] in self.PARSER_MODULES]
        if isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            if node.module.split(".")[0] in self.PARSER_MODULES:
                return [node.module]
            if node.module == "sys" and any(alias.name == "argv" for alias in node.names):
                return ["sys.argv"]
        if isinstance(node, ast.Attribute) and node.attr == "argv" and ast.unparse(node.value) == "sys":
            return ["sys.argv"]
        return []

    def _declared_scripts(self, project: Dict[str, object]) -> List[str]:
        """Return each script a ``[project]`` table declares, as ``<table> <name>``."""
        found = [
            f"[project.{table}] {name}"
            for table in self.SCRIPT_TABLES
            if isinstance(scripts := project.get(table), dict)
            for name in scripts
        ]
        entry_points = project.get("entry-points")
        if isinstance(entry_points, dict):
            found.extend(
                f"[project.entry-points.{group}] {name}"
                for group in self.SCRIPT_GROUPS
                if isinstance(scripts := entry_points.get(group), dict)
                for name in scripts
            )
        return found

    ############################
    # Publicly Exposed Methods #
    ############################

    def command_line_modules(self) -> List[str]:
        """Return every ``cli`` module or package, and every ``__main__.py``, of a package's ``src/`` or ``tests/``."""
        offenders: List[str] = []
        for folder in self._code_folders():
            for path in sorted(folder.rglob("*")):
                if "__pycache__" in path.parts:
                    continue
                is_module = path.is_file() and path.suffix == ".py"
                name = path.stem if is_module else path.name
                if path.name == self.ENTRY_MODULE or (
                    (is_module or path.is_dir()) and self._is_command_line_name(name)
                ):
                    offenders.append(str(path.relative_to(self.root)))
        return offenders

    def console_scripts(self) -> List[str]:
        """Return every console or GUI script that a package's ``pyproject.toml`` declares."""
        offenders: List[str] = []
        for package in self._packages():
            manifest = package / "pyproject.toml"
            if not manifest.is_file():
                continue
            project = tomllib.loads(manifest.read_text(encoding="utf-8")).get("project", {})
            if isinstance(project, dict):
                where = manifest.relative_to(self.root)
                offenders.extend(f"{where}: {script}" for script in self._declared_scripts(project))
        return offenders

    def argument_parsers(self) -> List[str]:
        """Return every import of an argument parser, and every read of ``sys.argv``, in a package's ``src/``."""
        offenders: List[str] = []
        for package in self._packages():
            for path in sorted((package / "src").rglob("*.py")):
                tree = ast.parse(path.read_text(encoding="utf-8"))
                for node in ast.walk(tree):
                    offenders.extend(
                        f"{path.relative_to(self.root)}:{getattr(node, 'lineno', 0)} {name}"
                        for name in self._parser_imports(node)
                    )
        return offenders
