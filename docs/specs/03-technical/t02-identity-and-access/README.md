🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) › 🔐 T2 Identity and access engine

# 🔐 T2 Identity and access engine

**Status:** ✅ specified

## Summary

Who signs in and what they may do, everywhere: screens, API, MCP, A2A, search and simulations.

## Scope

- Built-in accounts with two-factor authentication work as soon as SimpleERP is installed.
- An administrator can add single sign-on through OpenID Connect: Google, Microsoft 365, or a self-hosted Keycloak. See
  [D13](../../06-decisions/foundations/d13-sign-in.md).
- Ready-made providers: Google Workspace, Microsoft Entra ID, any OpenID Connect provider (such as Keycloak), and SAML
  2.0. See [D85](../../06-decisions/f01-administration/d85-single-sign-on-providers.md).
- With single sign-on on, only administrators keep a password. See
  [D86](../../06-decisions/f01-administration/d86-administrators-keep-a-password.md).
- Sign-in with Keycloak, single sign-on, passkeys, two-factor authentication.
- Rights and record rules as policies.
- Tokens, sessions, service accounts, federation with office suites.

## Functional capabilities served

Every capability; F1 defines the roles.

## Out of scope

- The roles' content: F1.
- Audit: T3.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 🏗️ |  | [Architecture](architecture.md) | ✅ |
| 📌 |  | [Requirements](requirements/README.md) | ✅ |
| 🔌 |  | [Interfaces](interfaces/README.md) | ✅ |
| 🗃️ |  | [Data](data/README.md) | ✅ |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | ✅ |
| 🛡️ |  | [Security](security.md) | ✅ |
| ⚙️ |  | [Operations](operations.md) | ✅ |
| 🚨 |  | [Errors](errors.md) | ✅ |
| 🧪 |  | [Tests](tests.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |

---

⬅️ [Companies and data isolation](../t01-companies-and-data-isolation/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Audit trail](../t03-audit-trail/README.md)
