🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D57 Administrator sees settings only

# 📜 D57 Administrator sees settings only

**Status:** ✅ decided

## Context

Whether the administrator role sees the company's business data (invoices, salaries, customers).

## Options

- Settings only.
- Everything.

## Choice

The administrator role manages settings, users and roles; seeing business data needs a business role too.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Least privilege: salaries stay with HR even when HR is not the administrator.

## Related

- [BR-F1-02](../../02-functional/f01-administration/business-rules/br-f01-02-administrator-sees-settings-only.md)

---

⬅️ [D56 Offboarding hand-over](d56-offboarding-hand-over.md) · ⬆️ [Up](README.md) ·
➡️ [D58 Setup steps](d58-setup-steps.md)
