🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🏪 [Point of sale (plugin)](README.md) ›
🔔 Notifications

# 🔔 Notifications

**Status:** ✅ specified

## Notifications

| Event | To | When |
|---|---|---|
| A cash difference over the threshold | manager | at closing |
| A sensitive action asks for approval | manager on duty | at once |
| An order late at a station | kitchen screen, waiter | when its timer turns red |
| An order ready to collect | customer (status screen, SMS) | at once |
| A delivery-platform order to accept | cashier, kitchen | at once |
| A till offline for long | manager | after the set delay (BR-F10-06) |
| A broken chain or a failed archive | manager, accounting | at once |
| A booking made or cancelled | waiter, manager | at once |
| A country rule flagged by a law change (D294) | administrator, manager | at once |

## Channels

In-app, kitchen and status screens, email, SMS for customers, phone push.

## Open questions

None.

---

⬅️ [Permissions](permissions.md) · ⬆️ [Up](README.md) · ➡️ [Reports](reports.md)
