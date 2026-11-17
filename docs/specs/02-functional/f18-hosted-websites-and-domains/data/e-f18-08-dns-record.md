🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F18-08 DNS record

# 🗃️ E-F18-08 DNS record

**Status:** ✅ specified

## Purpose

A record of the zone.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| domain, type, name, value | records | yes | BR-F18-11, BR-F18-12 | - | acme.fr, MX, @, mail host | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : UC-F18-10
```

## Indexes and search

By number, date, partner.

## Retention

Kept for the period of its kind of record in the country pack (D293), or else its kind's default in the
[retention schedule](../../../05-non-functional/data-retention.md).

## Audit

Every change.

## Import and export

CSV, FEC where relevant.

## Used by

- [UC-F18-10](../use-cases/03-domain-and-dns/uc-f18-10-connect-an-existing-domain.md)
- [UC-F18-11](../use-cases/03-domain-and-dns/uc-f18-11-manage-the-dns-zone-and-certificates.md)
- [UC-F18-12](../use-cases/03-domain-and-dns/uc-f18-12-set-mail-records-spf-dkim-and-dmarc.md)

## Open questions

None.

---

⬅️ [E-F18-07 Domain](e-f18-07-domain.md) · ⬆️ [Up](README.md) ·
➡️ [E-F18-09 TLS certificate](e-f18-09-tls-certificate.md)
