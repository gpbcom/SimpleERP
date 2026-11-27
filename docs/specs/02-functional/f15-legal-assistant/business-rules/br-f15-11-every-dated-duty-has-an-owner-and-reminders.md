🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-11 Every dated duty has an owner and reminders

# 📏 BR-F15-11 Every dated duty has an owner and reminders

**Status:** 🔄 waiting for the owner

## Statement

Each legal duty of the company in the compliance calendar has a due date, a source (the country-pack rule or the
article), an owner and reminders; a duty past its date turns overdue and its owner and the owner of the company are
told.

## Why

Missed filings and registers cost penalties; the calendar makes the company's duties visible (D472).

## Examples

| Case | Result |
|---|---|
| Approval of the accounts due 2027-06-30, owner the owner of the company | passes: reminders 30 and 7 days before (Proposed) |
| Duty with no owner | fails: assigned to the owner of the company by default |
| Duty past its date undone | passes: overdue, both told |

## Applies to

- [UC-F15-07 Keep the compliance calendar](../use-cases/05-duties-and-records/uc-f15-07-keep-the-compliance-calendar.md)
- [UC-F15-08 Track contract renewal and notice dates](../use-cases/05-duties-and-records/uc-f15-08-track-contract-renewal-and-notice-dates.md)
- [UC-F15-09 Approve the accounts and keep the company registers](../use-cases/05-duties-and-records/uc-f15-09-approve-the-accounts-and-keep-the-company-registers.md)

## Exceptions

None.

## Configurable

The company assigns owners and may add its own duties; reminder lead times per duty (Proposed).

## Open questions

None.

---

⬅️ [BR-F15-10 Standards as a register, own copies opt-in](br-f15-10-standards-as-a-register-own-copies-opt-in.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F15-12 Notice dates computed before renewals](br-f15-12-notice-dates-computed-before-renewals.md)
