🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 🗃️ [Data](README.md) ›
🗃️ E-F18-11 Audience figure

# 🗃️ E-F18-11 Audience figure

**Status:** ✅ specified

## Purpose

Consented audience and search figures.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| site, period, visits, top pages | records | yes | BR-F18-14 | - | Acme, Nov, 1 240, services | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : BR-F18-14
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

- [UC-F18-18](../use-cases/05-run-the-site/uc-f18-18-measure-audience-and-search-ranking.md)

## Open questions

None.

---

⬅️ [E-F18-10 Publication check report](e-f18-10-publication-check-report.md) · ⬆️ [Up](README.md) ·
➡️ [E-F18-12 Uptime event](e-f18-12-uptime-event.md)
