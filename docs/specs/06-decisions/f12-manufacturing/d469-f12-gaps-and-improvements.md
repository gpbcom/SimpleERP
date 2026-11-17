🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏭 [Decisions: F12 Manufacturing (plugin)](README.md) ›
📜 D469 F12 Manufacturing (plugin): gaps and improvements

# 📜 D469 F12 Manufacturing (plugin): gaps and improvements

**Status:** ✅ decided

## Context

The gaps-and-improvements round of 2026-11-12 (D457), for F12 and the sectors that rely on it.

## Options

- **Recipes and batch (process) manufacturing in the core.** Absent in F12; SC05, SC06 and SC13 each define recipes
  separately.
- **Calibration of measuring equipment.** Absent in F12; specified in SC05 UC-12 (ISO 9001 §7.1.5).
- **Operator qualifications required per work centre.** 1 mention. Serves SC05 UC-13; link to F9 certifications.
- **Finite-capacity scheduling.** Absent; only capacity load exists. Serves U21.
- **FMEA and statistical process control.** Absent. Odoo Quality appears in D21.
- **Energy per operation and digital product passport data.** Absent (ESPR, general knowledge).
- **Confirm the waiting proposals.** 37 items, plus BR-F12-09 and BR-F12-14.
- **Deepen the thinnest flows.** fl-f12-05 (259 words) and fl-f12-08 (260 words).
- **Offline and loading states on the shop-floor tablet.**
- **Month-end work-in-progress valuation.** U05 has 1 use case.
- **Versioned work instructions with operator acknowledgement.** No entity today.

## Choice

Confirmed by the owner on 2026-11-12:

- F12 Manufacturing: gaps and improvements: All four groups: calibration and qualifications; finite-capacity scheduling;
  FMEA, SPC, energy and product passport; flows, tablet states, WIP valuation, work instructions (recipes: shared)
- F12 Manufacturing: proposals: "Confirm all of F12"

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

- The chosen gaps and improvements become use cases, rules, entities, screens and flows of F12.
- F12's waiting proposals are confirmed (D457).

## Related

- [F12 Manufacturing (plugin)](../../02-functional/f12-manufacturing/README.md)

---

⬅️ [D468 F11 Online shop (plugin): gaps and improvements](../f11-online-shop/d468-f11-gaps-and-improvements.md) ·
⬆️ [Up](README.md) ·
➡️ [D470 F13 Payroll (plugin): gaps and improvements](../f13-payroll/d470-f13-gaps-and-improvements.md)
