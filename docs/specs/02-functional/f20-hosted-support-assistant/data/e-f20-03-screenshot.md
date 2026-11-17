🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F20-03 Screenshot

# 🗃️ E-F20-03 Screenshot

**Status:** ✅ specified

## Purpose

A masked screenshot.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| request, page, masked, kept to | records | yes | BR-F20-06 | - | R-41, invoices, yes, 2027-11 | yes | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Active : UC-F20-03
```

## Indexes and search

By number, date, partner.

## Retention

2 years after closing, then erased:
[CR-FR-052 Personal data kept no longer than needed](../../../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md).

## Audit

Every change.

## Import and export

CSV, FEC where relevant.

## Used by

- [UC-F20-03](../use-cases/01-talk-it-through/uc-f20-03-share-screenshots-when-needed.md)
- [UC-F20-18](../use-cases/04-govern-the-assistant/uc-f20-18-mask-personal-data-and-secrets.md)
- [UC-F20-20](../use-cases/04-govern-the-assistant/uc-f20-20-export-a-support-conversation.md)
- [UC-F20-28 Report something broken from the screen](../use-cases/07-employees-help/uc-f20-28-report-something-broken-from-the-screen.md)

## Open questions

None.

---

⬅️ [E-F20-02 Message](e-f20-02-message.md) · ⬆️ [Up](README.md) · ➡️ [E-F20-04 Diagnosis](e-f20-04-diagnosis.md)
