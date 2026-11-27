🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › ⚙️ [Decisions: Technical](README.md) ›
📜 D444 Backup targets per edition

# 📜 D444 Backup targets per edition

**Status:** ✅ decided

## Context

R6: two backup targets, D24 (daily, kept 30 days, one day lost at most) and D422 (RPO 15 minutes, RTO 4 hours), with
neither superseded.

## Options

- D422 for the hosted edition and IT providers, D24 the self-hosted default.
- D422 everywhere.

## Choice

D422 applies to the hosted edition and to IT providers' platforms: RPO 15 minutes, RTO 4 hours, tested monthly; daily
backups kept 30 days and monthly backups kept 12 months. D24 stays the self-hosted default (daily, kept 30 days, one day
lost at most); the same tooling lets a self-hosted company choose D422's targets.

## Decided by

The owner, on 2026-11-12 at 14:55, round 2 of the decisions on the independent review (R6, PROGRESS.md, step 21).

## Consequences

Revises D24 and D422. Backups, REQ-T09-04 and the operations chapter say so.

## Related

- [Backups](../../05-non-functional/backups.md)
- [Operations (docs/technical)](../../../technical/operations/operations.md)
- [D24](../foundations/d24-backups-and-updates.md)
- [D422](d422-backups-and-recovery.md)
- [Independent review of 2026-11-12](../../../tickets/GH-2/review/2026-11-12-review.md)

---

⬅️ [D443](../vision/d443-paid-plugins-sell-support-updates-hosting.md) · ⬆️ [Up](README.md) ·
➡️ [D445 Electronic payslips available 50 years from issue](../f13-payroll/d445-payslips-fifty-years-from-issue.md)
