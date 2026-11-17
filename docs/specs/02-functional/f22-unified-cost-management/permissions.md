🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) ›
💸 [Unified platform cost management](README.md) › 🔑 Permissions

# 🔑 Permissions

**Status:** ✅ specified

## Persona × action matrix

| Action | Owner (U13) | Accounting (U05) | Administrator (U07) | Manager (U02) | IT provider (U11) | Hosting engineer (U48) |
|---|---|---|---|---|---|---|
| See costs | ✅ | ✅ | ✅ | own team | own clients | hosting |
| Providers, prices, keys | approve | - | ✅ | - | ✅ | - |
| Budgets | ✅ | read | propose | own team | own clients | - |
| Raise a budget, approve a run | ✅ | - | - | - | - | - |
| Stop or pause a run | ✅ | - | ✅ | own runs | - | hosting |
| Allocation, matching, reports | read | ✅ | - | - | ✅ | - |
| Re-billing | - | - | - | - | ✅ | - |

## Record rules

- A manager sees the costs of their own team and projects.
- Usage records keep the user, so that a user sees their own costs.

## Open questions

None.

---

⬅️ [Screens](screens/README.md) · ⬆️ [Up](README.md) · ➡️ [Notifications](notifications.md)
