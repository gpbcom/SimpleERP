🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🧠 [T7 AI providers and models](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T07-01 One AI gateway

# 📌 REQ-T07-01 One AI gateway

**Status:** ✅ specified

## Statement

Every model call goes through one gateway: llama.cpp on CPU, vLLM on GPU nodes, outside providers per feature.

## Why

Confirmed by the owner on 2026-11-12; D417.

## Acceptance criteria

1. **Given** a feature switched to an outside provider, its calls go there.
2. **Given** no GPU, CPU models serve.

## Measure

Calls through the gateway.

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

⬆️ [Up](README.md) · ➡️ [REQ-T07-02 The gateway speaks Claude's Messages API](req-t07-02-messages-api.md)
