🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏪 [Decisions: F10 Point of sale (plugin)](README.md) ›
📜 D467 F10 Point of sale (plugin): gaps and improvements

# 📜 D467 F10 Point of sale (plugin): gaps and improvements

**Status:** ✅ decided

## Context

The gaps-and-improvements round of 2026-11-12 (D457), for F10 and the sectors that rely on it.

## Options

- **Meal vouchers as a payment means with the daily cap.** Absent in F10; specified only in SC06 UC-13 (cr-fr-112).
- **Age-restricted sales prompts.** Alcohol and tobacco; absent. Serves SC02, SC06, SC16 bars.
- **Cash beyond the session.** Safe, bank deposits and cash-in-transit; absent.
- **Clienteling and stock lookup or transfer across stores.** Absent; SC02 UC-04 and UC-10 re-specify them.
- **Tax-free export sales (détaxe).** Absent (general knowledge). Serves SC02.
- **Confirm the waiting proposals.** 38 items, plus BR-F10-05 and BR-F10-06.
- **Offline state on screens.** BR-F10-06 says the till keeps selling offline, but no screen shows an offline state.
- **Accounting use case.** Card-terminal settlements net of fees, matched to the bank. U05 has 1 use case.
- **More reports.** Hourly sales, staff performance and basket analysis.

## Choice

Confirmed by the owner on 2026-11-12:

- F10 Point of sale: gaps and improvements: All four groups: meal vouchers and age checks; cash beyond the session;
  clienteling, transfers and tax-free; offline screens, card settlements and reports
- F10 Point of sale: proposals: "Confirm all of F10"

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

- The chosen gaps and improvements become use cases, rules, entities, screens and flows of F10.
- F10's waiting proposals are confirmed (D457).

## Related

- [F10 Point of sale (plugin)](../../02-functional/f10-point-of-sale/README.md)

---

⬅️ [D466 F9 HR and projects: gaps and improvements](../f09-hr-and-projects/d466-f09-gaps-and-improvements.md) ·
⬆️ [Up](README.md) ·
➡️ [D468 F11 Online shop (plugin): gaps and improvements](../f11-online-shop/d468-f11-gaps-and-improvements.md)
