🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🚀 [T9 Install, backups and updates](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T09-08 A Terraform project for OVHcloud and Scaleway

# 📌 REQ-T09-08 A Terraform project for OVHcloud and Scaleway

**Status:** ✅ specified

## Statement

The repository provides a Terraform project that gives a fully working SimpleERP deployment on OVHcloud and on
Scaleway: network, managed Kubernetes, storage, registry, DNS and the Helm release, from an empty account to a running
company.

## Why

Confirmed by the owner on 2026-11-12; The owner, 2026-11-12: "SimpleERP repo will provide a Terraform project for FULLY
WORKING OVHcloud and Scaleway deployment"; D375, D419, D421.

## Acceptance criteria

1. **Given** an empty OVHcloud account and the project applied, SimpleERP runs and a company signs in.
2. **Given** an empty Scaleway account and the project applied, the same.

## Measure

Applies that end in a working sign-in, per cloud, on each release.

## Priority

Must

## Capabilities served

All; the hosted edition (F18 to F20, F25)

## Tests

Unit and contract tests of the service that implements it; isolation, policy and evaluation tests where it applies
(D426).

## Open questions

None.

---

⬅️ [REQ-T09-07 Read-only namespace access](req-t09-07-read-only-namespace-access.md) · ⬆️ [Up](README.md)
