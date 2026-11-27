🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🔐 [T2 Identity and access engine](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T02-05 Service accounts, least privilege

# 📌 REQ-T02-05 Service accounts, least privilege

**Status:** ✅ specified

## Statement

Workers and agents run as service accounts with only the rights their job needs.

## Why

Confirmed by the owner on 2026-11-12; D435.

## Acceptance criteria

1. **Given** an agent asks for a right outside its role, it is refused.
2. **Given** a worker's rights listed, none beyond its job.

## Measure

Rights per service account.

## Priority

Must

## Capabilities served

F16, F19, F20, F25

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T02-04 Sessions revoked on deactivation](req-t02-04-sessions-revoked.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T02-06 Every refusal audited](req-t02-06-refusals-audited.md)
