"""House rules that a reviewer should not have to catch by eye."""

from __future__ import annotations

from tests.conventions.convention_scanner import ConventionScanner
from tests.conventions.helpers import ROOT


class TestStructure:
    def test_no_nested_function(self) -> None:
        assert not ConventionScanner(ROOT).nested_functions()

    def test_no_staticmethod(self) -> None:
        assert not ConventionScanner(ROOT).staticmethods()

    def test_one_class_per_file(self) -> None:
        assert not ConventionScanner(ROOT).files_with_several_classes()

    def test_no_folder_holds_more_than_five_python_files(self) -> None:
        assert not ConventionScanner(ROOT).crowded_folders()

    def test_every_runnable_has_the_lifecycle_through_a_base_class(self) -> None:
        assert not ConventionScanner(ROOT).lifecycle_offenders()

    def test_every_node_is_called_rather_than_run(self) -> None:
        assert not ConventionScanner(ROOT).node_offenders()

    def test_no_pydantic_model_outside_the_models_layer(self) -> None:
        assert not ConventionScanner(ROOT).models_outside_models()

    def test_no_any_annotation(self) -> None:
        assert not ConventionScanner(ROOT).any_imports()
