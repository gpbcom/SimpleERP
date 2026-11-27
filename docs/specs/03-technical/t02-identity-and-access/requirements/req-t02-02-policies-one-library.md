🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🔐 [T2 Identity and access engine](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T02-02 Rights as policies in one library

# 📌 REQ-T02-02 Rights as policies in one library

**Status:** ✅ specified

## Statement

Rights and record rules are policies evaluated by one library in every service.

## Why

Confirmed by the owner on 2026-11-12; D414.

## Acceptance criteria

1. **Given** the same user and record, screen, API and MCP give the same decision.
2. **Given** a policy changes, every service applies it at once.

## Measure

Policy decision parity tests.

## Priority

Must

## Capabilities served

All: F1 to F25 and the sectors SC01 to SC16.

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T02-01 Keycloak for every user](req-t02-01-keycloak-sign-in.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T02-03 Scoped, short-lived tokens](req-t02-03-scoped-tokens.md)
