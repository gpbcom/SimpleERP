🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔌 [T4 Plugin runtime](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T04-04 Signed packages only

# 📌 REQ-T04-04 Signed packages only

**Status:** ✅ specified

## Statement

Only signed packages install; install and upgrade are checked on a copy first.

## Why

Confirmed by the owner on 2026-11-12; D415.

## Acceptance criteria

1. **Given** an unsigned package, refused.
2. **Given** an upgrade failing on the copy, not applied.

## Measure

Signature failures.

## Priority

Must

## Capabilities served

F14, F19

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T04-03 One click on or off](req-t04-03-module-registry.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T04-05 Migrations per plugin](req-t04-05-plugin-migrations.md)
