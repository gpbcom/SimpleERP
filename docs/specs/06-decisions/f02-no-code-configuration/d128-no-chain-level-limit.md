🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D128 No level limit on rule chains

# 📜 D128 No level limit on rule chains

**Status:** ✅ decided

## Context

Whether chains of rules triggering each other have a depth limit (UC-F2-07 proposed 5 levels).

## Options

- 5 levels (proposed).
- No level limit (the owner's answer).

## Choice

No level limit: a chain of rules can be as deep as needed.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Without a limit, two rules feeding each other would run forever; a loop guard that is not a depth limit is proposed in
BR-F2-13 (a rule never runs twice in the same chain).

## Related

- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md)
- [BR-F2-13](../../02-functional/f02-no-code-configuration/business-rules/br-f02-13-rules-cannot-loop.md)

---

⬅️ [D127 Rule accounts](d127-rule-accounts.md) · ⬆️ [Up](README.md) ·
➡️ [D129 Workflow designer blocks](d129-workflow-blocks.md)
