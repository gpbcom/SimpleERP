🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-27 Tokens are scoped, dated and shown once

# 📏 BR-F1-27 Tokens are scoped, dated and shown once

**Status:** ✅ specified

## Statement

An API token has scopes within its service account's role, an end date, and is shown once at creation; only its last
four characters are kept visible.

## Why

A leaked token must be limited in what it can do and for how long.

## Examples

| Case | Result |
|---|---|
| Token without end date | Refused: an end date is required (default: 1 year at most) |
| Copy the token the next day | Not possible; issue a new one |

## Applies to

- [UC-F1-20 Create and revoke API tokens and service accounts](../use-cases/12-portal-accounts-and-integrations/uc-f01-20-create-and-revoke-api-tokens-and-service-accounts.md)

## Exceptions

None.

## Configurable

Allowed IP addresses per token.

## Open questions

None.

---

⬅️ [BR-F1-26 Portal accounts see only their own records](br-f01-26-portal-accounts-see-only-their-own-records.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F1-28](br-f01-28-security-policies-never-lock-out-every-administrator.md)
