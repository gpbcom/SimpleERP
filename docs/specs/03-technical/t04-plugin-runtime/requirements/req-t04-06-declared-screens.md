🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔌 [T4 Plugin runtime](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T04-06 Declared screens

# 📌 REQ-T04-06 Declared screens

**Status:** ✅ specified

## Statement

Plugin screens are declared with the design system's components and rendered by the app; custom widgets run in a
sandboxed iframe.

## Why

Confirmed by the owner on 2026-11-12; D407.

## Acceptance criteria

1. **Given** a plugin screen, rendered with the app's components.
2. **Given** a widget reads the page, it cannot.

## Measure

Widget sandbox tests.

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

⬅️ [REQ-T04-05 Migrations per plugin](req-t04-05-plugin-migrations.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T04-07 Limits and metering per plugin](req-t04-07-plugin-limits.md)
