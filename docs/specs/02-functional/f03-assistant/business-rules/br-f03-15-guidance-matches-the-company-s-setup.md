🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-15 Guidance matches the company's setup

# 📏 BR-F3-15 Guidance matches the company's setup

**Status:** ✅ specified

## Statement

Guidance uses, in this order, the company's own procedures (knowledge base), the company's configuration (its custom
fields, statuses, rules and roles) and SimpleERP's user documentation; steps name the company's own labels, and each
step links to its screen; "Show me" highlights each button on the real screen, one step at a time.

## Why

A generic answer is wrong for a configured ERP. See [D166](../../../06-decisions/f03-assistant/d166-show-me-guidance.md)
and [D167](../../../06-decisions/f03-assistant/d167-guidance-sources.md).

## Examples

| Case | Result |
|---|---|
| "How do I close a job?" in a company where the status is "Finished" | Steps say "set the status to Finished", the company's label |
| A company procedure "Returns" exists | The procedure's steps first, with its link |
| "Show me" | The first button is highlighted, with "Next" |

## Applies to

- [UC-F3-05](../use-cases/05-find-and-get-guided/uc-f03-05-find-a-record-or-a-screen-get-guided.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-14 One match opens, several are listed](br-f03-14-one-match-opens-several-are-listed.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F3-16 Missing features become requests](br-f03-16-missing-features-become-requests.md)
