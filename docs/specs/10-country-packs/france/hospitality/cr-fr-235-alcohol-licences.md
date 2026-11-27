🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🍽️ [Hospitality](README.md) › ⚖️ CR-FR-235 Alcohol licences and opening hours

# ⚖️ CR-FR-235 Alcohol licences and opening hours

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

A place selling alcohol holds the licence of its category, declared at the town hall at least 15 days before opening,
and the person who runs it holds an operating permit; the prefect sets protected zones around health, youth and sports
establishments, and the mayor may ban takeaway alcohol sales in a time slot between 20:00 and 08:00
([Code de la santé publique, art. L3331-1, L3331-2, L3332-1-1, L3332-3, L3332-13, L3335-1](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006155036), read 2026-11-27).
Selling alcohol to minors is forbidden and the server asks for proof of age ([Code de la santé publique, art. L3342-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031927682), read 2026-11-27).
(⚖️ lawyer review before launch, D574) General hours of service set by the prefect: not in the title read. See also [CR-FR-109](cr-fr-109-alcohol-licences.md), which this rule
completes with the hours and the permit.

## Values

- Licence category (3rd or 4th, small or full restaurant licence) and a declaration at least 15 days before opening
  (L3331-1, L3331-2, L3332-3) ([CSP](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006155036), read 2026-11-27).
- Operating permit after a mandatory training, valid 10 years, extended 10 years by a refresher course (L3332-1-1)
  ([CSP](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006155036), read 2026-11-27).
- Protected zones set by the prefect (L3335-1); a takeaway ban slot set by the mayor (L3332-13) ([CSP](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006155036), read 2026-11-27);
  (⚖️ lawyer review before launch, D574) general hours, set locally, not read.
- SimpleERP enforces: alcohol is served within the licence's category and hours.
- Read on [Service-public F22379](https://entreprendre.service-public.gouv.fr/vosdroits/F22379) (verification date and
  article numbers not captured; read again before coding the dates); general bar closing hours are set locally by the
  prefect and are not on the page:
- Read: categories are licence III (up to 18 degrees), licence IV (over 18), restaurant licences (small and full) and
  takeaway licences (small and full); drinks under 1.2 degrees need none.
- Read: the operating permit for on-site sales needs at least 20 hours of training over at least 3 days and is valid 10
  years; night takeaway sales (22:00 to 8:00) need a specific training permit.
- Read: declaration (Cerfa 11542) at least 15 days before opening, transfer or relocation, to the mairie, or to the
  prefecture in Paris and Alsace-Moselle; receipt Cerfa 11543.
- Read: no new licence IV can be created; licence III is capped at one per 450 inhabitants (III and IV counted).
- Read: filling stations cannot sell alcohol from 18:00 to 8:00, nor chilled alcohol; a licence is cancelled after 5
  years of voluntary closure.
- Read: the holder is an adult, not under guardianship, with no barring conviction (5 years or permanent for some
  offences).

## Legal references

- Law to read: alcohol licences and hours (not read yet).

## Effective dates

L3331-1 and L3331-2 since 2016-01-01; L3332-3 since 2019-03-25; L3332-1-1 since 2020-01-30; L3332-13 and
L3335-1 since 2019-12-29 ([Code de la santé publique, title III Débits de boissons](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006155036), read 2026-11-27).

## Enforced by

- [BR-SC06-20 Alcohol is served within the licence's category and hours](../../../08-sectors/sc06-hospitality/business-rules/br-sc06-20-alcohol-is-served-within-the-licences-category-and-hours.md)
- [UC-SC06-20 Keep alcohol licences current](../../../08-sectors/sc06-hospitality/use-cases/06-campsites-catering-groups-and-pricing/uc-sc06-20-keep-alcohol-licences-current.md)

## When the law changes

Watched in the law corpus: Alcohol licences. A change flags this rule and warns the administrators; the corrected rule
ships in a pack update (D294).

## Penalty

Opening without the declaration: 3 750 EUR fine (L3352-3); a 3rd or 4th category outlet outside the legal
conditions: 3 750 EUR and closure (L3352-2); selling alcohol to minors: 7 500 EUR fine (L3353-3)
([Code de la santé publique, art. L3351-1 to L3355-8](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072665/LEGISCTA000006155038/), read 2026-11-27).

## Exceptions

Temporary bars of associations have their own authorisation: the mayor's, five a year, groups one and three only
([Code de la santé publique, art. L3334-2](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006155036), read 2026-11-27).

## Open questions

The general hours of service, set locally, are on the lawyer's list.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-234 Alcohol excise and bonded warehouses](../tax-and-vat/cr-fr-234-alcohol-excise.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-236 Passenger transport registration and licences](../transport/cr-fr-236-passenger-transport-licences.md)
