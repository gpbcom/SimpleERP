# T0.14: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- Every service is a regular FastAPI application served by uvicorn with `--factory`, with no command line (D406, AGENT.md "Layout"; [`backend/services/platform/src/erp_platform/api/app_factory.py:45-61`](../../../backend/services/platform/src/erp_platform/api/app_factory.py#L45-L61)).
- The image is built from the repository root, because [`uv.lock`](../../../uv.lock) is there (D419, D438; [`backend/services/platform/Dockerfile:2`](../../../backend/services/platform/Dockerfile#L2)).
- A refused call answers problem+json with its D122 code, and no secret is in the body (REQ-T05-03, acceptance criteria 3 and 4 of [TICKET.md](TICKET.md)).
- A request without a company is refused, through the middleware of T0.09 (REQ-T01-02, criterion 5).
- `tests/conventions/` passes with no change (criterion 6): one class per file, at most five files per folder, an exception per file, no module-level code.

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | How the shared refusal catalogue reaches the image | `COPY` into `conf/catalogs/` in the runtime stage | Ship it as `erp_context` package data | The path in `backend/shared/context/conf/` must stay where it is |
| [D2](#d2) | Where the problem body comes from | Catalogue keys only, no free text | Build it from the exception | `action` and `reference` of the catalogue are dropped for now |
| [D3](#d3) | How `/v1/health` skips the company check | `public_paths` from configuration, exact match | A path hard-coded in the builder | One more configuration key |
| [D4](#d4) | Python package name | `erp_platform`, uv name `platform` | `platform` | Two names for one service |
| [D5](#d5) | Health path and body | `GET /v1/health`, `{"status": "ok"}` | Another path or a richer body | A liveness answer only |
| [D6](#d6) | What the image copies from the SDK | Only [`sdk/pyproject.toml`](../../../sdk/pyproject.toml) | The whole `sdk/` | Depends on the lock needing only the manifest |

## <a id="d1"></a>D1: How the shared refusal catalogue reaches the image

**Chosen:** `COPY` the file from the build context into `/app/conf/catalogs/` in the runtime stage · **Where:** [`backend/services/platform/Dockerfile:24`](../../../backend/services/platform/Dockerfile#L24) · **Source:** K20

| Option | For | Against |
| --- | --- | --- |
| ✅ Extra `COPY` in the runtime stage | Changes the Dockerfile only, with no code or lock change, as the K20 brief demands. The image test proves it. [`app_builder.py:65-68`](../../../backend/services/platform/src/erp_platform/api/http/app_builder.py#L65-L68) finds the file beside the error catalogue | Reads the catalogue from the build context at its source path, so that path must not move. Every next service repeats the line |
| Package the catalogue inside `erp_context`'s `src/` | No `COPY` for any service | Changes a shared library and its lock, outside this ticket's files. Not done in K20 |
| Copy it from the build stage's `/repo` | Same result | No reason given for preferring it. The build context is already available to the runtime stage |

**Trade-off:** a Dockerfile line instead of a change to a shared library, because the ticket owns only the service.

**Revisit when:** the next service needs the middleware, or `erp_context` is next changed: ship the file as package data (a follow-up of the review).

## <a id="d2"></a>D2: Where the problem body comes from

**Chosen:** `ProblemService.problem` takes a code and a status and fills the body from the catalogue entry · **Where:** [`backend/services/platform/src/erp_platform/service/problems/problem_service.py:55-64`](../../../backend/services/platform/src/erp_platform/service/problems/problem_service.py#L55-L64) · **Source:** read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ Body from catalogue keys | No exception text can reach a body (REQ-T05-03 criterion 2, AC4). The handler never reads the exception ([`problem_handler.py:105-116`](../../../backend/services/platform/src/erp_platform/api/http/problem_handler.py#L105-L116)) | The title and detail are translation keys, not sentences. `action` and `reference` are dropped, which D122 asks for |
| Build the detail from the exception message | More specific answers | A message may quote a secret, which AC4 forbids |

**Trade-off:** less detail now for a body that cannot leak. The missing `action` and `reference` are a follow-up.

**Revisit when:** `ProblemDetails` gains `action` and `reference`, to match the `erp_context` refusals.

## <a id="d3"></a>D3: How `/v1/health` skips the company check

**Chosen:** the configuration's `public_paths` is given to the middleware's own `public_paths`, which matches exactly · **Where:** [`backend/services/platform/src/erp_platform/api/http/app_builder.py:90`](../../../backend/services/platform/src/erp_platform/api/http/app_builder.py#L90), [`backend/services/platform/conf/app.yaml:1-2`](../../../backend/services/platform/conf/app.yaml#L1-L2) · **Source:** read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ Paths in `conf/app.yaml` | AGENT.md: no data hard-coded in Python, every default written in `conf/app.yaml`. `/v1/health` is the only open path | A config key to validate ([`platform_config.py`](../../../backend/services/platform/src/erp_platform/models/config/platform_config.py)) |
| Constant in the builder | No config key | AGENT.md puts data in conf, not in Python |

**Trade-off:** one more validated key, so that an operator can see the open paths.

**Revisit when:** a second public path is needed (it is one line of config).

## <a id="d4"></a>D4: Python package name

**Chosen:** package `erp_platform`, uv name `platform` · **Where:** [`backend/services/platform/pyproject.toml:2`](../../../backend/services/platform/pyproject.toml#L2) and [`:32`](../../../backend/services/platform/pyproject.toml#L32) · **Source:** [TICKET.md](TICKET.md) assumption

| Option | For | Against |
| --- | --- | --- |
| ✅ `erp_platform` | The `erp_` prefix of the shared libraries. `platform` would shadow the standard-library module | The uv name and the import name differ |
| Package `platform` | Same name everywhere | Shadows the standard-library `platform` module, which the ticket anticipated |

**Trade-off:** two names, against a collision with the standard library.

**Revisit when:** never expected, since the collision stays.

## <a id="d5"></a>D5: Health path and body

**Chosen:** `GET /v1/health` answers `{"status": "ok"}` · **Where:** [`backend/services/platform/src/erp_platform/api/http/health_router.py:37`](../../../backend/services/platform/src/erp_platform/api/http/health_router.py#L37) · **Source:** [TICKET.md](TICKET.md) assumption

| Option | For | Against |
| --- | --- | --- |
| ✅ `/v1/health`, status only | The specifications name no path: the most conservative choice. The image `HEALTHCHECK` uses it | Says only that the process answers, never that a dependency is up |
| A richer body | More to monitor | Nothing in the specifications asks for it, and the skeleton has no dependency |

**Trade-off:** a liveness answer is enough for AC2 and the healthcheck.

**Revisit when:** the service gets a database or a bus: add readiness (open point: no ticket names it).

## <a id="d6"></a>D6: What the image copies from the SDK

**Chosen:** only [`sdk/pyproject.toml`](../../../sdk/pyproject.toml) · **Where:** [`backend/services/platform/Dockerfile:11`](../../../backend/services/platform/Dockerfile#L11) · **Source:** read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ Manifest only ([`sdk/pyproject.toml`](../../../sdk/pyproject.toml)) | Enough for `uv sync --locked` to see the workspace member, per the review note. A smaller context layer | If the lock ever needs more of the SDK, the build fails |
| Copy all of `sdk/` | Cannot miss a file | Puts SDK code in the build stage for no use |

**Trade-off:** a leaner build for a dependency on how uv reads the workspace.

**Revisit when:** `uv sync --locked` in the image fails on the SDK.

## 📝 Assumptions behind the choices

- The context middleware is erp_context's (T0.09): supports [D1](#d1) and [D3](#d3).
- The package is named `erp_platform`: supports [D4](#d4).
- The health path is `GET /v1/health`: supports [D5](#d5).
- The roadmap's "factories" are `AppFactory`: supports the choice of one factory and no runnable.
