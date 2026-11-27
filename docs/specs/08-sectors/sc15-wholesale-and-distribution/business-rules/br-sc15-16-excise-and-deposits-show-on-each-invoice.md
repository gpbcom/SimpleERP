🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 📦 [SC15 Wholesale and distribution](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC15-16 Excise and deposits show on each invoice

# 📏 BR-SC15-16 Excise and deposits show on each invoice

**Status:** ✅ specified

## Statement

Every invoice that contains alcohol shows the excise duty as a line of its own, and every returnable container shows its
deposit charged or credited as a line of its own. The credit for empties never exceeds the deposits charged to that
customer.

## Why

A buyer who cannot see the duty and the deposits cannot account for them, and a credit above the deposits charged is a
loss. The owner asked for beverage distribution
([D559](../../../06-decisions/sectors/d559-benchmark-gaps-sc15-wholesale-and-distribution.md)). The
France-pack rule is written later.

## Examples

| Case | Result |
|---|---|
| 20 crates at 3.00 EUR a crate | 60.00 EUR of deposits on the invoice |
| 14 crates of empties back | 42.00 EUR credited |
| Empties above the deposits charged | the credit is capped |
| Alcoholic item without a category | order refused |
| Lent equipment not returned | its value is billed |

## Applies to

- [UC-SC15-21](../use-cases/06-beverages-vans-weights-and-devices/uc-sc15-21-distribute-beverages.md)
- [E-SC15-15 Bar loan](../data/e-sc15-15-bar-loan.md)
- [E-F6-05 Invoice](../../../02-functional/f06-customers-and-sales/data/e-f06-05-invoice.md)
- [E-F7-25](../../../02-functional/f07-purchasing-and-stock/data/e-f07-25-packaging-deposit.md)

## Exceptions

None.

## Configurable

The deposit amounts per container, by purchasing; the duty rates come from the country pack.

## Open questions

None.

---

⬅️ [BR-SC15-15 Fair dealing with partners](br-sc15-15-fair-dealing-with-partners.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC15-17 The van's stock is counted at each reload](br-sc15-17-the-vans-stock-is-counted-at-each-reload.md)
