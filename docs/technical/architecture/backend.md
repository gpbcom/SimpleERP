# Back end

The back-end services: language, frameworks, service boundaries, data access, jobs and workers, events. Nothing of the
target is built yet.

## Today

The back end today is the Python 3.13 code under `src/`, described in [Architecture](architecture.md).

Ticket T0.05 builds the first shared library, `backend/shared/lifecycle` (package `erp_lifecycle`): the `Runnable` and `AsyncRunnable` base classes with `initialize()`, `run()`, `close()` and `execute()`, which always closes, and the abstract `RunnableFactory` that every concrete factory subclasses, as set by [D406](../../specs/06-decisions/technical/d406-back-end.md) and [AGENT.md](../../../AGENT.md#lifecycle-and-factories) ("Lifecycle and factories").

The shared libraries `backend/shared/logging` (package `erp_logging`, [pyproject](../../../backend/shared/logging/pyproject.toml))
and `backend/shared/config` (package `erp_config`, [pyproject](../../../backend/shared/config/pyproject.toml)) exist too.
They hold no business rules: logging writes each line to the console and to the files of `logs/`, and configuration loads
each service's `conf/app.yaml` ([Configuration](configuration.md#shared-configuration-library-erp_config)). They sit in
the `backend/shared/` folder of [D438](../../specs/06-decisions/technical/d438-repository-layout.md) and follow
[D406](../../specs/06-decisions/technical/d406-back-end.md).

Ticket T0.12 builds the country-pack rules library, `backend/shared/country-rules` (package `erp_country_rules`). `CountryRules.value(rule, country, date)` returns the value in force at the date of the
fact, as an exact `Decimal`, or as the `erp_models` money with its currency. Its layers follow `AGENT.md`: the models
`CountryPack`, `CountryRule`, `RuleVersion` and `CountryRulesConfig`; the storage `CountryPackRepository`, which reads
a pack from `<packs_dir>/<country in lower case>/rules.yaml` (by default `packs/countries`); and the service
`CountryRules`. A pack holds `country`, `version` and `rules`; each rule holds versions with `valid_from`, an inclusive
optional `valid_to` and a `value`. Versions never overlap, and a float value is refused. Signed packs
([REQ-T11-01](../../specs/03-technical/t11-legal-corpora/requirements/req-t11-01-signed-packs.md)) and the pack registry
are not built yet. The interface and the requirement are [I-T11-01](../../specs/03-technical/t11-legal-corpora/interfaces/i-t11-01-rules-library.md)
and [REQ-T11-02](../../specs/03-technical/t11-legal-corpora/requirements/req-t11-02-rules-library.md).

## Target design (specified in GH-2, not built yet)

**Language and framework (D406).** Python 3.13 with uv, Pydantic models and the api → service → storage layers
(`AGENT.md`); FastAPI for the HTTP services.

**A regular FastAPI application (D406, 2026-11-27).** Every service is a regular FastAPI application. Its `api` layer is
the application: the routers, their dependencies, the middlewares and the exception handlers, and the application
factory `AppFactory.create()` in `api/app_factory.py`, which reads `conf/app.yaml`, configures logging and returns the
application. uvicorn serves it (`uvicorn --factory <service_pkg>.api.app_factory:AppFactory.create`), in the image and on
a laptop. There is never a `cli` module, a console script or an argument parser: a job runs beside the application as an
`AsyncRunnable` its lifespan initialises and closes, an operation a person starts is an endpoint, a check is a test, and
a CI step is a script of `.github/scripts/` (`AGENT.md`, "Layout").

**Contracts (TC-07).** Each service publishes its OpenAPI generated from its Pydantic models; the MCP tools, A2A skills,
typed clients between services and the Bruno collection are generated from it, so that one change updates all; breaking
changes are caught in CI.

**Shared code.** `packages/` is a service kit with no business rules: the lifecycle base classes, logging, configuration
loading, the company-context and rights middleware, the event outbox, the metering client, the country-pack rules
library, test helpers.

**Business rules (TC-22).** Each service's rules (pricing, stock, planning, payroll, accounting) are pure functions over
the data they read, so that the same code runs on live data and on a what-if scenario overlay (F23); storage and side
effects stay at the edges.

Decided in [D406](../../specs/06-decisions/technical/d406-back-end.md).

Last reviewed: 2026-11-27 (T0.05, T0.12, GH-2)
