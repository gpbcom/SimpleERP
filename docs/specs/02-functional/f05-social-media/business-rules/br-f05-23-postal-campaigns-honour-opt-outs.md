🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📣 [F5 Social media and marketing](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F5-23 Postal campaigns honour opt-outs

# 📏 BR-F5-23 Postal campaigns honour opt-outs

**Status:** ✅ specified

## Statement

A postal campaign never includes a contact who objected to postal marketing, and an objection received before printing
removes that contact's letter; the opt-out list is checked again at the moment the file is sent.

## Why

A person may object to direct marketing at any time, whatever the channel
([CR-FR-051](../../../10-country-packs/france/data-protection/cr-fr-051-access-and-erasure.md)); the owner asked for
postal mail campaigns ([D524](../../../06-decisions/f05-social-media/d524-benchmark-gaps-f05-social-media.md)) and the
same consent record serves email and paper ([BR-F5-10](br-f05-10-consent-is-proven-and-withdrawn-at-once.md)).

## Examples

| Case | Result |
|---|---|
| A contact who objected to postal marketing in October | no letter is planned for them |
| An objection received the day before the file is sent | the contact is removed at sending |
| An objection received after posting | the contact is flagged for the next mailing |
| A contact with consent for email only | a postal letter is allowed if the contact did not object to postal marketing |
| An address that fails the format check | left out and listed |

## Applies to

- [UC-F5-28](../use-cases/10-referrals-push-and-listening/uc-f05-28-send-postal-mail-campaigns.md)
- [E-F5-25 Postal campaign](../data/e-f05-25-postal-campaign.md)
- [E-F5-10 Consent and suppression record](../data/e-f05-10-consent-and-suppression-record.md)
- [E-F5-18 Contact](../data/e-f05-18-contact.md)

## Exceptions

A letter the company must send by law (a notice, a recall) is not marketing and ignores the opt-out list.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F5-22 Listening collects public content only](br-f05-22-listening-collects-public-content-only.md) ·
⬆️ [Up](README.md)
