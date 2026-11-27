🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🚀 [T9 Install, backups and updates](../README.md) › 📌 [Requirements](README.md) › 📌 REQ-T09-01 Fully CNCF

# 📌 REQ-T09-01 Fully CNCF

**Status:** ✅ specified

## Statement

SimpleERP runs on self-managed and on managed European Kubernetes, with operators by default.

## Why

Confirmed by the owner on 2026-11-12; D421.

## Acceptance criteria

1. **Given** a self-managed cluster, it runs without a cloud service.
2. **Given** a managed PostgreSQL configured, it is used.

## Measure

Platforms tested.

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

⬆️ [Up](README.md) · ➡️ [REQ-T09-02 Compose and Helm everywhere](req-t09-02-compose-and-helm.md)
