🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛒 [F6 Customers and sales](../README.md) › 📏 [Business rules](README.md) › 📏 BR-F6-08 VAT is shown wherever it matters

# 📏 BR-F6-08 VAT is shown wherever it matters

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

Every line carries its VAT rate; every quote, order, invoice, credit note, subscription, deposit and payment request
shows the total excluding VAT, the VAT amount per rate and the total including VAT, in SimpleERP, in documents and in
the portal. Prices are shown including VAT to consumers (and excluding VAT with the VAT detail to businesses). When no
VAT is charged, the reason's legal mention replaces it: "Autoliquidation" (reverse charge, for example construction
subcontracting or intra-EU services), and for the small-business exemption and the intra-EU supply of goods the
mention of the article in force on the invoice date:

- until 2026-12-31: "TVA non applicable, art. 293 B du CGI" (small-business exemption), "Exonération de TVA, art.
  262 ter I du CGI" (intra-EU supply of goods);
- from 2027-01-01, when the VAT articles of the CGI move to the Code des impositions sur les biens et services (CIBS):
  "TVA non applicable, article L. 223-3 du CIBS" (small-business exemption); the CGI wording is still accepted until
  2028-06-30, and on invoices and contracts producing effects until 2028-06-30 a CGI reference is read as the CIBS
  article that takes it over;
- after 2028-06-30, the intra-EU supply mention quotes its CIBS article, (⚖️ lawyer review before launch, D574) to
  read: CIBS L213-9 to L213-54, as CR-FR-009 says.

The rules on the invoice format and its electronic transmission (CGI art. 289, 289 bis, 290, 290 A) stay in force from
2027-01-01 until the regulatory part of the CIBS takes them over
([CR-FR-016 Electronic invoicing](../../../10-country-packs/france/invoicing/cr-fr-016-electronic-invoicing.md)).

Figures in lists, dashboards and the AI assistant's answers say whether they are excluding or including VAT.

## Why

Customers and accountants must see the tax they pay or collect. See
[D259](../../../06-decisions/f06-customers-and-sales/d259-vat-visible.md).

Legal values from the France country pack:
[CR-FR-008 VAT rates](../../../10-country-packs/france/tax-and-vat/cr-fr-008-vat-rates.md),
[CR-FR-009 VAT exemption and reverse-charge mentions](../../../10-country-packs/france/tax-and-vat/cr-fr-009-vat-mentions.md),
[CR-FR-010 When VAT is due](../../../10-country-packs/france/tax-and-vat/cr-fr-010-vat-due-date.md),
[CR-FR-034 Consumers see prices including VAT](../../../10-country-packs/france/consumer/cr-fr-034-prices-shown-including-vat.md).

## Examples

| Case | Result |
|---|---|
| A quote to Durand SA | Total excl. VAT 48,806.00 · VAT 20 % 9,761.20 · Total incl. VAT 58,567.20 |
| Lines at 20 % and 10 % (renovation) | One VAT line per rate |
| A subcontracting invoice in construction | "Autoliquidation", no VAT amount |
| The turnover in the AI assistant | "48,200 EUR excl. VAT" |

## Applies to

Every F6 document and the portal; F3 and F8 figures.

- [UC-F6-22 Issue a pro-forma invoice and a statement of account](../use-cases/07-special-invoicing/uc-f06-22-issue-a-pro-forma-invoice-and-a-statement-of-account.md)

## Exceptions

None.

## Configurable

Yes ([D260](../../../06-decisions/f06-customers-and-sales/d260-vat-configurable.md)), by accounting and administrators:
rates and their validity dates per country; the rate per product or service category, changeable per line; the regime
per customer (normal, exempt, reverse charge, intra-EU, export, OSS); the legal mention per regime; VAT due on payment
or on invoice per company; amounts shown excluding or including VAT per document type and per user. A rate change
applies from its date, never to issued invoices.

## Open questions

None.

---

⬅️ [BR-F6-07 Invoice numbers never break](br-f06-07-invoice-numbers-never-break.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F6-09 Rentals are never double-booked](br-f06-09-rentals-are-never-double-booked.md)
