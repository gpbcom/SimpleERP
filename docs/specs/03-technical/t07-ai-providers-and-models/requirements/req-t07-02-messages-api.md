🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🧠 [T7 AI providers and models](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T07-02 The gateway speaks Claude's Messages API

# 📌 REQ-T07-02 The gateway speaks Claude's Messages API

**Status:** ✅ specified

## Statement

Besides its OpenAI-compatible API, the gateway speaks Claude's Messages API, for the DevOps agents.

## Why

Confirmed by the owner on 2026-11-12; F25 build study.

## Acceptance criteria

1. **Given** an Agent SDK call, served through the gateway.
2. **Given** a call through either API, metered the same.

## Measure

Calls per API.

## Priority

Must

## Capabilities served

F25

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T07-01 One AI gateway](req-t07-01-one-gateway.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T07-03 Metering, masking, tracing, fallback](req-t07-03-meter-mask-trace.md)
