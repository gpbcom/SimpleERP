🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-18 Allowed domains

# 📏 BR-F1-18 Allowed domains

**Status:** ✅ specified

## Statement

Single sign-on creates an account only for an email of an allowed domain, with the default role and site the
administrator set.

## Why

Only the company's own people get in. See [D87](../../../06-decisions/f01-administration/d87-allowed-domains.md).

## Examples

| First sign-in | Allowed domains | Result |
|---|---|---|
| paul@acme.fr | acme.fr | Account created, role Employee, site Head office |
| paul@gmail.com | acme.fr | Refused |
| marie@acme.fr, already invited | acme.fr | Signs in to her existing account (BR-F1-07) |

## Applies to

- [UC-F1-09](../use-cases/07-set-up-single-sign-on/uc-f01-09-set-up-single-sign-on.md); T2.
- [UC-F1-13 Provision users from the identity provider](../use-cases/10-bring-users-in-at-scale/uc-f01-13-provision-users-from-the-identity-provider.md)

## Exceptions

None.

## Configurable

Yes: the domains, the default role and the default site.

## Open questions

None.

---

⬅️ [BR-F1-17 Administrators keep a password](br-f01-17-administrators-keep-a-password.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F1-19 Templates copy configuration only](br-f01-19-templates-copy-configuration-only.md)
