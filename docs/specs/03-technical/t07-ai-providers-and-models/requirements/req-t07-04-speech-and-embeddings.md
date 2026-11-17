🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🧠 [T7 AI providers and models](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T07-04 Speech and embeddings local by default

# 📌 REQ-T07-04 Speech and embeddings local by default

**Status:** ✅ specified

## Statement

Whisper on CPU and local embeddings by default; outside speech services supported.

## Why

Confirmed by the owner on 2026-11-12; D417.

## Acceptance criteria

1. **Given** a meeting, transcribed locally.
2. **Given** an outside speech service chosen, used.

## Measure

Transcription time.

## Priority

Must

## Capabilities served

F4, T8

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T07-03 Metering, masking, tracing, fallback](req-t07-03-meter-mask-trace.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T07-05 Evaluation sets gate releases](req-t07-05-evaluation-sets.md)
