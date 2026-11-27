# Technical documentation

How SimpleERP is built, tested, released and run. `AGENT.md` at the repository root holds the rules code must follow;
these chapters describe what exists. Each also holds a "Target design" section: the
design specified in ticket GH-2 and not built yet.
Architecture and infrastructure show their target design in a diagram; for the other chapters, the decision each one
links (D405 to D438) holds the options weighed and the reasons. The open points of every topic are the questions of
[docs/specs/07-questions](../specs/07-questions/README.md).

The images of [docs/specs/](../specs/README.md) are stored with Git LFS (`.gitattributes`): run `git lfs install`
before cloning, or `git lfs pull` afterwards, to see them.

The chapters are sorted into seven themes, one folder each. The per-service and per-front-end chapters go in
`services/` and `frontend/` as the services and front ends are built, written by the `doc-writer` agent of each ticket.

## [Architecture](architecture/README.md)

How the code is laid out and configured: layers, repository, back end, front end.

| Chapter | Holds |
|---|---|
| [Architecture](architecture/architecture.md) | The layers, the current layout and the target mono-repo |
| [Configuration](architecture/configuration.md) | The configuration files and the logging |
| [Back end](architecture/backend.md) | The back-end services: language, frameworks, service boundaries, data access, jobs and workers, events |
| [Front end](architecture/frontend.md) | The front ends: framework, design system in code, offline and mobile, accessibility, Playwright tests |
| [Repository layout](architecture/repository-layout.md) | The mono-repo: backend/ (models, shared, services), frontend/, plugins/, sdk/, infra/, packs/ |

## [Interfaces](interfaces/README.md)

How people, programs and agents reach SimpleERP: API, MCP, A2A and the plugin SDK.

| Chapter | Holds |
|---|---|
| [API](interfaces/api.md) | The HTTP API of every service: a regular FastAPI application served by uvicorn, with no command line |
| [Plugin SDK and developer experience](interfaces/plugin-sdk.md) | How third parties build, test, sign and publish plugins (T4, F14) |
| [MCP](interfaces/mcp.md) | SimpleERP as an MCP server and as an MCP client: tools, rights, confirmations, transport, security (T6) |
| [A2A](interfaces/a2a.md) | SimpleERP as an A2A agent and as a caller of outside agents: skills, discovery, trust, rights (T6) |

## [Data](data/README.md)

What is stored, where, and how data comes in from other tools.

| Chapter | Holds |
|---|---|
| [Data model](data/data-model.md) | The models and what stores them |
| [Storage](data/storage.md) | Database choice (SQL or NoSQL), database configuration and security, file and object storage |
| [Data migration](data/data-migration.md) | Imports from Odoo, Dolibarr, Sage, EBP and spreadsheets, at scale (D61) |

## [Security](security/README.md)

Threats, controls and secrets, and the dependencies and licences of the supply chain.

| Chapter | Holds |
|---|---|
| [Security](security/security.md) | Threats, controls, secrets, sign-in, encryption, audits |
| [Supply chain and licences](security/supply-chain-and-licences.md) | Dependency policy, SBOM, CVE scanning, AGPL compliance of dependencies and plugins |

## [Delivery](delivery/README.md)

How a ticket becomes a tested, released version.

| Chapter | Holds |
|---|---|
| [CI/CD and stages](delivery/ci-cd-and-stages.md) | The workflows, the GitFlow branches, the dev and QA stages, the releases |
| [Tests and traceability](delivery/tests-and-traceability.md) | The test levels, test-first, evidence and kept reports |
| [Development process](delivery/development-process.md) | How a ticket goes from issue to release with the Claude Code harness |
| [Release and versioning](delivery/release-and-versioning.md) | Semantic versions, long-term support, upgrade paths |

## [Operations](operations/README.md)

How the running platform is operated, watched and helped by AI.

| Chapter | Holds |
|---|---|
| [Operations](operations/operations.md) | Images, logs and what runs where; target: backups, recovery and upgrades |
| [Observability](operations/observability.md) | Logs, metrics and dashboards (Loki, Prometheus, Grafana), alerts |
| [AI operations](operations/ai-operations.md) | Model hosting and GPUs, model choice and evaluation, RAG quality (T7, T8) |
| [DevOps](operations/devops.md) | How the platform is operated day to day: environments, infrastructure as code, GitOps, secrets, on-call, runbooks |

## [Infrastructure](infrastructure/README.md)

Where SimpleERP runs, how it is deployed and how it is sized.

| Chapter | Holds |
|---|---|
| [Performance and capacity](infrastructure/performance-and-capacity.md) | Sizing per company size and capacity planning for IT providers (D25) |
| [Deployment](infrastructure/deployment.md) | Targets OVHcloud, Scaleway and self-hosted; Terraform by default; Compose and Helm (D18) |
| [Infrastructure deployment](infrastructure/infrastructure.md) | The deployment targets, self-hosted and the fully managed hosted edition: clusters, regions, sizing, networks, Terraform |

Last reviewed: 2026-11-27 (GH-2)
