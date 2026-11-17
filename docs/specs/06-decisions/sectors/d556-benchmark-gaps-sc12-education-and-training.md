🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D556 Benchmark gaps of SC12 Education and training

# 📜 D556 Benchmark gaps of SC12 Education and training

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found four situations
that education suites handle and SC12 did not: apprentice training centres, driving schools, nurseries and canteens with
activities. Three carry a legal or funding rule (the support level of the operator, the instructor's authorisation, the
fund's scale); the canteen's cut-off is a school rule.

## Options

- G171 Apprentice centres (CFA): contracts with the support level and monthly claims, or the funding entered once a year
  by hand.
- G172 Driving schools: lessons tied to the instructor's authorisation, or lessons recorded as ordinary appointments.
- G173 Nurseries: places with the rate computed from the fund's scale, or a flat rate per family.
- G174 Canteen and activities: bookings locked at the cut-off, or bookings changed freely until the day.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC12 gets four use cases in one new flow, FL-SC12-06, each with its screen, its rule, its entity and its list. All at
full depth now. Each legal duty is written in plain words and marked (Proposed) until the France-pack rule is written;
no article is quoted.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G171 | Apprentice centres (CFA) | UC-SC12-21: funding claimed at the contract's support level, month by month | "Apprentice centres (CFA)" |
| G172 | Driving schools | UC-SC12-22: lessons given only by an authorised instructor | "Driving schools" |
| G173 | Nurseries | UC-SC12-23: hourly rate computed from the fund's scale | "Nurseries" |
| G174 | Canteen and activities | UC-SC12-24: bookings locked at the cut-off time | "Canteen and activities" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "SC12 Education and
training").

## Consequences

- G171 Apprentice centres (CFA):
  [UC-SC12-21](../../08-sectors/sc12-education-and-training/use-cases/06-apprentices-driving-nurseries-and-canteens/uc-sc12-21-run-an-apprentice-training-centre.md),
  [S-SC12-21](../../08-sectors/sc12-education-and-training/screens/06-apprentices-driving-nurseries-and-canteens/s-sc12-21-cfa.md)
  and
  [BR-SC12-16](../../08-sectors/sc12-education-and-training/business-rules/br-sc12-16-funding-follows-the-contracts-support-level.md),
  with [E-SC12-20](../../08-sectors/sc12-education-and-training/data/e-sc12-20-apprenticeship-contract.md)
  Apprenticeship contract and its list
  [S-SC12-L20](../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l20-apprenticeship-contracts.md).
- G172 Driving schools:
  [UC-SC12-22](../../08-sectors/sc12-education-and-training/use-cases/06-apprentices-driving-nurseries-and-canteens/uc-sc12-22-run-a-driving-school.md),
  [S-SC12-22](../../08-sectors/sc12-education-and-training/screens/06-apprentices-driving-nurseries-and-canteens/s-sc12-22-driving-school.md)
  and
  [BR-SC12-17](../../08-sectors/sc12-education-and-training/business-rules/br-sc12-17-lessons-are-taught-by-an-authorised-instructor.md),
  with [E-SC12-21](../../08-sectors/sc12-education-and-training/data/e-sc12-21-driving-lesson.md) Driving lesson and its
  list [S-SC12-L21](../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l21-driving-lessons.md).
- G173 Nurseries:
  [UC-SC12-23](../../08-sectors/sc12-education-and-training/use-cases/06-apprentices-driving-nurseries-and-canteens/uc-sc12-23-run-a-nursery.md),
  [S-SC12-23](../../08-sectors/sc12-education-and-training/screens/06-apprentices-driving-nurseries-and-canteens/s-sc12-23-nursery.md)
  and
  [BR-SC12-18](../../08-sectors/sc12-education-and-training/business-rules/br-sc12-18-hourly-funding-follows-the-caf-scale.md),
  with [E-SC12-22](../../08-sectors/sc12-education-and-training/data/e-sc12-22-childcare-place.md) Childcare place and
  its list [S-SC12-L22](../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l22-childcare-places.md).
- G174 Canteen and activities:
  [UC-SC12-24](../../08-sectors/sc12-education-and-training/use-cases/06-apprentices-driving-nurseries-and-canteens/uc-sc12-24-run-the-canteen-and-activities.md),
  [S-SC12-24](../../08-sectors/sc12-education-and-training/screens/06-apprentices-driving-nurseries-and-canteens/s-sc12-24-canteen.md)
  and
  [BR-SC12-19](../../08-sectors/sc12-education-and-training/business-rules/br-sc12-19-bookings-close-at-the-cut-off-time.md),
  with [E-SC12-23](../../08-sectors/sc12-education-and-training/data/e-sc12-23-meal-booking.md) Meal booking and its
  list [S-SC12-L23](../../08-sectors/sc12-education-and-training/screens/00-lists/s-sc12-l23-meal-bookings.md).
- Drawn in
  [FL-SC12-06](../../08-sectors/sc12-education-and-training/flows/fl-sc12-06-apprentices-driving-nurseries-and-canteens.md)
  Apprentices, driving schools, nurseries, canteens.

## Related

- [FL-SC12-06](../../08-sectors/sc12-education-and-training/flows/fl-sc12-06-apprentices-driving-nurseries-and-canteens.md)
- [D350 Education sector coverage](d350-education-sector-coverage.md)
- [D352 SC12 use cases](d352-sc12-use-cases.md)
- [U38 Training coordinator](../../01-users/personas/u38-training-coordinator.md)

---

⬅️ [D555 Benchmark gaps of SC11 Professional firms](d555-benchmark-gaps-sc11-professional-firms.md) ·
⬆️ [Up](README.md) ·
➡️ [D557 Benchmark gaps of SC13 Agriculture and food](d557-benchmark-gaps-sc13-agriculture-and-food.md)
