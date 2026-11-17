🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D125 Rule triggers

# 📜 D125 Rule triggers

**Status:** ✅ decided

## Context

Which triggers ("when") a simple rule offers.

## Options

- A record created or changed.
- A date comes.
- On a schedule.
- An outside event.

## Choice

All four: a record created or changed (a field or a status); a date field reached or passed, checked every day; a
schedule (every day, week or month at a time); an outside event (a webhook received, an email received, a file dropped).

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Rules can react to anything the company deals with.

## Related

- [UC-F2-07](../../02-functional/f02-no-code-configuration/use-cases/03-automate-with-a-rule/uc-f02-07-create-a-simple-rule.md)

---

⬅️ [D124 Mockups with each step](../ux/d124-mockups-with-each-step.md) · ⬆️ [Up](README.md) ·
➡️ [D126 Rule actions](d126-rule-actions.md)
