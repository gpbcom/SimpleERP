🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚖️ [Decisions: F15 Legal assistant](README.md) ›
📜 D534 Benchmark gaps of F15 Legal assistant

# 📜 D534 Benchmark gaps of F15 Legal assistant

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found that the legal
assistant kept the company's registers and approved its accounts but had no equity, no contract drafting, no shareholder
meetings, no IP portfolio and no litigation register. Equity (G05) is the one the owner asked for in full: share
register, employee equity and fundraising dilution. The shareholder is the new persona U50.

## Options

- G05 Yes, full equity (Recommended): a share register and cap table with registered movements, or a spreadsheet held by
  the accountant.
- G05 Yes, full equity (Recommended): employee equity under a plan the shareholders approved, or manual notes on each
  employee.
- G05 Yes, full equity (Recommended): a dilution simulation that never touches the register, or a simulation that writes
  to the cap table.
- G83 Contract drafting: drafting from a clause library with approval of changed clauses, or free documents.
- G84 Shareholder meetings: general meetings with quorum and majority counted by the system, or minutes written by hand.
- G85 Own IP portfolio: an IP portfolio with warned renewals, or the dates in the calendar of one person.
- G86 Litigation register: a litigation register that proposes provisions to accounting, or a list of cases outside
  accounting.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F15 gets seven use cases in one new flow, FL-F15-07, each with its screen, its rule, its entity and its list. Equity is
written in full (three use cases). All at full depth now. Every legal duty is written in plain words and marked
(Proposed) until the France-pack rule is written.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G05 | Yes, full equity (Recommended) | UC-F15-14: a share-movement register written before any transfer is final | "Yes, full equity (Recommended)" |
| G05 | Yes, full equity (Recommended) | UC-F15-15: grants that follow the plan approved by shareholders | "Yes, full equity (Recommended)" |
| G05 | Yes, full equity (Recommended) | UC-F15-16: simulations that never change the register | "Yes, full equity (Recommended)" |
| G83 | Contract drafting | UC-F15-17: non-standard clauses that need legal approval | "Contract drafting" |
| G84 | Shareholder meetings | UC-F15-18: votes counted only within quorum and majority | "Shareholder meetings" |
| G85 | Own IP portfolio | UC-F15-19: renewals warned before their deadline | "Own IP portfolio" |
| G86 | Litigation register | UC-F15-20: a probable loss that gets a provision proposal in F8 | "Litigation register" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "F15 Legal assistant").

## Consequences

- G05 Yes, full equity (Recommended):
  [UC-F15-14](../../02-functional/f15-legal-assistant/use-cases/07-equity-contracts-and-disputes/uc-f15-14-keep-the-cap-table-and-share-movements.md),
  [S-F15-12](../../02-functional/f15-legal-assistant/screens/07-equity-contracts-and-disputes/s-f15-12-cap-table.md) and
  [BR-F15-18](../../02-functional/f15-legal-assistant/business-rules/br-f15-18-the-share-movement-register-is-written-before-a-transfer-is-final.md),
  with [E-F15-15](../../02-functional/f15-legal-assistant/data/e-f15-15-shareholding.md) Shareholding and its list
  [S-F15-L15](../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l15-shareholdings.md).
- G05 Yes, full equity (Recommended):
  [UC-F15-15](../../02-functional/f15-legal-assistant/use-cases/07-equity-contracts-and-disputes/uc-f15-15-grant-and-vest-employee-equity.md),
  [S-F15-13](../../02-functional/f15-legal-assistant/screens/07-equity-contracts-and-disputes/s-f15-13-employee-equity.md)
  and
  [BR-F15-19](../../02-functional/f15-legal-assistant/business-rules/br-f15-19-grants-follow-the-plan-approved-by-shareholders.md),
  with [E-F15-16](../../02-functional/f15-legal-assistant/data/e-f15-16-equity-grant.md) Equity grant and its list
  [S-F15-L16](../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l16-equity-grants.md).
- G05 Yes, full equity (Recommended):
  [UC-F15-16](../../02-functional/f15-legal-assistant/use-cases/07-equity-contracts-and-disputes/uc-f15-16-simulate-a-fundraising-dilution.md),
  [S-F15-14](../../02-functional/f15-legal-assistant/screens/07-equity-contracts-and-disputes/s-f15-14-dilution.md) and
  [BR-F15-20](../../02-functional/f15-legal-assistant/business-rules/br-f15-20-simulations-never-change-the-register.md),
  with [E-F15-17](../../02-functional/f15-legal-assistant/data/e-f15-17-funding-round.md) Funding round and its list
  [S-F15-L17](../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l17-funding-rounds.md).
- G83 Contract drafting:
  [UC-F15-17](../../02-functional/f15-legal-assistant/use-cases/07-equity-contracts-and-disputes/uc-f15-17-draft-a-contract-from-the-clause-library.md),
  [S-F15-15](../../02-functional/f15-legal-assistant/screens/07-equity-contracts-and-disputes/s-f15-15-contract-drafting.md)
  and
  [BR-F15-21](../../02-functional/f15-legal-assistant/business-rules/br-f15-21-non-standard-clauses-need-legal-approval.md),
  with [E-F15-18](../../02-functional/f15-legal-assistant/data/e-f15-18-clause.md) Clause and its list
  [S-F15-L18](../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l18-clauses.md).
- G84 Shareholder meetings:
  [UC-F15-18](../../02-functional/f15-legal-assistant/use-cases/07-equity-contracts-and-disputes/uc-f15-18-run-a-shareholders-general-meeting.md),
  [S-F15-16](../../02-functional/f15-legal-assistant/screens/07-equity-contracts-and-disputes/s-f15-16-shareholder-meetings.md)
  and
  [BR-F15-22](../../02-functional/f15-legal-assistant/business-rules/br-f15-22-votes-count-only-within-quorum-and-majority.md),
  with [E-F15-19](../../02-functional/f15-legal-assistant/data/e-f15-19-general-meeting.md) General meeting and its list
  [S-F15-L19](../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l19-general-meetings.md).
- G85 Own IP portfolio:
  [UC-F15-19](../../02-functional/f15-legal-assistant/use-cases/07-equity-contracts-and-disputes/uc-f15-19-keep-the-companys-ip-portfolio.md),
  [S-F15-17](../../02-functional/f15-legal-assistant/screens/07-equity-contracts-and-disputes/s-f15-17-ip-portfolio.md)
  and
  [BR-F15-23](../../02-functional/f15-legal-assistant/business-rules/br-f15-23-renewals-are-warned-before-their-deadline.md),
  with [E-F15-20](../../02-functional/f15-legal-assistant/data/e-f15-20-ip-right.md) IP right and its list
  [S-F15-L20](../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l20-ip-rights.md).
- G86 Litigation register:
  [UC-F15-20](../../02-functional/f15-legal-assistant/use-cases/07-equity-contracts-and-disputes/uc-f15-20-keep-the-litigation-register.md),
  [S-F15-18](../../02-functional/f15-legal-assistant/screens/07-equity-contracts-and-disputes/s-f15-18-litigation.md)
  and
  [BR-F15-24](../../02-functional/f15-legal-assistant/business-rules/br-f15-24-a-probable-loss-gets-a-provision-proposal-in-f8.md),
  with [E-F15-21](../../02-functional/f15-legal-assistant/data/e-f15-21-dispute.md) Dispute and its list
  [S-F15-L21](../../02-functional/f15-legal-assistant/screens/00-lists/s-f15-l21-disputes.md).
- Drawn in [FL-F15-07](../../02-functional/f15-legal-assistant/flows/fl-f15-07-equity-contracts-and-disputes.md) Equity,
  contracts, meetings and disputes.

## Related

- [FL-F15-07](../../02-functional/f15-legal-assistant/flows/fl-f15-07-equity-contracts-and-disputes.md)
- [D472 F15 Legal assistant: gaps and improvements](d472-f15-gaps-and-improvements.md)
- [D28 Legal assistant](../foundations/d28-legal-assistant.md)
- [U50 Shareholder](../../01-users/personas/u50-shareholder.md)

---

⬅️ [D533 Benchmark gaps of F14 Plugin store](../f14-plugin-store/d533-benchmark-gaps-f14-plugin-store.md) ·
⬆️ [Up](README.md) · ➡️ [D535](../f16-customer-support-agents/d535-benchmark-gaps-f16-customer-support-agents.md)
