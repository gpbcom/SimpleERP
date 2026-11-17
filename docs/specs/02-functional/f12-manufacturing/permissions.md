🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🏭 [Manufacturing (plugin)](README.md) ›
🔑 Permissions

# 🔑 Permissions

**Status:** ✅ specified

## Persona × action matrix

| Action | Planner (U21) | Operator (U20) | Warehouse (U15) | Purchasing (U04) | Manager (U02) | Accounting (U05) | Administrator (U07) |
|---|---|---|---|---|---|---|---|
| Bills of materials, routings, work centres | ✅ | read | - | read | read | read work centres, for costing (UC-F12-12) | read work centres, to connect machines (UC-F12-14) |
| Approve an engineering change (BR-F12-02) | ✅ | - | - | - | ✅ | - | - |
| Plan, release and reschedule orders | ✅ | - | - | proposals | read | - | - |
| Start anyway with missing components (BR-F12-03) | ✅ | - | - | - | - | - | - |
| Work orders, quantities, scrap, checks | ✅ | ✅ own | - | - | read | - | - |
| Pick and stage components | - | - | ✅ | - | - | - | - |
| Non-conformities, maintenance | ✅ | report | - | - | read | - | - |
| Costs and variances | ✅ | - | - | - | read | ✅ | - |
| Compliance files, safety and waste registers | ✅ | read | waste lines | - | ✅ | - | - |
| Machine connections (T12) | read | - | - | - | - | - | ✅ |

## Record rules

- Operators see the orders of their work centres and record work under their own name (BR-F12-07).
- Approved versions, consumed lots, safety-register entries and risk-assessment versions are read-only for everyone
  (BR-F12-02, BR-F12-04, BR-F12-15).
- Each site's staff see that site's orders when the company has several.
- Read access where a use case needs it
  ([D519](../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md), VC-15: "Read access where the
  use case needs it (Recommended)"): U05: read work centres, for costing (UC-F12-12); U07: read work centres, to connect
  machines (UC-F12-14).

## Open questions

None.

---

⬅️ [Screens](screens/README.md) · ⬆️ [Up](README.md) · ➡️ [Notifications](notifications.md)
