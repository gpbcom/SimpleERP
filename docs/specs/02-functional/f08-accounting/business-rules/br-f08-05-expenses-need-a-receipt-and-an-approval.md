🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-05 Expenses need a receipt and an approval

# 📏 BR-F8-05 Expenses need a receipt and an approval

**Status:** ✅ specified

## Statement

An expense needs its receipt (photo or file, read by the AI) unless its category allows none (mileage, per diem), and an
approval by the employee's manager (and accounting above 500 EUR, D282); mileage uses the official scale (barème
kilométrique).

## Why

See [D282](../../../06-decisions/f08-accounting/d282-f8-use-cases.md).

Legal values from the France country pack:
[CR-FR-012 Mileage allowance scale](../../../10-country-packs/france/tax-and-vat/cr-fr-012-mileage-scale.md).

## Examples

| Case | Result |
|---|---|
| A 23.40 EUR lunch with its photo | Approved by the manager, reimbursed |
| Mileage 120 km, 5 hp car | Scale applied |
| No receipt | Refused |

## Applies to

Every F8 use case concerned.

- [UC-F8-29 Answer the accountant's questions and requests](../use-cases/10-accountant-collaboration/uc-f08-29-answer-the-accountants-questions-and-requests.md)

## Exceptions

None.

## Configurable

Yes: categories, thresholds.

## Open questions

None.

---

⬅️ [BR-F8-04 Filings need an accountant](br-f08-04-filings-need-an-accountant.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F8-06 Balanced entries, continuous numbers](br-f08-06-balanced-entries-continuous-numbers.md)
