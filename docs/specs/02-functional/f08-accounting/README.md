🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 📒 F8 Accounting

# 📒 F8 Accounting

**Status:** ✅ specified

Build step: 5. Accounting.

## Summary

The company's books end to end, with in-house accounting and the external accountant, covering every accounting feature
of the benchmark and more ([D277](../../06-decisions/f08-accounting/d277-accounting-coverage.md) to
[D281](../../06-decisions/f08-accounting/d281-consolidation-eliminations.md)).

## Scope

- **Ledger:** country packs (France: PCG), journals, fiscal years, lock dates, multi-company, multi-currency and
  revaluation, fiscal positions, inalterability.
- **Customers and suppliers:** invoices from F6, bills from F7 or email read by the AI, credit notes, payment terms,
  discounts, follow-up, SEPA transfers and direct debits, cheques, batch payments.
- **Bank and cash:** aggregators and files, reconciliation models, AI matching, cash journals.
- **Taxes:** VAT (D259, D260), cash basis, reverse charge, withholding, OSS, Intrastat, CA3/CA12, DAS2, liasse fiscale,
  FEC, e-invoicing and e-reporting (Q13), filed through an EDI partner.
- **Analytics and budgets.**
- **Assets and deferrals:** depreciation, disposals, deferred revenues and expenses, accruals, cut-off, loans.
- **Closing and reports:** every financial report, closing checklist, year-end, consolidation with eliminations, audit
  trail, annotations, cash forecast.
- **Expenses:** receipts by photo, mileage scale, company cards, reimbursement, re-invoicing.
- **The accountant:** access, review, exports and imports.
- **Benchmark additions (D306):** several books (French GAAP, IFRS, management), IFRS 15 revenue, continuous close with
  agents, spend control with cards, planning and forecasting, profitability.
- **Gaps and improvements round ([D465](../../06-decisions/f08-accounting/d465-f08-gaps-and-improvements.md),
  2026-11-12):** third-party client money and grants and subsidies (shared capabilities,
  [D457](../../06-decisions/sectors/d457-gaps-and-improvements-round.md)), non-profit accounting, corporate tax and the
  annual accounts, provisions for doubtful debts, the sustainability report (VSME), a payment run, monthly flux analysis
  with AI comments, collaboration with the external accountant, a named bank aggregator with its French coverage, and
  more flows.

## Personas

[U05 Accounting](../../01-users/personas/u05-accounting.md),
[U08 External accountant](../../01-users/personas/u08-external-accountant.md),
[U13 Owner](../../01-users/personas/u13-owner.md), [U02 Manager](../../01-users/personas/u02-manager.md),
[U01 Employee](../../01-users/personas/u01-employee.md),
[U07 Administrator](../../01-users/personas/u07-administrator.md),
[U34 Property manager](../../01-users/personas/u34-property-manager.md),
[U36 Professional](../../01-users/personas/u36-professional.md),
[U31 Treasurer](../../01-users/personas/u31-treasurer.md), [U40 Farmer](../../01-users/personas/u40-farmer.md).

## Out of scope

- Payroll computation: F13 (F8 receives its entries).
- Sales and purchase documents themselves: F6, F7.

## Technical capabilities used

- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (banks, EDI partner,
  e-invoicing)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md) (reading, matching)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md)

## Build step

Step 5, Accounting, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | 🔄 |
| 🔀 |  | [Flows](flows/README.md) | 🔄 |
| 📏 |  | [Business rules](business-rules/README.md) | 🔄 |
| 🗃️ |  | [Data](data/README.md) | 🔄 |
| 🖥️ |  | [Screens](screens/README.md) | 🔄 |
| 🔑 |  | [Permissions](permissions.md) | ✅ |
| 🔔 |  | [Notifications](notifications.md) | ✅ |
| 📈 |  | [Reports](reports.md) | ✅ |
| 🔗 |  | [Integrations](integrations.md) | ✅ |
| 🤖 |  | [AI](ai.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | 🔄 |

---

⬅️ [Purchasing and stock](../f07-purchasing-and-stock/README.md) · ⬆️ [Up](../README.md) ·
➡️ [HR and projects](../f09-hr-and-projects/README.md)
