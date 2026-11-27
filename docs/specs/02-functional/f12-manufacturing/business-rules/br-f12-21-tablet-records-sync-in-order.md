🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-21 Tablet records sync in order

# 📏 BR-F12-21 Tablet records sync in order

**Status:** ✅ specified

## Statement

Records made offline on the tablet keep their time and sync in order; a record that conflicts with a change made
meanwhile, or would take stock below zero, waits for the planner.

## Why

Offline work must not lose or double production records.

## Examples

| Case | Result |
|---|---|
| No conflict | Synced |
| Order changed meanwhile | Waits for the planner |

## Applies to

- [UC-F12-26 Keep working on the tablet without the network](../use-cases/11-finite-schedule-and-the-tablet/uc-f12-26-keep-working-on-the-tablet-without-the-network.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F12-20 Out-of-control signals alert at once](br-f12-20-out-of-control-signals-alert-at-once.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F12-22 Work in progress is valued at costs incurred](br-f12-22-work-in-progress-is-valued-at-costs-incurred.md)
