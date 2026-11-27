🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🚛 [SC07 Transport and logistics](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC07-12 Fuel surcharge from the index

# 📏 BR-SC07-12 Fuel surcharge from the index

**Status:** ✅ specified

## Statement

The freight price is adjusted for the change in energy costs between the contract and the transport, and the invoice
shows those costs; in France:
[CR-FR-123 Fuel price indexation](../../../10-country-packs/france/transport/cr-fr-123-fuel-indexation.md).

## Why

Without a clause, the energy costs are set at the contract date from the CNR prices and the share of energy in the CNR
indices, then revised by the change in the CNR index of that energy, or else the diesel index, between the contract and
the transport; the same for autonomous refrigeration units. Until 2022-12-31 the revision ran between the order and the
transport; for contracts concluded from 2023-01-01 it runs between the contract and the transport
([CR-FR-123](../../../10-country-packs/france/transport/cr-fr-123-fuel-indexation.md)).

## Examples

| Case | Result |
|---|---|
| Fuel up 4 % | Surcharge on the invoice |

## Applies to

Every SC07 use case concerned.

## Exceptions

None.

## Configurable

Index and fuel share.

## Open questions

None.

---

⬅️ [BR-SC07-11 Chartered carriers checked](br-sc07-11-chartered-carriers-checked.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC07-13 Storage billed by the contract](br-sc07-13-storage-billed-by-the-contract.md)
