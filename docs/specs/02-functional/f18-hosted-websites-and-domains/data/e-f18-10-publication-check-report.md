🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 🗃️ [Data](README.md) ›
🗃️ E-F18-10 Publication check report

# 🗃️ E-F18-10 Publication check report

**Status:** ✅ specified

## Purpose

Results of the publication checks.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| site version, check, result | records | yes | BR-F18-04 | - | v12, accessibility, passed | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Recorded : BR-F18-04
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

- [UC-F18-14](../use-cases/04-test-and-publish/uc-f18-14-run-the-automatic-checks.md)
- [UC-F18-15](../use-cases/04-test-and-publish/uc-f18-15-approve-publish-and-roll-back.md)

## Open questions

None.

---

⬅️ [E-F18-09 TLS certificate](e-f18-09-tls-certificate.md) · ⬆️ [Up](README.md) ·
➡️ [E-F18-11 Audience figure](e-f18-11-audience-figure.md)
