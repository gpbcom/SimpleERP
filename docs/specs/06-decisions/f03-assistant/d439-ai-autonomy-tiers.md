🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D439 AI autonomy tiers per feature

# 📜 D439 AI autonomy tiers per feature

**Status:** ✅ decided

## Context

The review of 2026-11-12 (R1) found the AI forbidden to act alone in one place (D157, BR-F3-07, CR-FR-057: "never does
irreversible or outward acts", "confirmation for every write") and allowed to in others (BR-F3-35 accruals posted,
BR-F8-09 auto-validated models, BR-F16-03 refunds in automatic, D246 automatic posts).

## Options

- Autonomy tiers set per feature.
- The AI assistant's rule for every AI.
- Free autonomy within the user's rights.

## Choice

Autonomy tiers set per feature. The **assistant** (the F3 panel, voice, chat apps) always asks before writing: it shows
the change and a person confirms (D140, D157). **Agents and automations** (F3 agents, F5 automatic posts, F8
auto-validated reconciliation models, F16 support agents, F2 workflow AI steps) act alone only within a procedure an
administrator switched to automatic, within that procedure's limits (amounts, counts, confidence), every act audited and
a sample checked by a person. **Never alone**, whatever the tier: payments and refunds, legal sendings (an invoice
validated or sent, a tax or social filing, a signature), deletions, and decisions about a person (hiring, scores, pay,
discipline): these are prepared and a person finishes them. The hosted support assistant and the DevOps agents (F20,
F25) act only after an engineer's or a maintainer's yes.

## Decided by

The owner, on 2026-11-12 at 14:53, round 1 of the decisions on the independent review (R1, PROGRESS.md, step 21).

## Consequences

Revises D157 (the AI assistant tier), D246 (automatic posts within limits, audited and sampled), D284 and D301 (agents
and auto-validated models are procedures switched to automatic) and D238 (a support agent never pays a refund alone).
BR-F3-07, BR-F3-35, BR-F5-02, BR-F8-09 and BR-F16-03 are aligned; CR-FR-057 keeps only the AI Act's own duties, the
product policy being this decision. The sampling rate is in AI governance.

## Related

- [F3 Assistant](../../02-functional/f03-assistant/README.md)
- [AI governance](../../05-non-functional/ai-governance.md)
- [D157](d157-assistant-actions.md)
- [D246](../f05-social-media/d246-social-auto-mode.md)
- [Independent review of 2026-11-12](../../../tickets/GH-2/review/2026-11-12-review.md)

---

⬅️ [D438 Repository layout](../technical/d438-repository-layout.md) · ⬆️ [Up](README.md) ·
➡️ [D440](../vision/d440-local-by-default-outside-by-choice.md)
