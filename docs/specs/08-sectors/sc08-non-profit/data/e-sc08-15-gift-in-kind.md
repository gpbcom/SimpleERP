🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🤲 [SC08 Non-profit association](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC08-15 Gift in kind

# 🗃️ E-SC08-15 Gift in kind

**Status:** 🔄 waiting for the owner

## Purpose

Goods, property or a bequest.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| donor, kind, value | records | yes | BR-SC08-15 | - | estate X, flat, 180 000 | yes | no |
| accepted | date | no | - | - | board 3 Nov | no | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : BR-SC08-15
```

## Indexes and search

(Proposed) By number, date, partner.

## Retention

Kept for the period of its kind of record in the country pack (D293), or else its kind's default in the
[retention schedule](../../../05-non-functional/data-retention.md).

## Audit

Every change.

## Import and export

(Proposed) CSV, FEC where relevant.

## Used by

- [UC-SC08-16](../use-cases/02-donations-and-receipts/uc-sc08-16-manage-bequests-and-gifts-in-kind.md)

## Open questions

None.

---

⬅️ [E-SC08-14 Dedicated fund](e-sc08-14-dedicated-fund.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC08-16 Grant application](e-sc08-16-grant-application.md)
