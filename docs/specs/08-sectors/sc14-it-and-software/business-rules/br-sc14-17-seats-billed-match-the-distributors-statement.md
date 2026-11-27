🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💻 [SC14 IT and software](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC14-17 Seats billed match the distributor's statement

# 📏 BR-SC14-17 Seats billed match the distributor's statement

**Status:** 🔄 waiting for the owner

## Statement

The seats invoiced to a customer for a month equal the seats the distributor billed the reseller for that customer, or
the difference is explained and recorded. An invoice is not released while a difference is open.

## Why

Billing more than the statement hides a dispute, billing less loses margin, and an invoice that differs without a reason
cannot be defended. The owner asked for licence reselling
([D558](../../../06-decisions/sectors/d558-benchmark-gaps-sc14-it-and-software.md)). (Proposed) The France-pack rule is
written later.

## Examples

| Case | Result |
|---|---|
| 40 seats ordered and 40 on the statement | invoice released |
| 45 on the statement for 40 ordered | 5 seats in difference, invoice held |
| Seats added on the 20th | difference explained by the date of the change |
| Seats never ordered | disputed and left out of the invoice |
| Statement in an unknown format | import refused |

## Applies to

- [UC-SC14-23](../use-cases/07-hardware-licences-and-tax-credits/uc-sc14-23-resell-cloud-licences.md)
- [E-SC14-18 Licence subscription](../data/e-sc14-18-licence-subscription.md)
- [E-F6-07](../../../02-functional/f06-customers-and-sales/data/e-f06-07-subscription-contract.md)

## Exceptions

None.

## Configurable

The comparison tolerance, by accounting, which defaults to zero seats.

## Open questions

None.

---

⬅️ [BR-SC14-16 Leased devices stay listed until returned](br-sc14-16-leased-devices-stay-listed-until-returned.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC14-18 Claimed hours have timesheet evidence](br-sc14-18-claimed-hours-have-timesheet-evidence.md)
