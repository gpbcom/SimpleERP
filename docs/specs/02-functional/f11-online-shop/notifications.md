🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🛍️ [Online shop (plugin)](README.md) ›
🔔 Notifications

# 🔔 Notifications

**Status:** ✅ specified

## Notifications

| Event | To | When |
|---|---|---|
| Order confirmed, with the terms accepted | customer | at once, on a durable medium (BR-F11-15) |
| Order shipped, ready to collect, delivered | customer | at each step |
| Withdrawal received | customer (acknowledgement), sales | at once (BR-F11-03) |
| Refund due within the legal period | sales | before the deadline |
| Delivery date at risk | sales, customer | before the promised date |
| B2B access requested | sales | at once |
| Abandoned cart | customer, if allowed (BR-F11-11) | after the set delay |
| Product back in stock | customers who asked | at once |
| Review to moderate, review rejected | marketing; the author with the reason | at once |
| Channel connector down | administrator, marketing | at once |
| A country rule flagged by a law change (D294) | administrator, marketing | at once |

## Channels

Email for customers, in-app and phone push for staff, SMS for delivery steps.

## Open questions

None.

---

⬅️ [Permissions](permissions.md) · ⬆️ [Up](README.md) · ➡️ [Reports](reports.md)
