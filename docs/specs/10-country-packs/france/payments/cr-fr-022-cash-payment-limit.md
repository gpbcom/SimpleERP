🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
💳 [Payments](README.md) › ⚖️ CR-FR-022 Cash payment limit

# ⚖️ CR-FR-022 Cash payment limit

**Status:** ✅ specified

## Statement

A sale cannot be paid in cash above the legal limit; the till and the payment screens refuse the excess.

## Values

- 1 000 EUR in cash (3 000 EUR in e-money) when the payer's tax home is in France or the payment is professional.
- 10 000 EUR for a non-resident individual not acting professionally.
- 15 000 EUR for that payer when the seller is an entity bound by anti-money-laundering duties (CMF L561-2).

## Legal references

- [Code monétaire et financier](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072026/) art. L112-6
  (amended by loi n° 2025-532 of 13 June 2025) and D112-3 (décret n° 2018-284).

## Effective dates

D112-3 in force since 2018-10-01; L112-6 version in force since 2025-06-15.

## Enforced by

- [UC-F8-05 Collect customer payments](../../../02-functional/f08-accounting/use-cases/03-bank-and-collect/uc-f08-05-collect-customer-payments.md)
- [Regulatory](../../../02-functional/f10-point-of-sale/regulatory.md)

## When the law changes

Watched in the law corpus: CMF L112-6, D112-3, L112-7. A change flags this rule and warns the administrators; the
corrected rule ships in a pack update (D294).

## Penalty

A fine of up to 5 % of the sums paid in breach, the payer and the seller jointly liable (CMF L112-7).

## Exceptions

Payments between individuals not acting professionally; people without a bank account (CMF L112-6 III).

## Open questions

None.

---

⬅️ [CR-FR-021 Construction retention guarantee](../invoicing/cr-fr-021-construction-retention-guarantee.md) ·
⬆️ [Up](README.md) · ➡️ [CR-FR-023 SEPA payment formats](cr-fr-023-sepa-formats.md)
