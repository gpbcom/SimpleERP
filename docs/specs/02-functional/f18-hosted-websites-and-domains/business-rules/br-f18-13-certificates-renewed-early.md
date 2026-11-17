🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F18-13 Certificates renewed early

# 📏 BR-F18-13 Certificates renewed early

**Status:** ✅ specified

## Statement

TLS certificates renew automatically well before expiry; a failure alerts the maintainer and the administrator.

## Why

See [D385](../../../06-decisions/f18-hosted-websites-and-domains/d385-hosted-websites-coverage.md).

## Examples

| Case | Result |
|---|---|
| Renewal fails 20 days before | Alert at once |

## Applies to

Every F18 use case concerned.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F18-12 Mail records for delivery](br-f18-12-mail-records-for-delivery.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F18-14 Analytics only with consent](br-f18-14-analytics-only-with-consent.md)
