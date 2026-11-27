🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-17 Administrators keep a password

# 📏 BR-F1-17 Administrators keep a password

**Status:** ✅ specified

## Statement

When single sign-on is on, only users holding the administrator role can also sign in with a password and two-factor
authentication.

## Why

A way in when the provider is down. See
[D86](../../../06-decisions/f01-administration/d86-administrators-keep-a-password.md).

## Examples

| User | Single sign-on on | Password sign-in |
|---|---|---|
| Sales person | yes | Refused, with "Sign in with your company account" |
| Administrator | yes | Allowed, with two-factor |
| Anyone | no | Allowed |

## Applies to

- [UC-F1-09](../use-cases/07-set-up-single-sign-on/uc-f01-09-set-up-single-sign-on.md); T2.
- [UC-F1-18 Run an access review campaign](../use-cases/11-team-delegation-and-access-review/uc-f01-18-run-an-access-review-campaign.md)
- [UC-F1-21 Set the security policies](../use-cases/13-security-and-audit/uc-f01-21-set-the-security-policies.md)

## Exceptions

Outside users (accountant, portals, provider administrator) are not concerned: they keep their own way in.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-16 Fall back to the local model](br-f01-16-fall-back-to-the-local-model.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-18 Allowed domains](br-f01-18-allowed-domains.md)
