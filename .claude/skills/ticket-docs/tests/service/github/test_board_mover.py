from __future__ import annotations

import json
import logging

import pytest

from tests.builders.fake_gh import FakeGh
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.github.board_mover import BoardMover
from ticket_docs.service.github.exceptions import SEBoardAnswerError, SEBoardStatusUnknownError
from ticket_docs.storage.github.gh_client import GhClient


class TestBoardMover:
    def mover(self, logger: logging.Logger) -> BoardMover:
        catalog = GithubCatalog.load(GithubCatalog.SKILL_DIR / "conf" / "github.yaml")
        return BoardMover(GhClient(catalog.full_name, logger=logger), catalog, logger)

    def items(self, gh: FakeGh, nodes: str) -> None:
        issue = {"id": "I_7", "projectItems": {"nodes": json.loads(nodes)}}
        answer = json.dumps({"data": {"repository": {"issue": issue}}})
        gh.answer(["api", "graphql", "-f", f"query={BoardMover.ITEMS_QUERY}"], stdout=answer)

    def test_an_item_already_on_the_board_gets_its_status(self, logger: logging.Logger, gh: FakeGh) -> None:
        self.items(gh, '[{"id": "PVTI_other", "project": {"id": "PVT_x"}}, '
                       '{"id": "PVTI_7", "project": {"id": "PVT_kwHOBZDE-c4Bq9-t"}}]')  # fmt: skip
        gh.answer(["api", "graphql"], stdout=json.dumps({"data": {"updateProjectV2ItemFieldValue": {}}}))
        assert self.mover(logger).move("GH-7", "In progress") == "PVTI_7"
        calls = gh.calls()
        assert calls[0][-6:] == ["-f", "owner=gpbcom", "-f", "repo=simple-erp", "-F", "number=7"]
        assert calls[1][3] == f"query={BoardMover.UPDATE_MUTATION}"
        assert calls[1][4:] == [
            "-f", "project=PVT_kwHOBZDE-c4Bq9-t", "-f", "item=PVTI_7",
            "-f", "field=PVTSSF_lAHOBZDE-c4Bq9-tzhpSuG0", "-f", "option=63440315",
        ]  # fmt: skip

    def test_an_issue_off_the_board_is_added_first(self, logger: logging.Logger, gh: FakeGh) -> None:
        self.items(gh, "[]")
        gh.answer(
            ["api", "graphql", "-f", f"query={BoardMover.ADD_MUTATION}"],
            stdout=json.dumps({"data": {"addProjectV2ItemById": {"item": {"id": "PVTI_new"}}}}),
        )
        gh.answer(["api", "graphql"], stdout="{}")
        assert self.mover(logger).move("GH-7", "In review") == "PVTI_new"
        calls = gh.calls()
        assert calls[1][4:] == ["-f", "project=PVT_kwHOBZDE-c4Bq9-t", "-f", "content=I_7"]
        assert calls[2][-1] == "option=f5693b1f"

    def test_an_unknown_status_names_the_valid_ones(self, logger: logging.Logger, gh: FakeGh) -> None:
        with pytest.raises(SEBoardStatusUnknownError, match="Backlog, Ready, In progress, In review, QA, Done"):
            self.mover(logger).move("GH-7", "Doing")
        assert gh.calls() == []

    def test_an_issue_github_does_not_know_is_refused(self, logger: logging.Logger, gh: FakeGh) -> None:
        gh.answer(["api", "graphql"], stdout='{"data": {"repository": {"issue": null}}}')
        with pytest.raises(SEBoardAnswerError):
            self.mover(logger).move("GH-404", "Done")
