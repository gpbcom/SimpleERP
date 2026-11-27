🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔮 [F23 What-if simulation and impact](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F23-13 Goal seeking moves only the chosen levers

# 📏 BR-F23-13 Goal seeking moves only the chosen levers

**Status:** ✅ specified

## Statement

Goal seeking changes only the levers the user chose, within the bounds the user set, and shows the smallest combination
that reaches the goal, or the closest result and the gap.

## Why

The owner keeps control of what may change (D480); results stay explainable (BR-F23-09).

## Examples

| Case | Result |
|---|---|
| Goal margin 12 % by June, levers price within +5 % and purchases within -5 % | passes: +2.5 % and -3 % |
| Same goal with price within +1 % only | passes: closest 10.8 %, gap 1.2 points |
| Engine changing staff to reach the goal | fails: staff not a chosen lever |

## Applies to

- [UC-F23-21 Seek a goal](../use-cases/06-goals-and-financing/uc-f23-21-seek-a-goal.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F23-12 No automated decisions about people](br-f23-12-no-automated-decisions-on-people.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F23-14](br-f23-14-financing-options-with-their-terms-and-covenants.md)
