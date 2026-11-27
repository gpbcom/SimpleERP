🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🛡️ [F1 Administration](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F1-26 Portal accounts see only their own records

# 📏 BR-F1-26 Portal accounts see only their own records

**Status:** ✅ specified

## Statement

A portal account sees and changes only the records linked to it, through a record rule that cannot be widened; it never
sees the company's other data or users.

## Why

Outside people must never see another customer's, tenant's or family's records.

## Examples

| Case | Result |
|---|---|
| Customer opens her invoices | Only Durand SA's |
| Tenant opens the building's documents | Only those shared with the building's tenants |
| Supplier types another order number in the address | Refused, not found |

## Applies to

- [UC-F1-19 Manage portal accounts](../use-cases/12-portal-accounts-and-integrations/uc-f01-19-manage-portal-accounts.md)
- [UC-F2-20 Expose a record type on a portal](../../f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-20-expose-a-record-type-on-a-portal.md)
- [UC-F9-31 Follow a project as a customer](../../f09-hr-and-projects/use-cases/11-capacity-rounds-and-partners/uc-f09-31-follow-a-project-as-a-customer.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F1-25 Uncertified rights are reported, not removed](br-f01-25-uncertified-rights-are-reported-not-removed.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-F1-27 Tokens are scoped, dated and shown once](br-f01-27-tokens-are-scoped-dated-and-shown-once.md)
