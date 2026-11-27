🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🔐 [T2 Identity and access engine](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T02-07 Office suites' identity federated

# 📌 REQ-T02-07 Office suites' identity federated

**Status:** ✅ specified

## Statement

The identity providers of openDesk (Nubus, Keycloak) and La Suite numérique (ProConnect) are federated.

## Why

Confirmed by the owner on 2026-11-12; D428.

## Acceptance criteria

1. **Given** a suite user, single sign-on into SimpleERP.
2. **Given** a suite group, it maps to a role.

## Measure

Federated sign-ins.

## Priority

Must

## Capabilities served

F24

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T02-06 Every refusal audited](req-t02-06-refusals-audited.md) · ⬆️ [Up](README.md)
