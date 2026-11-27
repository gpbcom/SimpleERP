🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🧾 [T3 Audit trail](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T03-02 Inalterable, hash-chained

# 📌 REQ-T03-02 Inalterable, hash-chained

**Status:** ✅ specified

## Statement

The audit trail is append-only and hash-chained per company.

## Why

Confirmed by the owner on 2026-11-12; TC-05.

## Acceptance criteria

1. **Given** an entry altered, the chain check fails.
2. **Given** a restore, the chain is verified.

## Measure

Chain checks.

## Priority

Must

## Capabilities served

F8, F10

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T03-01 Every action recorded](req-t03-01-everything-recorded.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T03-03 Kept as the law says, erasable where it must](req-t03-03-retention-and-erasure.md)
