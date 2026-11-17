🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🧾 [T3 Audit trail](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T03-01 Every action recorded

# 📌 REQ-T03-01 Every action recorded

**Status:** ✅ specified

## Statement

Every creation, change, validation, sending and AI action is recorded: who, what, when, before and after.

## Why

Confirmed by the owner on 2026-11-12; D405.

## Acceptance criteria

1. **Given** a record changed, the audit trail holds before and after.
2. **Given** an e-invoice sent, the sending is recorded.

## Measure

Coverage of actions.

## Priority

Must

## Capabilities served

All: F1 to F25 and the sectors SC01 to SC16.

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [REQ-T03-02 Inalterable, hash-chained](req-t03-02-hash-chained.md)
