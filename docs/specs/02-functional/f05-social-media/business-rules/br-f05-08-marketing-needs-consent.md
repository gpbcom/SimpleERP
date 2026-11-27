🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📣 [F5 Social media and marketing](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F5-08 Marketing messages need consent

# 📏 BR-F5-08 Marketing messages need consent

**Status:** ✅ specified

## Statement

Email and SMS marketing goes only to people who may receive it under the country pack, and every message carries an
opt-out that is honoured at once.

## Why

See [D303](../../../06-decisions/f05-social-media/d303-f5-benchmark-gaps.md).

Legal values from the France country pack:
[CR-FR-063 Consent for email and SMS marketing](../../../10-country-packs/france/consumer/cr-fr-063-electronic-marketing-consent.md).

## Examples

| Case | Result |
|---|---|
| Consumer without consent | Left out |
| Opt-out clicked | Removed from every list |

## Applies to

UC-F5-08, UC-F5-09, UC-F5-10, UC-F5-11

- [UC-F5-14 Build a segment of contacts](../use-cases/06-audiences-consent-and-journeys/uc-f05-14-build-a-segment-of-contacts.md)

- [UC-F5-15 Record and prove consent](../use-cases/06-audiences-consent-and-journeys/uc-f05-15-record-and-prove-consent.md)

- [UC-F5-20 Message customers on WhatsApp Business](../use-cases/08-pages-forms-surveys-and-whatsapp/uc-f05-20-message-customers-on-whatsapp-business.md)

## Exceptions

None.

## Configurable

Lists and consent sources.

## Open questions

None.

---

⬅️ [BR-F5-07 Posts queue within network limits](br-f05-07-posts-queue-within-network-limits.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F5-09 Segments are evaluated at send time](br-f05-09-segments-are-evaluated-at-send-time.md)
