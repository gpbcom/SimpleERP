"""Each layer only calls the one below it, and every layer may use ``models``."""

from __future__ import annotations

import ast
from typing import List

from tests.conventions.helpers import ALLOWED_IMPORTS, trees, where


class TestLayers:
    def test_no_layer_imports_what_it_may_not(self) -> None:
        offenders: List[str] = []
        for layer, allowed in ALLOWED_IMPORTS.items():
            for path, tree in trees(layer):
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        names = [alias.name for alias in node.names]
                    elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                        names = [node.module]
                    else:
                        continue
                    roots = {name.split(".")[0] for name in names}
                    forbidden = (roots & set(ALLOWED_IMPORTS)) - allowed
                    offenders += [f"{where(path, node)} {layer} imports {root}" for root in sorted(forbidden)]
        assert not offenders

    def test_every_layer_exists(self) -> None:
        assert all(next(trees(layer), None) for layer in ALLOWED_IMPORTS)
