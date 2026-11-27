🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › ⚖️ [F15 Legal assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F15-12 Notice dates computed before renewals

# 📏 BR-F15-12 Notice dates computed before renewals

**Status:** 🔄 waiting for the owner

## Statement

A contract recorded with its term, renewal kind and notice period shows the last day to give notice; reminders come
before that day, and a contract left alone renews by its own terms.

## Why

Tacit renewals of leases, insurance and supplier contracts surprise companies (D472); the law on notice and renewal is
(Proposed) to read for the France pack.

## Examples

| Case | Result |
|---|---|
| Insurance renewing on 2027-01-01, 2 months' notice | passes: last notice day 2026-10-31, reminders before |
| Commercial lease of 9 years with 6 months' notice at each 3-year term | passes: last notice days computed for each term |
| Contract with no notice period | passes: flagged "notice unknown" |

## Applies to

- [UC-F15-08 Track contract renewal and notice dates](../use-cases/05-duties-and-records/uc-f15-08-track-contract-renewal-and-notice-dates.md)

## Exceptions

None.

## Configurable

Reminder lead times per contract kind (Proposed) 60 and 15 days.

## Open questions

None.

---

⬅️ [BR-F15-11 Every dated duty has an owner and reminders](br-f15-11-every-dated-duty-has-an-owner-and-reminders.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F15-13 Company-law deadlines kept](br-f15-13-company-law-deadlines-kept.md)
