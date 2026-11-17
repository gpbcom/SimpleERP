🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-02 Answers use only what the user may see

# 📏 BR-F3-02 Answers use only what the user may see

**Status:** ✅ specified

## Statement

The AI assistant reads and computes only from the records, fields and documents the user may see (D12); it never says or
hints that other records exist. Under every figure, a fixed sentence reads "Based on the records you can see."

## Why

The AI assistant must not be a way around permissions. See
[D150](../../../06-decisions/f03-assistant/d150-hidden-data-silent.md).

## Examples

| Case | Result |
|---|---|
| A sales person asks the company's turnover; they see only their own customers | The total of their customers, with the fixed sentence |
| An employee asks a colleague's salary | Nothing found among the records they can see; no mention of salaries existing |
| A manager with a field hidden (D12) | The field is never read or quoted |

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

⬅️ [BR-F3-01 Answers cite their sources](br-f03-01-answers-cite-their-sources.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-03 Figures come from queries, never the model](br-f03-03-figures-come-from-queries.md)
