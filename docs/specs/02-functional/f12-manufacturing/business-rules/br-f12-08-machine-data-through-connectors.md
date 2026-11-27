🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-08 Machine data through connectors

# 📏 BR-F12-08 Machine data through connectors

**Status:** ✅ specified

## Statement

Counts, cycle times and stops come from T12 connectors; manual entries stay possible and are marked as manual.

## Why

See [D314](../../../06-decisions/f12-manufacturing/d314-machines-through-connectors.md).

## Examples

| Case | Result |
|---|---|
| PLC counts 480 parts | Quantity 480 recorded, source: machine |

## Applies to

Every F12 use case concerned.

- [UC-F12-29 Measure energy per operation](../use-cases/13-energy-passport-and-work-in-progress/uc-f12-29-measure-energy-per-operation.md)

## Exceptions

None.

## Configurable

Connectors per work centre.

## Open questions

None.

---

⬅️ [BR-F12-07 Operators sign in at the work centre](br-f12-07-operators-sign-in-at-the-work-centre.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F12-09 Equipment checks before use](br-f12-09-equipment-checks-before-use.md)
