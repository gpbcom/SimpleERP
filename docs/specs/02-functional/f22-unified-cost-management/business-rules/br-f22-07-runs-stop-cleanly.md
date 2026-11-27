🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
💸 [F22 Unified platform cost management](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F22-07 Runs stop cleanly

# 📏 BR-F22-07 Runs stop cleanly

**Status:** ✅ specified

## Statement

A run stopped by a budget or by a user ends after its current step, keeps what is done, and can resume; nothing is
half-written.

## Why

See [D398](../../../06-decisions/f22-unified-cost-management/d398-budgets-warn-then-stop.md).

## Examples

| Case | Result |
|---|---|
| Scraping stopped at page 140 of 400 | 140 kept, resume offered |

## Applies to

Every F22 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F22-06 Stop at the budget, legal duties kept](br-f22-06-stop-at-budget-legal-duties-kept.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F22-08 Estimate before a large run](br-f22-08-estimate-before-a-run.md)
