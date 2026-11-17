🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🧠 [T7 AI providers and models](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T07-03 Metering, masking, tracing, fallback

# 📌 REQ-T07-03 Metering, masking, tracing, fallback

**Status:** ✅ specified

## Statement

The gateway meters, masks personal data, traces every call and falls back to local.

## Why

Confirmed by the owner on 2026-11-12; D84, D417.

## Acceptance criteria

1. **Given** a call with an email address, masked.
2. **Given** an outside provider down, local fallback.

## Measure

Masked fields.

## Priority

Must

## Capabilities served

F22

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T07-02 The gateway speaks Claude's Messages API](req-t07-02-messages-api.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T07-04 Speech and embeddings local by default](req-t07-04-speech-and-embeddings.md)
