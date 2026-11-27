🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🧭 [Decisions: Foundations](README.md) › 📜 D13 Sign-in

# 📜 D13 Sign-in

**Status:** ✅ decided

## Context

How users sign in.

## Options

- Built-in accounts plus optional single sign-on.
- Single sign-on only.
- Built-in accounts only.

## Choice

Built-in accounts with two-factor authentication, and optional single sign-on through OpenID Connect.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

See the related pages.

Revised by D450 on 2026-11-12: two factors for every user, passkeys preferred; a fresh sign-in before a link opens a
payslip or personal data.

## Related

- [T2 Identity and access engine](../../03-technical/t02-identity-and-access/README.md)

---

⬅️ [D12 Permissions model](d12-permissions-model.md) · ⬆️ [Up](README.md) ·
➡️ [D14 Every employee is a user](d14-every-employee-is-a-user.md)
