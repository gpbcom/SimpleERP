🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🧭 [Decisions: Foundations](README.md) ›
📜 D24 Backups and updates

# 📜 D24 Backups and updates

**Status:** ✅ decided

## Context

What backups and uptime guarantee.

## Options

- Daily backups and a short downtime for updates.
- Point-in-time recovery.
- High availability.

## Choice

Daily backups kept 30 days, at most one day of data lost, a few minutes' downtime for an update.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

See the related pages.

Revised by D444 on 2026-11-12: these are the self-hosted default; the hosted edition and IT providers' platforms follow
D422.

## Related

- [Backups](../../05-non-functional/backups.md)
- [Updates](../../05-non-functional/updates.md)

---

⬅️ [D23 Meeting bot consent](d23-meeting-bot-consent.md) · ⬆️ [Up](README.md) ·
➡️ [D25 First-version targets](d25-first-version-targets.md)
