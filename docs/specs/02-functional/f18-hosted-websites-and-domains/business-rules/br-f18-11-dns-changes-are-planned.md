🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F18-11 DNS changes are planned and checked

# 📏 BR-F18-11 DNS changes are planned and checked

**Status:** ✅ specified

## Statement

A DNS change is shown as a plan (records added, changed, removed), checked for conflicts with mail and existing
services, applied, then verified.

## Why

See [D385](../../../06-decisions/f18-hosted-websites-and-domains/d385-hosted-websites-coverage.md).

## Examples

| Case | Result |
|---|---|
| MX record would be removed | Blocked, warning |

## Applies to

Every F18 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F18-10 Domains through registrar APIs](br-f18-10-domains-through-registrar-apis.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F18-12 Mail records for delivery](br-f18-12-mail-records-for-delivery.md)
