🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F2-13 Rules cannot loop

# 📏 BR-F2-13 Rules cannot loop

**Status:** ✅ specified

## Statement

Chains of rules have no level limit (D128). A rule never runs twice in the same chain: when a change would
trigger a rule already run in that chain, the chain stops and the configurators are told.

## Why

Two rules feeding each other would run forever. See
[D128](../../../06-decisions/f02-no-code-configuration/d128-no-chain-level-limit.md).

## Examples

| Case | Result |
|---|---|
| Rule A sets a field that triggers rule B, which triggers rule C | A, B and C run, however long the chain |
| A triggers B, B's change would trigger A again | A does not run again; the configurators are told |

## Applies to

- [UC-F2-07](../use-cases/03-automate-with-a-rule/uc-f02-07-create-a-simple-rule.md); UC-F2-08 (planned).
- [UC-F2-24 Test rules and workflows with test cases](../use-cases/10-change-safely/uc-f02-24-test-rules-and-workflows-with-test-cases.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F2-12 Rule accounts never exceed their author](br-f02-12-rule-accounts-never-exceed-their-author.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F2-14 AI steps return their declared format](br-f02-14-ai-steps-return-their-declared-format.md)
