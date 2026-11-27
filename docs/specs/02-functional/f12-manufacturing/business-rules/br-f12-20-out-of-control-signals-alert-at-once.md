🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-20 Out-of-control signals alert at once

# 📏 BR-F12-20 Out-of-control signals alert at once

**Status:** ✅ specified

## Statement

A measure beyond the control limits, or a run the rules define, raises a signal to the operator and the quality manager;
limits are computed only with enough measures.

## Why

Drift caught early saves scrap.

## Examples

| Case | Result |
|---|---|
| 12.08 above 12.06 | Signal |
| 12 measures | No limits yet (Proposed: 25) |

## Applies to

- [UC-F12-25 Monitor a process with control charts](../use-cases/12-quality-engineering/uc-f12-25-monitor-a-process-with-control-charts.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F12-19 High risks in an FMEA need an action](br-f12-19-high-risks-in-an-fmea-need-an-action.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F12-21 Tablet records sync in order](br-f12-21-tablet-records-sync-in-order.md)
