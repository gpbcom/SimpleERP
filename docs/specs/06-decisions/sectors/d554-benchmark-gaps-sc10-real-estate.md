🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D554 Benchmark gaps of SC10 Real estate

# 📜 D554 Benchmark gaps of SC10 Real estate

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found four situations
that property suites handle and SC10 did not: short-term rentals, commercial leases, furnished rentals and coworking.
Three carry a legal duty (the tourist tax, the index and caps of the commercial rent, the depreciation of furnished
rentals).

## Options

- G163 Short-term rentals: stays with the tourist tax counted per night and guest, or a flat tax added to the price.
- G164 Commercial leases: leases with their periods and an index within the caps, or a rent changed by hand each year.
- G165 Furnished rentals (LMNP): a tax file with the depreciation limited to the result, or the figures left to the
  landlord's own sheet.
- G166 Coworking: memberships with room credits, or each booking billed on its own.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC10 gets four use cases in one new flow, FL-SC10-07, each with its screen, its rule, its entity and its list. All at
full depth now. Each legal duty is written in plain words and marked as proposed until its France-pack rule was
written (the rules now exist);
no article is quoted.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G163 | Short-term rentals | UC-SC10-21: stays with the tourist tax counted per night and guest | "Short-term rentals" |
| G164 | Commercial leases | UC-SC10-22: commercial rents revised on the named index within the caps | "Commercial leases" |
| G165 | Furnished rentals (LMNP) | UC-SC10-23: depreciation deducted only up to the rental result | "Furnished rentals (LMNP)" |
| G166 | Coworking | UC-SC10-24: rooms booked within the membership's credits | "Coworking" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "SC10 Real estate").

## Consequences

- G163 Short-term rentals:
  [UC-SC10-21](../../08-sectors/sc10-real-estate/use-cases/07-short-stays-commercial-and-coworking/uc-sc10-21-manage-short-term-rentals.md),
  [S-SC10-21](../../08-sectors/sc10-real-estate/screens/07-short-stays-commercial-and-coworking/s-sc10-21-short-term-rentals.md)
  and
  [BR-SC10-16](../../08-sectors/sc10-real-estate/business-rules/br-sc10-16-the-tourist-tax-is-collected-per-night-and-guest.md),
  with [E-SC10-17](../../08-sectors/sc10-real-estate/data/e-sc10-17-stay.md) Stay and its list
  [S-SC10-L17](../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l17-stays.md).
- G164 Commercial leases:
  [UC-SC10-22](../../08-sectors/sc10-real-estate/use-cases/07-short-stays-commercial-and-coworking/uc-sc10-22-manage-commercial-leases.md),
  [S-SC10-22](../../08-sectors/sc10-real-estate/screens/07-short-stays-commercial-and-coworking/s-sc10-22-commercial-leases.md)
  and
  [BR-SC10-17](../../08-sectors/sc10-real-estate/business-rules/br-sc10-17-rents-are-indexed-on-ilc-or-ilat-within-the-caps.md),
  with [E-SC10-18](../../08-sectors/sc10-real-estate/data/e-sc10-18-commercial-lease.md) Commercial lease and its list
  [S-SC10-L18](../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l18-commercial-leases.md).
- G165 Furnished rentals (LMNP):
  [UC-SC10-23](../../08-sectors/sc10-real-estate/use-cases/07-short-stays-commercial-and-coworking/uc-sc10-23-keep-furnished-rental-figures.md),
  [S-SC10-23](../../08-sectors/sc10-real-estate/screens/07-short-stays-commercial-and-coworking/s-sc10-23-furnished-rentals.md)
  and
  [BR-SC10-18](../../08-sectors/sc10-real-estate/business-rules/br-sc10-18-depreciation-never-creates-a-rental-loss.md),
  with [E-SC10-19](../../08-sectors/sc10-real-estate/data/e-sc10-19-furnished-property.md) Furnished property and its
  list [S-SC10-L19](../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l19-furnished-properties.md).
- G166 Coworking:
  [UC-SC10-24](../../08-sectors/sc10-real-estate/use-cases/07-short-stays-commercial-and-coworking/uc-sc10-24-run-a-coworking-space.md),
  [S-SC10-24](../../08-sectors/sc10-real-estate/screens/07-short-stays-commercial-and-coworking/s-sc10-24-coworking.md)
  and
  [BR-SC10-19](../../08-sectors/sc10-real-estate/business-rules/br-sc10-19-rooms-are-booked-within-the-memberships-credits.md),
  with [E-SC10-20](../../08-sectors/sc10-real-estate/data/e-sc10-20-membership.md) Membership and its list
  [S-SC10-L20](../../08-sectors/sc10-real-estate/screens/00-lists/s-sc10-l20-memberships.md).
- Drawn in [FL-SC10-07](../../08-sectors/sc10-real-estate/flows/fl-sc10-07-short-stays-commercial-and-coworking.md)
  Short stays, commercial leases, LMNP and coworking.

## Related

- [FL-SC10-07](../../08-sectors/sc10-real-estate/flows/fl-sc10-07-short-stays-commercial-and-coworking.md)
- [D344 Real estate sector coverage](d344-real-estate-sector-coverage.md)
- [D346 SC10 use cases](d346-sc10-use-cases.md)
- [U34 Property manager](../../01-users/personas/u34-property-manager.md)

---

⬅️ [D553 Benchmark gaps of SC09 Health practices](d553-benchmark-gaps-sc09-health-practices.md) · ⬆️ [Up](README.md) ·
➡️ [D555 Benchmark gaps of SC11 Professional firms](d555-benchmark-gaps-sc11-professional-firms.md)
