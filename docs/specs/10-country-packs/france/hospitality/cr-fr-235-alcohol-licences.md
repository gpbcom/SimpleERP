🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🍽️ [Hospitality](README.md) › ⚖️ CR-FR-235 Alcohol licences and opening hours

# ⚖️ CR-FR-235 Alcohol licences and opening hours

**Status:** 🔄 (Proposed) values to read in the official source

## Statement

(Proposed) A place selling alcohol holds the licence of its category, declared at the town hall before opening, and the
person who runs it holds an operating permit. The mayor or the prefect may set the hours of service and ban sales near
certain places. Serving a minor is an offence. See also [CR-FR-109](cr-fr-109-alcohol-licences.md), which this rule
completes with the hours and the permit.

## Values

- (Proposed) Licence category and declaration before opening.
- (Proposed) Operating permit obtained by a training course and renewed by a shorter one.
- (Proposed) Hours and banned zones set by the authority.
- (Proposed) SimpleERP enforces: alcohol is served within the licence's category and hours.
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

(Proposed) To read.

## Enforced by

- [BR-SC06-20 Alcohol is served within the licence's category and hours](../../../08-sectors/sc06-hospitality/business-rules/br-sc06-20-alcohol-is-served-within-the-licences-category-and-hours.md)
- [UC-SC06-20 Keep alcohol licences current](../../../08-sectors/sc06-hospitality/use-cases/06-campsites-catering-groups-and-pricing/uc-sc06-20-keep-alcohol-licences-current.md)

## When the law changes

Watched in the law corpus: Alcohol licences. A change flags this rule and warns the administrators; the corrected rule
ships in a pack update (D294).

## Penalty

Not read yet.

## Exceptions

(Proposed) Temporary bars of associations have their own authorisation.

## Open questions

The law on alcohol licences and hours is not read yet; the values are to read before launch.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-234 Alcohol excise and bonded warehouses](../tax-and-vat/cr-fr-234-alcohol-excise.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-236 Passenger transport registration and licences](../transport/cr-fr-236-passenger-transport-licences.md)
