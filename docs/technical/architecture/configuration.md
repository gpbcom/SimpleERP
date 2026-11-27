# Configuration

Where SimpleERP reads its settings.

| File | Holds |
|---|---|
| `backend/services/<service>/conf/logger.yaml` | The logging: a coloured console handler and a coloured rotating file in `logs/`, root level `DEBUG` |
| `backend/services/<service>/conf/app.yaml` | Planned: the application settings, with every default written out |
| `backend/services/<service>/conf/catalogs/` | Planned: data that would otherwise be hard-coded, loaded by `YamlCatalog` models. The base `YamlCatalog` exists in `erp_models.catalogs.yaml_catalog`: it reads a UTF-8 YAML mapping and raises the catalogue's `UNREADABLE` exception. The catalogue files themselves come with the tickets that need them |

Each service keeps its configuration in its own `conf/` folder, next to its `src/` and `tests/` ([D438](../../specs/06-decisions/technical/d438-repository-layout.md)).

- Secrets live in a secret store, never in configuration or logs. A field ending in `_key` names a secret store entry.
- The log file holds colour codes: read it with `tail -f` or `less -R`.

## Workspaces

The workspace files at the repository root set up the toolchains for every package ([D438](../../specs/06-decisions/technical/d438-repository-layout.md)).

| File | Holds |
|---|---|
| `pyproject.toml` | The uv workspace root, with its members `backend/models`, `backend/shared/*`, `backend/services/*`, `plugins/*` and `sdk` |
| `uv.lock` | Every Python dependency pinned, one lock for every Python package ([D415](../../specs/06-decisions/technical/d415-supply-chain-controls.md)) |
| `.python-version` | Python 3.13 |
| `package.json` | The pnpm workspace root, with `packageManager` pinning pnpm and `engines.node` set to Node 22 |
| `pnpm-workspace.yaml` | The front-end members `frontend/backoffice`, `frontend/mobile`, `frontend/portals/*` and `frontend/packages/*` |
| `pnpm-lock.yaml` | Every front-end dependency pinned ([D415](../../specs/06-decisions/technical/d415-supply-chain-controls.md)) |

## Target design (specified in GH-2, not built yet)

**Layers (D413).** Each service's `conf/app.yaml` holds every default (`AGENT.md`), overridden per deployment by
environment variables or Helm values; each company's settings sit in its database, changed through F1, F2 and F21;
secrets sit only in the vault (D240), referenced by name (`_key` fields).

**Configuration as code (TC-03).** A company's configuration (fields, statuses, forms, templates, workflows, roles,
modules) exports as versioned files that can be diffed, tested on a test company and promoted to the live one; sector
packs and IT providers' templates use the same format.

**Module switches (TC-02).** The platform core keeps each company's modules and their dependencies, published as events
so that every service, the front end and the assistant's tools follow at once; read through an OpenFeature-compatible
interface, also used for gradual rollouts of new features.

**No-code workflows.** Workflows compile to runs on the durable workflow engine, with limits: no unbounded loops,
outside calls only through connectors, time and cost budgets, scheduled runs allowed; a workflow that fails its test
does not go live.

Decided in [D413](../../specs/06-decisions/technical/d413-configuration-layers.md).

Last reviewed: 2026-11-27 (T0.03, GH-2)
