🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-24 Energy is allocated by meter, else by time

# 📏 BR-F12-24 Energy is allocated by meter, else by time

**Status:** ✅ specified

## Statement

Energy is allocated to operations from meters where they exist, otherwise by run time and the machine's rated power,
each figure showing its method.

## Why

Comparable energy figures per product.

## Examples

| Case | Result |
|---|---|
| Meter | Measured |
| No meter, 15 kW for 4 h | 60 kWh, estimated |

## Applies to

- [UC-F12-29 Measure energy per operation](../use-cases/13-energy-passport-and-work-in-progress/uc-f12-29-measure-energy-per-operation.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F12-23](br-f12-23-a-new-instruction-version-is-acknowledged-before-work.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F12-25](br-f12-25-passport-data-come-from-records-with-their-source.md)
