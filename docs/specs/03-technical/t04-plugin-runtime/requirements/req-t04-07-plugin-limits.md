🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🔌 [T4 Plugin runtime](../README.md) ›
📌 [Requirements](README.md) › 📌 REQ-T04-07 Limits and metering per plugin

# 📌 REQ-T04-07 Limits and metering per plugin

**Status:** ✅ specified

## Statement

Each plugin has CPU, memory and call limits and is metered.

## Why

Confirmed by the owner on 2026-11-12; D398.

## Acceptance criteria

1. **Given** a plugin over its limit, throttled.
2. **Given** a plugin's paid calls, in F22.

## Measure

Throttles per plugin.

## Priority

Must

## Capabilities served

F14, F22

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T04-06 Declared screens](req-t04-06-declared-screens.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T04-08 Planning and calculation workers](req-t04-08-planning-and-calculation-workers.md)
