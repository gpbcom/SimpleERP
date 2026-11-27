🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 💶 [Payroll (plugin)](README.md) ›
🔑 Permissions

# 🔑 Permissions

**Status:** ✅ specified

## Persona × action matrix

| Action | Payroll officer (U45) | HR (U06) | Accounting (U05) | Owner (U13) | Employee (U01) | Administrator (U07) |
|---|---|---|---|---|---|---|
| Payroll set-up, agreements | ✅ | read | - | read | - | ✅ settings |
| Employees' pay profiles | ✅ | ✅ contracts | - | read | own | - |
| Pay inputs | ✅ | ✅ | - | - | own requests (F9) | - |
| Compute and check the run | ✅ | - | - | - | - | - |
| Approve the run | ✅ | - | - | ✅ second approver | - | - |
| Payslips | ✅ all | - | - | - | own only | - |
| Declarations, contributions | ✅ | - | read | read | - | - |
| Payroll entries, transfers | prepare | - | ✅ post, send | approve | read their own entries only (UC-F13-28) | - |
| Rate updates | ✅ review | - | - | - | - | ✅ apply |

## Record rules

- Pay data is seen only by payroll, the employee concerned and the roles allowed (BR-F13-12); every access is logged.
- Paid runs are read-only (BR-F13-10).
- Managers never see pay amounts.
- Read access where a use case needs it
  ([D519](../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md), VC-15: "Read access where the
  use case needs it (Recommended)"): U01: read their own entries only (UC-F13-28).

## Open questions

None.

---

⬅️ [Screens](screens/README.md) · ⬆️ [Up](README.md) · ➡️ [Notifications](notifications.md)
