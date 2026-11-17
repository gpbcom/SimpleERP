🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🏪 [Point of sale (plugin)](README.md) ›
🔑 Permissions

# 🔑 Permissions

**Status:** ✅ specified

## Persona × action matrix

| Action | Cashier (U17) | Waiter (U18) | Kitchen (U19) | Manager (U02) | Accounting (U05) | Administrator (U07) | Customer (U09) |
|---|---|---|---|---|---|---|---|
| Open, close a session, cash in and out | ✅ | ✅ own | - | ✅ | - | - | - |
| Sell, take payment | ✅ | ✅ | - | ✅ | - | - | self-order, kiosk |
| Refund, discount, price change, reprint | within limits | within limits | - | ✅ approves (BR-F10-05) | - | - | - |
| Tables, bookings, bills | - | ✅ | - | ✅ | - | - | book |
| Preparation screens | - | see ready | ✅ | ✅ | - | - | order status |
| Point of sale settings, devices | - | - | - | ✅ | - | ✅ | - |
| Reports, closures, archives | own session | own session | - | ✅ | ✅ | - | - |
| Training mode | ✅ | ✅ | - | ✅ | - | - | - |

## Record rules

- Staff see their point of sale's sessions; managers see their shops'.
- Closures, archives and the event log are read-only for everyone (BR-F10-01).
- Customers see only their own orders, receipts, loyalty and gift card balances.

## Open questions

None.

---

⬅️ [Screens](screens/README.md) · ⬆️ [Up](README.md) · ➡️ [Notifications](notifications.md)
