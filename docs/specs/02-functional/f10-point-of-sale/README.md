🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🏪 F10 Point of sale (plugin)

# 🏪 F10 Point of sale (plugin)

**Status:** ✅ specified

Build step: 7. Plugins and the plugin store.

## Summary

Selling in shops, restaurants, bars, kiosks and on the move: sessions and cash control, baskets, payments and terminals,
receipts and invoices, prices and promotions, loyalty and gift cards, restaurant floors and kitchen screens, QR
self-order and kiosks, offline selling, delivery-platform orders and the French till rules, covering everything the
benchmark offers ([D295](../../06-decisions/f10-point-of-sale/d295-pos-coverage.md),
[D296](../../06-decisions/f10-point-of-sale/d296-till-certified-before-france.md)).

## Scope

- **Shop counter:** sessions, float and cash control, baskets, variants, combos, weights, barcodes, parked orders, ship
  later, refunds and exchanges.
- **Payments:** cash with the legal limit, card terminals, tap-to-pay, QR bank payments, gift cards, e-wallet, split
  payments, tips, service charges, several currencies.
- **Prices:** pricelists, promotions with reference prices, combos, discounts, fiscal positions, cash rounding.
- **Customers:** loyalty, gift cards, e-wallet, invoices at the till or later by QR, digital receipts.
- **Restaurant and bar:** floor plans, tables, courses, kitchen and bar screens and printers, bill splitting, bookings,
  take-away.
- **Self-order:** QR menu and ordering, kiosks, order-status screens.
- **Mobile and delivery:** mobile and offline selling, delivery-platform orders through connectors (D298).
- **Hardware:** receipt and kitchen printers, cash drawers, scanners, scales, customer displays, card terminals.
- **Staff:** PIN, badge, role rights, manager approval.
- **Law:** the till rules of the country pack (certificate before selling in France, D296).
- **Gaps and improvements round ([D467](../../06-decisions/f10-point-of-sale/d467-f10-gaps-and-improvements.md),
  2026-11-12):** meal vouchers within the daily cap, age checks for restricted sales, cash beyond the session (safe,
  bank deposits, cash collection), card-terminal settlements net of fees, clienteling, stock lookup and transfers
  between stores, tax-free sales, store reports (hourly sales, staff, baskets), and the offline state of every till
  screen.

## Personas

[U17 Cashier](../../01-users/personas/u17-cashier.md), [U18 Waiter](../../01-users/personas/u18-waiter.md),
[U19 Kitchen staff](../../01-users/personas/u19-kitchen-staff.md),
[U09 Customer](../../01-users/personas/u09-customer.md), [U02 Manager](../../01-users/personas/u02-manager.md),
[U07 Administrator](../../01-users/personas/u07-administrator.md),
[U05 Accounting](../../01-users/personas/u05-accounting.md), [U13 Owner](../../01-users/personas/u13-owner.md),
[U14 Field worker](../../01-users/personas/u14-field-worker.md),
[U44 Box-office agent](../../01-users/personas/u44-box-office-agent.md),
[U23 Store manager](../../01-users/personas/u23-store-manager.md),
[U15 Warehouse operator](../../01-users/personas/u15-warehouse-operator.md).

## Out of scope

- Online shop: F11.
- Stock management itself: F7 (F10 posts moves).
- Accounting itself: F8 (F10 posts entries).

## Technical capabilities used

- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (payment terminals, delivery
  platforms)
- [T11 Legal corpora](../../03-technical/t11-legal-corpora/README.md) (the country pack)
- [T3 Audit trail](../../03-technical/t03-audit-trail/README.md) (till event log)

## Build step

Step 7, Plugins and the plugin store, of the [roadmap](../../00-vision/roadmap/roadmap.md)
([D483](../../06-decisions/vision/d483-roadmap-devops-agents-first.md)): in V1, like everything the specifications hold.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📝 |  | [Use cases](use-cases/README.md) | ✅ |
| 🔀 |  | [Flows](flows/README.md) | ✅ |
| 📏 |  | [Business rules](business-rules/README.md) | 🔄 |
| 🗃️ |  | [Data](data/README.md) | 🔄 |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🔑 |  | [Permissions](permissions.md) | ✅ |
| 🔔 |  | [Notifications](notifications.md) | ✅ |
| 📈 |  | [Reports](reports.md) | ✅ |
| 🔗 |  | [Integrations](integrations.md) | ✅ |
| 🤖 |  | [AI](ai.md) | ✅ |
| ⚖️ |  | [Regulatory](regulatory.md) | ✅ |
| ❓ |  | [Open questions](open-questions.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | 🔄 |

---

⬅️ [HR and projects](../f09-hr-and-projects/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Online shop (plugin)](../f11-online-shop/README.md)
