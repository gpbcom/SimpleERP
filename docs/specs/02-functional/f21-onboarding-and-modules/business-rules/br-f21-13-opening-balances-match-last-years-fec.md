🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🧭 [F21 Onboarding and module activation](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F21-13 Opening balances match last year's FEC

# 📏 BR-F21-13 Opening balances match last year's FEC

**Status:** ✅ specified

## Statement

The opening entry is posted only when its totals per account equal the closing balances of the previous year's FEC; each
difference is listed for the accountant, who corrects it or records why.

## Why

The books must continue from the last closing
([CR-FR-005 FEC export](../../../10-country-packs/france/accounting/cr-fr-005-fec-export.md)).

## Examples

| Case | Result |
|---|---|
| Account 411 opening 48 210.00, FEC closing 48 210.00 | passes |
| Account 512 opening 12 000.00, FEC closing 12 040.00 | fails: difference 40.00 listed |
| Difference explained by the accountant with a reason | passes: posted with the note |

## Applies to

- [UC-F21-22 Check opening balances against last year's FEC](../use-cases/05-migration-from-another-tool/uc-f21-22-check-opening-balances-against-last-years-fec.md)

## Exceptions

A company in its first year has no FEC: the check is skipped.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F21-12 Migrations read the old tool's known formats](br-f21-12-migrations-read-the-old-tools-known-formats.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F21-14](br-f21-14-the-accountant-joins-with-the-accountant-role.md)
