🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🚀 [T9 Install, backups and updates](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T09-02 Compose and Helm everywhere

# 📌 REQ-T09-02 Compose and Helm everywhere

**Status:** ✅ specified

## Statement

Docker Compose and Helm are both supported, from the same images.

## Why

Confirmed by the owner on 2026-11-12; D419, D421.

## Acceptance criteria

1. **Given** one server, Compose installs it.
2. **Given** a cluster, Helm installs it.

## Measure

Install success.

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

⬅️ [REQ-T09-01 Fully CNCF](req-t09-01-fully-cncf.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T09-03 The laptop profile within 8 GB](req-t09-03-laptop-profile.md)
