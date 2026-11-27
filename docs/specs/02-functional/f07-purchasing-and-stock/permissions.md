🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 📦 [Purchasing and stock](README.md) ›
🔑 Permissions

# 🔑 Permissions

**Status:** ✅ specified

## Persona × action matrix

| Action | Employee (U01) | Purchasing (U04) | Warehouse (U15) | Accounting (U05) | Manager (U02) | Owner (U13) | Supplier (U10) | Administrator (U07) |
|---|---|---|---|---|---|---|---|---|
| Purchase request | ✅ | ✅ | - | - | ✅ approve | ✅ approve | - | - |
| Purchase orders | read the orders of their own requests (UC-F7-01) | ✅ | - | read, to match supplier invoices (UC-F7-04) | ✅ | ✅ | confirm | - |
| Receipts, picking, counts | - | - | ✅ | - | ✅ approve counts | - | delivery notes | - |
| Supplier invoices | - | ✅ view | - | ✅ | - | ✅ | send | - |
| Replenishment | - | ✅ | - | - | ✅ | - | - | - |
| Valuation, landed costs | - | - | - | ✅ | - | ✅ | - | - |
| Analytics | - | ✅ | - | - | ✅ | ✅ | - | - |
| Warehouses, routes, rules | - | - | - | - | ✅ rules | - | - | ✅ |

## Record rules

- Suppliers see only their own orders and invoices (D17).
- Moves are never deleted (BR-F7-05); stock never goes negative unless allowed (BR-F7-08).
- Read access where a use case needs it
  ([D519](../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md), VC-15: "Read access where the
  use case needs it (Recommended)"): U01: read the orders of their own requests (UC-F7-01); U05: read, to match supplier
  invoices (UC-F7-04).

## Open questions

None.

---

⬅️ [Screens](screens/README.md) · ⬆️ [Up](README.md) · ➡️ [Notifications](notifications.md)
