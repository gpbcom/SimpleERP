🏠 [Specs](../README.md) › ⚙️ Technical capabilities

# ⚙️ Technical capabilities

**Status:** 🔄 waiting for the owner

What the platform provides, invisible to business users.

## Dependency graph

⬜ To be specified.

## Technical challenges

Read first: the [technical challenges](challenges/README.md) the functional side brings (TC-01 to TC-24), each mapped to
the interviews below.

## Technical design topics

Cross-cutting design, interviewed before T1 to T11 (D146 to D148; seven more rounds added on 2026-11-12, PLAN D35 and
D39). Each
topic is written in the
"Target design" section of its docs/technical chapter (D147).

| Step | Topic | Chapter | Status |
|---|---|---|---|
| 19a | Architecture and scalability | [docs/technical](../../technical/architecture/architecture.md) | ✅ |
| 19v | Back end | [docs/technical](../../technical/architecture/backend.md) | ✅ |
| 19w | Front end | [docs/technical](../../technical/architecture/frontend.md) | ✅ |
| 19b | Performance and capacity | [docs/technical](../../technical/infrastructure/performance-and-capacity.md) | ✅ |
| 19c | Storage: data model, database choice (SQL or NoSQL), database configuration and security, file and object storage (D189) | [docs/technical](../../technical/data/data-model.md) and [storage](../../technical/data/storage.md) | ✅ |
| 19d | API design and contracts | [docs/technical](../../technical/interfaces/api.md) | ✅ |
| 19x | MCP | [docs/technical](../../technical/interfaces/mcp.md) | ✅ |
| 19y | A2A | [docs/technical](../../technical/interfaces/a2a.md) | ✅ |
| 19e | Configuration | [docs/technical](../../technical/architecture/configuration.md) | ✅ |
| 19f | Security | [docs/technical](../../technical/security/security.md) | ✅ |
| 19g | Supply chain and licences | [docs/technical](../../technical/security/supply-chain-and-licences.md) | ✅ |
| 19h | Observability (Loki, Prometheus, Grafana) | [docs/technical](../../technical/operations/observability.md) | ✅ |
| 19i | AI operations | [docs/technical](../../technical/operations/ai-operations.md) | ✅ |
| 19j | CI/CD and deployment (OVHcloud, Scaleway, self-hosted; Terraform by default) | [docs/technical](../../technical/delivery/ci-cd-and-stages.md) and [deployment](../../technical/infrastructure/deployment.md) | ✅ |
| 19z | DevOps | [docs/technical](../../technical/operations/devops.md) | ✅ |
| 19za | Infrastructure deployment | [docs/technical](../../technical/infrastructure/infrastructure.md) | ✅ |
| 19zb | Repository layout | [docs/technical](../../technical/architecture/repository-layout.md) | ✅ |
| 19k | Backups, recovery and upgrades | [docs/technical](../../technical/operations/operations.md) | ✅ |
| 19l | Release and versioning | [docs/technical](../../technical/delivery/release-and-versioning.md) | ✅ |
| 19m | Data migration from other ERPs | [docs/technical](../../technical/data/data-migration.md) | ✅ |
| 19n | Plugin SDK and developer experience | [docs/technical](../../technical/interfaces/plugin-sdk.md) | ✅ |
| 19o | Tests: unit, GUI, E2E and load | [docs/technical](../../technical/delivery/tests-and-traceability.md) | ✅ |

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 🧗 |  | [Technical challenges from the functional side](challenges/README.md) | ✅ |
| 🏢 | T1 | [Companies and data isolation](t01-companies-and-data-isolation/README.md) | ✅ |
| 🔐 | T2 | [Identity and access engine](t02-identity-and-access/README.md) | ✅ |
| 🧾 | T3 | [Audit trail](t03-audit-trail/README.md) | ✅ |
| 🔌 | T4 | [Plugin runtime](t04-plugin-runtime/README.md) | ✅ |
| 🔗 | T5 | [API and webhooks](t05-api-and-webhooks/README.md) | ✅ |
| 🛰️ | T6 | [MCP and A2A gateway](t06-mcp-and-a2a-gateway/README.md) | ✅ |
| 🧠 | T7 | [AI providers and models](t07-ai-providers-and-models/README.md) | ✅ |
| 📚 | T8 | [RAG platform (Milvus)](t08-rag-platform/README.md) | ✅ |
| 🚀 | T9 | [Install, backups and updates](t09-install-backups-and-updates/README.md) | ✅ |
| 🌐 | T10 | [Translations and notifications](t10-translations-and-notifications/README.md) | ✅ |
| 🏛️ | T11 | [Legal corpora](t11-legal-corpora/README.md) | ✅ |
| 🕸️ | T12 | [Connectors and scrapers](t12-connectors-and-scrapers/README.md) | ✅ |
| 🗺️ | T13 | [Maps and geodata](t13-maps-and-geodata/README.md) | 🔄 |

---

⬅️ [Functional capabilities](../02-functional/README.md) · ⬆️ [Up](../README.md) · ➡️ [UX](../04-ux/README.md)
