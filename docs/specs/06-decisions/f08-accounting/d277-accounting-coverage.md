🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 📒 [Decisions: F8 Accounting](README.md) ›
📜 D277 Accounting coverage

# 📜 D277 Accounting coverage

**Status:** ✅ decided

## Context

The owner asked that F8 cover everything a leading open-source ERP offers about accounting.

## Options

- Everything found.
- A selection.

## Choice

Everything found: ledger and setup (charts, journals, fiscal years, lock dates, multi-company, multi-currency with
revaluation, fiscal positions); customer side (invoices from F6, credit notes, payment terms, early-payment discounts,
follow-up, online payments, deferred revenues); supplier side (AI reading, approval, matching, batch payments, SEPA
credit transfers and direct debits, cheques); bank and cash (aggregators, statement files, reconciliation models, AI
matching, cash journals); taxes (VAT with D260, cash basis, reverse charge, withholding, OSS, Intrastat, FEC, liasse
fiscale, e-invoicing and e-reporting); analytic plans and budgets; fixed assets, deferrals, accruals, cut-off; closing,
every financial report, data inalterability, audit trail, annotations; expenses (receipts, mileage, company cards,
reimbursement, re-invoicing); loans, intercompany, cash forecast, imports from other software.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Fourteen use cases; gaps of the benchmark filled by D278 and D281.

## Related

- [F8 Accounting](../../02-functional/f08-accounting/README.md)

---

⬅️ [D276 The AI assistant reaches every capability](../f03-assistant/d276-assistant-reaches-every-capability.md) ·
⬆️ [Up](README.md) · ➡️ [D278 French filings prepared and filed](d278-french-filings.md)
