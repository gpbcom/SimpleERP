🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-14 AI steps return their declared format

# 📏 BR-F2-14 AI steps return their declared format

**Status:** ✅ specified

## Statement

An AI operation in a workflow declares its output format (named fields and their types); an answer that does
not fit the format is retried once, then the workflow takes the step's error path.

## Why

The next blocks rely on the AI step's fields. See
[D129](../../../06-decisions/f02-no-code-configuration/d129-workflow-blocks.md).

## Examples

| Step | Output format | Answer | Result |
|---|---|---|---|
| "Classify this supplier email" | category (list), urgency (1 to 3) | category: invoice, urgency: 2 | Next block runs |
| same | same | free text | Retried, then the error path (notify a person) |

## Applies to

- [UC-F2-08](../use-cases/04-design-a-visual-workflow/uc-f02-08-design-a-visual-workflow.md)

## Exceptions

None.

## Configurable

The format, per AI step.

## Open questions

None.

---

⬅️ [BR-F2-13 Rules cannot loop](br-f02-13-rules-cannot-loop.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-15 Packs carry no data](br-f02-15-packs-carry-no-data.md)
