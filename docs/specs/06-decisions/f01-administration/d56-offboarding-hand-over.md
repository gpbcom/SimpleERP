🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D56 Offboarding hand-over

# 📜 D56 Offboarding hand-over

**Status:** ✅ decided

## Context

What happens to what a leaving user owns (customers, open quotes, pending approvals).

## Options

- Hand over to a colleague.
- Go to their manager.
- Stay unassigned.

## Choice

The administrator picks who takes over; open items move to that colleague, the history keeps the leaver's name. The
account is deactivated, never deleted.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Accounts are never deleted, so the audit trail stays readable.

## Related

- [BR-F1-01](../../02-functional/f01-administration/business-rules/br-f01-01-offboarding-hand-over.md)

---

⬅️ [D55 How users get an account](../technical/d55-user-onboarding.md) · ⬆️ [Up](README.md) ·
➡️ [D57 Administrator sees settings only](d57-administrator-sees-settings-only.md)
