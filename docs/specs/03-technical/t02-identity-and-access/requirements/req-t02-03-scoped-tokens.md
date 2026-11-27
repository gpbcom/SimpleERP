🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🔐 [T2 Identity and access engine](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T02-03 Scoped, short-lived tokens

# 📌 REQ-T02-03 Scoped, short-lived tokens

**Status:** ✅ specified

## Statement

Apps and agents use scoped, short-lived OAuth tokens on a user's or a service account's behalf.

## Why

Confirmed by the owner on 2026-11-12; D410.

## Acceptance criteria

1. **Given** a token without the write scope, a write is refused.
2. **Given** a token expired, the call is refused.

## Measure

Token lifetimes.

## Priority

Must

## Capabilities served

F3, F16, F24, F25

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T02-02 Rights as policies in one library](req-t02-02-policies-one-library.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T02-04 Sessions revoked on deactivation](req-t02-04-sessions-revoked.md)
