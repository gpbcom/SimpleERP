🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-31 Trips outside the travel policy need approval

# 📏 BR-F8-31 Trips outside the travel policy need approval

**Status:** ✅ specified

## Statement

A trip that has any leg outside the company's travel policy (a class, a price cap, a hotel cap, a booking too late) is
not booked until the employee's manager approves it with a recorded decision; a trip entirely within the policy is
booked without approval.

## Why

Managers should decide exceptions only, and the policy must hold without checking every trip. The owner asked for
business travel ([D527](../../../06-decisions/f08-accounting/d527-benchmark-gaps-f08-accounting.md));
[BR-F8-12 Spend follows card and approval limits](br-f08-12-spend-follows-limits.md) sets the same logic for spend.

## Examples

| Case | Result |
|---|---|
| A 2nd-class train at 62 EUR, cap 100 EUR | within the policy, booked at once |
| A hotel at 142 EUR, cap 120 EUR | outside the policy, needs approval |
| A flight booked 2 days ahead, policy 7 days | outside the policy, needs approval |
| The manager rejects | nothing booked, the reason is sent |
| The manager is away | the delegate decides |

## Applies to

- [UC-F8-39](../use-cases/12-audit-leases-and-special-books/uc-f08-39-book-business-travel.md)
- [E-F8-43 Trip](../data/e-f08-43-trip.md)
- [E-F8-15 Company card](../data/e-f08-15-company-card.md)
- [E-F8-09 Expense claim](../data/e-f08-09-expense-claim.md)

## Exceptions

None.

## Configurable

Yes: the policy's classes, caps and advance booking, per role, by the owner.

## Open questions

None.

---

⬅️ [BR-F8-30](br-f08-30-peppol-serves-only-flows-outside-the-french-platforms.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F8-32](br-f08-32-cash-basis-books-record-receipts-and-payments-only.md)
