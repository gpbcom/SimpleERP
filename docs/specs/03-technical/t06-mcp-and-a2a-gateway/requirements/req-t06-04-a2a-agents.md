🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🛰️ [T6 MCP and A2A gateway](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T06-04 A2A agents per domain

# 📌 REQ-T06-04 A2A agents per domain

**Status:** ✅ specified

## Statement

Agent cards per domain, A2A agents as KEDA pods, signed cards, mutual TLS for partners.

## Why

Confirmed by the owner on 2026-11-12; D412.

## Acceptance criteria

1. **Given** an outside agent fetches a card, it is signed.
2. **Given** a partner call without mutual TLS, refused.

## Measure

A2A tasks.

## Priority

Must

## Capabilities served

F16, F23

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T06-03 Writes confirmed](req-t06-03-writes-confirmed.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T06-05 Outside servers and agents allow-listed](req-t06-05-outside-allow-listed.md)
