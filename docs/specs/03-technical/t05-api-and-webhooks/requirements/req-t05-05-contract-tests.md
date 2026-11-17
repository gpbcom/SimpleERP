🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔗 [T5 API and webhooks](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T05-05 Contracts tested

# 📌 REQ-T05-05 Contracts tested

**Status:** ✅ specified

## Statement

Contract tests run in CI and catch breaking changes.

## Why

Confirmed by the owner on 2026-11-12; D406, D426.

## Acceptance criteria

1. **Given** a field removed, CI fails.
2. **Given** a field added, CI passes.

## Measure

Breaking changes caught.

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

⬅️ [REQ-T05-04 Signed webhooks](req-t05-04-signed-webhooks.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T05-06 Rate limits](req-t05-06-rate-limits.md)
