🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔌 [T4 Plugin runtime](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T04-05 Migrations per plugin

# 📌 REQ-T04-05 Migrations per plugin

**Status:** ✅ specified

## Statement

Each plugin's schema migrations run on activation and upgrade, expand then contract.

## Why

Confirmed by the owner on 2026-11-12; D423.

## Acceptance criteria

1. **Given** a plugin activated, its tables created.
2. **Given** an upgrade, old and new versions run side by side.

## Measure

Failed migrations.

## Priority

Must

## Capabilities served

F10 to F14

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T04-04 Signed packages only](req-t04-04-signed-packages.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T04-06 Declared screens](req-t04-06-declared-screens.md)
