🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💻 [SC14 IT and software](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC14-16 Leased devices stay listed until returned

# 📏 BR-SC14-16 Leased devices stay listed until returned

**Status:** ✅ specified

## Statement

A leased device stays on its customer's list and on the monthly invoice until its return has been scanned and checked. A
returned device returns to stock only with its wipe certificate.

## Why

A device that left the list without a return is lost revenue and a data risk. The owner asked for hardware resale and
leasing ([D558](../../../06-decisions/sectors/d558-benchmark-gaps-sc14-it-and-software.md)). No France-pack rule
sets this: it follows the lease contract, and the wipe protects the personal data left on the device (CR-FR-052).

## Examples

| Case | Result |
|---|---|
| 20 devices leased, 2 returned and checked | the next invoice bills 18 |
| Device collected but not scanned | still billed |
| Device returned without a wipe | not back in stock |
| Device lost | billed at its replacement value |
| Device bought at the end of the lease | Resold at the residual price |

## Applies to

- [UC-SC14-22](../use-cases/07-hardware-licences-and-tax-credits/uc-sc14-22-resell-and-lease-it-hardware.md)
- [E-SC14-17 Leased device](../data/e-sc14-17-leased-device.md)
- [E-F7-10](../../../02-functional/f07-purchasing-and-stock/data/e-f07-10-lot-or-serial.md)

## Exceptions

None.

## Configurable

The term, the fee grid and the residual values, by sales.

## Open questions

None.

---

⬅️ [BR-SC14-15 Partners' commissions from deals](br-sc14-15-partners-commissions-from-deals.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC14-17](br-sc14-17-seats-billed-match-the-distributors-statement.md)
