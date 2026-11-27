🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D55 How users get an account

# 📜 D55 How users get an account

**Status:** ✅ decided

## Context

How new users get their account.

## Options

- An email invitation.
- Single sign-on, auto-created.
- A bulk import.
- Self sign-up with approval.

## Choice

Two ways: an email invitation (the user sets their password and two-factor through a link valid a few days), and single
sign-on with automatic creation (a colleague of an allowed domain signing in for the first time gets an account with a
default role).

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

No bulk import of users and no self sign-up.

## Related

- [T2 Identity and access engine](../../03-technical/t02-identity-and-access/README.md)

---

⬅️ [D54 Guided setup with a sector pack](../f01-administration/d54-guided-setup.md) · ⬆️ [Up](README.md) ·
➡️ [D56 Offboarding hand-over](../f01-administration/d56-offboarding-hand-over.md)
