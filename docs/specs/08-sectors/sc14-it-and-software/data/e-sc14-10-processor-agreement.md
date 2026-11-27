🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💻 [SC14 IT and software](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC14-10 Processor agreement

# 🗃️ E-SC14-10 Processor agreement

**Status:** ✅ specified

## Purpose

A signed processor agreement.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| customer, version, signed | records | yes | BR-SC14-06 | - | Acme, v3, 2 Nov | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Sent : UC-SC14-11
  Sent --> Signed : UC-SC14-11
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

- [UC-SC14-11](../use-cases/05-security-and-data-compliance/uc-sc14-11-sign-data-processing-agreements.md)

## Open questions

None.

---

⬅️ [E-SC14-09 Health score](e-sc14-09-health-score.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC14-11 Component](e-sc14-11-component.md)
