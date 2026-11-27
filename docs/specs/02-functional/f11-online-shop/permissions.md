🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🛍️ [Online shop (plugin)](README.md) ›
🔑 Permissions

# 🔑 Permissions

**Status:** ✅ specified

## Persona × action matrix

| Action | Marketing (U12) | Sales (U03) | Administrator (U07) | Warehouse (U15) | Management (U13) | Customer (U09) |
|---|---|---|---|---|---|---|
| Pages, themes, menus, SEO, languages | ✅ | - | ✅ | - | - | - |
| Catalogue online, ribbons, visibility | ✅ | read | - | - | - | browse |
| Pricelists, promotions, codes | ✅ | ✅ B2B | - | - | - | use codes |
| Approve B2B access (BR-F11-13) | - | ✅ | - | - | - | ask |
| Orders, withdrawals, returns, refunds | read | ✅ | - | ✅ returns | - | own |
| Pickup and shipping | - | - | - | ✅ | - | choose |
| Reviews moderation (BR-F11-09) | ✅ | - | - | - | - | write, report |
| Cart reminders, analytics | ✅ | read | - | - | ✅ read | - |
| Payment providers, carriers, channels (T12) | - | - | ✅ | - | - | the active payment providers, at checkout (UC-F11-06) |
| Legal pages (BR-F11-15) | draft | - | ✅ publishes | - | - | read |

## Record rules

- Customers see only their own account, orders, invoices, withdrawals and consents.
- Accepted terms versions and withdrawal acknowledgements are read-only for everyone (BR-F11-03, BR-F11-15).
- Payment keys are never shown, only their vault reference (BR-F11-14).
- Each website's staff see that website's data when an install runs several.
- Read access where a use case needs it
  ([D519](../../06-decisions/ux/d519-view-cards-reviewed-list-pages-and-workspaces.md), VC-15: "Read access where the
  use case needs it (Recommended)"): U09: the active payment providers, at checkout (UC-F11-06).

## Open questions

None.

---

⬅️ [Screens](screens/README.md) · ⬆️ [Up](README.md) · ➡️ [Notifications](notifications.md)
