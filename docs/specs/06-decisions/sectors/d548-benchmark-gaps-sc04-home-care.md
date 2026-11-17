🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: Sectors](README.md) ›
📜 D548 Benchmark gaps of SC04 Home care

# 📜 D548 Benchmark gaps of SC04 Home care

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found five situations
that home-care suites handle and SC04 did not: the care home (the community care gap G21), CESU vouchers, the agent mode
for family employers, childcare at home and home nursing on prescription. Four carry a legal duty (the health-data
rules, the family as employer, the family allowance aid, the prescription).

## Options

- G21 Community care: a care-home record with health-data access rules, or residents handled as ordinary care
  recipients.
- G139 CESU payments: vouchers reconciled with the issuer batch by batch, or vouchers booked as cash.
- G140 Agent mode: mandates where the family stays the employer, or the provider as employer of every carer.
- G141 Childcare at home: childcare contracts with the aid computed from the fund's table, or a manual aid on each
  invoice.
- G142 Nursing care services: care acts tied to a prescription, or nursing visits recorded as ordinary visits.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

SC04 gets five use cases in one new flow, FL-SC04-06, each with its screen, its rule, its entity and its list. All at
full depth now. Each legal duty is written in plain words and marked until its rule is written.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G21 | Community care | UC-SC04-16: residents' care records that follow the health-data rules | "Community care" |
| G139 | CESU payments | UC-SC04-17: vouchers reconciled with the issuer | "CESU payments" |
| G140 | Agent mode | UC-SC04-18: agent mode where the family is the employer | "Agent mode" |
| G141 | Childcare at home | UC-SC04-19: family allowance aid that follows the fund's rules | "Childcare at home" |
| G142 | Nursing care services | UC-SC04-20: care acts that need a prescription | "Nursing care services" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "SC04 Home care").

## Consequences

- G21 Community care:
  [UC-SC04-16](../../08-sectors/sc04-home-care/use-cases/06-care-homes-cesu-and-nursing/uc-sc04-16-run-a-care-home.md),
  [S-SC04-16](../../08-sectors/sc04-home-care/screens/06-care-homes-cesu-and-nursing/s-sc04-16-care-home.md) and
  [BR-SC04-16](../../08-sectors/sc04-home-care/business-rules/br-sc04-16-residents-care-records-follow-health-data-rules.md),
  with [E-SC04-14](../../08-sectors/sc04-home-care/data/e-sc04-14-resident.md) Resident and its list
  [S-SC04-L14](../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l14-residents.md).
- G139 CESU payments:
  [UC-SC04-17](../../08-sectors/sc04-home-care/use-cases/06-care-homes-cesu-and-nursing/uc-sc04-17-accept-cesu-vouchers.md),
  [S-SC04-17](../../08-sectors/sc04-home-care/screens/06-care-homes-cesu-and-nursing/s-sc04-17-cesu.md) and
  [BR-SC04-17](../../08-sectors/sc04-home-care/business-rules/br-sc04-17-cesu-vouchers-are-reconciled-with-the-issuer.md),
  with [E-SC04-15](../../08-sectors/sc04-home-care/data/e-sc04-15-cesu-voucher.md) CESU voucher and its list
  [S-SC04-L15](../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l15-cesu-vouchers.md).
- G140 Agent mode:
  [UC-SC04-18](../../08-sectors/sc04-home-care/use-cases/06-care-homes-cesu-and-nursing/uc-sc04-18-run-the-agent-mode-for-family-employers.md),
  [S-SC04-18](../../08-sectors/sc04-home-care/screens/06-care-homes-cesu-and-nursing/s-sc04-18-agent-mode.md) and
  [BR-SC04-18](../../08-sectors/sc04-home-care/business-rules/br-sc04-18-in-agent-mode-the-family-is-the-employer.md),
  with [E-SC04-16](../../08-sectors/sc04-home-care/data/e-sc04-16-mandate.md) Mandate and its list
  [S-SC04-L16](../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l16-mandates.md).
- G141 Childcare at home:
  [UC-SC04-19](../../08-sectors/sc04-home-care/use-cases/06-care-homes-cesu-and-nursing/uc-sc04-19-provide-childcare-at-home.md),
  [S-SC04-19](../../08-sectors/sc04-home-care/screens/06-care-homes-cesu-and-nursing/s-sc04-19-childcare.md) and
  [BR-SC04-19](../../08-sectors/sc04-home-care/business-rules/br-sc04-19-family-allowance-aid-follows-the-caf-rules.md),
  with [E-SC04-17](../../08-sectors/sc04-home-care/data/e-sc04-17-childcare-contract.md) Childcare contract and its list
  [S-SC04-L17](../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l17-childcare-contracts.md).
- G142 Nursing care services:
  [UC-SC04-20](../../08-sectors/sc04-home-care/use-cases/06-care-homes-cesu-and-nursing/uc-sc04-20-run-home-nursing-care.md),
  [S-SC04-20](../../08-sectors/sc04-home-care/screens/06-care-homes-cesu-and-nursing/s-sc04-20-home-nursing.md) and
  [BR-SC04-20](../../08-sectors/sc04-home-care/business-rules/br-sc04-20-care-acts-need-a-prescription.md), with
  [E-SC04-18](../../08-sectors/sc04-home-care/data/e-sc04-18-care-act.md) Care act and its list
  [S-SC04-L18](../../08-sectors/sc04-home-care/screens/00-lists/s-sc04-l18-care-acts.md).
- Drawn in [FL-SC04-06](../../08-sectors/sc04-home-care/flows/fl-sc04-06-care-homes-cesu-and-nursing.md) Care homes,
  CESU, agent mode, childcare and nursing.

## Related

- [FL-SC04-06](../../08-sectors/sc04-home-care/flows/fl-sc04-06-care-homes-cesu-and-nursing.md)
- [D326 Home care sector coverage](d326-home-care-sector-coverage.md)
- [D328 SC04 use cases](d328-sc04-use-cases.md)
- [U25 Care coordinator](../../01-users/personas/u25-care-coordinator.md)

---

⬅️ [D547 Benchmark gaps of SC03 Services](d547-benchmark-gaps-sc03-services.md) · ⬆️ [Up](README.md) ·
➡️ [D549 Benchmark gaps of SC05 Manufacturing](d549-benchmark-gaps-sc05-manufacturing.md)
