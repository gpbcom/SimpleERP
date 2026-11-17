🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🔐 [T2 Identity and access engine](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T02-04 Sessions revoked on deactivation

# 📌 REQ-T02-04 Sessions revoked on deactivation

**Status:** ✅ specified

## Statement

Deactivating a user revokes every session and token at once.

## Why

Confirmed by the owner on 2026-11-12; D73.

## Acceptance criteria

1. **Given** a user deactivated, their next call fails.
2. **Given** a token of that user, it is refused.

## Measure

Revocation delay.

## Priority

Must

## Capabilities served

F1

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T02-03 Scoped, short-lived tokens](req-t02-03-scoped-tokens.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T02-05 Service accounts, least privilege](req-t02-05-service-accounts.md)
