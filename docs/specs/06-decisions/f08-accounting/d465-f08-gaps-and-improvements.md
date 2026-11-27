🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 📒 [Decisions: F8 Accounting](README.md) ›
📜 D465 F8 Accounting: gaps and improvements

# 📜 D465 F8 Accounting: gaps and improvements

**Status:** ✅ decided

## Context

The gaps-and-improvements round of 2026-11-12 (D457), for F8 and the sectors that rely on it.

## Options

- **Third-party funds (client money).** Segregated accounts and per-client balances for SC10 (Hoguet, cr-fr-139) and
  SC11 (CARPA, cr-fr-151). Absent in F8.
- **Non-profit accounting.** Dedicated funds, volunteer valuation and publication of accounts are absent in F8, yet SC08
  relies on F8 (UC-SC08-14/15).
- **Corporate income tax and annual accounts.** Corporate tax instalments, CFE/CVAE, approval and filing of the annual
  accounts are absent; UC-F8-10 lists only "filings".
- **Provisions for doubtful debts.** Absent; a standard closing step.
- **Grants and subsidies spread over the asset's life.** 1 mention. Serves SC08, SC12, SC13 CAP aid.
- **Sustainability data (VSME, carbon).** About 2 mentions in all the specs; banks and customers increasingly ask SMEs
  for it (general knowledge).
- **Confirm the waiting proposals.** 26 items: 14 screens and 12 entities, plus the integrations and AI pages.
- **More flows.** Only 6 flows for 20 use cases; fl-f08-03 has 226 words; UC-F8-06 bank reconciliation has 3 steps.
- **Payment run use case.** A payment proposal by due date, then approval, then the SEPA file ("batch payments" appears
  only in the README).
- **Monthly flux and variance analysis with AI comments.** Rillet offers it (D14).
- **Accountant collaboration.** Questions on entries and missing-receipt requests to the client. Serves U08.
- **Name the bank aggregator and French bank coverage.** Light lists 342 banks, including 8 French ones (B08).

## Choice

Confirmed by the owner on 2026-11-12:

- F8 Accounting: gaps: All four: non-profit accounting; corporate tax and annual accounts; doubtful debts;
  sustainability (VSME) (third-party funds and grants: shared)
- F8 Accounting: improvements: All four groups: more flows and a payment run; flux analysis with AI; accountant
  collaboration; named bank aggregator and French coverage
- F8 Accounting: proposals: "Confirm all of F8"

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

- The chosen gaps and improvements become use cases, rules, entities, screens and flows of F8.
- F8's waiting proposals are confirmed (D457).

## Related

- [F8 Accounting](../../02-functional/f08-accounting/README.md)

---

⬅️ [D464](../f07-purchasing-and-stock/d464-f07-gaps-and-improvements.md) · ⬆️ [Up](README.md) ·
➡️ [D466 F9 HR and projects: gaps and improvements](../f09-hr-and-projects/d466-f09-gaps-and-improvements.md)
