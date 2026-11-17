🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
💸 [Decisions: F22 Unified platform cost management](README.md) › 📜 D398 Budgets warn, then stop

# 📜 D398 Budgets warn, then stop

**Status:** ✅ decided

## Context

What happens when a budget is reached.

## Options

- Warn, then stop, legal duties excepted.
- Warn only.
- Stop at once, no exception.

## Choice

Budgets per company, module, feature, connector and user; warnings at set thresholds; at 100 % new paid calls stop until
the owner raises the budget, except what a legal duty needs (e-invoicing, payroll declarations); a run in progress is
stopped cleanly, never half-written.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

BR-F22-04 to BR-F22-07.

## Related

- [F22 Unified platform cost management](../../02-functional/f22-unified-cost-management/README.md)

---

⬅️ [D397 Unified platform cost management coverage](d397-cost-management-coverage.md) · ⬆️ [Up](README.md) ·
➡️ [D399 Hosted usage: quota, then per unit](d399-hosted-usage-billing.md)
