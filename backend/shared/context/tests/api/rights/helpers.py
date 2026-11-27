from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from erp_context.api.middleware.company_context_middleware import CompanyContextMiddleware
from erp_context.api.problems.problem_builder import ProblemBuilder
from erp_context.api.problems.refusal_handler import RefusalHandler
from erp_context.api.rights.rights_guard import RightsGuard
from erp_context.models.context.context_config import ContextConfig
from erp_context.models.context.record_ref import RecordRef
from erp_context.models.context.user_context import UserContext
from erp_context.models.refusals.exceptions import SEAccessError
from erp_context.models.refusals.refusal_catalog import RefusalCatalog
from erp_context.service.context.company_context_service import CompanyContextService
from erp_context.service.rights.policy import Policy
from erp_context.service.rights.rights_service import RightsService
from erp_context.storage.context.request_context_store import RequestContextStore
from erp_models.ids.company_id import CompanyId
from fastapi import FastAPI, Request

USER_ID = "user-9b2c"
COMPANY_ID = "company-7f3a"
OTHER_COMPANY_ID = "company-1d4e"
REQUEST_ID = "req-5e8f"
SECRET_TOKEN = "Bearer secret-token-123"


def load_catalog() -> RefusalCatalog:
    """Load the shipped refusal catalogue, found from this file."""
    path = Path(__file__).resolve().parents[3] / "conf" / "catalogs" / "refusal_codes.yaml"
    return RefusalCatalog.load(path)


def a_user(company: str = COMPANY_ID) -> UserContext:
    """Build the user of the requests."""
    return UserContext(user_id=USER_ID, company_id=CompanyId(value=company))


def a_record(company: str = COMPANY_ID, record_type: str = "invoice", record_id: str = "R-1") -> RecordRef:
    """Build a record reference of a company."""
    return RecordRef(record_type=record_type, company_id=CompanyId(value=company), record_id=record_id)


def request_headers() -> Dict[str, str]:
    """Build the headers of a request that carries a company, a user, a request id and a secret."""
    return {
        "X-Company-Id": COMPANY_ID,
        "X-User-Id": USER_ID,
        "X-Request-Id": REQUEST_ID,
        "Authorization": SECRET_TOKEN,
    }


async def read_record(request: Request, record_type: str, record_id: str, action: str, company: str) -> Dict[str, str]:
    """Guard a record, then answer 200. ``company`` is the company of the record."""
    guard: RightsGuard = request.app.state.guard
    guard.check(action, a_record(company, record_type, record_id))
    return {"record": record_id}


def build_rights(policies: List[Policy], catalog: RefusalCatalog) -> RightsService:
    """Build the rights service that both the route and the direct calls use."""
    return RightsService(policies, catalog)


def build_app(rights: RightsService, catalog: RefusalCatalog) -> FastAPI:
    """Build a real app with the middleware, the refusal handler and the guarded route."""
    context = CompanyContextService(RequestContextStore())
    app = FastAPI()
    app.state.guard = RightsGuard(rights, context)
    app.add_middleware(
        CompanyContextMiddleware,
        config=ContextConfig(),
        context=context,
        builder=ProblemBuilder(catalog),
    )
    app.add_exception_handler(SEAccessError, RefusalHandler(ProblemBuilder(catalog), context))
    app.add_api_route("/records/{record_type}/{record_id}", read_record, methods=["GET"])
    return app
