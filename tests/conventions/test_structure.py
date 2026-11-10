"""House rules that a reviewer should not have to catch by eye."""

from __future__ import annotations

import ast
from collections import Counter
from typing import List

from tests.conventions.helpers import (
    FOLDER_LIMIT,
    FOLDER_LIMIT_IGNORES,
    ROOT,
    RUNNABLE_BASES,
    all_trees,
    logic_trees,
    where,
)


class TestStructure:
    def test_no_nested_function(self) -> None:
        offenders: List[str] = []
        for path, tree in all_trees():
            for outer in ast.walk(tree):
                if isinstance(outer, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    for inner in ast.walk(outer):
                        if inner is not outer and isinstance(inner, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            offenders.append(where(path, inner))
        assert not offenders

    def test_no_staticmethod(self) -> None:
        offenders = [
            where(path, node)
            for path, tree in all_trees()
            for node in ast.walk(tree)
            if isinstance(node, ast.Name) and node.id == "staticmethod"
        ]
        assert not offenders

    def test_one_class_per_file(self) -> None:
        offenders = [
            str(path.relative_to(ROOT))
            for path, tree in all_trees()
            if sum(isinstance(node, ast.ClassDef) for node in tree.body) > 1
        ]
        assert not offenders

    def test_no_folder_holds_more_than_five_python_files(self) -> None:
        counts = Counter(
            path.parent.relative_to(ROOT) for path, _ in all_trees() if path.name not in FOLDER_LIMIT_IGNORES
        )
        assert not {str(folder): count for folder, count in counts.items() if count > FOLDER_LIMIT}

    def test_every_runnable_has_the_lifecycle_through_a_base_class(self) -> None:
        offenders: List[str] = []
        for path, tree in logic_trees():
            for node in tree.body:
                if not isinstance(node, ast.ClassDef):
                    continue
                methods = {item.name for item in node.body if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))}
                bases = {ast.unparse(base) for base in node.bases}
                if "start" in methods or "stop" in methods:
                    offenders.append(f"{where(path, node)} {node.name} uses start or stop")
                if "run" in methods and not bases & RUNNABLE_BASES and node.name not in RUNNABLE_BASES:
                    offenders.append(f"{where(path, node)} {node.name} has run but no lifecycle base class")
        assert not offenders

    def test_every_node_is_called_rather_than_run(self) -> None:
        offenders: List[str] = []
        for path, tree in logic_trees():
            for node in tree.body:
                if isinstance(node, ast.ClassDef) and node.name.endswith("Node"):
                    methods = {item.name for item in node.body if isinstance(item, ast.AsyncFunctionDef)}
                    if "__call__" not in methods or "run" in methods:
                        offenders.append(where(path, node))
        assert not offenders

    def test_no_pydantic_model_outside_the_models_layer(self) -> None:
        offenders = [
            where(path, node)
            for path, tree in logic_trees()
            for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef)
            and any(isinstance(base, ast.Name) and base.id == "BaseModel" for base in node.bases)
        ]
        assert not offenders

    def test_no_any_annotation(self) -> None:
        offenders = [
            where(path, node)
            for path, tree in all_trees()
            for node in ast.walk(tree)
            if isinstance(node, ast.ImportFrom)
            and node.module == "typing"
            and any(alias.name == "Any" for alias in node.names)
        ]
        assert not offenders
