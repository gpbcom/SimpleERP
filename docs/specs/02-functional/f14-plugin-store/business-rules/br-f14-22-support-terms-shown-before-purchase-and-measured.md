🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F14-22 Support terms shown before purchase and measured

# 📏 BR-F14-22 Support terms shown before purchase and measured

**Status:** ✅ specified

## Statement

A paid plan states its support terms (channels, languages, hours, first-response time) before purchase; the store
measures the first-response time of each support request and shows the publisher's record on the listing.

## Why

Paid plugins sell support, updates and hosting (D443); buyers must know what they pay for.

## Examples

| Case | Result |
|---|---|
| Plan "team": email, French and English, weekdays 9 to 18, first response within 1 business day | passes: shown |
| Plan with no support terms | fails: cannot be published |
| Request answered in 3 business days on a 1-day term | passes: counted as missed on the record |

## Applies to

- [UC-F14-27 Set and honour support terms of a paid plan](../use-cases/02-buy-and-licence/uc-f14-27-set-and-honour-support-terms-of-a-paid-plan.md)
- [UC-F14-05 Buy a paid plugin or subscription](../use-cases/02-buy-and-licence/uc-f14-05-buy-a-paid-plugin-or-subscription.md)
- [UC-F14-06 Manage licences and seats](../use-cases/02-buy-and-licence/uc-f14-06-manage-licences-and-seats.md)
- [UC-F14-12 Set prices and plans](../use-cases/04-money-and-taxes/uc-f14-12-set-prices-and-plans.md)

## Exceptions

Free plans may state "community support only".

## Configurable

The publisher sets the terms per plan.

## Open questions

None.

---

⬅️ [BR-F14-21 Listings and plugins in the user's language](br-f14-21-listings-and-plugins-in-the-users-language.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F14-23](br-f14-23-rollback-restores-the-previous-version-and-data.md)
