# Repository layout

How the SimpleERP repository is organised: back end, front end, shared models and libraries, plugins, SDK,
infrastructure, packs, documentation and workflows.

## Today

The repository follows the layout of D438 for its first folders. Every folder of the tree exists, with a README saying
what it holds:

- [`backend/`](../../../backend/README.md), with [`backend/models/`](../../../backend/models/README.md) (package
  `erp_models`, still empty), [`backend/shared/`](../../../backend/shared/README.md) and
  [`backend/services/`](../../../backend/services/README.md), which hold no service or library yet;
- [`frontend/`](../../../frontend/README.md), with [`frontend/backoffice/`](../../../frontend/backoffice/README.md),
  [`frontend/mobile/`](../../../frontend/mobile/README.md) and [`frontend/packages/`](../../../frontend/packages/README.md);
- [`plugins/`](../../../plugins/README.md) and [`sdk/`](../../../sdk/README.md), the plugin SDK;
- [`infra/`](../../../infra/README.md), with [`infra/compose/`](../../../infra/compose/README.md),
  [`infra/helm/`](../../../infra/helm/README.md) and [`infra/terraform/`](../../../infra/terraform/README.md);
- [`packs/`](../../../packs/README.md), with [`packs/countries/`](../../../packs/countries/README.md) and
  [`packs/sectors/`](../../../packs/sectors/README.md).

The uv workspace (`pyproject.toml` at the root) has two members that exist on disk: `backend/models` and `sdk`. Its
other members (`backend/shared/*`, `backend/services/*`, `plugins/*`) are declared and come with the tickets that create
them. The pnpm workspace (`pnpm-workspace.yaml`) has two members that exist on disk: `frontend/backoffice` and
`frontend/mobile`. `frontend/portals/` and the front-end packages of `frontend/packages/` come with the later tickets of
the roadmap, as do the services, the shared libraries and the plugins.

## Target design (specified in GH-2, not built yet)

**Layout (D438).** One mono-repo, the back end and the front end separated:

```text
backend/
  models/            the shared Pydantic models of every public contract (API resources, events, plugin and
                     connector contracts, enums and their SE exceptions); imported by services, plugins and the SDK
  shared/            shared libraries imported by the services (lifecycle, logging, configuration, company context and
                     rights, event outbox, metering client, country-pack rules library, test helpers); no business rules
  services/
    <service>/       one image each: Dockerfile, pyproject.toml, conf/, tests/
      src/<service>/
        models/      the service's private models
        storage/     the repositories
        service/     the business logic
        api/         the endpoints
frontend/
  backoffice/        one web app (D407)
  portals/           customer and supplier portals
  mobile/            the offline-first app
plugins/             first-party plugins, built on backend/models/
sdk/                 the plugin SDK and its CLI (D425), built on backend/models/
infra/
  compose/           laptop and one-server profiles (D408, D421)
  helm/              an umbrella chart and a chart per service
  terraform/         modules/, ovhcloud/ and scaleway/: fully working deployments (REQ-T09-08)
packs/
  countries/         signed country packs as data (T11)
  sectors/           sector packs
docs/                specs/, functional/, technical/
.github/workflows/   ci, stage, release, and the DevOps agents' workflows (D437)
.claude/             the Claude Code harness
pyproject.toml, uv.lock   the uv workspace root
compose.e2e.yaml     the real images for Playwright (AGENT.md)
```

**Rules.**

- Each back-end micro-service is layered: models, storage (the repositories), service (the business logic), api (the
  endpoints); each layer calls only the one below (AGENT.md).
- What several business domains share is a library under `backend/shared/`, imported by the services; a service never
  imports another service.
- `backend/models/` is the one shared Pydantic models library: services, `plugins/` and `sdk/` import it, so that every
  public contract is defined once.
- Plugins and the SDK are separate: `plugins/` holds first-party plugins, `sdk/` the plugin SDK and CLI.
- Outside this repository: the closed hosted services (D388, D415), the store's plugins and generated features, and the
  private GitOps repository of the hosted clusters (D420).
- AGENT.md's "Mono-repo" section and the conventions tests (`tests/conventions/`) follow this layout since
  2026-11-27; the first tickets of phase P0 create its folders.

Decided in [D438](../../specs/06-decisions/technical/d438-repository-layout.md).

Last reviewed: 2026-11-12 (GH-2)
