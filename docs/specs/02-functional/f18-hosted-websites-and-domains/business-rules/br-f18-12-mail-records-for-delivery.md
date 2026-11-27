🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F18-12 Mail records for delivery

# 📏 BR-F18-12 Mail records for delivery

**Status:** ✅ specified

## Statement

SPF, DKIM and DMARC records are set so that the ERP's emails are delivered, and checked weekly.

## Why

See [D385](../../../06-decisions/f18-hosted-websites-and-domains/d385-hosted-websites-coverage.md).

## Examples

| Case | Result |
|---|---|
| DKIM key missing | Alert, fix proposed |

## Applies to

Every F18 use case concerned.

- [UC-F18-23 Create mailboxes on the domain](../use-cases/03-domain-and-dns/uc-f18-23-create-mailboxes-on-the-domain.md)

## Exceptions

None.

## Configurable

DMARC policy.

## Open questions

None.

---

⬅️ [BR-F18-11 DNS changes are planned and checked](br-f18-11-dns-changes-are-planned.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F18-13 Certificates renewed early](br-f18-13-certificates-renewed-early.md)
