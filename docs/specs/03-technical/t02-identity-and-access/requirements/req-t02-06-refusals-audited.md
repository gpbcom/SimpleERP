🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🔐 [T2 Identity and access engine](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T02-06 Every refusal audited

# 📌 REQ-T02-06 Every refusal audited

**Status:** ✅ specified

## Statement

Every refused action is recorded in the audit trail.

## Why

Confirmed by the owner on 2026-11-12; D414.

## Acceptance criteria

1. **Given** a refusal, the audit trail holds who, what and why.
2. **Given** many refusals from one token, an alert.

## Measure

Refusals per day.

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

⬅️ [REQ-T02-05 Service accounts, least privilege](req-t02-05-service-accounts.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T02-07 Office suites' identity federated](req-t02-07-suite-federation.md)
