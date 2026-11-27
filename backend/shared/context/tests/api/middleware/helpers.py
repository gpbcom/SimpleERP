from __future__ import annotations

from functools import partial
from logging import Logger, getLogger
from pathlib import Path
from typing import Dict, List, Optional

from erp_context.api.middleware.company_context_middleware import CompanyContextMiddleware
from erp_context.api.problems.problem_builder import ProblemBuilder
from erp_context.models.context.context_config import ContextConfig
from erp_context.models.refusals.refusal_catalog import RefusalCatalog
from erp_context.service.context.company_context_service import CompanyContextService
from erp_context.storage.context.request_context_store import RequestContextStore
from fastapi import FastAPI

COMPANY_HEADER = "X-Company-Id"
USER_HEADER = "X-User-Id"
REQUEST_HEADER = "X-Request-Id"
PUBLIC_PATH = "/health"
PROTECTED_PATH = "/whoami"
SECRET = "Bearer s3cr3t-token-value"
LOGGER_NAME = "erp_context.tests.middleware"


def catalog_path() -> Path:
    return Path(__file__).resolve().parents[3] / "conf" / "catalogs" / "refusal_codes.yaml"


def load_catalog() -> RefusalCatalog:
    return RefusalCatalog.load(catalog_path())


def whoami(calls: List[str], service: CompanyContextService, store: RequestContextStore) -> Dict[str, Optional[str]]:
    """Return the context bound for the call, read through the service layer and through the storage layer."""
    calls.append(PROTECTED_PATH)
    seen_by_service = service.peek()
    seen_by_storage = store.get()
    return {
        "service_company": seen_by_service.user.company_id.value if seen_by_service else None,
        "service_user": seen_by_service.user.user_id if seen_by_service else None,
        "service_request": seen_by_service.request_id if seen_by_service else None,
        "storage_company": seen_by_storage.user.company_id.value if seen_by_storage else None,
        "storage_user": seen_by_storage.user.user_id if seen_by_storage else None,
    }


def health(calls: List[str], store: RequestContextStore) -> Dict[str, Optional[str]]:
    """Return a status and the request id of the context bound for the call, if any."""
    calls.append(PUBLIC_PATH)
    seen = store.get()
    return {"status": "ok", "bound": None if seen is None else seen.request_id}


def build_app(logger: Optional[Logger] = None) -> FastAPI:
    """Build a real FastAPI app behind the middleware, with a protected route and a public one."""
    store = RequestContextStore()
    service = CompanyContextService(store)
    app = FastAPI()
    calls: List[str] = []
    app.state.calls = calls
    app.add_api_route(PROTECTED_PATH, partial(whoami, calls, service, store), methods=["GET"])
    app.add_api_route(PUBLIC_PATH, partial(health, calls, store), methods=["GET"])
    app.add_middleware(
        CompanyContextMiddleware,
        config=ContextConfig(public_paths=[PUBLIC_PATH]),
        context=service,
        builder=ProblemBuilder(load_catalog()),
        logger=logger if logger else getLogger(LOGGER_NAME),
    )
    return app


def valid_headers(company: str = "C-12", user: str = "U-7", request_id: Optional[str] = "req-1") -> Dict[str, str]:
    headers = {COMPANY_HEADER: company, USER_HEADER: user, "Authorization": SECRET}
    if request_id is not None:
        headers[REQUEST_HEADER] = request_id
    return headers
