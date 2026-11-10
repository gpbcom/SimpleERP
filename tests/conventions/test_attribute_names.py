"""House rules that a reviewer should not have to catch by eye."""

from __future__ import annotations

import ast
from typing import List

from tests.conventions.helpers import THIRD_PARTY_ATTRIBUTES, all_trees, where


class TestAttributeNames:
    def test_no_instance_attribute_starts_with_an_underscore(self) -> None:
        offenders: List[str] = []
        for path, tree in all_trees():
            for node in ast.walk(tree):
                targets = node.targets if isinstance(node, ast.Assign) else [getattr(node, "target", None)]
                if not isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
                    continue
                for target in targets:
                    if (
                        isinstance(target, ast.Attribute)
                        and isinstance(target.value, ast.Name)
                        and target.value.id in ("self", "cls")
                        and target.attr.startswith("_")
                    ):
                        offenders.append(f"{where(path, node)} {target.attr}")
        assert not offenders

    def test_no_class_attribute_starts_with_an_underscore(self) -> None:
        offenders: List[str] = []
        for path, tree in all_trees():
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
                        f"{where(path, node)} {name}"
                        for name in names
                        if name.startswith("_") and name not in THIRD_PARTY_ATTRIBUTES
                    ]
        assert not offenders
