🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D86 Administrators keep a password

# 📜 D86 Administrators keep a password

**Status:** ✅ decided

## Context

Whether users can still sign in with a password once single sign-on is on.

## Options

- Administrators only.
- Everyone may.
- No one.

## Choice

Administrators only: users sign in through the provider; administrators keep a password and two-factor authentication,
to get in if the provider is down.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

A provider outage never locks the company out.

## Related

- [UC-F1-09](../../02-functional/f01-administration/use-cases/07-set-up-single-sign-on/uc-f01-09-set-up-single-sign-on.md)
- [BR-F1-17](../../02-functional/f01-administration/business-rules/br-f01-17-administrators-keep-a-password.md)

---

⬅️ [D85 Single sign-on providers](d85-single-sign-on-providers.md) · ⬆️ [Up](README.md) ·
➡️ [D87 Allowed domains](d87-allowed-domains.md)
