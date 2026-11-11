from __future__ import annotations

from typing import Optional

import pytest

from harness_core.models.branches.branch_kind import BranchKind
from harness_core.models.branches.branch_name import BranchName
from harness_core.models.branches.exceptions import SEBranchNameInvalidValue


class TestBranchName:
    @pytest.mark.parametrize(
        ("value", "kind", "ticket", "version"),
        [
            ("master", BranchKind.MASTER, None, None),
            ("main", BranchKind.OTHER, None, None),
            ("develop", BranchKind.DEVELOP, None, None),
            ("feature/GH-12-add-customers", BranchKind.FEATURE, "GH-12", None),
            ("bugfix/GH-7-wrong-total", BranchKind.BUGFIX, "GH-7", None),
            ("release/1.4.0", BranchKind.RELEASE, None, "1.4.0"),
            ("hotfix/1.4.1-GH-30-crash-on-save", BranchKind.HOTFIX, "GH-30", "1.4.1"),
            ("dependabot/uv/pydantic-2.12", BranchKind.OTHER, None, None),
        ],
    )
    def test_parse(self, value: str, kind: BranchKind, ticket: Optional[str], version: Optional[str]) -> None:
        branch = BranchName.parse(value)
        assert (branch.value, branch.kind, branch.ticket, branch.version) == (value, kind, ticket, version)

    @pytest.mark.parametrize(
        "value",
        ["feature/add-customers", "feature/GH-12", "bugfix/gh-7-x", "release/1.4", "hotfix/1.4.1", "feature/GH-1-Big"],
    )
    def test_gitflow_prefixes_need_their_full_shape(self, value: str) -> None:
        with pytest.raises(SEBranchNameInvalidValue):
            BranchName.parse(value)

    def test_a_ticket_branch_carries_work(self) -> None:
        assert BranchName.parse("feature/GH-1-x").carries_ticket_work
        assert BranchName.parse("hotfix/1.0.1-GH-2-x").carries_ticket_work
        assert not BranchName.parse("release/1.0.0").carries_ticket_work

    def test_round_trip(self) -> None:
        branch = BranchName.parse("feature/GH-12-add-customers")
        assert BranchName.model_validate(branch.model_dump()) == branch
