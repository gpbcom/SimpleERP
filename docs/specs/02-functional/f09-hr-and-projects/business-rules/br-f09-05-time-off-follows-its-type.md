🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-05 Time off follows its type

# 📏 BR-F9-05 Time off follows its type

**Status:** ✅ specified

## Statement

A time-off request follows its type's rules: balance and allocations (regular or accrual), approvers (one or several
steps), blackout days refused, public holidays and mandatory days counted; the legal assistant warns on rest and leave
rules (F15).

## Why

See [D289](../../../06-decisions/f09-hr-and-projects/d289-hr-coverage.md).

Legal values from the France country pack:
[CR-FR-044 Paid leave](../../../10-country-packs/france/labour/cr-fr-044-paid-leave.md).

## Examples

| Case | Result |
|---|---|
| 5 days, balance 12.5 | To approve |
| A blackout day | Refused, with the reason |

## Applies to

Every F9 use case concerned.

## Exceptions

None.

## Configurable

Yes: per type.

## Open questions

None.

---

⬅️ [BR-F9-04 Professional interviews on time](br-f09-04-professional-interviews-on-time.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F9-06 Location only at check-in](br-f09-06-location-only-at-check-in.md)
