🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F12-16 Only calibrated instruments record checks

# 📏 BR-F12-16 Only calibrated instruments record checks

**Status:** ✅ specified

## Statement

A quality check's measure is accepted only from an instrument whose calibration is current; an out-of-tolerance
calibration blocks it and lists the checks made with it since the last good calibration.

## Why

A measure from a wrong instrument proves nothing.

## Examples

| Case | Result |
|---|---|
| Calibration expired | Measure refused |
| Out of tolerance | 84 checks to review |

## Applies to

- [UC-F12-21 Calibrate measuring equipment](../use-cases/10-people-and-tools/uc-f12-21-calibrate-measuring-equipment.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F12-15 Risk assessment versions kept](br-f12-15-risk-assessment-versions-kept.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F12-17 Operators sign in only where qualified](br-f12-17-operators-sign-in-only-where-qualified.md)
