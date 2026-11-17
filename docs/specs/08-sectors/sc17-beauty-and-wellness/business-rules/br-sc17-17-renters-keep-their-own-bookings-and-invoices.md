🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💇 [SC17 Beauty and wellness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC17-17 Renters keep their own bookings and invoices

# 📏 BR-SC17-17 Renters keep their own bookings and invoices

**Status:** ✅ specified

## Statement

A renter keeps their own bookings, clients and invoices: the salon sees only the rent and the renter's occupation of the
place, never the renter's client list or sales, and the renter sees nothing of the salon's other staff or takings.

## Why

Mixing a renter's clients and sales with the salon's treats them as an employee, with legal consequences, and exposes
the renter's data. The owner chose both staff models side by side
([D561](../../../06-decisions/sectors/d561-benchmark-gaps-sc17-beauty-and-wellness.md)). The independence
checks come from the France pack, written later.

## Examples

| Case | Result |
|---|---|
| Renter's calendar | visible only to the renter and the manager as occupation |
| Renter's invoices | own series, own name |
| Renter's client list | never shown to the salon |
| Contract fixing the renter's prices | a warning and a reason asked |
| Renter's sales collected by the salon | kept apart as a paid-out account |

## Applies to

- [UC-SC17-17](../use-cases/05-rentals-care-records-and-loyalty/uc-sc17-17-rent-chairs-and-cabins-to-independents.md)
- [E-SC17-11 Rental contract](../data/e-sc17-11-rental-contract.md)
- [E-SC17-11 Rental contract](../data/e-sc17-11-rental-contract.md)

## Exceptions

A renter may choose to share their calendar's free times with the salon's online booking page.

## Configurable

The rent, the notice, the delay before suspension and the independence checks, by the manager.

## Open questions

None.

---

⬅️ [BR-SC17-16 Answers follow the asker's rights](br-sc17-16-answers-follow-the-askers-rights.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC17-18](br-sc17-18-tattoo-piercing-and-laser-need-the-declared-activity-and-consent.md)
