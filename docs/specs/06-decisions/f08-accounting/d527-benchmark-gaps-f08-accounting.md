🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 📒 [Decisions: F8 Accounting](README.md) ›
📜 D527 Benchmark gaps of F8 Accounting

# 📜 D527 Benchmark gaps of F8 Accounting

**Status:** ✅ decided

## Context

The owner asked on 2026-11-14 for a benchmark of the specifications against the other ERPs and the AI-native contenders,
and was asked one question per block
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md)). The benchmark found eleven features
that F8 had no use case for. Loans, French payment means, FX revaluation, the daily cash position, payments from the ERP
and recurring entries are treasury and bookkeeping tools; the statutory auditor workspace, lease accounting, Peppol,
business travel and cash-basis books complete the compliance and special-book side. The statutory auditor is the new
persona U49.

## Options

- G01 Loans and borrowings: loans with a schedule and accrued interest, or manual entries.
- G02 French payment means: cheques and LCR on remittance slips, or SEPA only.
- G03 FX revaluation: FX revaluation at each period end, or at settlement only.
- G55 Daily cash position: a daily cash position and forecast, or the bank balance alone.
- G56 Pay from the ERP: payments from the ERP through the bank, or files uploaded to the bank site.
- G57 Recurring entries: recurring entries from templates, or retyped entries.
- G04 Statutory auditor workspace: a read-only auditor workspace, or files by email.
- G23 Lease accounting: lease accounting per book, or rent expense only.
- G22 Peppol e-invoicing: Peppol for exchanges outside the French platforms, or the French platforms only.
- G25 Business travel: business travel with a policy, or expense claims after the trip.
- G58 Cash-basis books: cash-basis books, or accrual books only.
- Every answer was a choice among adding the gap with full depth now, later or never; the interview record keeps the
  owner's answers, not every option.

## Choice

F8 gets eleven use cases in two new flows, FL-F8-11 for treasury and payment means and FL-F8-12 for audit, leases and
special books, each with its screen and its rule, and ten entities with their lists; the cash-basis book has no entity
of its own. All at full depth now.

| Gap | Point | Decision | The owner's answer |
|---|---|---|---|
| G01 | Loans and borrowings | UC-F8-30: loans whose interest is accrued each period | "Loans and borrowings" |
| G02 | French payment means | UC-F8-31: cheques and LCR posted when the bank credits them | "French payment means" |
| G03 | FX revaluation | UC-F8-32: FX revaluation with unrealised differences reversed next period | "FX revaluation" |
| G55 | Daily cash position | UC-F8-33: a daily cash position built from open items and approved plans | "Daily cash position" |
| G56 | Pay from the ERP | UC-F8-34: payments from the ERP, two approvals above the limit | "Pay from the ERP" |
| G57 | Recurring entries | UC-F8-35: recurring entries that stop at their end date | "Recurring entries" |
| G04 | Statutory auditor workspace | UC-F8-36: an auditor who reads only, with every view logged | "Statutory auditor workspace" |
| G23 | Lease accounting | UC-F8-37: leases accounted for by each book's standard | "Lease accounting" |
| G22 | Peppol e-invoicing | UC-F8-38: Peppol only for flows outside the French platforms | "Peppol e-invoicing" |
| G25 | Business travel | UC-F8-39: business travel, trips outside the policy approved | "Business travel" |
| G58 | Cash-basis books | UC-F8-40: cash-basis books recording receipts and payments only | "Cash-basis books" |

## Decided by

The owner, on 2026-11-14, in the GH-2 benchmark-gaps interview
([interview record](../../../tickets/GH-2/interviews/2026-11-14-benchmark-gaps.md), section "F8 Accounting").

## Consequences

- G01 Loans and borrowings:
  [UC-F8-30](../../02-functional/f08-accounting/use-cases/11-treasury-and-payment-means/uc-f08-30-manage-loans-and-borrowings.md),
  [S-F8-29](../../02-functional/f08-accounting/screens/11-treasury-and-payment-means/s-f08-29-loans.md) and
  [BR-F8-22](../../02-functional/f08-accounting/business-rules/br-f08-22-loan-interest-is-accrued-each-period.md), with
  [E-F8-34](../../02-functional/f08-accounting/data/e-f08-34-loan.md) Loan and its list
  [S-F8-L34](../../02-functional/f08-accounting/screens/00-lists/s-f08-l34-loans.md).
- G02 French payment means:
  [UC-F8-31](../../02-functional/f08-accounting/use-cases/11-treasury-and-payment-means/uc-f08-31-issue-lcr-and-deposit-cheques.md),
  [S-F8-30](../../02-functional/f08-accounting/screens/11-treasury-and-payment-means/s-f08-30-payment-means.md) and
  [BR-F8-23](../../02-functional/f08-accounting/business-rules/br-f08-23-a-cheque-or-lcr-is-posted-when-the-bank-credits-it.md),
  with [E-F8-35](../../02-functional/f08-accounting/data/e-f08-35-remittance-slip.md) Remittance slip and its list
  [S-F8-L35](../../02-functional/f08-accounting/screens/00-lists/s-f08-l35-remittance-slips.md).
- G03 FX revaluation:
  [UC-F8-32](../../02-functional/f08-accounting/use-cases/11-treasury-and-payment-means/uc-f08-32-revalue-foreign-currency-items.md),
  [S-F8-31](../../02-functional/f08-accounting/screens/11-treasury-and-payment-means/s-f08-31-fx-revaluation.md) and
  [BR-F8-24](../../02-functional/f08-accounting/business-rules/br-f08-24-unrealised-differences-are-reversed-next-period.md),
  with [E-F8-36](../../02-functional/f08-accounting/data/e-f08-36-revaluation-run.md) Revaluation run and its list
  [S-F8-L36](../../02-functional/f08-accounting/screens/00-lists/s-f08-l36-revaluation-runs.md).
- G55 Daily cash position:
  [UC-F8-33](../../02-functional/f08-accounting/use-cases/11-treasury-and-payment-means/uc-f08-33-follow-the-daily-cash-position.md),
  [S-F8-32](../../02-functional/f08-accounting/screens/11-treasury-and-payment-means/s-f08-32-cash-position.md) and
  [BR-F8-25](../../02-functional/f08-accounting/business-rules/br-f08-25-the-forecast-uses-only-open-items-and-approved-plans.md),
  with [E-F8-37](../../02-functional/f08-accounting/data/e-f08-37-cash-forecast.md) Cash forecast and its list
  [S-F8-L37](../../02-functional/f08-accounting/screens/00-lists/s-f08-l37-cash-forecasts.md).
- G56 Pay from the ERP:
  [UC-F8-34](../../02-functional/f08-accounting/use-cases/11-treasury-and-payment-means/uc-f08-34-pay-suppliers-from-the-erp.md),
  [S-F8-33](../../02-functional/f08-accounting/screens/11-treasury-and-payment-means/s-f08-33-payment-initiation.md) and
  [BR-F8-26](../../02-functional/f08-accounting/business-rules/br-f08-26-payments-above-the-limit-need-two-approvals.md),
  with [E-F8-38](../../02-functional/f08-accounting/data/e-f08-38-payment-order.md) Payment order and its list
  [S-F8-L38](../../02-functional/f08-accounting/screens/00-lists/s-f08-l38-payment-orders.md).
- G57 Recurring entries:
  [UC-F8-35](../../02-functional/f08-accounting/use-cases/11-treasury-and-payment-means/uc-f08-35-schedule-recurring-entries.md),
  [S-F8-34](../../02-functional/f08-accounting/screens/11-treasury-and-payment-means/s-f08-34-recurring-entries.md) and
  [BR-F8-27](../../02-functional/f08-accounting/business-rules/br-f08-27-recurring-entries-stop-at-their-end-date.md),
  with [E-F8-39](../../02-functional/f08-accounting/data/e-f08-39-entry-template.md) Entry template and its list
  [S-F8-L39](../../02-functional/f08-accounting/screens/00-lists/s-f08-l39-entry-templates.md).
- G04 Statutory auditor workspace:
  [UC-F8-36](../../02-functional/f08-accounting/use-cases/12-audit-leases-and-special-books/uc-f08-36-open-the-books-to-the-statutory-auditor.md),
  [S-F8-35](../../02-functional/f08-accounting/screens/12-audit-leases-and-special-books/s-f08-35-auditor-workspace.md)
  and
  [BR-F8-28](../../02-functional/f08-accounting/business-rules/br-f08-28-the-auditor-reads-only-and-every-view-is-logged.md),
  with [E-F8-40](../../02-functional/f08-accounting/data/e-f08-40-audit-request.md) Audit request and its list
  [S-F8-L40](../../02-functional/f08-accounting/screens/00-lists/s-f08-l40-audit-requests.md).
- G23 Lease accounting:
  [UC-F8-37](../../02-functional/f08-accounting/use-cases/12-audit-leases-and-special-books/uc-f08-37-account-for-leases.md),
  [S-F8-36](../../02-functional/f08-accounting/screens/12-audit-leases-and-special-books/s-f08-36-leases.md) and
  [BR-F8-29](../../02-functional/f08-accounting/business-rules/br-f08-29-leases-follow-the-books-standard.md), with
  [E-F8-41](../../02-functional/f08-accounting/data/e-f08-41-lease.md) Lease and its list
  [S-F8-L41](../../02-functional/f08-accounting/screens/00-lists/s-f08-l41-leases.md).
- G22 Peppol e-invoicing:
  [UC-F8-38](../../02-functional/f08-accounting/use-cases/12-audit-leases-and-special-books/uc-f08-38-send-and-receive-invoices-through-peppol.md),
  [S-F8-37](../../02-functional/f08-accounting/screens/12-audit-leases-and-special-books/s-f08-37-peppol.md) and
  [BR-F8-30](../../02-functional/f08-accounting/business-rules/br-f08-30-peppol-serves-only-flows-outside-the-french-platforms.md),
  with [E-F8-42](../../02-functional/f08-accounting/data/e-f08-42-peppol-participant.md) Peppol participant and its list
  [S-F8-L42](../../02-functional/f08-accounting/screens/00-lists/s-f08-l42-peppol-participants.md).
- G25 Business travel:
  [UC-F8-39](../../02-functional/f08-accounting/use-cases/12-audit-leases-and-special-books/uc-f08-39-book-business-travel.md),
  [S-F8-38](../../02-functional/f08-accounting/screens/12-audit-leases-and-special-books/s-f08-38-business-travel.md)
  and
  [BR-F8-31](../../02-functional/f08-accounting/business-rules/br-f08-31-trips-outside-the-travel-policy-need-approval.md),
  with [E-F8-43](../../02-functional/f08-accounting/data/e-f08-43-trip.md) Trip and its list
  [S-F8-L43](../../02-functional/f08-accounting/screens/00-lists/s-f08-l43-trips.md).
- G58 Cash-basis books:
  [UC-F8-40](../../02-functional/f08-accounting/use-cases/12-audit-leases-and-special-books/uc-f08-40-keep-cash-basis-books.md),
  [S-F8-39](../../02-functional/f08-accounting/screens/12-audit-leases-and-special-books/s-f08-39-cash-basis-books.md)
  and
  [BR-F8-32](../../02-functional/f08-accounting/business-rules/br-f08-32-cash-basis-books-record-receipts-and-payments-only.md).
- Drawn in [FL-F8-11](../../02-functional/f08-accounting/flows/fl-f08-11-treasury-and-payment-means.md) Treasury and
  payment means.
- Drawn in [FL-F8-12](../../02-functional/f08-accounting/flows/fl-f08-12-audit-leases-and-special-books.md) Audit,
  leases and special books.

## Related

- [FL-F8-11](../../02-functional/f08-accounting/flows/fl-f08-11-treasury-and-payment-means.md)
- [FL-F8-12](../../02-functional/f08-accounting/flows/fl-f08-12-audit-leases-and-special-books.md)
- [BR-F8-01](../../02-functional/f08-accounting/business-rules/br-f08-01-posted-entries-never-change.md)
- [U49 Statutory auditor](../../01-users/personas/u49-statutory-auditor.md)

---

⬅️ [D526](../f07-purchasing-and-stock/d526-benchmark-gaps-f07-purchasing-and-stock.md) · ⬆️ [Up](README.md) ·
➡️ [D528 Benchmark gaps of F9 HR and projects](../f09-hr-and-projects/d528-benchmark-gaps-f09-hr-and-projects.md)
