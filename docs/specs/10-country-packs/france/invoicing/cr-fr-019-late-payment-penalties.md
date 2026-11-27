🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🧾 [Invoicing](README.md) › ⚖️ CR-FR-019 Late-payment penalties

# ⚖️ CR-FR-019 Late-payment penalties

**Status:** ✅ specified

## Statement

A late business customer owes late-payment penalties and a fixed recovery indemnity; a consumer owes neither unless
agreed.

## Values

- Penalty rate: the contract's, at least three times the legal interest rate; by default the ECB refinancing rate plus
  10 points.
- Fixed recovery indemnity: 40 EUR per invoice.

## Legal references

- [Code de commerce](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000005634379/) art. L441-10 II and D441-5.

## Effective dates

Since 2021-02-27: L441-10 in force since 2019-04-26, D441-5 since 2021-02-27 ([Code de commerce, art. L441-10](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038414392), [art. D441-5](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043197457), read 2026-11-27). Until 2026-12-31, the L441-10 version of 2019-04-26; from 2027-01-01, the version amended by Ordonnance n° 2026-671
art. 2 keeps the 30-day default, the 60-day and 45-days-end-of-month caps, the penalty rate and the fixed indemnity,
and caps periodic invoices of CIBS L216-34 at 45 days ([Code de commerce, art. L441-10, version of 2027-01-01](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038414392/2027-01-02), read 2026-11-27).

## Enforced by

- [BR-F6-05 Reminders run on their own](../../../02-functional/f06-customers-and-sales/business-rules/br-f06-05-reminders-run-on-their-own.md)
- [UC-F6-08 Remind late payers](../../../02-functional/f06-customers-and-sales/use-cases/03-invoice-and-get-paid/uc-f06-08-remind-late-payers.md)
- [BR-F15-08 Document checks list, never rewrite](../../../02-functional/f15-legal-assistant/business-rules/br-f15-08-document-checks-list-never-rewrite.md)

## When the law changes

Watched in the law corpus: CCom L441-10, D441-5. A change flags this rule and warns the administrators; the corrected
rule ships in a pack update (D294).

## Penalty

An administrative fine up to 75 000 EUR (natural person) or 2 000 000 EUR (legal person), doubled
on a repeat within 2 years, for terms of sale without the L441-10 II mentions or with a penalty rate that does
not comply (L441-16) ([Code de commerce, art. L441-16](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043750778), read 2026-11-27).

## Exceptions

Consumers: no recovery indemnity.

## Open questions

[Q17 Country-rule penalties and start dates still to read](../../../07-questions/q17-unread-penalties-and-dates.md).

---

⬅️ [CR-FR-018 Payment terms cap](cr-fr-018-payment-terms-cap.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-020 Proof of acceptance and e-signature](cr-fr-020-electronic-acceptance-and-signature.md)
