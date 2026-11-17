🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🧠 [T7 AI providers and models](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T07-06 Versioned prompts, policy outside

# 📌 REQ-T07-06 Versioned prompts, policy outside

**Status:** ✅ specified

## Statement

Prompt templates are versioned and tested; rights and budgets are enforced outside the prompt; untrusted content fenced.

## Why

Confirmed by the owner on 2026-11-12; D417.

## Acceptance criteria

1. **Given** an injected instruction in a document, not followed.
2. **Given** a prompt changed, its tests run.

## Measure

Injection tests.

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

⬅️ [REQ-T07-05 Evaluation sets gate releases](req-t07-05-evaluation-sets.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T07-07 Any model, listed](req-t07-07-any-model-listed.md)
