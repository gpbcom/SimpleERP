🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🤲 [SC08 Non-profit association](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-SC08-10 Mission

# 🗃️ E-SC08-10 Mission

**Status:** 🔄 waiting for the owner

## Purpose

A volunteer mission.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| title, date, places | records | yes | - | - | Food drive, 5 Dec, 12 | no | no |
| volunteers | list | no | - | - | 9 | yes | no |

## Relations

(Proposed) As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-SC08-10
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

- [UC-SC08-10](../use-cases/04-volunteers/uc-sc08-10-recruit-and-register-volunteers-for-missions.md)

## Open questions

None.

---

⬅️ [E-SC08-09 Grant report](e-sc08-09-grant-report.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC08-11 Volunteer hours](e-sc08-11-volunteer-hours.md)
