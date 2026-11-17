🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D127 Rule accounts

# 📜 D127 Rule accounts

**Status:** ✅ decided

## Context

Under whose rights a rule acts.

## Options

- A rule account with chosen rights.
- The person who triggered it.
- Full rights.

## Choice

Each rule runs as a rule account whose rights the configurator chooses, no more than their own; every change it makes
shows "by rule: ..." in the history.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Rules never widen anyone's rights.

## Related

- [UC-F2-07](../../02-functional/f02-no-code-configuration/use-cases/03-automate-with-a-rule/uc-f02-07-create-a-simple-rule.md)
- [BR-F2-12](../../02-functional/f02-no-code-configuration/business-rules/br-f02-12-rule-accounts-never-exceed-their-author.md)

---

⬅️ [D126 Rule actions](d126-rule-actions.md) · ⬆️ [Up](README.md) ·
➡️ [D128 No level limit on rule chains](d128-no-chain-level-limit.md)
