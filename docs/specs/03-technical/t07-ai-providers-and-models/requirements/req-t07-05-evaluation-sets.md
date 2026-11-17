🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🧠 [T7 AI providers and models](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T07-05 Evaluation sets gate releases

# 📌 REQ-T07-05 Evaluation sets gate releases

**Status:** ✅ specified

## Statement

Each AI feature has an evaluation set that gates releases.

For the legal assistant (F15), the set gates changes of model and prompts, never a law refresh (D206, D448).

## Why

Confirmed by the owner on 2026-11-12; D417.

## Acceptance criteria

1. **Given** a prompt change below threshold, release blocked.
2. **Given** a model change, the set runs.

## Measure

Scores per feature.

## Priority

Must

## Capabilities served

Every AI feature of F1 to F25 and the sectors SC01 to SC16, one per AI feature setting (E-F1-09).

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T07-04 Speech and embeddings local by default](req-t07-04-speech-and-embeddings.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T07-06 Versioned prompts, policy outside](req-t07-06-prompts-and-policy.md)
