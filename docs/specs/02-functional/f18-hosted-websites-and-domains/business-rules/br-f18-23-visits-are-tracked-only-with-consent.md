🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🌐 [F18 Hosted websites and domains (hosted edition)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F18-23 Visits are tracked only with consent

# 📏 BR-F18-23 Visits are tracked only with consent

**Status:** 🔄 waiting for the owner

## Statement

A visit is recorded only after the visitor accepted tracking on the consent banner; a visitor who refuses or has not
chosen leaves no record, not even a count, and consent withdrawn erases the visits of that device and cuts their link to
a contact.

## Why

Following a person across a site without their agreement is not allowed and, once recorded, cannot be undone. The owner
asked for visitor tracking for sales
[D537](../../../06-decisions/f18-hosted-websites-and-domains/d537-benchmark-gaps-f18-hosted-websites-and-domains.md).
(Proposed) The France-pack rule on consent for trackers stays in
[CR-FR-070](../../../10-country-packs/france/data-protection/cr-fr-070-cookie-consent.md).

## Examples

| Case | Result |
|---|---|
| A visitor who accepts, then sends a form | visits linked to the contact |
| A visitor who refuses | nothing recorded, the site works as usual |
| A visitor who has not yet chosen | nothing recorded until they accept |
| A visitor who withdraws consent | visits erased, link cut |
| A visit 14 months old with a 13-month retention | erased |

## Applies to

- [UC-F18-29](../use-cases/07-tests-visitors-and-accessibility/uc-f18-29-track-known-visitors-for-sales.md)
- [E-F18-21 Visit](../data/e-f18-21-visit.md)
- [E-F18-11 Audience figure](../data/e-f18-11-audience-figure.md)
- [E-F11-15 Tracker consent](../../f11-online-shop/data/e-f11-15-tracker-consent.md)

## Exceptions

None.

## Configurable

The retention of visits (13 months by default) and the daily limit of alerts, by the owner.

## Open questions

None.

---

⬅️ [BR-F18-22 Tests end at significance or their end date](br-f18-22-tests-end-at-significance-or-their-end-date.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F18-24](br-f18-24-an-e-shop-publishes-its-accessibility-statement.md)
