🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🚛 [SC07 Transport and logistics](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC07-14 CO2 shown per transport

# 📏 BR-SC07-14 CO2 shown per transport

**Status:** ✅ specified

## Statement

Each transport's emissions are computed and given to the client; in France:
[CR-FR-120 CO2 information to clients](../../../10-country-packs/france/transport/cr-fr-120-co2-information.md).

## Why

The emissions are computed per segment of one means of transport, from the energy used (consumption rate times
distance) times the emission factor set by order, upstream production included, with values of level 1 to 4; for goods
they are given on the date agreed with the client, otherwise within 2 months of the end of the service
([CR-FR-120](../../../10-country-packs/france/transport/cr-fr-120-co2-information.md)).

## Examples

| Case | Result |
|---|---|
| 420 km, full load | Emissions on the invoice |

## Applies to

Every SC07 use case concerned.

## Exceptions

None.

## Configurable

Method.

## Open questions

None.

---

⬅️ [BR-SC07-13 Storage billed by the contract](br-sc07-13-storage-billed-by-the-contract.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC07-15 Cabotage counted](br-sc07-15-cabotage-counted.md)
