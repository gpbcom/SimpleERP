🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T12-04 One action contract

# 📌 REQ-T12-04 One action contract

**Status:** ✅ specified

## Statement

Every connector action declares: name, read or write, input and output schemas, idempotency key, dry-run
behaviour, the credential it needs, rate limits and errors; static workflows, agents, MCP clients (T6) and the API (T5)
use the same contract.

## Why

Two modes, one catalogue (D238).

Confirmed by the owner on 2026-11-12 (14:08).

## Acceptance criteria

A new connector appears at once in the workflow designer and in the agents' tools.

## Measure

Actions with a complete contract.

## Priority

Must

## Capabilities served

F16, F3, F4, F5, F6, F7, F8, F15

## Tests

Unit tests of the contract, sandbox tests of each connector, live probes on a staging account.

## Open questions

None.

---

⬅️ [REQ-T12-03 Agentic mode](req-t12-03-agentic-mode.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T12-05 Browser automation for tools without an API](req-t12-05-browser-automation.md)
