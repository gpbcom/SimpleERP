🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-03 Figures come from queries, never the model

# 📏 BR-F3-03 Figures come from queries, never the model

**Status:** ✅ specified

## Statement

Every total, count, average or trend is computed by a database query that the ERP runs, never by the model; it is shown
as a table or a chart, can be exported, and has a "How this was computed" view: record type, filters, period, fields and
the number of records.

## Why

A model can miscount; a query is exact and can be run again. See
[D151](../../../06-decisions/f03-assistant/d151-figures-from-queries.md).

## Examples

| Case | Result |
|---|---|
| "Turnover in October?" | A figure from the invoices query; How: Invoices, issued 1 to 31 October, status not cancelled, 214 records |
| "Sales per month this year?" | A bar chart and its table, exportable |
| A question no query can answer | The AI assistant says it cannot compute it, never estimates |

## Applies to

- [UC-F3-01](../use-cases/01-ask-the-assistant/uc-f03-01-ask-a-question-about-the-company-s-data.md); every
  assistant answer of F3.
- [UC-F3-16 See the query behind a figure](../use-cases/11-trust-the-answers/uc-f03-16-see-the-query-behind-a-figure.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-02 Answers use only what the user may see](br-f03-02-answers-use-only-what-the-user-may-see.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F3-04 Ask or say not found, never invent](br-f03-04-never-invent.md)
