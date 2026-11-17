🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F18-05 Job posting

# 🗃️ E-F18-05 Job posting

**Status:** ✅ specified

## Purpose

An opening posted on a channel.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| opening, channel, status, posted on | records | yes | BR-F18-07 | - | Carer, Indeed, live, 2026-11-05 | no | no |

## Relations

As its use cases.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Checked : UC-F18-05
  Checked --> Live : UC-F18-06
  Live --> Blocked : BR-F18-07
  Blocked --> Live : UC-F18-06
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

- [UC-F18-05](../use-cases/02-careers/uc-f18-05-publish-a-careers-page-from-openings.md)
- [UC-F18-06](../use-cases/02-careers/uc-f18-06-post-openings-to-linkedin-and-indeed.md)

## Open questions

None.

---

⬅️ [E-F18-04 Contact message](e-f18-04-contact-message.md) · ⬆️ [Up](README.md) ·
➡️ [E-F18-06 Application](e-f18-06-application.md)
