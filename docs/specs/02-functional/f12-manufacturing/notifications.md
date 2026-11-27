🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🏭 [Manufacturing (plugin)](README.md) ›
🔔 Notifications

# 🔔 Notifications

**Status:** ✅ specified

## Notifications

| Event | To | When |
|---|---|---|
| Components missing for a planned order | planner, purchasing | when the plan runs |
| An order late against its date | planner, sales | at once |
| A failed mandatory check, a non-conformity | planner, manager | at once |
| A machine stop over the threshold | planner, maintenance | at once |
| A maintenance or a legal check due | planner | before the date |
| An engineering change to approve | approvers | at once |
| A compliance file incomplete for a delivery | planner, sales | at once |
| A risk-assessment version due | manager | before the date |
| A machine connector down | administrator, planner | at once |
| A country rule flagged by a law change (D294) | administrator, planner | at once |

## Channels

In-app, the shop-floor tablet, email, phone push.

## Open questions

None.

---

⬅️ [Permissions](permissions.md) · ⬆️ [Up](README.md) · ➡️ [Reports](reports.md)
