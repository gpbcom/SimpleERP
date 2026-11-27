🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-12 Rule accounts never exceed their author

# 📏 BR-F2-12 Rule accounts never exceed their author

**Status:** ✅ specified

## Statement

A rule runs as its own rule account; its rights are chosen by the configurator and can never exceed the configurator's
own; every change it makes is signed "by rule: name".

## Why

Automation must not widen anyone's rights. See
[D127](../../../06-decisions/f02-no-code-configuration/d127-rule-accounts.md).

## Examples

| Case | Result |
|---|---|
| A manager gives their rule "Change invoices" but cannot change invoices themself | Refused |
| The rule sets a quote's status | History: "Status Sent, by rule: Remind after 3 days" |
| The rule's author loses a right later | The rule is paused and its author told |

## Applies to

- [UC-F2-07](../use-cases/03-automate-with-a-rule/uc-f02-07-create-a-simple-rule.md); UC-F2-08 (planned).

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F2-11 Electronic formats with the PDF](br-f02-11-electronic-formats-with-the-pdf.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F2-13 Rules cannot loop](br-f02-13-rules-cannot-loop.md)
