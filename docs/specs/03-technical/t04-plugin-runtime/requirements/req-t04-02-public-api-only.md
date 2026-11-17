🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔌 [T4 Plugin runtime](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T04-02 Only the public API

# 📌 REQ-T04-02 Only the public API

**Status:** ✅ specified

## Statement

Plugins reach the ERP only through the public API with their declared permissions.

## Why

Confirmed by the owner on 2026-11-12; D377, D405.

## Acceptance criteria

1. **Given** a plugin calls an undeclared endpoint, refused.
2. **Given** a plugin update adds a permission, consent asked.

## Measure

Permission checks.

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

⬅️ [REQ-T04-01 Sandbox by trust level](req-t04-01-sandbox-by-trust.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T04-03 One click on or off](req-t04-03-module-registry.md)
