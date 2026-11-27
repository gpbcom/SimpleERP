🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-28 Security policies never lock out every administrator

# 📏 BR-F1-28 Security policies never lock out every administrator

**Status:** ✅ specified

## Statement

A security policy change is refused when no administrator would still be able to sign in under it.

## Why

A company locked out of its own settings needs the provider to recover it.

## Examples

| Case | Result |
|---|---|
| IP rule excluding the administrator's current address | Refused |
| Two-factor required for all | Allowed; administrators set it at next sign-in |

## Applies to

- [UC-F1-19 Manage portal accounts](../use-cases/12-portal-accounts-and-integrations/uc-f01-19-manage-portal-accounts.md)
- [UC-F1-21 Set the security policies](../use-cases/13-security-and-audit/uc-f01-21-set-the-security-policies.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-27 Tokens are scoped, dated and shown once](br-f01-27-tokens-are-scoped-dated-and-shown-once.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F1-29 Audit exports carry the checksum chain](br-f01-29-audit-exports-carry-the-checksum-chain.md)
