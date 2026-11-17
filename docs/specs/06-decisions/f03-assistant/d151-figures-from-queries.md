🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D151 Figures come from queries

# 📜 D151 Figures come from queries

**Status:** ✅ decided

## Context

How totals, counts, averages and trends are produced.

## Options

- Computed by queries, with a "how this was computed" view.
- Computed, no detail.
- The model reads records and computes.

## Choice

The ERP computes every figure with a database query, never the model; the result is shown as a table or chart,
exportable, with a "how this was computed" view (record type, filters, period, fields).

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Figures are exact and reproducible (BR-F3-03).

## Related

- [UC-F3-01](../../02-functional/f03-assistant/use-cases/01-ask-the-assistant/uc-f03-01-ask-a-question-about-the-company-s-data.md)

---

⬅️ [D150 Answers never hint at hidden records](d150-hidden-data-silent.md) · ⬆️ [Up](README.md) ·
➡️ [D152 Ask back, or say not found](d152-ask-or-not-found.md)
