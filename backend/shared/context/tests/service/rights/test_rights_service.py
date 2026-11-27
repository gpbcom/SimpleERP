from __future__ import annotations

import logging
from typing import List

import pytest
from erp_context.models.context.record_ref import RecordRef
from erp_context.models.context.user_context import UserContext
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.refusals.exceptions import SEAccessDeniedError
from erp_context.models.refusals.refusal_catalog import RefusalCatalog
from erp_context.service.rights.policy import Policy
from erp_context.service.rights.rights_service import RightsService

from tests.service.rights.allow_action_policy import AllowActionPolicy
from tests.service.rights.deny_action_policy import DenyActionPolicy


class TestRightsService:
    def service(self, policies: List[Policy], catalog: RefusalCatalog, logger: logging.Logger) -> RightsService:
        return RightsService(policies, catalog, logger)

    @pytest.mark.parametrize("action", ["read", "write", "delete", "export"])
    def test_with_no_policy_every_action_is_denied(
        self, action: str, user: UserContext, record: RecordRef, catalog: RefusalCatalog, logger: logging.Logger
    ) -> None:
        decision = self.service([], catalog, logger).decide(user, action, record)
        assert decision.allowed is False
        assert decision.reason is RefusalReason.NO_POLICY

    def test_an_allowing_policy_allows_only_its_action(
        self, user: UserContext, record: RecordRef, catalog: RefusalCatalog, logger: logging.Logger
    ) -> None:
        service = self.service([AllowActionPolicy("read")], catalog, logger)
        assert service.decide(user, "read", record).allowed is True
        assert service.decide(user, "read", record).reason is None
        refused = service.decide(user, "write", record)
        assert refused.allowed is False
        assert refused.reason is RefusalReason.NO_POLICY

    @pytest.mark.parametrize("allow_first", [True, False])
    def test_a_deny_beats_an_allow(
        self, allow_first: bool, user: UserContext, record: RecordRef, catalog: RefusalCatalog, logger: logging.Logger
    ) -> None:
        allow, deny = AllowActionPolicy("read"), DenyActionPolicy("read")
        policies: List[Policy] = [allow, deny] if allow_first else [deny, allow]
        decision = self.service(policies, catalog, logger).decide(user, "read", record)
        assert decision.allowed is False
        assert decision.reason is RefusalReason.POLICY_DENIED

    def test_a_record_of_another_company_is_refused_even_when_allowed(
        self, user: UserContext, other_company_record: RecordRef, catalog: RefusalCatalog, logger: logging.Logger
    ) -> None:
        service = self.service([AllowActionPolicy("read")], catalog, logger)
        decision = service.decide(user, "read", other_company_record)
        assert decision.allowed is False
        assert decision.reason is RefusalReason.OTHER_COMPANY

    @pytest.mark.parametrize("action", ["read", "write"])
    def test_allowed_equals_the_decision(
        self, action: str, user: UserContext, record: RecordRef, catalog: RefusalCatalog, logger: logging.Logger
    ) -> None:
        service = self.service([AllowActionPolicy("read")], catalog, logger)
        assert service.allowed(user, action, record) is service.decide(user, action, record).allowed

    def test_enforce_raises_with_the_reason_of_the_refusal(
        self, user: UserContext, record: RecordRef, catalog: RefusalCatalog, logger: logging.Logger
    ) -> None:
        service = self.service([DenyActionPolicy("read")], catalog, logger)
        with pytest.raises(SEAccessDeniedError) as raised:
            service.enforce(user, "read", record)
        assert raised.value.reason is RefusalReason.POLICY_DENIED

    def test_enforce_raises_no_policy_when_nothing_votes(
        self, user: UserContext, record: RecordRef, catalog: RefusalCatalog, logger: logging.Logger
    ) -> None:
        with pytest.raises(SEAccessDeniedError) as raised:
            self.service([], catalog, logger).enforce(user, "read", record)
        assert raised.value.reason is RefusalReason.NO_POLICY

    def test_enforce_returns_none_when_allowed(
        self, user: UserContext, record: RecordRef, catalog: RefusalCatalog, logger: logging.Logger
    ) -> None:
        assert self.service([AllowActionPolicy("read")], catalog, logger).enforce(user, "read", record) is None

    @pytest.mark.parametrize(
        ("policies", "reason"),
        [
            ([], RefusalReason.NO_POLICY),
            ([DenyActionPolicy("read")], RefusalReason.POLICY_DENIED),
        ],
    )
    def test_each_refusal_is_logged_at_warning_with_its_details(
        self,
        policies: List[Policy],
        reason: RefusalReason,
        user: UserContext,
        record: RecordRef,
        catalog: RefusalCatalog,
        logger: logging.Logger,
        caplog: pytest.LogCaptureFixture,
    ) -> None:
        with caplog.at_level(logging.DEBUG, logger=logger.name):
            self.service(policies, catalog, logger).decide(user, "read", record)
        warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
        assert len(warnings) == 1
        text = warnings[0].getMessage()
        code = catalog.code_for(reason).code
        for expected in (code, str(reason), user.user_id, user.company_id.value, "read", "invoice"):
            assert expected in text

    def test_a_refusal_for_another_company_is_logged_with_its_code(
        self,
        user: UserContext,
        other_company_record: RecordRef,
        catalog: RefusalCatalog,
        logger: logging.Logger,
        caplog: pytest.LogCaptureFixture,
    ) -> None:
        with caplog.at_level(logging.DEBUG, logger=logger.name):
            self.service([AllowActionPolicy("read")], catalog, logger).decide(user, "read", other_company_record)
        text = " ".join(r.getMessage() for r in caplog.records if r.levelno == logging.WARNING)
        assert catalog.code_for(RefusalReason.OTHER_COMPANY).code in text
        assert str(RefusalReason.OTHER_COMPANY) in text
        assert other_company_record.company_id.value in text

    def test_an_allowed_call_logs_no_warning(
        self,
        user: UserContext,
        record: RecordRef,
        catalog: RefusalCatalog,
        logger: logging.Logger,
        caplog: pytest.LogCaptureFixture,
    ) -> None:
        with caplog.at_level(logging.DEBUG, logger=logger.name):
            self.service([AllowActionPolicy("read")], catalog, logger).decide(user, "read", record)
        assert [r for r in caplog.records if r.levelno >= logging.WARNING] == []

    def test_no_log_line_holds_the_content_of_a_record(
        self,
        user: UserContext,
        record: RecordRef,
        catalog: RefusalCatalog,
        logger: logging.Logger,
        caplog: pytest.LogCaptureFixture,
    ) -> None:
        with caplog.at_level(logging.DEBUG, logger=logger.name):
            self.service([DenyActionPolicy("read")], catalog, logger).decide(user, "read", record)
        text = " ".join(r.getMessage() for r in caplog.records)
        assert "rec-42" in text
        for forbidden in ("RecordRef(", "UserContext(", "record_id=", "model_dump"):
            assert forbidden not in text
