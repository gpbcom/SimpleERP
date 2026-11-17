🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🛰️ [T6 MCP and A2A gateway](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T06-05 Outside servers and agents allow-listed

# 📌 REQ-T06-05 Outside servers and agents allow-listed

**Status:** ✅ specified

## Statement

Outside MCP servers and agents are allow-listed per role; their outputs are untrusted.

## Why

Confirmed by the owner on 2026-11-12; D411, D412.

## Acceptance criteria

1. **Given** an outside server not on the list, refused.
2. **Given** an output with instructions, treated as data.

## Measure

Injection tests.

## Priority

Must

## Capabilities served

F3, F24

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T06-04 A2A agents per domain](req-t06-04-a2a-agents.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T06-06 Every call audited and metered](req-t06-06-audited-and-metered.md)
