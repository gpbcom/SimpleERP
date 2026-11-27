🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💼 [SC03 Services](../README.md) › 🗃️ [Data](README.md) ›
🗃️ E-SC03-12 Shared item

# 🗃️ E-SC03-12 Shared item

**Status:** ✅ specified

## Purpose

Something shared with a client in the portal.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| engagement, kind | records | yes | BR-SC03-12 | - | E-207, report | no | no |
| approval | asked, approved, refused | no | - | - | approved | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : BR-SC03-12
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

- [UC-SC03-11](../use-cases/05-client-and-people/uc-sc03-11-share-with-the-client-in-the-portal.md)

## Open questions

None.

---

⬅️ [E-SC03-11 Skill](e-sc03-11-skill.md) · ⬆️ [Up](README.md) ·
➡️ [E-SC03-13 Satisfaction survey](e-sc03-13-satisfaction-survey.md)
