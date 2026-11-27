🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏘️ [SC10 Real estate](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC10-16 The tourist tax is collected per night and guest

# 📏 BR-SC10-16 The tourist tax is collected per night and guest

**Status:** ✅ specified

## Statement

The tourist tax of a stay is the rate of the commune times the nights times the guests who owe it, shown apart on the
invoice, and counted by the manager only when the platform does not collect it. Guests who are exempt are not counted
and are recorded as exempt.

## Why

The tax belongs to the commune and the manager is liable for it; a wrong count means an assessment and a penalty. The
owner asked for short-term rentals ([D554](../../../06-decisions/sectors/d554-benchmark-gaps-sc10-real-estate.md)).
The rates and exemptions come from the France pack, written later.

## Examples

| Case | Result |
|---|---|
| 4 nights, 2 adults, 1 child, rate 1.05 | 8.40 EUR, child exempt |
| Stay booked on a platform that collects the tax | no tax counted by the manager |
| Departure moved earlier by one night | the tax is recomputed |
| No rate for the commune | no tax computed, rate requested |
| Tax of the period | the sum of the stays' tax collected by the manager |

## Applies to

- [UC-SC10-21](../use-cases/07-short-stays-commercial-and-coworking/uc-sc10-21-manage-short-term-rentals.md)
- [E-SC10-17 Stay](../data/e-sc10-17-stay.md)
- [E-SC10-02 Property listing](../data/e-sc10-02-property-listing.md)

## Exceptions

None.

## Configurable

The rate and the exemptions by commune, as data of the country pack; the yearly night limit of a main residence, as data
of the commune.

## Open questions

None.

---

⬅️ [BR-SC10-15 Register kept current](br-sc10-15-register-kept-current.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC10-17](br-sc10-17-rents-are-indexed-on-ilc-or-ilat-within-the-caps.md)
