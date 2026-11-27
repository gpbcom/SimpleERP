🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏘️ [SC10 Real estate](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC10-17 Rents are indexed on ILC or ILAT within the caps

# 📏 BR-SC10-17 Rents are indexed on ILC or ILAT within the caps

**Status:** ✅ specified

## Statement

The rent of a commercial lease is revised only with the index the lease names (ILC or ILAT), at the dates the lease
sets, and the new rent never exceeds the cap the lease or the law sets. A revision above the cap is cut to it and the
difference is shown.

## Why

An index or a rise the lease does not allow can be challenged by the tenant, and the landlord may have to repay the
excess. The owner asked for commercial leases
([D554](../../../06-decisions/sectors/d554-benchmark-gaps-sc10-real-estate.md)). The indices and the caps
come from the France pack ([CR-FR-239](../../../10-country-packs/france/real-estate/cr-fr-239-commercial-leases.md)).

## Examples

| Case | Result |
|---|---|
| Rent 18,000.00, index rise 2.0 % | 18,360.00 EUR |
| Rise above the cap | cut to the cap, difference shown |
| Index not published | the revision waits |
| Lease with no index | the manager chooses from the activity and records it |
| Home rent index used for a shop | refused |

## Applies to

- [UC-SC10-22](../use-cases/07-short-stays-commercial-and-coworking/uc-sc10-22-manage-commercial-leases.md)
- [E-SC10-18 Commercial lease](../data/e-sc10-18-commercial-lease.md)
- [E-SC10-09 Rent call](../data/e-sc10-09-rent-call.md)
- France-pack rule:
  [CR-FR-239 Commercial leases (3-6-9, ILC/ILAT)](../../../10-country-packs/france/real-estate/cr-fr-239-commercial-leases.md)

## Exceptions

A rent step written in the lease is applied as written; it is not a revision.

## Configurable

The indices and the caps, as data of the country pack; the delay before a revision date at which the manager is told (90
days by default), by the manager.

## Open questions

None.

---

⬅️ [BR-SC10-16](br-sc10-16-the-tourist-tax-is-collected-per-night-and-guest.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC10-18 Depreciation never creates a rental loss](br-sc10-18-depreciation-never-creates-a-rental-loss.md)
