🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🚛 [SC07 Transport and logistics](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC07-16 Drivers hold the licence for the vehicle class

# 📏 BR-SC07-16 Drivers hold the licence for the vehicle class

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

A driver is assigned to a passenger trip only when their licence category and professional card cover the class of the
vehicle, are valid on the date of the trip and leave enough driving time. Otherwise the assignment is refused and the
qualified drivers are listed.

## Why

Driving a vehicle for which the driver has no licence makes the trip illegal and the insurance void. The owner asked for
passenger transport ([D551](../../../06-decisions/sectors/d551-benchmark-gaps-sc07-transport.md)). The
France-pack rule is listed below.

## Examples

| Case | Result |
|---|---|
| Class D coach, driver with category D valid | accepted |
| Class D coach, driver with category B | refused |
| Card ending the week before the trip | refused for that date |
| Minibus of 9 seats with a category B driver | refused, bus category needed above 8 passengers |
| Driver with only 1 h of driving time left | refused for a long trip |

## Applies to

- [UC-SC07-21](../use-cases/07-passengers-removals-courier-and-freight/uc-sc07-21-run-passenger-transport.md)
- [E-SC07-18 Passenger trip](../data/e-sc07-18-passenger-trip.md)
- [E-SC07-04 Driver document](../data/e-sc07-04-driver-document.md)
- France-pack rule, (⚖️ lawyer review before launch, D574) until the coach, bus and taxi regimes of the Code des transports and the
  driving-licence categories of the Code de la route are read:
  [CR-FR-236 Passenger transport registration and licences](../../../10-country-packs/france/transport/cr-fr-236-passenger-transport-licences.md)

## Exceptions

None.

## Configurable

The warning delay before a licence or card ends, by the dispatcher.

## Open questions

None.

---

⬅️ [BR-SC07-15 Cabotage counted](br-sc07-15-cabotage-counted.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC07-17 The removal quote binds once signed](br-sc07-17-the-removal-quote-binds-once-signed.md)
