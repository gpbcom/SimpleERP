from __future__ import annotations

import ast
from collections import Counter
from pathlib import Path
from typing import Iterator, List, Optional, Set, Tuple

from tests.conventions.helpers import (
    ALLOWED_IMPORTS,
    FOLDER_LIMIT,
    FOLDER_LIMIT_IGNORES,
    RUNNABLE_BASES,
    SERVICE_SOURCE_GLOB,
    SHARED_MODELS_SOURCE,
    SOURCE_GLOBS,
    TEST_GLOBS,
    THIRD_PARTY_ATTRIBUTES,
)


class ConventionScanner:
    """The rules of ``AGENT.md`` that a test enforces, read from the Python files of one repository tree.

    Each rule returns its offenders as ``path:line`` texts, so that a test asserts the list is empty. The tree is a
    parameter, so that the rules are also run on a small tree written by their own tests.
    """

    def __init__(self, root: Path) -> None:
        self.root = root

    ############################
    # Internal Helpers Methods #
    ############################

    def _source_folders(self) -> List[Path]:
        return sorted(folder for pattern in SOURCE_GLOBS for folder in self.root.glob(pattern) if folder.is_dir())

    def _test_folders(self) -> List[Path]:
        return sorted(folder for pattern in TEST_GLOBS for folder in self.root.glob(pattern) if folder.is_dir())

    def _parse(self, path: Path) -> ast.Module:
        return ast.parse(path.read_text(encoding="utf-8"))

    def _layer_of(self, source: Path, path: Path) -> Tuple[str, Optional[str]]:
        """Return the package of a source file and its layer, or None when it sits in no layer folder."""
        parts = path.relative_to(source).parts
        if source == self.root / SHARED_MODELS_SOURCE:
            return parts[0], "models"
        if len(parts) >= 3 and parts[1] in ALLOWED_IMPORTS:
            return parts[0], parts[1]
        return parts[0], None

    def _imported(self, node: ast.AST) -> List[str]:
        if isinstance(node, ast.Import):
            return [alias.name for alias in node.names]
        if isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            return [node.module]
        return []

    def _source_trees(self) -> Iterator[Tuple[Path, Path, ast.Module]]:
        for source in self._source_folders():
            for path in sorted(source.rglob("*.py")):
                yield source, path, self._parse(path)

    def _non_model_trees(self) -> Iterator[Tuple[Path, ast.Module]]:
        """Every source file outside a ``models`` layer and the shared models."""
        for source, path, tree in self._source_trees():
            if self._layer_of(source, path)[1] != "models":
                yield path, tree

    def _packages(self, source: Path) -> List[Path]:
        """The package folders of a ``src/`` folder, leaving out caches and build metadata."""
        return sorted(
            folder
            for folder in source.iterdir()
            if folder.is_dir() and folder.name.isidentifier() and not folder.name.startswith("__")
        )

    def _service_packages(self) -> Set[str]:
        return {package.name for source in self.root.glob(SERVICE_SOURCE_GLOB) for package in self._packages(source)}

    ############################
    # Publicly Exposed Methods #
    ############################

    def all_trees(self) -> Iterator[Tuple[Path, ast.Module]]:
        """Every Python file of every package source folder and every test folder."""
        for _, path, tree in self._source_trees():
            yield path, tree
        for folder in self._test_folders():
            for path in sorted(folder.rglob("*.py")):
                yield path, self._parse(path)

    def where(self, path: Path, node: ast.AST) -> str:
        return f"{path.relative_to(self.root)}:{getattr(node, 'lineno', 0)}"

    def nested_functions(self) -> List[str]:
        offenders: List[str] = []
        for path, tree in self.all_trees():
            for outer in ast.walk(tree):
                if isinstance(outer, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    for inner in ast.walk(outer):
                        if inner is not outer and isinstance(inner, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            offenders.append(self.where(path, inner))
        return offenders

    def staticmethods(self) -> List[str]:
        return [
            self.where(path, node)
            for path, tree in self.all_trees()
            for node in ast.walk(tree)
            if isinstance(node, ast.Name) and node.id == "staticmethod"
        ]

    def files_with_several_classes(self) -> List[str]:
        return [
            str(path.relative_to(self.root))
            for path, tree in self.all_trees()
            if sum(isinstance(node, ast.ClassDef) for node in tree.body) > 1
        ]

    def crowded_folders(self) -> List[str]:
        counts = Counter(
            path.parent.relative_to(self.root) for path, _ in self.all_trees() if path.name not in FOLDER_LIMIT_IGNORES
        )
        return sorted(f"{folder} holds {count}" for folder, count in counts.items() if count > FOLDER_LIMIT)

    def any_imports(self) -> List[str]:
        return [
            self.where(path, node)
            for path, tree in self.all_trees()
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom)
            and node.module == "typing"
            and any(alias.name == "Any" for alias in node.names)
        ]

    def underscore_instance_attributes(self) -> List[str]:
        offenders: List[str] = []
        for path, tree in self.all_trees():
            for node in ast.walk(tree):
                if not isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
                    continue
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                for target in targets:
                    if (
                        isinstance(target, ast.Attribute)
                        and isinstance(target.value, ast.Name)
                        and target.value.id in ("self", "cls")
                        and target.attr.startswith("_")
                        and target.attr not in THIRD_PARTY_ATTRIBUTES
                    ):
                        offenders.append(f"{self.where(path, node)} {target.attr}")
        return offenders

    def underscore_class_attributes(self) -> List[str]:
        offenders: List[str] = []
        for path, tree in self.all_trees():
            for owner in ast.walk(tree):
                if not isinstance(owner, ast.ClassDef):
                    continue
                for node in owner.body:
                    names: List[str] = []
                    if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                        names = [node.target.id]
                    elif isinstance(node, ast.Assign):
                        names = [target.id for target in node.targets if isinstance(target, ast.Name)]
                    offenders += [
                        f"{self.where(path, node)} {name}"
                        for name in names
                        if name.startswith("_") and name not in THIRD_PARTY_ATTRIBUTES
                    ]
        return offenders

    def layer_imports(self) -> List[str]:
        """Imports of a layer of the same package that the layer may not use (``api`` -> ``service`` -> ...)."""
        offenders: List[str] = []
        for source, path, tree in self._source_trees():
            package, layer = self._layer_of(source, path)
            if layer is None or source == self.root / SHARED_MODELS_SOURCE:
                continue
            allowed = ALLOWED_IMPORTS[layer]
            for node in ast.walk(tree):
                for name in self._imported(node):
                    parts = name.split(".")
                    target = parts[1] if parts[0] == package and len(parts) > 1 else parts[0]
                    if target in ALLOWED_IMPORTS and target not in allowed:
                        offenders.append(f"{self.where(path, node)} {layer} imports {target}")
        return offenders

    def foreign_service_imports(self) -> List[str]:
        """Imports of a service's package from anywhere but that service: a service never imports another."""
        services = self._service_packages()
        offenders: List[str] = []
        for source, path, tree in self._source_trees():
            package = self._layer_of(source, path)[0]
            for node in ast.walk(tree):
                for name in self._imported(node):
                    root = name.split(".")[0]
                    if root in services and root != package:
                        offenders.append(f"{self.where(path, node)} {package} imports {root}")
        return offenders

    def top_level_layer_packages(self) -> List[str]:
        """Layer folders put straight under a ``src/``: services share one environment, so they would collide."""
        return [
            str((source / layer).relative_to(self.root))
            for source in self._source_folders()
            for layer in ALLOWED_IMPORTS
            if (source / layer).exists()
        ]

    def services_missing_layers(self) -> List[str]:
        return [
            f"{package.relative_to(self.root)} has no {layer}/"
            for source in sorted(self.root.glob(SERVICE_SOURCE_GLOB))
            for package in self._packages(source)
            if package.name not in ALLOWED_IMPORTS
            for layer in ALLOWED_IMPORTS
            if not (package / layer).is_dir()
        ]

    def lifecycle_offenders(self) -> List[str]:
        offenders: List[str] = []
        for path, tree in self._non_model_trees():
            for node in tree.body:
                if not isinstance(node, ast.ClassDef):
                    continue
                methods = {item.name for item in node.body if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))}
                bases = {ast.unparse(base) for base in node.bases}
                if "start" in methods or "stop" in methods:
                    offenders.append(f"{self.where(path, node)} {node.name} uses start or stop")
                if "run" in methods and not bases & RUNNABLE_BASES and node.name not in RUNNABLE_BASES:
                    offenders.append(f"{self.where(path, node)} {node.name} has run but no lifecycle base class")
        return offenders

    def node_offenders(self) -> List[str]:
        offenders: List[str] = []
        for path, tree in self._non_model_trees():
            for node in tree.body:
                if isinstance(node, ast.ClassDef) and node.name.endswith("Node"):
                    methods = {item.name for item in node.body if isinstance(item, ast.AsyncFunctionDef)}
                    if "__call__" not in methods or "run" in methods:
                        offenders.append(self.where(path, node))
        return offenders

    def models_outside_models(self) -> List[str]:
        return [
            self.where(path, node)
            for path, tree in self._non_model_trees()
            for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef)
            and any(isinstance(base, ast.Name) and base.id == "BaseModel" for base in node.bases)
        ]
