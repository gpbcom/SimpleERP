🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📣 [F5 Social media and marketing](../README.md) › 🗃️ [Data](README.md) › 🗃️ E-F5-10 Consent and suppression record

# 🗃️ E-F5-10 Consent and suppression record

**Status:** 🔄 waiting for the owner

## Purpose

A contact's marketing consent per channel with its proof, and their suppression.

## Fields

| Name | Type | Required | Validation | Default | Example | Personal data | Custom fields |
|---|---|---|---|---|---|---|---|
| contact | contact | yes | - | - | lea@mail.fr | yes | - |
| channel | email, SMS, WhatsApp | yes | - | - | email | no | - |
| status | given, withdrawn, suppressed | yes | - | - | given | no | - |
| proof | text version, date, source | yes | - | - | form Autumn sale v3, 2026-11-12 | yes | - |
| reason | unsubscribe, bounce, complaint | no | - | - | - | no | - |

## Relations

One per contact and channel.

## Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Given : UC-F5-15
  Given --> Withdrawn : unsubscribe, UC-F5-15
  Given --> Suppressed : bounce or complaint, UC-F5-14
  Withdrawn --> Given : new consent, UC-F5-15
```

## Indexes and search

By contact and channel; the consent register.

## Retention

3 years after the last contact (Proposed).

## Audit

Every change with its source.

## Import and export

Proof exported as PDF or CSV; imports need source and date.

## Used by

- [UC-F5-14 Build a segment of contacts](../use-cases/06-audiences-consent-and-journeys/uc-f05-14-build-a-segment-of-contacts.md)
- [UC-F5-15 Record and prove consent](../use-cases/06-audiences-consent-and-journeys/uc-f05-15-record-and-prove-consent.md)
- [UC-F5-16 Keep emails delivered](../use-cases/06-audiences-consent-and-journeys/uc-f05-16-keep-emails-delivered.md)
- [UC-F5-19 Publish a landing page with a form](../use-cases/08-pages-forms-surveys-and-whatsapp/uc-f05-19-publish-a-landing-page-with-a-form.md)

## Open questions

None.

---

⬅️ [E-F5-09 Contact segment](e-f05-09-contact-segment.md) · ⬆️ [Up](README.md) ·
➡️ [E-F5-11 Ticket type and seat map](e-f05-11-ticket-type-and-seat-map.md)
