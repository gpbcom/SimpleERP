🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔭 [F17 Competitive analysis](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F17-06 IP filing

# 🗃️ E-F17-06 IP filing

**Status:** ✅ specified

## Purpose

A patent, trademark or design.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| competitor, kind, title, date | records | yes | BR-F17-02 | - | Rival SA, trademark, RIVALPAY, 2026-09-01 | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-F17-06
```

## Indexes and search

By number, date, partner.

## Retention

Kept 3 years by default, then summarised (BR-F17-11).

## Audit

Every change.

## Import and export

CSV, FEC where relevant.

## Used by

- [UC-F17-06](../use-cases/02-collect-signals/uc-f17-06-follow-patents-trademarks-and-designs.md)

## Open questions

None.

---

⬅️ [E-F17-05 Tender award](e-f17-05-tender-award.md) · ⬆️ [Up](README.md) ·
➡️ [E-F17-07 Review digest](e-f17-07-review-digest.md)
