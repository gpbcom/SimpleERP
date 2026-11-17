🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F18-07 Domain

# 🗃️ E-F18-07 Domain

**Status:** ✅ specified

## Purpose

A domain held or connected.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| name, registrar, holder, renewal | records | yes | BR-F18-10 | - | acme.fr, registrar R, Acme, auto | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-F18-09
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

- [UC-F18-09](../use-cases/03-domain-and-dns/uc-f18-09-buy-or-transfer-a-domain.md)
- [UC-F18-10](../use-cases/03-domain-and-dns/uc-f18-10-connect-an-existing-domain.md)
- [UC-F18-20](../use-cases/05-run-the-site/uc-f18-20-watch-uptime-renewals-and-expiry.md)

## Open questions

None.

---

⬅️ [E-F18-06 Application](e-f18-06-application.md) · ⬆️ [Up](README.md) ·
➡️ [E-F18-08 DNS record](e-f18-08-dns-record.md)
