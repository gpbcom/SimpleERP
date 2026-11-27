🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
💳 [Payments](README.md) › ⚖️ CR-FR-023 SEPA payment formats

# ⚖️ CR-FR-023 SEPA payment formats

**Status:** ✅ specified

## Statement

Transfers and direct debits in euro use the SEPA formats, and direct debits need a signed mandate.

## Values

- Credit transfer: pain.001.
- Direct debit: pain.008, with a mandate reference and signature date.

## Legal references

- [SEPA Regulation (EU) 260/2012](https://eur-lex.europa.eu/eli/reg/2012/260/oj).

## Effective dates

In force the day after its publication (art. 18); credit transfers and direct debits in euro
meet its technical requirements from 2014-02-01 (art. 6): the ISO 20022 XML message standard (Annex, point 1(b))
and, for a direct debit, the payer's consent given to the payee and to the payer's bank, the mandates kept by
the payee (art. 5(3)(a)) ([Regulation (EU) 260/2012, consolidated text of 2024-04-08, Publications Office](http://publications.europa.eu/resource/cellar/ff7a3e82-f6bc-11ee-a251-01aa75ed71a1.0001.02/DOC_1), read 2026-11-27).

## Enforced by

- [UC-F8-04 Pay suppliers](../../../02-functional/f08-accounting/use-cases/02-purchase-to-pay/uc-f08-04-pay-suppliers.md)
- [UC-F8-05 Collect customer payments](../../../02-functional/f08-accounting/use-cases/03-bank-and-collect/uc-f08-05-collect-customer-payments.md)

## When the law changes

Watched in the law corpus: Regulation (EU) 260/2012. A change flags this rule and warns the administrators; the
corrected rule ships in a pack update (D294).

## Penalty

None stated in the sources read.

## Exceptions

None.

## Open questions

[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-022 Cash payment limit](cr-fr-022-cash-payment-limit.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-024](../point-of-sale/cr-fr-024-certified-till-software.md)
