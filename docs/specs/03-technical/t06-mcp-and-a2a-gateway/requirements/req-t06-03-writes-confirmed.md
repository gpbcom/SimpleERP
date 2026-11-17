🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🛰️ [T6 MCP and A2A gateway](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T06-03 Writes confirmed

# 📌 REQ-T06-03 Writes confirmed

**Status:** ✅ specified

## Statement

Write tools ask for confirmation unless pre-approved; irreversible acts always.

## Why

Confirmed by the owner on 2026-11-12; D411.

## Acceptance criteria

1. **Given** a deletion through MCP, confirmation asked.
2. **Given** a read, no confirmation.

## Measure

Confirmations.

## Priority

Must

## Capabilities served

F3

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T06-02 Tools from OpenAPI, tool search](req-t06-02-tools-from-openapi.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T06-04 A2A agents per domain](req-t06-04-a2a-agents.md)
