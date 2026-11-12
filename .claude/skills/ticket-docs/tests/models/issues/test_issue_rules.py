from __future__ import annotations

import re
from pathlib import Path
from typing import Dict

import pytest
from pydantic import JsonValue, ValidationError

from ticket_docs.models.issues.exceptions import (
    SEIssueRulesInconsistent,
    SEIssueRulesInvalidFamilies,
    SEIssueRulesInvalidLength,
    SEIssueRulesInvalidList,
    SEIssueRulesInvalidMapping,
    SEIssueRulesInvalidPattern,
    SEIssueRulesInvalidReferenceKinds,
    SEIssueRulesInvalidText,
    SEIssueRulesUnreadable,
)
from ticket_docs.models.issues.issue_rules import IssueRules


class TestIssueRules:
    CONF = Path(__file__).resolve().parents[3] / "conf" / "issue-rules.yaml"
    SHA = "b2507e41547ef8017f964d4ee7a6283e6a19e3ef"

    def valid(self) -> Dict[str, JsonValue]:
        return {
            "feature_label": "feature",
            "families": {"HARNESS": ["HARNESS"], "PRODUCT": ["BACKEND", "FRONTEND"]},
            "components": ["HARNESS", "BACKEND", "FRONTEND"],
            "title_pattern": r"^\[(?P<label>[A-Z]+)\] [A-Z].*$",
            "title_max_length": 79,
            "ticket_sections": ["Description", "References"],
            "feature_sections": ["Goal", "Tickets"],
            "implementation_bullets": ["Approach"],
            "acceptance_pattern": r"^- \[ \] \*\*(?P<id>AC\d+)\*\* Given .+$",
            "tests_columns": ["ID", "Level", "Proves", "AC"],
            "references_columns": ["ID", "What", "Link"],
            "reference_kinds": {
                "spec": {"paths": ["docs/specs/"], "patterns": {"feature": r"f\d{2}"}},
                "harness": {"paths": [".claude/"], "patterns": {"rule": r"GIT-\d+"}},
            },
            "required_reference_kinds": {"HARNESS": "harness", "BACKEND": "spec", "FRONTEND": "spec"},
            "permalink": "https://github.com/{repository}/blob/{sha}/{path}",
            "permalink_pattern": r"^https://github\.com/{repository}/blob/(?P<sha>[0-9a-f]{40})/(?P<path>[^#?]+)",
            "repository_link_pattern": r"^https://github\.com/{repository}/(?:blob|tree)/",
            "pinned_prefixes": ["docs/specs/"],
            "type_labels": {"feature": "type:feature", "bug": "type:bug"},
            "type_kinds": {"feature": "Feature", "bug": "Bug"},
            "default_type": "feature",
            "priority_labels": {"high": "priority:high"},
            "priority_options": {"high": "High"},
            "default_priority": "high",
            "feature_kind": "Feature",
            "new_issue_statuses": ["Backlog", "Ready"],
            "comment_marker": "<!-- issue-check -->",
            "empty_form_answer": "_No response_",
            "approval_label": "needs-maintainer-approval",
            "approval_statuses": ["Backlog"],
        }

    def test_defaults(self) -> None:
        rules = IssueRules.model_validate(self.valid())
        assert rules.title_max_length == 79
        assert rules.family_ticket_limits == {}

    def test_full_valid_construction(self) -> None:
        rules = IssueRules.load(self.CONF)
        assert rules.families == {
            "HARNESS": ["HARNESS"],
            "SPECS": ["SPECS"],
            "PRODUCT": ["INFRA", "BACKEND", "FRONTEND", "E2E-TESTS", "LOAD-TESTS", "UNIT-TESTS"],
            "TESTS": ["E2E-TESTS", "LOAD-TESTS", "UNIT-TESTS"],
            "USER": ["USER-FEATURE-REQUEST", "USER-REPORTED-BUG"],
        }
        assert rules.components == [
            "HARNESS",
            "SPECS",
            "INFRA",
            "BACKEND",
            "FRONTEND",
            "E2E-TESTS",
            "LOAD-TESTS",
            "UNIT-TESTS",
            "USER-FEATURE-REQUEST",
            "USER-REPORTED-BUG",
        ]
        assert rules.ticket_sections == [
            "Description",
            "Implementation",
            "Acceptance criteria",
            "Tests",
            "References",
            "Attachments",
        ]
        assert rules.feature_sections == ["Goal", "Specifications delivered", "Out of scope", "Tickets"]
        assert rules.reference_kinds["spec"].matches("br-f01-07")
        assert rules.reference_kinds["harness"].matches("GIT-10")
        assert rules.required_reference_kinds["INFRA"] == "spec"
        assert rules.required_reference_kinds["E2E-TESTS"] == "spec"
        assert rules.required_reference_kinds["LOAD-TESTS"] == "spec"
        assert rules.required_reference_kinds["UNIT-TESTS"] == "spec"
        assert rules.new_issue_statuses == ["Backlog", "Ready"]

    def test_labels_are_read_as_families_and_components(self) -> None:
        rules = IssueRules.load(self.CONF)
        assert rules.families_of(["feature", "HARNESS", "priority:high"]) == ["HARNESS"]
        assert rules.components_of(["type:bug", "INFRA", "BACKEND"]) == ["INFRA", "BACKEND"]
        assert rules.allows("PRODUCT", "FRONTEND")
        assert not rules.allows("HARNESS", "INFRA")
        assert not rules.allows("UNKNOWN", "INFRA")

    def test_test_tickets_belong_to_product_and_tests_features_only(self) -> None:
        rules = IssueRules.load(self.CONF)
        assert rules.families_of(["feature", "TESTS"]) == ["TESTS"]
        assert rules.components_of(["E2E-TESTS", "priority:low"]) == ["E2E-TESTS"]
        for component in ("E2E-TESTS", "LOAD-TESTS", "UNIT-TESTS"):
            assert rules.allows("PRODUCT", component)
            assert rules.allows("TESTS", component)
            assert not rules.allows("HARNESS", component)
            assert not rules.allows("SPECS", component)
        assert not rules.allows("TESTS", "BACKEND")

    def test_customer_requests_are_user_features_of_one_ticket_waiting_for_approval(self) -> None:
        rules = IssueRules.load(self.CONF)
        assert rules.families_of(["feature", "USER", "needs-maintainer-approval"]) == ["USER"]
        assert rules.components_of(["USER-REPORTED-BUG", "needs-maintainer-approval"]) == ["USER-REPORTED-BUG"]
        assert rules.family_ticket_limits == {"USER": 1}
        assert rules.approval_label == "needs-maintainer-approval"
        assert rules.approval_statuses == ["Backlog"]
        for component in ("USER-FEATURE-REQUEST", "USER-REPORTED-BUG"):
            assert rules.required_reference_kinds[component] == "spec"
            assert rules.allows("USER", component)
            for family in ("HARNESS", "SPECS", "PRODUCT", "TESTS"):
                assert not rules.allows(family, component)
        assert not rules.allows("USER", "BACKEND")

    @pytest.mark.parametrize(
        ("title", "label"),
        [
            ("[E2E-TESTS] Cover the checkout journey", "E2E-TESTS"),
            ("[LOAD-TESTS] Hold 200 invoices per minute", "LOAD-TESTS"),
            ("[UNIT-TESTS] Cover the VAT rounding rules", "UNIT-TESTS"),
            ("[BACKEND] Store a customer with its VAT number", "BACKEND"),
            ("[USER-FEATURE-REQUEST] Export the invoices to CSV", "USER-FEATURE-REQUEST"),
            ("[USER-REPORTED-BUG] Fix the VAT total on credit notes", "USER-REPORTED-BUG"),
        ],
    )
    def test_a_title_starts_with_its_component_label(self, title: str, label: str) -> None:
        rules = IssueRules.load(self.CONF)
        match = re.match(rules.title_pattern, title)
        assert match is not None
        assert match.group("label") == label
        assert len(title) <= rules.title_max_length

    def test_the_kind_of_a_path_comes_from_its_prefix(self) -> None:
        rules = IssueRules.load(self.CONF)
        assert rules.kind_of("docs/specs/05-non-functional/updates.md") == "spec"
        assert rules.kind_of(".claude/rules/git-rules-and-deploy.md") == "harness"
        assert rules.kind_of("AGENT.md") == "harness"
        assert rules.kind_of("docs/technical/ci-cd-and-stages.md") is None

    def test_permalinks_are_built_and_read_for_one_repository(self) -> None:
        rules = IssueRules.load(self.CONF)
        link = rules.permalink_of("gpbcom/simple-erp", self.SHA, "docs/specs/README.md")
        assert link == f"https://github.com/gpbcom/simple-erp/blob/{self.SHA}/docs/specs/README.md"
        match = rules.permalink_regex("gpbcom/simple-erp").match(f"{link}#anchor")
        assert match is not None
        assert (match["sha"], match["path"]) == (self.SHA, "docs/specs/README.md")
        assert rules.permalink_regex("gpbcom/other").match(link) is None
        assert rules.repository_link_regex("gpbcom/simple-erp").match(
            "https://github.com/gpbcom/simple-erp/blob/develop/AGENT.md"
        )

    @pytest.mark.parametrize(("name", "default"), [("title_max_length", 79), ("family_ticket_limits", {})])
    def test_none_becomes_the_default(self, name: str, default: JsonValue) -> None:
        assert getattr(IssueRules.model_validate({**self.valid(), name: None}), name) == default

    def test_the_approval_label_is_required(self) -> None:
        values = self.valid()
        del values["approval_label"]
        with pytest.raises(ValidationError):
            IssueRules.model_validate(values)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("feature_label", " ", SEIssueRulesInvalidText),
            ("comment_marker", 3, SEIssueRulesInvalidText),
            ("components", [], SEIssueRulesInvalidList),
            ("ticket_sections", "Description", SEIssueRulesInvalidList),
            ("tests_columns", ["ID", ""], SEIssueRulesInvalidList),
            ("title_pattern", "[A-Z", SEIssueRulesInvalidPattern),
            ("title_pattern", r"^\[[A-Z]+\]", SEIssueRulesInvalidPattern),
            ("acceptance_pattern", r"^- AC\d+", SEIssueRulesInvalidPattern),
            ("permalink_pattern", r"^https://github\.com/{repository}/blob/", SEIssueRulesInvalidPattern),
            ("title_max_length", 5, SEIssueRulesInvalidLength),
            ("title_max_length", True, SEIssueRulesInvalidLength),
            ("title_max_length", 500, SEIssueRulesInvalidLength),
            ("families", {}, SEIssueRulesInvalidFamilies),
            ("families", {"HARNESS": []}, SEIssueRulesInvalidFamilies),
            ("families", ["HARNESS"], SEIssueRulesInvalidFamilies),
            ("type_labels", {}, SEIssueRulesInvalidMapping),
            ("priority_options", {"high": ""}, SEIssueRulesInvalidMapping),
            ("reference_kinds", {}, SEIssueRulesInvalidReferenceKinds),
            ("reference_kinds", ["spec"], SEIssueRulesInvalidReferenceKinds),
            ("family_ticket_limits", {"USER": 0}, SEIssueRulesInvalidFamilies),
            ("family_ticket_limits", {"USER": True}, SEIssueRulesInvalidFamilies),
            ("family_ticket_limits", {"USER": "1"}, SEIssueRulesInvalidFamilies),
            ("family_ticket_limits", {"": 1}, SEIssueRulesInvalidFamilies),
            ("family_ticket_limits", ["USER"], SEIssueRulesInvalidFamilies),
            ("approval_label", " ", SEIssueRulesInvalidText),
            ("approval_label", 3, SEIssueRulesInvalidText),
            ("approval_statuses", [], SEIssueRulesInvalidList),
            ("approval_statuses", "Backlog", SEIssueRulesInvalidList),
            ("approval_statuses", ["Backlog", ""], SEIssueRulesInvalidList),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            IssueRules.model_validate({**self.valid(), name: value})

    @pytest.mark.parametrize(
        ("name", "value"),
        [
            ("families", {"HARNESS": ["HARNESS"], "PRODUCT": ["INFRA"]}),
            ("required_reference_kinds", {"HARNESS": "doc", "BACKEND": "spec", "FRONTEND": "spec"}),
            ("required_reference_kinds", {"HARNESS": "harness"}),
            ("type_kinds", {"feature": "Feature"}),
            ("priority_options", {"low": "Low"}),
            ("default_type", "chore"),
            ("default_priority", "low"),
            ("family_ticket_limits", {"UNKNOWN": 1}),
            ("approval_label", "HARNESS"),
            ("approval_label", "BACKEND"),
            ("approval_statuses", ["Done"]),
        ],
    )
    def test_rejects_rules_that_contradict_each_other(self, name: str, value: JsonValue) -> None:
        with pytest.raises(SEIssueRulesInconsistent):
            IssueRules.model_validate({**self.valid(), name: value})

    def test_a_missing_file_is_unreadable(self, tmp_path: Path) -> None:
        with pytest.raises(SEIssueRulesUnreadable):
            IssueRules.load(tmp_path / "missing.yaml")

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            IssueRules.model_validate({**self.valid(), "areas": ["area:api"]})

    def test_round_trip(self) -> None:
        rules = IssueRules.load(self.CONF)
        assert IssueRules.model_validate(rules.model_dump()) == rules
