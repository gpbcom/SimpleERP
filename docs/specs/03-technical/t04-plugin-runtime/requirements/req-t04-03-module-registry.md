🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔌 [T4 Plugin runtime](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T04-03 One click on or off

# 📌 REQ-T04-03 One click on or off

**Status:** ✅ specified

## Statement

The module registry switches a module on or off in one click, checks dependencies and keeps data read-only when off.

## Why

Confirmed by the owner on 2026-11-12; D413, D395.

## Acceptance criteria

1. **Given** a module switched on, its menus appear at once.
2. **Given** a module others need, switching it off refused.

## Measure

Switch time.

## Priority

Must

## Capabilities served

F21

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T04-02 Only the public API](req-t04-02-public-api-only.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T04-04 Signed packages only](req-t04-04-signed-packages.md)
