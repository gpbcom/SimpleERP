from __future__ import annotations

import ast
from pathlib import Path
from typing import Dict, FrozenSet, Iterator, Tuple

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
TESTS = ROOT / "tests"
# Each layer, and the layers it may import. A layer may always import itself.
ALLOWED_IMPORTS: Dict[str, FrozenSet[str]] = {
    "api": frozenset({"api", "service", "models"}),
    "service": frozenset({"service", "storage", "models"}),
    "storage": frozenset({"storage", "models"}),
    "models": frozenset({"models"}),
}
LOGIC_LAYERS = ("api", "service", "storage")
# Names a third-party protocol owns, which may start with an underscore.
THIRD_PARTY_ATTRIBUTES: FrozenSet[str] = frozenset()
RUNNABLE_BASES = {"Runnable", "AsyncRunnable", "Command"}
FOLDER_LIMIT = 5
FOLDER_LIMIT_IGNORES = {"__init__.py", "conftest.py"}


def sources(folder: str = "") -> Iterator[Path]:
    yield from (SRC / folder).rglob("*.py")


def trees(folder: str = "") -> Iterator[Tuple[Path, ast.Module]]:
    for path in sources(folder):
        yield path, ast.parse(path.read_text(encoding="utf-8"))


def logic_trees() -> Iterator[Tuple[Path, ast.Module]]:
    """Every file of every layer except ``models``."""
    for layer in LOGIC_LAYERS:
        yield from trees(layer)


def all_trees() -> Iterator[Tuple[Path, ast.Module]]:
    """Every file of ``src`` and ``tests``."""
    yield from trees()
    for path in TESTS.rglob("*.py"):
        yield path, ast.parse(path.read_text(encoding="utf-8"))


def where(path: Path, node: ast.AST) -> str:
    return f"{path.relative_to(ROOT)}:{node.lineno}"
