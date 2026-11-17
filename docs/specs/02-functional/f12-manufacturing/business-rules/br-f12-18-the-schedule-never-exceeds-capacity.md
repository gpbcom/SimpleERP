🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-18 The schedule never exceeds capacity

# 📏 BR-F12-18 The schedule never exceeds capacity

**Status:** ✅ specified

## Statement

The finite schedule places operations only within each work centre's calendar, capacity and maintenance; what does not
fit moves later and shows as late.

## Why

An infinite plan is a wish, not a schedule.

## Examples

| Case | Result |
|---|---|
| Centre full | Next free slot, late shown |
| Maintenance | No operation placed |

## Applies to

- [UC-F12-23 Schedule with finite capacity](../use-cases/11-finite-schedule-and-the-tablet/uc-f12-23-schedule-with-finite-capacity.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F12-17 Operators sign in only where qualified](br-f12-17-operators-sign-in-only-where-qualified.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F12-19 High risks in an FMEA need an action](br-f12-19-high-risks-in-an-fmea-need-an-action.md)
