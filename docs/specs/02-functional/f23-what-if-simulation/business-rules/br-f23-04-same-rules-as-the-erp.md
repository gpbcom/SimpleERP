🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔮 [F23 What-if simulation and impact](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F23-04 The same rules as the ERP

# 📏 BR-F23-04 The same rules as the ERP

**Status:** ✅ specified

## Statement

Impacts are computed by the same business rules the capabilities use (pricing, stock, planning, payroll, accounting),
never by a separate simplified model unless the scenario says so.

## Why

See [D402](../../../06-decisions/f23-what-if-simulation/d402-impact-through-the-real-rules.md).

## Examples

| Case | Result |
|---|---|
| Pay rise | Payroll cost by F13's rules |

## Applies to

Every F23 use case concerned.

- [UC-F23-21 Seek a goal](../use-cases/06-goals-and-financing/uc-f23-21-seek-a-goal.md)
- [UC-F23-22 Find the break-even point](../use-cases/06-goals-and-financing/uc-f23-22-find-the-break-even-point.md)
- [UC-F23-27 Simulate a supplier switch](../use-cases/03-see-the-impact/uc-f23-27-simulate-a-supplier-switch.md)
- [UC-F23-30 Simulate a new shift or machine](../use-cases/03-see-the-impact/uc-f23-30-simulate-a-new-shift-or-machine.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F23-03 A scenario runs on a copy](br-f23-03-runs-on-a-copy.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F23-05 The impact across every area](br-f23-05-impact-across-every-area.md)
