🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 💶 [Decisions: F13 Payroll (plugin)](README.md) ›
📜 D532 Benchmark gaps of F13 Payroll

# 📜 D532 Benchmark gaps of F13 Payroll

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found four situations
that payroll suites handle and F13 did not: employees posted to another country, days-based contracts, payroll made by
an outside firm and the hours of staff representatives. Each changes how a month is paid or what is handed over, and
each has a legal paper or limit that must be visible.

## Options

- G75 Posted workers: a posting with its A1 certificate or declaration receipt, or a manual allowance on the pay
  profile.
- G76 Days-based contracts: a days package with declared days and a rest check, or hours converted to days outside the
  system.
- G77 Outsourced payroll: a frozen monthly handover to an outside firm with a returned-file check, or a plain export.
- G78 Staff representatives: delegation hours with a credit and paid as work time, or free-text absences.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F13 gets four use cases in one new flow, FL-F13-10, each with its screen, its rule, its entity and its list. All at full
depth now. Each legal duty is written in plain words and marked (Proposed) until the France-pack rule is written.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G75 | Posted workers | UC-F13-35: postings that need their A1 certificate or declaration receipt | "Posted workers" |
| G76 | Days-based contracts | UC-F13-36: days packages that days worked never exceed | "Days-based contracts" |
| G77 | Outsourced payroll | UC-F13-37: a handover whose inputs are frozen once sent | "Outsourced payroll" |
| G78 | Staff representatives | UC-F13-38: delegation hours paid as work time | "Staff representatives" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "F13 Payroll").

## Consequences

- G75 Posted workers:
  [UC-F13-35](../../02-functional/f13-payroll/use-cases/10-special-contracts-and-outsourcing/uc-f13-35-pay-posted-workers.md),
  [S-F13-28](../../02-functional/f13-payroll/screens/10-special-contracts-and-outsourcing/s-f13-28-posted-workers.md)
  and
  [BR-F13-25](../../02-functional/f13-payroll/business-rules/br-f13-25-a-posting-needs-an-a1-certificate-or-a-sipsi-declaration.md),
  with [E-F13-28](../../02-functional/f13-payroll/data/e-f13-28-posting.md) Posting and its list
  [S-F13-L28](../../02-functional/f13-payroll/screens/00-lists/s-f13-l28-postings.md).
- G76 Days-based contracts:
  [UC-F13-36](../../02-functional/f13-payroll/use-cases/10-special-contracts-and-outsourcing/uc-f13-36-follow-days-based-contracts.md),
  [S-F13-29](../../02-functional/f13-payroll/screens/10-special-contracts-and-outsourcing/s-f13-29-days-based-contracts.md)
  and [BR-F13-26](../../02-functional/f13-payroll/business-rules/br-f13-26-days-worked-never-exceed-the-package.md),
  with [E-F13-29](../../02-functional/f13-payroll/data/e-f13-29-days-package.md) Days package and its list
  [S-F13-L29](../../02-functional/f13-payroll/screens/00-lists/s-f13-l29-days-packages.md).
- G77 Outsourced payroll:
  [UC-F13-37](../../02-functional/f13-payroll/use-cases/10-special-contracts-and-outsourcing/uc-f13-37-hand-pay-inputs-to-an-outsourced-payroll-firm.md),
  [S-F13-30](../../02-functional/f13-payroll/screens/10-special-contracts-and-outsourcing/s-f13-30-outsourced-payroll.md)
  and [BR-F13-27](../../02-functional/f13-payroll/business-rules/br-f13-27-inputs-are-frozen-once-handed-over.md), with
  [E-F13-30](../../02-functional/f13-payroll/data/e-f13-30-payroll-handover.md) Payroll handover and its list
  [S-F13-L30](../../02-functional/f13-payroll/screens/00-lists/s-f13-l30-payroll-handovers.md).
- G78 Staff representatives:
  [UC-F13-38](../../02-functional/f13-payroll/use-cases/10-special-contracts-and-outsourcing/uc-f13-38-follow-staff-representatives-hours.md),
  [S-F13-31](../../02-functional/f13-payroll/screens/10-special-contracts-and-outsourcing/s-f13-31-staff-representatives.md)
  and [BR-F13-28](../../02-functional/f13-payroll/business-rules/br-f13-28-delegation-hours-are-paid-as-work-time.md),
  with [E-F13-31](../../02-functional/f13-payroll/data/e-f13-31-delegation-hours.md) Delegation hours and its list
  [S-F13-L31](../../02-functional/f13-payroll/screens/00-lists/s-f13-l31-delegation-hours.md).
- Drawn in [FL-F13-10](../../02-functional/f13-payroll/flows/fl-f13-10-special-contracts-and-outsourcing.md) Special
  contracts and outsourced payroll.

## Related

- [FL-F13-10](../../02-functional/f13-payroll/flows/fl-f13-10-special-contracts-and-outsourcing.md)
- [D470 F13 Payroll (plugin): gaps and improvements](d470-f13-gaps-and-improvements.md)
- [U45 Payroll officer](../../01-users/personas/u45-payroll-officer.md)

---

⬅️ [D531 Benchmark gaps of F12 Manufacturing](../f12-manufacturing/d531-benchmark-gaps-f12-manufacturing.md) ·
⬆️ [Up](README.md) ·
➡️ [D533 Benchmark gaps of F14 Plugin store](../f14-plugin-store/d533-benchmark-gaps-f14-plugin-store.md)
