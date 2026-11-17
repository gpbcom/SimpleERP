🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D148 The 15 technical design topics

# 📜 D148 The 15 technical design topics

**Status:** ✅ decided

## Context

Which technical topics are interviewed.

## Options

- The owner's seven: architecture and scalability, observability, security, CI/CD and deployment, data model, tests,
  configuration.
- Eight more proposed: API design and contracts, backups recovery and upgrades, release and versioning, data migration,
  supply chain and licences, plugin SDK, AI operations, performance and capacity.

## Choice

All fifteen. Observability uses Loki, Prometheus and Grafana; deployment targets OVHcloud, Scaleway and self-hosted
installs, with Terraform by default; tests cover unit, GUI, E2E and load tests.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Fifteen interview steps, 19a to 19o, each ending with its docs/technical chapter's target design.

## Related

- [Technical capabilities](../../03-technical/README.md)
- [Technical documentation](../../../technical/README.md)

---

⬅️ [D147 Target design sections in docs/technical](d147-technical-docs-target-design.md) · ⬆️ [Up](README.md) ·
➡️ [D149 How answers show their sources](../f03-assistant/d149-answer-sources.md)
