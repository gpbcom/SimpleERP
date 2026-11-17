🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D126 Rule actions

# 📜 D126 Rule actions

**Status:** ✅ decided

## Context

Which actions ("then") a simple rule offers.

## Options

- Notify and assign.
- Change the record.
- Ask for approval.
- Call outside.

## Choice

All four: notify people and assign or create a task; set a field, change the status or create a linked record; start an
approval by one or more people; send a webhook or have the AI assistant use an outside tool (D80, D81).

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Approval chains are rules; outside calls obey the connection's confirmation setting.

## Related

- [UC-F2-07](../../02-functional/f02-no-code-configuration/use-cases/03-automate-with-a-rule/uc-f02-07-create-a-simple-rule.md)

---

⬅️ [D125 Rule triggers](d125-rule-triggers.md) · ⬆️ [Up](README.md) · ➡️ [D127 Rule accounts](d127-rule-accounts.md)
