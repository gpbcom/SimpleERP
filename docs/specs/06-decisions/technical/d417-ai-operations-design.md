🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D417 AI operations design

# 📜 D417 AI operations design

**Status:** ✅ decided

## Context

Step 19i of the technical interview, from TC-07, TC-08, TC-09 and TC-10.

## Options

- One model gateway with CPU and GPU runtimes, or Ollama everywhere.
- Whisper and embeddings locally, or outside speech services.
- An evaluation set per feature, or manual review.
- Versioned prompts with policy outside the prompt, or prompts edited live.

## Choice

Confirmed by the owner on 2026-11-12: one model gateway; Whisper on CPU and local embeddings by default, outside speech
services supported as well; an evaluation set per feature that gates releases; versioned prompt templates with the
policy outside the prompt.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The AI operations chapter's target design.

## Related

- [AI operations design](../../../technical/operations/ai-operations.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D416 Observability design](d416-observability-design.md) · ⬆️ [Up](README.md) ·
➡️ [D418 Open points of F17 to F21](../vision/d418-open-points-of-f17-to-f21.md)
