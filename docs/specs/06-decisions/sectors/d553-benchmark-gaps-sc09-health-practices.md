🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D553 Benchmark gaps of SC09 Health practices

# 📜 D553 Benchmark gaps of SC09 Health practices

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)). The benchmark found six situations
that health suites handle and SC09 did not: pharmacies, opticians, veterinary practices, dental quotes, health centres
and multi-professional practices. Each carries a legal duty (a valid prescription, a valid ophthalmic prescription, the
veterinary register, the regulated quote, the report to the regional health agency, the funding indicators).

## Options

- G18 Pharmacy and opticians: dispensations tied to a valid prescription, or medicines sold as ordinary stock items.
- G18 Pharmacy and opticians: orders checked against the prescription's validity, or lenses ordered from typed values.
- G159 Veterinary practices: an animal record with the medicine register, or consultations recorded as ordinary
  appointments.
- G160 Dental practices: a regulated quote signed before the care, or a price shown at the end of the visit.
- G161 Health centres: activity counted from the records and reported, or figures typed for the agency.
- G162 Multi-professional practices: indicators counted with their evidence, or a yearly figure entered by hand.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC09 gets six use cases in one new flow, FL-SC09-07, each with its screen, its rule, its entity and its list. All at
full depth now. Each legal duty is written in plain words and marked as proposed until its France-pack rule was
written (the rules now exist);
no article is quoted.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G18 | Pharmacy and opticians | UC-SC09-21: dispensations that need a valid prescription | "Pharmacy and opticians" |
| G18 | Pharmacy and opticians | UC-SC09-22: lenses ordered only to a valid prescription | "Pharmacy and opticians" |
| G159 | Veterinary practices | UC-SC09-23: medicines of a practice written in the register | "Veterinary practices" |
| G160 | Dental practices | UC-SC09-24: prosthetics that need the signed regulated quote | "Dental practices" |
| G161 | Health centres | UC-SC09-25: activity reported to the regional health agency from the records | "Health centres" |
| G162 | Multi-professional practices | UC-SC09-26: funding computed from the indicators reached | "Multi-professional practices" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "SC09 Health practices").

## Consequences

- G18 Pharmacy and opticians:
  [UC-SC09-21](../../08-sectors/sc09-health-practices/use-cases/07-pharmacy-vets-dental-and-centres/uc-sc09-21-dispense-in-a-pharmacy.md),
  [S-SC09-21](../../08-sectors/sc09-health-practices/screens/07-pharmacy-vets-dental-and-centres/s-sc09-21-pharmacy.md)
  and
  [BR-SC09-16](../../08-sectors/sc09-health-practices/business-rules/br-sc09-16-prescription-medicines-need-a-valid-prescription.md),
  with [E-SC09-14](../../08-sectors/sc09-health-practices/data/e-sc09-14-dispensation.md) Dispensation and its list
  [S-SC09-L14](../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l14-dispensations.md).
- G18 Pharmacy and opticians:
  [UC-SC09-22](../../08-sectors/sc09-health-practices/use-cases/07-pharmacy-vets-dental-and-centres/uc-sc09-22-sell-eyewear-to-a-prescription.md),
  [S-SC09-22](../../08-sectors/sc09-health-practices/screens/07-pharmacy-vets-dental-and-centres/s-sc09-22-eyewear.md)
  and
  [BR-SC09-17](../../08-sectors/sc09-health-practices/business-rules/br-sc09-17-lenses-follow-the-prescription-and-its-validity.md),
  with [E-SC09-15](../../08-sectors/sc09-health-practices/data/e-sc09-15-eyewear-order.md) Eyewear order and its list
  [S-SC09-L15](../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l15-eyewear-orders.md).
- G159 Veterinary practices:
  [UC-SC09-23](../../08-sectors/sc09-health-practices/use-cases/07-pharmacy-vets-dental-and-centres/uc-sc09-23-run-a-veterinary-practice.md),
  [S-SC09-23](../../08-sectors/sc09-health-practices/screens/07-pharmacy-vets-dental-and-centres/s-sc09-23-veterinary.md)
  and
  [BR-SC09-18](../../08-sectors/sc09-health-practices/business-rules/br-sc09-18-dispensed-medicines-enter-the-register.md),
  with [E-SC09-16](../../08-sectors/sc09-health-practices/data/e-sc09-16-animal.md) Animal and its list
  [S-SC09-L16](../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l16-animals.md).
- G160 Dental practices:
  [UC-SC09-24](../../08-sectors/sc09-health-practices/use-cases/07-pharmacy-vets-dental-and-centres/uc-sc09-24-quote-dental-work-with-the-regulated-quote.md),
  [S-SC09-24](../../08-sectors/sc09-health-practices/screens/07-pharmacy-vets-dental-and-centres/s-sc09-24-dental-quotes.md)
  and
  [BR-SC09-19](../../08-sectors/sc09-health-practices/business-rules/br-sc09-19-prosthetics-need-the-regulated-quote-before-care.md),
  with [E-SC09-17](../../08-sectors/sc09-health-practices/data/e-sc09-17-dental-quote.md) Dental quote and its list
  [S-SC09-L17](../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l17-dental-quotes.md).
- G161 Health centres:
  [UC-SC09-25](../../08-sectors/sc09-health-practices/use-cases/07-pharmacy-vets-dental-and-centres/uc-sc09-25-run-a-health-centre.md),
  [S-SC09-25](../../08-sectors/sc09-health-practices/screens/07-pharmacy-vets-dental-and-centres/s-sc09-25-health-centre.md)
  and
  [BR-SC09-20](../../08-sectors/sc09-health-practices/business-rules/br-sc09-20-activity-is-reported-to-the-regional-health-agency.md),
  with [E-SC09-18](../../08-sectors/sc09-health-practices/data/e-sc09-18-centre-activity.md) Centre activity and its
  list [S-SC09-L18](../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l18-centre-activities.md).
- G162 Multi-professional practices:
  [UC-SC09-26](../../08-sectors/sc09-health-practices/use-cases/07-pharmacy-vets-dental-and-centres/uc-sc09-26-run-a-multi-professional-practice.md),
  [S-SC09-26](../../08-sectors/sc09-health-practices/screens/07-pharmacy-vets-dental-and-centres/s-sc09-26-msp.md) and
  [BR-SC09-21](../../08-sectors/sc09-health-practices/business-rules/br-sc09-21-aci-funding-follows-the-indicators-reached.md),
  with [E-SC09-19](../../08-sectors/sc09-health-practices/data/e-sc09-19-aci-indicator.md) ACI indicator and its list
  [S-SC09-L19](../../08-sectors/sc09-health-practices/screens/00-lists/s-sc09-l19-aci-indicators.md).
- Drawn in [FL-SC09-07](../../08-sectors/sc09-health-practices/flows/fl-sc09-07-pharmacy-vets-dental-and-centres.md)
  Pharmacy, eyewear, vets, dental and health centres.

## Related

- [FL-SC09-07](../../08-sectors/sc09-health-practices/flows/fl-sc09-07-pharmacy-vets-dental-and-centres.md)
- [D341 Health practices sector coverage](d341-health-practices-sector-coverage.md)
- [D343 SC09 use cases](d343-sc09-use-cases.md)
- [U33 Medical secretary](../../01-users/personas/u33-medical-secretary.md)

---

⬅️ [D552 Benchmark gaps of SC08 Non-profit](d552-benchmark-gaps-sc08-non-profit.md) · ⬆️ [Up](README.md) ·
➡️ [D554 Benchmark gaps of SC10 Real estate](d554-benchmark-gaps-sc10-real-estate.md)
