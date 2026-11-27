🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
💸 [Decisions: F22 Unified platform cost management](README.md) › 📜 D397 Unified platform cost management coverage

# 📜 D397 Unified platform cost management coverage

**Status:** ✅ decided

## Context

The owner asked for a unified platform cost management, including AI and paid connectors or scraping (PLAN D34).

## Options

- Every paid usage of the platform.
- AI, connectors and scraping only.
- Also the company's other software subscriptions.

## Choice

Every paid usage of the platform, confirmed by the owner on 2026-11-12: AI per feature and per provider (local AI as an
estimated server cost), paid connectors and data providers, scraping (proxies, browser workers, paid scraping services),
plugin and sector-pack subscriptions (F14), feature-factory features (F19) and the hosting; with budgets, alerts, caps,
forecasts, cost per module, feature, department, project or client, and the suppliers' invoices matched in accounting
(F8).

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

Twenty use cases (D400); every paid call is metered where it is made (TC-21).

## Related

- [F22 Unified platform cost management](../../02-functional/f22-unified-cost-management/README.md)

---

⬅️ [D396 F21 use cases](../f21-onboarding-and-modules/d396-f21-use-cases.md) · ⬆️ [Up](README.md) ·
➡️ [D398 Budgets warn, then stop](d398-budgets-warn-then-stop.md)
