🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D422 Backups and recovery targets

# 📜 D422 Backups and recovery targets

**Status:** ✅ decided

## Context

Step 19k of the technical interview (T9).

## Options

- RPO 15 minutes, RTO 4 hours, tested.
- Daily backups.

## Choice

Confirmed by the owner on 2026-11-12: RPO 15 minutes and RTO 4 hours in the hosted edition, tested monthly; the same
tooling for self-hosting with a daily default.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

The operations chapter's target design.

Revised by D444 on 2026-11-12: it applies to the hosted edition and to IT providers' platforms, with daily backups kept
30 days and monthly backups kept 12 months; D24 stays the self-hosted default.

## Related

- [Backups and recovery targets](../../../technical/operations/operations.md)
- [Technical challenges](../../03-technical/challenges/README.md)

---

⬅️ [D421 Infrastructure: fully CNCF compatible](d421-infrastructure-cncf.md) · ⬆️ [Up](README.md) ·
➡️ [D423 Release train and long-term support](d423-release-train-and-lts.md)
