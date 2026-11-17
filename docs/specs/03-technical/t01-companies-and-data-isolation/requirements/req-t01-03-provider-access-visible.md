🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🏢 [T1 Companies and data isolation](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T01-03 Provider access visible and audited

# 📌 REQ-T01-03 Provider access visible and audited

**Status:** ✅ specified

## Statement

An IT provider's administrator may enter a client company; every session is shown to the client and audited.

## Why

Confirmed by the owner on 2026-11-12; D89, D90.

## Acceptance criteria

1. **Given** a provider session starts, the client sees the banner.
2. **Given** a provider session ends, the audit trail holds it.

## Measure

Provider sessions audited.

## Priority

Must

## Capabilities served

F1

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T01-02 The company context at every layer](req-t01-02-company-context-everywhere.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T01-04 A dedicated namespace or cluster when needed](req-t01-04-dedicated-plans.md)
