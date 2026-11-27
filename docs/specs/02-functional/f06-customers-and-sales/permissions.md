🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🛒 [Customers and sales](README.md) ›
🔑 Permissions

# 🔑 Permissions

**Status:** ✅ specified

## Persona × action matrix

| Action | Sales (U03) | Manager (U02) | Accounting (U05) | Office (U16) | Owner (U13) | Customer (U09) |
|---|---|---|---|---|---|---|
| Leads, pipeline | ✅ own | ✅ team | - | read the leads made from inbox messages (UC-F5-05) | ✅ | the leads of their own form answers (UC-F5-19) |
| Quotes | ✅ | ✅ approve discounts | - | ✅ | ✅ | accept, sign |
| Orders | ✅ | ✅ | read, to release held orders (UC-F6-18) | ✅ | ✅ | follow |
| Invoices, credit notes | read their own customers' invoices (UC-F6-24) | read their team's invoices (UC-F6-26) | ✅ | ✅ | ✅ | pay, download |
| Reminders | - | - | ✅ | - | ✅ | - |
| Subscriptions | ✅ | ✅ | ✅ | - | ✅ | manage own |
| Price lists, thresholds | - | ✅ | - | - | ✅ | - |

## Record rules

- Sales people see their own leads and opportunities; managers their team's.
- Customers see only their company's records (BR-F6-03).
- Issued invoices never change (BR-F6-07).
- Read access where a use case needs it
  ([D519](../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md), VC-15: "Read access where the
  use case needs it (Recommended)"): U09: the leads of their own form answers (UC-F5-19); U16: read the leads made from
  inbox messages (UC-F5-05); U05: read, to release held orders (UC-F6-18); U02: read their team's invoices (UC-F6-26);
  U03: read their own customers' invoices (UC-F6-24).

## Open questions

None.

---

⬅️ [Screens](screens/README.md) · ⬆️ [Up](README.md) · ➡️ [Notifications](notifications.md)
