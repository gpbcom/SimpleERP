🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-23 A cheque or LCR is posted when the bank credits it

# 📏 BR-F8-23 A cheque or LCR is posted when the bank credits it

**Status:** ✅ specified

## Statement

A cheque or an LCR is posted to the bank account only on the date the bank credits it; until then it sits on a transit
account, the customer's invoice is shown as remitted and not as paid in the bank, and an unpaid item reverses the
credit.

## Why

A cheque in hand is not money in the bank until the bank credits it, and it may come back unpaid. The owner asked for
French payment means ([D527](../../../06-decisions/f08-accounting/d527-benchmark-gaps-f08-accounting.md));
[BR-F8-03 Every bank line is reconciled](br-f08-03-every-bank-line-is-reconciled.md) requires every bank line to be
reconciled. The France-pack rule on LCR and cheque remittances is
[CR-FR-212 LCR and cheque remittances](../../../10-country-packs/france/payments/cr-fr-212-lcr-and-cheque-remittances.md): a cheque or an LCR is a
claim until the bank credits it.

## Examples

| Case | Result |
|---|---|
| 12 cheques remitted on 12 November | on transit until the bank credits |
| The bank credits 8,490 EUR on 14 November | 8,490 EUR posted to the bank on 14 November |
| One cheque unpaid on 20 November | its invoice is reopened and the credit reversed |
| An LCR discounted by the bank | the advance is posted as a short-term loan |
| A slip not credited after 10 working days | accounting is alerted |

## Applies to

- [UC-F8-31](../use-cases/11-treasury-and-payment-means/uc-f08-31-issue-lcr-and-deposit-cheques.md)
- [E-F8-35 Remittance slip](../data/e-f08-35-remittance-slip.md)
- [E-F8-04 Bank line](../data/e-f08-04-bank-line.md)
- [E-F6-06 Customer payment](../../f06-customers-and-sales/data/e-f06-06-customer-payment.md)
- France-pack rule:
  [CR-FR-212 LCR and cheque remittances](../../../10-country-packs/france/payments/cr-fr-212-lcr-and-cheque-remittances.md)

## Exceptions

None.

## Configurable

Yes: the number of working days before an uncredited slip raises an alert.

## Open questions

None.

---

⬅️ [BR-F8-22 Loan interest is accrued each period](br-f08-22-loan-interest-is-accrued-each-period.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F8-24](br-f08-24-unrealised-differences-are-reversed-next-period.md)
