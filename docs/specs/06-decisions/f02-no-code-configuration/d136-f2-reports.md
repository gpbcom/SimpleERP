🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D136 F2 reports

# 📜 D136 F2 reports

**Status:** ✅ decided

## Context

Which reports and KPIs F2 offers.

## Options

- Configuration overview.
- Automation health.
- Workflows in progress.
- Unused configuration.

## Choice

All four: a configuration overview (custom fields, record types, statuses, templates, rules and workflows: how many, by
whom, last change); automation health (runs, failures, retries, loops stopped, time saved); workflows in progress
(running instances, where they wait, overdue human tasks); unused configuration (fields never filled, rules never
triggered, templates never used).

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

The reports read the run logs and the configuration versions.

## Related

- [F2 No-code configuration](../../02-functional/f02-no-code-configuration/README.md)

---

⬅️ [D135 Pack sharing](d135-pack-sharing.md) · ⬆️ [Up](README.md) ·
➡️ [D137 F2 notifications](d137-f2-notifications.md)
