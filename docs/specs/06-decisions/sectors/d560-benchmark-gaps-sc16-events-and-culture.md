🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D560 Benchmark gaps of SC16 Events and culture

# 📜 D560 Benchmark gaps of SC16 Events and culture

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found four situations
that event and culture suites handle and SC16 did not: cashless payments, cinemas, touring productions and
photographers. Each carries a duty (balances refundable, admissions reported, shows settled on their contract, releases
before publication).

## Options

- G187 Cashless payments: cashless accounts refundable after the event, or cash tokens with no way to get the balance
  back.
- G188 Cinemas: screenings with their figures reported to the national film centre, or a ticket total typed each week.
- G189 Touring productions: dates settled on their contract terms, or a settlement computed in a spreadsheet.
- G190 Photographers: galleries published only with the releases, or releases kept on paper outside the system.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC16 gets four use cases in one new flow, FL-SC16-06, each with its screen, its rule, its entity and its list. All at
full depth now. Each legal duty is written in plain words and marked as proposed until its France-pack rule was
written (the rules now exist).

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G187 | Cashless payments | UC-SC16-21: unused balances refundable after the event | "Cashless payments" |
| G188 | Cinemas | UC-SC16-22: box-office figures reported to the national film centre | "Cinemas" |
| G189 | Touring productions | UC-SC16-23: each show settled per its contract | "Touring productions" |
| G190 | Photographers | UC-SC16-24: images sold only with the model's release | "Photographers" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "SC16 Events and culture").

## Consequences

- G187 Cashless payments:
  [UC-SC16-21](../../08-sectors/sc16-events-and-culture/use-cases/06-cashless-cinemas-tours-and-photos/uc-sc16-21-run-cashless-payments-at-a-festival.md),
  [S-SC16-21](../../08-sectors/sc16-events-and-culture/screens/06-cashless-cinemas-tours-and-photos/s-sc16-21-cashless.md)
  and
  [BR-SC16-16](../../08-sectors/sc16-events-and-culture/business-rules/br-sc16-16-unused-balances-are-refundable-after-the-event.md),
  with [E-SC16-19](../../08-sectors/sc16-events-and-culture/data/e-sc16-19-cashless-account.md) Cashless account and its
  list [S-SC16-L19](../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l19-cashless-accounts.md).
- G188 Cinemas:
  [UC-SC16-22](../../08-sectors/sc16-events-and-culture/use-cases/06-cashless-cinemas-tours-and-photos/uc-sc16-22-run-a-cinema.md),
  [S-SC16-22](../../08-sectors/sc16-events-and-culture/screens/06-cashless-cinemas-tours-and-photos/s-sc16-22-cinema.md)
  and
  [BR-SC16-17](../../08-sectors/sc16-events-and-culture/business-rules/br-sc16-17-box-office-figures-are-reported-to-the-cnc.md),
  with [E-SC16-20](../../08-sectors/sc16-events-and-culture/data/e-sc16-20-screening.md) Screening and its list
  [S-SC16-L20](../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l20-screenings.md).
- G189 Touring productions:
  [UC-SC16-23](../../08-sectors/sc16-events-and-culture/use-cases/06-cashless-cinemas-tours-and-photos/uc-sc16-23-run-a-tour.md),
  [S-SC16-23](../../08-sectors/sc16-events-and-culture/screens/06-cashless-cinemas-tours-and-photos/s-sc16-23-touring.md)
  and
  [BR-SC16-18](../../08-sectors/sc16-events-and-culture/business-rules/br-sc16-18-each-show-is-settled-per-its-contract.md),
  with [E-SC16-21](../../08-sectors/sc16-events-and-culture/data/e-sc16-21-tour-date.md) Tour date and its list
  [S-SC16-L21](../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l21-tour-dates.md).
- G190 Photographers:
  [UC-SC16-24](../../08-sectors/sc16-events-and-culture/use-cases/06-cashless-cinemas-tours-and-photos/uc-sc16-24-book-shoots-and-sell-photos.md),
  [S-SC16-24](../../08-sectors/sc16-events-and-culture/screens/06-cashless-cinemas-tours-and-photos/s-sc16-24-photography.md)
  and
  [BR-SC16-19](../../08-sectors/sc16-events-and-culture/business-rules/br-sc16-19-images-are-sold-only-with-the-models-release.md),
  with [E-SC16-22](../../08-sectors/sc16-events-and-culture/data/e-sc16-22-gallery.md) Gallery and its list
  [S-SC16-L22](../../08-sectors/sc16-events-and-culture/screens/00-lists/s-sc16-l22-galleries.md).
- Drawn in [FL-SC16-06](../../08-sectors/sc16-events-and-culture/flows/fl-sc16-06-cashless-cinemas-tours-and-photos.md)
  Cashless, cinemas, tours and photographers.

## Related

- [FL-SC16-06](../../08-sectors/sc16-events-and-culture/flows/fl-sc16-06-cashless-cinemas-tours-and-photos.md)
- [D293](../country-packs/d293-capabilities-take-legal-rules-from-the-pack.md)
- [U43 Event producer](../../01-users/personas/u43-event-producer.md)

---

⬅️ [D559 Benchmark gaps of SC15 Wholesale and distribution](d559-benchmark-gaps-sc15-wholesale-and-distribution.md) ·
⬆️ [Up](README.md) ·
➡️ [D561 Benchmark gaps of SC17 Beauty and wellness](d561-benchmark-gaps-sc17-beauty-and-wellness.md)
