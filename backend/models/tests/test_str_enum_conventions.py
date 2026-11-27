from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import ClassVar, List, Optional

import pytest


class TestStrEnumConventions:
    GOOD: ClassVar[str] = (
        "from enum import StrEnum, unique\n\n\n"
        "@unique\n"
        "class PaymentStatus(StrEnum):\n"
        '    """Where a payment stands.\n\n'
        "    Attributes:\n"
        "        PAID: The payment is settled.\n"
        "        DUE: The payment is awaited.\n"
        '    """\n\n'
        '    PAID = "paid"\n'
        '    DUE = "due"\n'
    )

    def is_str_enum(self, node: ast.ClassDef) -> bool:
        names = [base.attr if isinstance(base, ast.Attribute) else getattr(base, "id", "") for base in node.bases]
        return "StrEnum" in names

    def is_unique(self, node: ast.ClassDef) -> bool:
        names = [
            deco.attr if isinstance(deco, ast.Attribute) else getattr(deco, "id", "") for deco in node.decorator_list
        ]
        return "unique" in names

    def snake_case(self, name: str) -> str:
        step = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
        return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", step).lower()

    def members(self, node: ast.ClassDef) -> List[str]:
        found: List[str] = []
        for statement in node.body:
            if isinstance(statement, ast.Assign):
                found.extend(target.id for target in statement.targets if isinstance(target, ast.Name))
            elif isinstance(statement, ast.AnnAssign) and isinstance(statement.target, ast.Name):
                found.append(statement.target.id)
        return found

    def documents_members(self, node: ast.ClassDef) -> bool:
        docstring = ast.get_docstring(node) or ""
        if "Attributes:" not in docstring:
            return False
        section = docstring.split("Attributes:", 1)[1]
        section = re.split(r"\n\s*\n(?=\S)|\n[A-Z][A-Za-z ]*:\s*\n", section)[0]
        return all(re.search(rf"^\s*{re.escape(member)}\b", section, re.MULTILINE) for member in self.members(node))

    def exported_names(self, init: Path) -> Optional[List[str]]:
        tree = ast.parse(init.read_text(encoding="utf-8"))
        for statement in tree.body:
            is_all = isinstance(statement, ast.Assign) and any(
                isinstance(target, ast.Name) and target.id == "__all__" for target in statement.targets
            )
            if is_all and isinstance(statement.value, (ast.List, ast.Tuple)):
                return [item.value for item in statement.value.elts if isinstance(item, ast.Constant)]
        return None

    def is_reexported(self, path: Path, root: Path, name: str) -> bool:
        for parent in path.parents:
            if parent == root.parent:
                break
            if parent.name == "enums":
                init = parent / "__init__.py"
                return init.is_file() and name in (self.exported_names(init) or [])
        return True

    def offenders(self, root: Path) -> List[str]:
        found: List[str] = []
        if not root.is_dir():
            return found
        for path in sorted(root.rglob("*.py")):
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for node in tree.body:
                if not isinstance(node, ast.ClassDef) or not self.is_str_enum(node):
                    continue
                if not self.is_unique(node):
                    found.append(f"{path.name}: {node.name} is not decorated with unique")
                if path.stem != self.snake_case(node.name):
                    found.append(f"{path.name}: {node.name} is not in {self.snake_case(node.name)}.py")
                if not self.documents_members(node):
                    found.append(f"{path.name}: {node.name} does not list every member under Attributes")
                if not self.is_reexported(path, root, node.name):
                    found.append(f"{path.name}: {node.name} is not in the __all__ of enums/__init__.py")
        return found

    def write_tree(self, root: Path, file_name: str, source: str, exports: str) -> None:
        folder = root / "payments" / "enums"
        folder.mkdir(parents=True)
        (folder / "__init__.py").write_text(f"__all__ = [{exports}]\n", encoding="utf-8")
        (folder / file_name).write_text(source, encoding="utf-8")

    def test_the_real_tree_has_no_offender(self) -> None:
        root = Path(__file__).resolve().parents[1] / "src" / "erp_models"
        assert self.offenders(root) == []

    def test_a_well_formed_enum_passes(self, tmp_path: Path) -> None:
        self.write_tree(tmp_path, "payment_status.py", self.GOOD, '"PaymentStatus"')
        assert self.offenders(tmp_path) == []

    @pytest.mark.parametrize(
        ("file_name", "source", "exports"),
        [
            ("payment_status.py", GOOD.replace("@unique\n", ""), '"PaymentStatus"'),
            ("status.py", GOOD, '"PaymentStatus"'),
            ("payment_status.py", GOOD.replace("        DUE: The payment is awaited.\n", ""), '"PaymentStatus"'),
            ("payment_status.py", GOOD, ""),
        ],
        ids=["no-unique", "wrong-file-name", "member-missing-from-attributes", "not-re-exported"],
    )
    def test_each_broken_convention_is_reported_once(
        self, tmp_path: Path, file_name: str, source: str, exports: str
    ) -> None:
        self.write_tree(tmp_path, file_name, source, exports)
        assert len(self.offenders(tmp_path)) == 1

    def test_a_class_that_is_not_a_str_enum_is_ignored(self, tmp_path: Path) -> None:
        self.write_tree(tmp_path, "whatever.py", "class Whatever:\n    pass\n", "")
        assert self.offenders(tmp_path) == []

    def test_a_missing_tree_has_no_offender(self, tmp_path: Path) -> None:
        assert self.offenders(tmp_path / "absent") == []
