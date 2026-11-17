🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔧 [F2 No-code configuration](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F2-30 Time-based rules run once per record and period

# 📏 BR-F2-30 Time-based rules run once per record and period

**Status:** ✅ specified

## Statement

A time-based rule fires at most once for a given record and period (a day for an offset rule, the schedule's own period
for a recurring one); a firing already done is never repeated when the rule runs again, the system restarts or the date
field changes, and a missed run fires only within its window.

## Why

A reminder sent twice, or a clean-up run on every restart, is worse than none. The owner's answer: "Time-based rules"
([D521](../../../06-decisions/f02-no-code-configuration/d521-benchmark-gaps-f02-no-code-configuration.md)).

## Examples

| Case | Result |
|---|---|
| A reminder 3 days after sending, the rule runs daily | one reminder per quote |
| The sent date of a quote is corrected after the reminder | no second reminder for that quote |
| Down for a day, window 24 hours | the missed runs fire once when it is back |
| Down for 3 days, window 24 hours | the older runs are skipped and listed |
| A recurring Monday rule | once per Monday per record |

## Applies to

- [UC-F2-33 Set a time-based rule](../use-cases/13-low-code-bulk-and-cleaning/uc-f02-33-set-a-time-based-rule.md)
- [E-F2-32 Scheduled trigger](../data/e-f02-32-scheduled-trigger.md)
- [UC-F2-07 Create a simple rule](../use-cases/03-automate-with-a-rule/uc-f02-07-create-a-simple-rule.md)

## Exceptions

None.

## Configurable

Yes: the window of a missed run, up to 7 days.

## Open questions

None.

---

⬅️ [BR-F2-29 Bulk changes are previewed and can be undone](br-f02-29-bulk-changes-are-previewed-and-can-be-undone.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F2-31 In-place translations ship as packs](br-f02-31-in-place-translations-ship-as-packs.md)
