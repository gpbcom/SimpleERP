🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D460 F3 Assistant: gaps and improvements

# 📜 D460 F3 Assistant: gaps and improvements

**Status:** ✅ decided

## Context

The gaps-and-improvements round of 2026-11-12 (D457), for F3 and the sectors that rely on it.

## Options

- **Quality evaluation set.** No test questions with expected answers, run on every model or prompt change (absent). F15
  blocks updates on a quality drop (BR-F15-06) and F16 has non-regression tests. Serves U07, all users.
- **Prompt-injection defences.** Outside tools and documents feed answers (UC-F3-06, UC-F3-07), but the term appears
  only in T12. The benchmark itself met vendor pages that embed instructions aimed at AI agents (benchmark key
  findings).
- **Personal memory and preferences.** Opt-in, visible and erasable preferences such as "my site" or "my format"
  (absent).
- **Assistant for portal users.** The personas are internal only (D142). Customers, suppliers and tenants get no
  assistant. Serves SC10, SC14, SC15.
- **Ready-made agents per sector pack.** Ximi's Plizi replacement planner (E01) shows the value, for example a
  replacement agent for SC04.
- **Confirm the waiting proposals.** Nine use-case detail groups (UC-F3-01 to 09) and D139, D144, D145, D159 are still
  waiting.
- **Inspectable query behind each figure.** Doss offers a SQL query layer (C01); this extends BR-F3-03.
- **Cost estimate before expensive questions.** Link to F22 UC-F22-10.
- **"Not found" topics feed knowledge proposals.** Unanswered topics become E-F3-11 proposals.
- **Screen states.** Add empty, loading and read-only states (11 of 17 screens have no empty state).

## Choice

Confirmed by the owner on 2026-11-12:

- F3 Assistant: gaps: Quality evaluation set; prompt-injection defences; personal memory. **Not chosen:** portal
  assistant and ready-made sector agents
- F3 Assistant: improvements: All three: query behind each figure; cost estimate first; unanswered topics
- F3 Assistant: proposals: "Confirm all of F3"

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

- The chosen gaps and improvements become use cases, rules, entities, screens and flows of F3.
- F3's waiting proposals are confirmed (D457).

## Related

- [F3 Assistant](../../02-functional/f03-assistant/README.md)

---

⬅️ [D459](../f02-no-code-configuration/d459-f02-gaps-and-improvements.md) · ⬆️ [Up](README.md) ·
➡️ [D461 F4 Meetings: gaps and improvements](../f04-meetings/d461-f04-gaps-and-improvements.md)
