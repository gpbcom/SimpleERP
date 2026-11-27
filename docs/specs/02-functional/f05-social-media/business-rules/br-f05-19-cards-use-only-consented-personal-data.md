🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📣 [F5 Social media and marketing](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F5-19 Cards use only consented personal data

# 📏 BR-F5-19 Cards use only consented personal data

**Status:** ✅ specified

## Statement

A marketing card shows a contact's personal data (name, purchase, loyalty tier or any other field) only when that
contact's recorded consent covers that use; for every other contact the card shows the generic text of the same field.

## Why

Marketing by electronic means needs the contact's consent, and personal data is used only for the purpose it was
collected for ([CR-FR-063](../../../10-country-packs/france/consumer/cr-fr-063-electronic-marketing-consent.md),
[CR-FR-050](../../../10-country-packs/france/data-protection/cr-fr-050-privacy-by-design.md));
[BR-F5-08 Marketing messages need consent](br-f05-08-marketing-needs-consent.md) already forbids marketing without
consent. The owner asked for marketing cards
([D524](../../../06-decisions/f05-social-media/d524-benchmark-gaps-f05-social-media.md)).

## Examples

| Case | Result |
|---|---|
| A contact who consented to marketing emails and personalisation | the card shows the first name and the last order |
| A contact who consented to emails but not to personalisation | the card shows the generic text |
| A contact with no consent record | the card is not generated for any channel |
| A consent withdrawn after the card was made | the card is withdrawn at once and its link shows the generic card |
| A merge field that needs data the system does not hold | the generic text, counted in the preview |

## Applies to

- [UC-F5-24](../use-cases/10-referrals-push-and-listening/uc-f05-24-create-marketing-cards.md)
- [E-F5-21 Marketing card](../data/e-f05-21-marketing-card.md)
- [E-F5-10 Consent and suppression record](../data/e-f05-10-consent-and-suppression-record.md)
- [E-F5-18 Contact](../data/e-f05-18-contact.md)

## Exceptions

None; a contact the company must write to by law (a recall, a legal notice) is not a marketing card and does not use
this rule.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F5-18 Return counts only traced revenue](br-f05-18-return-counts-only-traced-revenue.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F5-20](br-f05-20-referral-rewards-wait-until-the-referred-sale-is-paid.md)
