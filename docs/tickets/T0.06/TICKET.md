# T0.06: Logging and configuration library

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.06](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S01](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01), 7 to 18 Dec 2026: the layout, its rules and the first shared code
- **Epic:** [E0.3 Service kit](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): the libraries of Back end (lifecycle, logging, configuration, company context and rights, outbox, metering client, country-pack rules, test helpers), one library per agent, each with its own folder, tests and pyproject

## What it delivers

- The logging setup of `conf/logger.yaml` in `backend/shared/logging`: a coloured console, a coloured rotating file and JSON lines for collection, each line tagged with the service, the company as an opaque id and the request, as [Observability design](../../technical/operations/observability.md) and [📜 D416](../../specs/06-decisions/technical/d416-observability-design.md) decide.
- The loading of `conf/app.yaml` in `backend/shared/config`: every default written out, overridden by environment variables, as [Configuration](../../technical/architecture/configuration.md) and [📜 D413](../../specs/06-decisions/technical/d413-configuration-layers.md) decide.
- `_key` fields that name vault entries only and never hold a secret, as [📜 D240](../../specs/06-decisions/security-and-compliance/d240-credential-vault.md) and [Configuration](../../technical/architecture/configuration.md) state.
- Both libraries as their own uv packages under `backend/shared/`, with their folders, tests and `pyproject.toml`, as [📜 D438](../../specs/06-decisions/technical/d438-repository-layout.md) lays out.

## Features, use cases and business rules

- [📜 D416 Observability design](../../specs/06-decisions/technical/d416-observability-design.md): logs, metrics and traces on one stack.
- [📜 D413 Configuration layers](../../specs/06-decisions/technical/d413-configuration-layers.md): files, environment, database and vault.
- [📜 D240 Customers' credentials in a vault](../../specs/06-decisions/security-and-compliance/d240-credential-vault.md): secrets referenced by name.
- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md): `backend/shared/<lib>`.
- [📜 D406 Back end](../../specs/06-decisions/technical/d406-back-end.md): the service kit has no business rules.

## Technical pages it builds on

- [🏗️ Configuration](../../technical/architecture/configuration.md): `conf/logger.yaml` (coloured console and rotating file in `logs/`, root level `DEBUG`), `conf/app.yaml` with every default overridden by environment variables or Helm values, a `_key` field names a secret store entry, secrets never in configuration or logs.
- [🏗️ Back end](../../technical/architecture/backend.md): the service kit of `backend/shared/` with logging and configuration, no business rules.
- [🏗️ Observability](../../technical/operations/observability.md): every signal tagged with the service, the company (as an opaque id) and the request.
- [🏗️ Repository layout](../../technical/architecture/repository-layout.md): where `backend/shared/<lib>` sits in the workspace.

## Screens touched

- ➖ No screen: the ticket builds two back-end libraries and touches no front end.

## Budgets touched

- [🔭 Observability](../../specs/05-non-functional/observability.md#requirement): every signal is tagged with the service, the company as an opaque id and the request, and secrets are masked at collection.

## Acceptance criteria

1. **Given** a default in `conf/app.yaml`, **when** the matching environment variable is set, **then** the loaded configuration holds the environment value. ([📜 D413](../../specs/06-decisions/technical/d413-configuration-layers.md))
2. **Given** a configuration with a `_key` field, **when** it is loaded and logged, **then** the `_key` value never appears in a log line, and the field only names a vault entry. ([📜 D240](../../specs/06-decisions/security-and-compliance/d240-credential-vault.md))
3. **Given** the logging set up from `conf/logger.yaml`, **when** a line is written, **then** it carries the service, the company as an opaque id and the request. ([📜 D416](../../specs/06-decisions/technical/d416-observability-design.md))
4. **Given** the two libraries, **when** the tests and the convention tests run, **then** they pass, with the libraries in `backend/shared/logging` and `backend/shared/config`. ([📜 D438](../../specs/06-decisions/technical/d438-repository-layout.md))

## Out of scope

- The company context and rights middleware that supplies the company and the request, see [T0.09](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02).
- The lifecycle and factories library, see [T0.05](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01).
- The vault itself and the per-company settings in the database, which P2 builds, see [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#scope).
- The logs, metrics and traces stack (Loki, Prometheus, Tempo, Grafana), see [🔭 Observability](../../specs/05-non-functional/observability.md).

## Assumptions

- The roadmap names no use case, business rule, entity, flow or requirement for this ticket, so it links the decisions and design pages that settle it.
- The folder names `backend/shared/logging` and `backend/shared/config` are the roadmap's own, confirmed by the owner (D572).
- The tags are named `service`, `company` and `request` after the roadmap; their exact field names in the JSON lines are not specified, so the most conservative names are taken.
- The logger configuration keeps the existing `conf/logger.yaml` shape of the Configuration page.
