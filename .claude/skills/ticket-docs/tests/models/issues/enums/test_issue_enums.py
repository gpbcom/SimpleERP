from __future__ import annotations

from ticket_docs.models.issues.enums import FormField, IssueState


class TestIssueEnums:
    def test_the_issue_states_are_the_rest_api_ones(self) -> None:
        assert [state.value for state in IssueState] == ["open", "closed"]

    def test_the_form_fields_are_the_issue_form_labels(self) -> None:
        assert [field.value for field in FormField] == ["Component", "Feature", "Family", "Type", "Priority"]
