🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📣 [F5 Social media and marketing](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F5-21 Push needs the device's opt-in

# 📏 BR-F5-21 Push needs the device's opt-in

**Status:** ✅ specified

## Statement

A marketing push goes only to a device on which the customer gave the push opt-in, and stops reaching it at once when
they opt out; a device without an opt-in is never counted as reachable.

## Why

A push writes to the customer's own device and is electronic marketing
([CR-FR-063](../../../10-country-packs/france/consumer/cr-fr-063-electronic-marketing-consent.md),
[CR-FR-070](../../../10-country-packs/france/data-protection/cr-fr-070-cookie-consent.md));
[BR-F5-08 Marketing messages need consent](br-f05-08-marketing-needs-consent.md) requires consent for marketing. The
owner asked for push notifications
([D524](../../../06-decisions/f05-social-media/d524-benchmark-gaps-f05-social-media.md)).

## Examples

| Case | Result |
|---|---|
| A device that accepted push in the app | reachable |
| A device that never answered the opt-in | left out |
| A customer with consent for email only | no push is sent |
| An opt-out recorded at 10:00 and a send at 10:05 | the device receives nothing |
| A delivery update for an order | a service message under the notification settings, not this rule |

## Applies to

- [UC-F5-26](../use-cases/10-referrals-push-and-listening/uc-f05-26-send-push-notifications.md)
- [E-F5-23 Push campaign](../data/e-f05-23-push-campaign.md)
- [E-F5-10 Consent and suppression record](../data/e-f05-10-consent-and-suppression-record.md)

## Exceptions

Service messages about an order or an account are not marketing and follow the customer's notification settings.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F5-20](br-f05-20-referral-rewards-wait-until-the-referred-sale-is-paid.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F5-22 Listening collects public content only](br-f05-22-listening-collects-public-content-only.md)
