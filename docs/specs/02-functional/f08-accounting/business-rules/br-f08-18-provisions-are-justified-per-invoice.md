🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 📒 [F8 Accounting](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F8-18 Provisions are justified per invoice

# 📏 BR-F8-18 Provisions are justified per invoice

**Status:** ✅ specified

## Statement

A doubtful-debt provision is set per invoice, excluding VAT, with its reason; it is reversed when paid and turned into a
loss when written off.

## Why

Provisions must be justified to be deductible.

## Examples

| Case | Result |
|---|---|
| 200 days overdue | 50 % proposed (default rates) |
| Paid later | Reversed |

## Applies to

- [UC-F8-26 Provision doubtful debts](../use-cases/08-year-end-duties/uc-f08-26-provision-doubtful-debts.md)

## Exceptions

None.

## Configurable

Rates by age (default: 50 % beyond 180 days).

## Open questions

None.

---

⬅️ [BR-F8-17](br-f08-17-annual-accounts-are-approved-within-six-months.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F8-19 Flux comments are drafts until reviewed](br-f08-19-flux-comments-are-drafts-until-reviewed.md)
