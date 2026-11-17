🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🚀 [T9 Install, backups and updates](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T09-07 Read-only namespace access

# 📌 REQ-T09-07 Read-only namespace access

**Status:** ✅ specified

## Statement

F20 reads a customer's namespace through a read-only, audited, masked service account; F25 reads only a masked copy of
the customer's company, from its isolated cluster (D442); a namespace holding health data (SC09) stays out of both
models' reach unless the hosting and the model path are HDS-certified (BR-F20-13, BR-F25-13).

## Why

Confirmed by the owner on 2026-11-12; D393, D435.

Revised after the review of 2026-11-12: D442 and R27.

## Acceptance criteria

1. **Given** an agent tries a write, refused.
2. **Given** a read, audited.

## Measure

Reads audited.

## Priority

Must

## Capabilities served

F20, F25

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T09-06 GitOps for hosted clusters](req-t09-06-gitops.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T09-08 A Terraform project for OVHcloud and Scaleway](req-t09-08-terraform-ovhcloud-scaleway.md)
