🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: F1 Administration](README.md) ›
📜 D85 Single sign-on providers

# 📜 D85 Single sign-on providers

**Status:** ✅ decided

## Context

Which single sign-on providers the setup offers ready-made.

## Options

- Google Workspace.
- Microsoft Entra ID.
- Keycloak or any OpenID Connect provider.
- SAML 2.0.

## Choice

All four: Google Workspace, Microsoft Entra ID, any OpenID Connect provider by its discovery address (such as a
self-hosted Keycloak), and SAML 2.0.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Extends D13, which named OpenID Connect only: SAML 2.0 is supported too.

## Related

- [UC-F1-09](../../02-functional/f01-administration/use-cases/07-set-up-single-sign-on/uc-f01-09-set-up-single-sign-on.md)
- [D13](../foundations/d13-sign-in.md)
- [T2](../../03-technical/t02-identity-and-access/README.md)

---

⬅️ [D84 Fall back to the local model](d84-fall-back-to-local.md) · ⬆️ [Up](README.md) ·
➡️ [D86 Administrators keep a password](d86-administrators-keep-a-password.md)
