🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
💳 [Payments](README.md) › ⚖️ CR-FR-212 LCR and cheque remittances

# ⚖️ CR-FR-212 LCR and cheque remittances

**Status:** 🔄 (Proposed) values to read in the official source

## Statement

(Proposed) A cheque or a bill of exchange (LCR) is a claim until the bank credits it; cheques are remitted to the bank
on a deposit slip and an LCR is remitted and followed until the bank credits or rejects it.

## Values

- (Proposed) Cheques grouped on a numbered deposit slip.
- (Proposed) An LCR remitted to the bank with its due date.
- (Proposed) A rejection puts the claim back to the customer's account.
- (Proposed) simple-ERP enforces: a cheque or an LCR is posted to the bank only when the bank credits it.
- Read on [Service-public F2402](https://www.service-public.gouv.fr/particuliers/vosdroits/F2402) (verified 16 June
  2026), cheques only; the LCR is not read:
- Read: a cheque can be cashed within 1 year and 8 days of the date written on it; the payee endorses it (signs the
  back) and hands it to a bank within that period.
- Read: the issuer's account is debited when the payee cashes it, and the amount must stay available until then.
- Read: the place of payment and the date of writing must appear; an omission or a false date can cost a fine of 6 % of
  the amount, minimum 0.75 EUR.
- Read: Code monetaire et financier L131-2 to L131-15, L131-31 to L131-43, L131-59 and L131-60, L131-69 to L131-87;
  remittance slips, bank cut-offs and unpaid-cheque handling are not on the page.

## Legal references

- Law to read: cheque and LCR remittance (not read yet).

## Effective dates

(Proposed) To read.

## Enforced by

- [BR-F8-23 A cheque or LCR is posted when the bank credits it](../../../02-functional/f08-accounting/business-rules/br-f08-23-a-cheque-or-lcr-is-posted-when-the-bank-credits-it.md)
- [UC-F8-31 Issue LCR and deposit cheques](../../../02-functional/f08-accounting/use-cases/11-treasury-and-payment-means/uc-f08-31-issue-lcr-and-deposit-cheques.md)

## When the law changes

Watched in the law corpus: Cheque and LCR remittance rules. A change flags this rule and warns the administrators; the
corrected rule ships in a pack update (D294).

## Penalty

Not read yet.

## Exceptions

(Proposed) Companies that accept neither cheques nor LCR.

## Open questions

The law on cheque and LCR remittance is not read yet; the values are to read before launch.
[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-211 Live geolocation of employees](../data-protection/cr-fr-211-live-geolocation-of-employees.md) ·
⬆️ [Up](README.md) ·
➡️ [CR-FR-213 When a statutory auditor is required](../accounting/cr-fr-213-statutory-auditor-thresholds.md)
