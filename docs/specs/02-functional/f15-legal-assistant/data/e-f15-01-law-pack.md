🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
🗃️ [Data](README.md) › 🗃️ E-F15-01 Law pack

# 🗃️ E-F15-01 Law pack

**Status:** ✅ specified

## Purpose

A country's legal sources, ingestion rules, warnings, referral contacts and sources pulled on a schedule (D199, D205).

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| name | text | yes | - | - | France | no | no |
| country | country | yes | one pack per country | - | FR | no | no |
| sources | list | yes | each with its licence (T11) | - | Légifrance codes, KALI, BOSS, Judilibre | no | no |
| warnings | list | no | - | - | Daily rest, CSE threshold | no | no |
| referral contacts | list | yes | - | - | Labour inspectorate offices | no | no |
| publisher | SimpleERP or partner | yes | no review: content pulled from official sources (D205) | SimpleERP | SimpleERP | no | no |
| pull schedule | per source | yes | BR-F15-09 | daily or weekly | daily | no | no |

## Relations

Used by UC-F15-01.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Scheduled : UC-F15-04
```

Installed, refreshed by each scheduled pull (BR-F15-09), removed.

## Indexes and search

By kind, record and date.

## Retention

13 months, law packs while installed.

## Audit

See UC-F15-01's audit events.

## Import and export

Law packs from the store (F14).

## Used by

- [UC-F15-01](../use-cases/01-ask-a-legal-question/uc-f15-01-use-the-legal-assistant.md)
- [UC-F15-04](../use-cases/04-set-up-the-legal-assistant/uc-f15-04-set-up-the-legal-assistant.md)
- [UC-F15-05](../use-cases/04-set-up-the-legal-assistant/uc-f15-05-follow-the-law-packs-refresh.md)
- [UC-F15-07 Keep the compliance calendar](../use-cases/05-duties-and-records/uc-f15-07-keep-the-compliance-calendar.md)
- [UC-F15-13 Answer a client's tax question with their data](../use-cases/01-ask-a-legal-question/uc-f15-13-answer-a-clients-tax-question-with-their-data.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [E-F15-02 Legal warning](e-f15-02-legal-warning.md)
