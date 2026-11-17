🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🧭 [F21 Onboarding and module activation](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F21-18 Go-live waits for a complete checklist

# 📏 BR-F21-18 Go-live waits for a complete checklist

**Status:** 🔄 waiting for the owner

## Statement

The go-live of a company can be started only when every step marked required in its cutover plan is done, including the
opening balances signed off, a backup and the legal check; a locked go-live names the open steps, and a go-live that
went wrong can be rolled back within 48 hours.

## Why

A go-live with a forgotten step costs days of repair in the first month; a rollback point turns a disaster into a bad
afternoon. The owner asked for the go-live cutover
([D540](../../../06-decisions/f21-onboarding-and-modules/d540-benchmark-gaps-f21-onboarding-and-modules.md)).

## Examples

| Case | Result |
|---|---|
| Nine steps, eight done | Go live locked, the ninth named |
| Opening balances not yet signed off | locked until the accountant signs |
| Every required step done, optional step open | unlocked |
| Backup failed | go-live refused until a backup exists |
| A problem 6 hours after go-live | roll back to the rollback point |

## Applies to

- [UC-F21-27](../use-cases/06-experts-cutover-and-parallel-run/uc-f21-27-run-the-go-live-cutover.md)
- [E-F21-20 Cutover plan](../data/e-f21-20-cutover-plan.md)
- [E-F21-01 Onboarding progress](../data/e-f21-01-onboarding-progress.md)
- [E-F21-15 Opening balance check](../data/e-f21-15-opening-balance-check.md)

## Exceptions

None.

## Configurable

Which steps are required, by the administrator; backup, opening balances and legal check are always required.

## Open questions

None.

---

⬅️ [BR-F21-17 Paid sessions are quoted before booking](br-f21-17-paid-sessions-are-quoted-before-booking.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F21-19](br-f21-19-differences-are-explained-before-the-old-tool-stops.md)
