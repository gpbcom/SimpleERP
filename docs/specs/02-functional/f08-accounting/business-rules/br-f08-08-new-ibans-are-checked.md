🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-08 New IBANs are checked

# 📏 BR-F8-08 New IBANs are checked

**Status:** ✅ specified

## Statement

A supplier's new or changed IBAN is checked with the supplier through a known channel (a call-back to a number already
on file), approved by a second person, and the first payment to it waits 48 hours; every step is logged.

## Why

See [D283](../../../06-decisions/f08-accounting/d283-iban-change-protection.md).

## Examples

| Case | Result |
|---|---|
| An email announcing new bank details | Not applied until the call-back and a second approval |
| First payment to the new IBAN | Held 48 hours |

## Applies to

Every F8 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F8-07 Intercompany mirrored and eliminated](br-f08-07-intercompany-mirrored-and-eliminated.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F8-09 The AI proposes, people post](br-f08-09-the-ai-proposes-people-post.md)
