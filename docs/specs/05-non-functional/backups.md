🏠 [Specs](../README.md) › 📏 [Non-functional requirements](README.md) › 💾 Backups

# 💾 Backups

**Status:** ✅ specified

## Requirement

- Every company database and file is backed up automatically each day, and kept 30 days.
- A restore is tested when SimpleERP is installed.
- At most one day of data can be lost. See [D24](../06-decisions/foundations/d24-backups-and-updates.md).

- These are the self-hosted default ([D444](../06-decisions/technical/d444-backups-per-edition.md)). The hosted edition
  and IT providers' platforms follow [D422](../06-decisions/technical/d422-backups-and-recovery.md): continuous
  archiving with point-in-time recovery (at most 15 minutes lost, RPO), recovery within 4 hours (RTO), a restore test
  every month; daily backups kept 30 days and monthly backups kept 12 months, encrypted per company, in another region.
  A self-hosted company may choose these targets with the same tooling.

## Measures

- Backups encrypted per company, one company restorable alone (REQ-T09-04).
- Restore tests: monthly in the hosted edition and on IT providers' platforms, at installation when self-hosted.
- The retention of backups is in [Data retention](data-retention.md).

## Open questions

⬜ To be specified.

---

⬅️ [Availability](availability.md) · ⬆️ [Up](README.md) · ➡️ [Updates](updates.md)
