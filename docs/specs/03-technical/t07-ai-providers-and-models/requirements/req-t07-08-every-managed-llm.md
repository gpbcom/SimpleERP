🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🧠 [T7 AI providers and models](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T07-08 Every managed LLM through LangChain-type calls

# 📌 REQ-T07-08 Every managed LLM through LangChain-type calls

**Status:** ✅ specified

## Statement

A provider-neutral client layer with LangChain-type calls can use every managed LLM (the hosted models of every major
provider), through the gateway's metering and masking.

## Why

Confirmed by the owner on 2026-11-12; The owner, 2026-11-12: "LangChain type call: MUST be able to use every managed LLM
models".

## Acceptance criteria

1. **Given** a managed model of another provider chosen, called through the same client.
2. **Given** a new provider added, no feature code changes.

## Measure

Providers supported.

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

⬅️ [REQ-T07-07 Any model, listed](req-t07-07-any-model-listed.md) · ⬆️ [Up](README.md)
