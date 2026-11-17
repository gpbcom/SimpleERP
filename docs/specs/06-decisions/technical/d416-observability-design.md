🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D416 Observability design

# 📜 D416 Observability design

**Status:** ✅ decided

## Context

Step 19h of the technical interview.

## Options

- Logs, metrics and traces on one stack, or logs and metrics only.
- A status page and each company's health, or operators only.
- SLOs with error budgets, or threshold alerts.
- Every AI call traced, or cost and latency only.

## Choice

Confirmed by the owner on 2026-11-12: logs, metrics and traces on one stack; a status page and each company's own
health; SLOs with error budgets; every AI call traced.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The observability chapter's target design.

## Related

- [Observability design](../../../technical/operations/observability.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D415 Supply chain controls](d415-supply-chain-controls.md) · ⬆️ [Up](README.md) ·
➡️ [D417 AI operations design](d417-ai-operations-design.md)
