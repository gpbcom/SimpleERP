🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 💶 [F13 Payroll (plugin)](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F13-19 Garnishment within the attachable portion

# 📏 BR-F13-19 Garnishment within the attachable portion

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

A wage garnishment deducts no more than the attachable portion of the net for the month, computed with the country
pack's scale and the employee's dependants, and always leaves the protected amount; several orders are ranked by
priority.

## Why

The law protects part of the pay from seizure; the scale and the protected amount are (⚖️ lawyer review before launch, D574) to read in
the France pack: Code du travail R3252-2 and following.

## Examples

| Case | Result |
|---|---|
| Net 2 100.00 EUR, one dependant, one order | passes: deduction at the scale's amount, rest paid |
| Order larger than the attachable portion | passes: capped, the rest carried to next month |
| Deduction leaving less than the protected amount | fails: refused |
| Maintenance order and tax notice together | passes: the maintenance order first |

## Applies to

- [UC-F13-26 Apply a wage garnishment](../use-cases/08-deductions-savings-and-leave-pay/uc-f13-26-apply-a-wage-garnishment.md)
- [UC-F13-09 Pay employees by SEPA transfer](../use-cases/03-declarations-and-payments/uc-f13-09-pay-employees-by-sepa-transfer.md)

## Exceptions

Maintenance orders follow their own priority rules from the country pack.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F13-18 Special regimes declared to their own bodies](br-f13-18-special-regimes-declared-to-their-own-bodies.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F13-20 Advances recovered from the next pay](br-f13-20-advances-recovered-from-the-next-pay.md)
