🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎧 [Decisions: F16 Customer support agents](README.md) ›
📜 D473 F16 Customer support agents: gaps and improvements

# 📜 D473 F16 Customer support agents: gaps and improvements

**Status:** ✅ decided

## Context

The gaps-and-improvements round of 2026-11-12 (D457), for F16 and the sectors that rely on it.

## Options

- **Service levels and response-time targets.** Absent in F16, yet SC14 UC-05 needs them. Frappe Helpdesk has SLAs
  (D23).
- **Human agent workspace.** Queues, assignment rules, macros, collision detection. U16 has 2 use cases.
- **Customer satisfaction survey (CSAT).** Absent; quality is judged only by the AI judge and sampled reviews.
- **Public help centre and FAQ for customers.** The F3 knowledge base is internal.
- **Multilingual requests.** 1 mention.
- **Customer use cases.** Follow status, ask for a person, rate the answer.
- **Confirm the waiting proposals.** 14 items, BR-F16-02, plus the AI and integrations pages.
- **More rules for a block that moves money.** Refund limits per intent and a duplicate-action guard (only 4 rules
  today).
- **Intent discovery screen.** Clustering of past requests (UC-F16-03).
- **Refund abuse and fraud signals.** Absent in F16.

## Choice

Confirmed by the owner on 2026-11-12:

- F16 Customer support agents: gaps and improvements: All four groups: SLAs and agent workspace; CSAT, help centre and
  languages; customer use cases; refund limits, duplicate guard, intent discovery, fraud signals
- F16 Customer support agents: proposals: "Confirm all of F16"

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

- The chosen gaps and improvements become use cases, rules, entities, screens and flows of F16.
- F16's waiting proposals are confirmed (D457).

## Related

- [F16 Customer support agents](../../02-functional/f16-customer-support-agents/README.md)

---

⬅️ [D472 F15 Legal assistant: gaps and improvements](../f15-legal-assistant/d472-f15-gaps-and-improvements.md) ·
⬆️ [Up](README.md) · ➡️ [D474](../f17-competitive-analysis/d474-f17-gaps-and-improvements.md)
