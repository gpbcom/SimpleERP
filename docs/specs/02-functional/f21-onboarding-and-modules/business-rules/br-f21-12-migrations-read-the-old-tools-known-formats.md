🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🧭 [F21 Onboarding and module activation](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F21-12 Migrations read the old tool's known formats

# 📏 BR-F21-12 Migrations read the old tool's known formats

**Status:** ✅ specified

## Statement

A migration from a named tool reads that tool's own export files (the guide shows how to produce them) with a ready
mapping of customers, suppliers, products, open invoices and balances; the old tool is never changed, and rows that
cannot be read are listed, never dropped.

## Why

French companies come from EBP, Sage, Pennylane and Excel, others from QuickBooks, NetSuite, Odoo and ERPNext (D478); a
ready mapping saves days.

## Examples

| Case | Result |
|---|---|
| EBP customer and article exports | passes: mapped and imported |
| Pennylane FEC and customer list | passes |
| Excel sheet with unknown columns | passes: the generic mapping opens (UC-F21-09) |
| 3 rows with an invalid SIRET | passes: listed, not imported until fixed |

## Applies to

- [UC-F21-21 Migrate from a named tool](../use-cases/05-migration-from-another-tool/uc-f21-21-migrate-from-a-named-tool.md)
- [UC-F21-09 Import existing data](../use-cases/03-team-and-data/uc-f21-09-import-existing-data.md)

## Exceptions

Tools or versions not supported use the generic import.

## Configurable

No; the list of supported tools grows with releases, each added once its export format is read.

## Open questions

None.

---

⬅️ [BR-F21-11 Onboarding measured without people](br-f21-11-onboarding-measured-anonymously.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F21-13 Opening balances match last year's FEC](br-f21-13-opening-balances-match-last-years-fec.md)
