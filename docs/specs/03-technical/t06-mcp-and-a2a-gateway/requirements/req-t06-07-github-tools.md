🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🛰️ [T6 MCP and A2A gateway](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T06-07 GitHub tools for the DevOps agents

# 📌 REQ-T06-07 GitHub tools for the DevOps agents

**Status:** ✅ specified

## Statement

The DevOps agents use GitHub tools with the GitHub App's scopes only.

## Why

Confirmed by the owner on 2026-11-12; D435.

## Acceptance criteria

1. **Given** an agent tries to merge, refused.
2. **Given** an agent opens a pull request, it works.

## Measure

Agent calls refused.

## Priority

Must

## Capabilities served

F25

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T06-06 Every call audited and metered](req-t06-06-audited-and-metered.md) · ⬆️ [Up](README.md)
