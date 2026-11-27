🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D550 Benchmark gaps of SC06 Hospitality

# 📜 D550 Benchmark gaps of SC06 Hospitality

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found six situations
that hospitality suites handle and SC06 did not: campsites and catering, groups and seminars, dynamic pricing, alcohol
licences (a French legal duty) and guest profiles. Three carry a limit (the season grid, the cut-off date and the
licence's category and hours), and one a safety duty (the allergies).

## Options

- G19 Campsites and catering: pitches priced by a season grid, or pitches handled as ordinary rooms with manual prices.
- G19 Campsites and catering: catering quotes that list the allergens of every dish, or free-text quotes.
- G147 Groups and seminars: room blocks released at the cut-off date, or one reservation per room entered by hand.
- G148 Dynamic pricing: rate rules with a floor and a ceiling, or manual rate changes by the receptionist.
- G149 Alcohol licences: licences read by the till with category and hours, or a paper file outside the system.
- G150 Guest profiles: a guest profile with allergies shown at every order, or notes on the reservation only.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC06 gets six use cases in one new flow, FL-SC06-06, each with its screen, its rule, its entity and its list. All at
full depth now. Each legal duty is written in plain words and marked as proposed until its France-pack rule was
written (the rules now exist).

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G19 | Campsites and catering | UC-SC06-16: pitch prices that follow the season grid | "Campsites and catering" |
| G19 | Campsites and catering | UC-SC06-17: catering quotes that list the allergens | "Campsites and catering" |
| G147 | Groups and seminars | UC-SC06-18: room blocks released at the cut-off date | "Groups and seminars" |
| G148 | Dynamic pricing | UC-SC06-19: dynamic prices kept between a floor and a ceiling | "Dynamic pricing" |
| G149 | Alcohol licences | UC-SC06-20: alcohol served only within the licence's category and hours | "Alcohol licences" |
| G150 | Guest profiles | UC-SC06-21: allergies shown at every order | "Guest profiles" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "SC06 Hospitality").

## Consequences

- G19 Campsites and catering:
  [UC-SC06-16](../../08-sectors/sc06-hospitality/use-cases/06-campsites-catering-groups-and-pricing/uc-sc06-16-rent-campsite-pitches.md),
  [S-SC06-16](../../08-sectors/sc06-hospitality/screens/06-campsites-catering-groups-and-pricing/s-sc06-16-campsite.md)
  and [BR-SC06-16](../../08-sectors/sc06-hospitality/business-rules/br-sc06-16-pitch-prices-follow-the-season-grid.md),
  with [E-SC06-13](../../08-sectors/sc06-hospitality/data/e-sc06-13-pitch.md) Pitch and its list
  [S-SC06-L13](../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l13-pitches.md).
- G19 Campsites and catering:
  [UC-SC06-17](../../08-sectors/sc06-hospitality/use-cases/06-campsites-catering-groups-and-pricing/uc-sc06-17-quote-and-deliver-catering.md),
  [S-SC06-17](../../08-sectors/sc06-hospitality/screens/06-campsites-catering-groups-and-pricing/s-sc06-17-catering.md)
  and [BR-SC06-17](../../08-sectors/sc06-hospitality/business-rules/br-sc06-17-catering-quotes-list-allergens.md), with
  [E-SC06-14](../../08-sectors/sc06-hospitality/data/e-sc06-14-catering-order.md) Catering order and its list
  [S-SC06-L14](../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l14-catering-orders.md).
- G147 Groups and seminars:
  [UC-SC06-18](../../08-sectors/sc06-hospitality/use-cases/06-campsites-catering-groups-and-pricing/uc-sc06-18-book-groups-and-seminars.md),
  [S-SC06-18](../../08-sectors/sc06-hospitality/screens/06-campsites-catering-groups-and-pricing/s-sc06-18-groups-and-seminars.md)
  and
  [BR-SC06-18](../../08-sectors/sc06-hospitality/business-rules/br-sc06-18-room-blocks-are-released-at-the-cut-off-date.md),
  with [E-SC06-15](../../08-sectors/sc06-hospitality/data/e-sc06-15-group-booking.md) Group booking and its list
  [S-SC06-L15](../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l15-group-bookings.md).
- G148 Dynamic pricing:
  [UC-SC06-19](../../08-sectors/sc06-hospitality/use-cases/06-campsites-catering-groups-and-pricing/uc-sc06-19-set-prices-dynamically.md),
  [S-SC06-19](../../08-sectors/sc06-hospitality/screens/06-campsites-catering-groups-and-pricing/s-sc06-19-dynamic-pricing.md)
  and
  [BR-SC06-19](../../08-sectors/sc06-hospitality/business-rules/br-sc06-19-dynamic-prices-stay-within-floor-and-ceiling.md),
  with [E-SC06-16](../../08-sectors/sc06-hospitality/data/e-sc06-16-price-rule.md) Price rule and its list
  [S-SC06-L16](../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l16-price-rules.md).
- G149 Alcohol licences:
  [UC-SC06-20](../../08-sectors/sc06-hospitality/use-cases/06-campsites-catering-groups-and-pricing/uc-sc06-20-keep-alcohol-licences-current.md),
  [S-SC06-20](../../08-sectors/sc06-hospitality/screens/06-campsites-catering-groups-and-pricing/s-sc06-20-alcohol-licences.md)
  and
  [BR-SC06-20](../../08-sectors/sc06-hospitality/business-rules/br-sc06-20-alcohol-is-served-within-the-licences-category-and-hours.md),
  with [E-SC06-17](../../08-sectors/sc06-hospitality/data/e-sc06-17-licence.md) Licence and its list
  [S-SC06-L17](../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l17-licences.md).
- G150 Guest profiles:
  [UC-SC06-21](../../08-sectors/sc06-hospitality/use-cases/06-campsites-catering-groups-and-pricing/uc-sc06-21-know-the-guest.md),
  [S-SC06-21](../../08-sectors/sc06-hospitality/screens/06-campsites-catering-groups-and-pricing/s-sc06-21-guest-profiles.md)
  and [BR-SC06-21](../../08-sectors/sc06-hospitality/business-rules/br-sc06-21-allergies-are-shown-at-every-order.md),
  with [E-SC06-18](../../08-sectors/sc06-hospitality/data/e-sc06-18-guest-profile.md) Guest profile and its list
  [S-SC06-L18](../../08-sectors/sc06-hospitality/screens/00-lists/s-sc06-l18-guest-profiles.md).
- Drawn in [FL-SC06-06](../../08-sectors/sc06-hospitality/flows/fl-sc06-06-campsites-catering-groups-and-pricing.md)
  Campsites, catering, groups, pricing and licences.

## Related

- [FL-SC06-06](../../08-sectors/sc06-hospitality/flows/fl-sc06-06-campsites-catering-groups-and-pricing.md)
- [D332 Hospitality sector coverage](d332-hospitality-sector-coverage.md)
- [D334 SC06 use cases](d334-sc06-use-cases.md)
- [U28 Hotel receptionist](../../01-users/personas/u28-hotel-receptionist.md)

---

⬅️ [D549 Benchmark gaps of SC05 Manufacturing](d549-benchmark-gaps-sc05-manufacturing.md) · ⬆️ [Up](README.md) ·
➡️ [D551 Benchmark gaps of SC07 Transport](d551-benchmark-gaps-sc07-transport.md)
