🏠 [Specs](../../README.md) › 🧩 [Functional capabilities](../README.md) › 🛍️ F11 Online shop (plugin)

# 🛍️ F11 Online shop (plugin)

**Status:** ✅ specified

Build step: 7. Plugins and the plugin store.

## Summary

Selling online: the website and its pages, the catalogue, prices and promotions, cart and checkout, payments, delivery
and click & collect, withdrawals and returns, the customer account, B2B, subscriptions, rentals and digital products,
reviews, abandoned carts, SEO and languages, several websites, analytics with cookie consent, marketplaces through
connectors, and the legal pages, covering everything the benchmark offers
([D308](../../06-decisions/f11-online-shop/d308-online-shop-coverage.md),
[D309](../../06-decisions/f11-online-shop/d309-shop-channels-through-connectors.md)).

## Scope

- **Website:** pages from blocks, themes, AI configurator and texts, forms, menus, content by visitor.
- **Catalogue:** categories, variants, ribbons, filters, comparison, wishlist, cross-selling, stock and back-in-stock
  alerts.
- **Prices:** pricelists by country, customer or currency, promotions and codes, loyalty, gift cards, e-wallet, B2B or
  B2C tax display.
- **Checkout:** guest or account, addresses, delivery and pickup, terms, the order button, express checkout, payments
  through providers.
- **After the order:** confirmation, invoices, withdrawal function, returns and refunds, customer account.
- **Special sales:** B2B access and pay on invoice, subscriptions, rentals, digital products.
- **Growth:** abandoned carts, reviews, SEO, languages, several websites, analytics with consent.
- **Channels:** marketplaces and shop platforms through T12 connectors (D309).
- **Law:** the online-selling rules of the country pack, and versioned legal pages.
- **Gaps and improvements round ([D468](../../06-decisions/f11-online-shop/d468-f11-gaps-and-improvements.md),
  2026-11-12):** fraud screening, 3-D Secure and chargebacks; product feeds; product safety information (GPSR);
  pre-orders and back-in-stock reservations; product content per channel; B2B quote requests and punch-out; a deeper
  withdrawal process; the shopper's states (empty cart, out of stock, payment pending); fulfilment from stores; and
  funnel, customer value and return-reason reports.

## Personas

[U12 Marketing](../../01-users/personas/u12-marketing.md), [U03 Sales](../../01-users/personas/u03-sales.md),
[U09 Customer](../../01-users/personas/u09-customer.md),
[U07 Administrator](../../01-users/personas/u07-administrator.md),
[U15 Warehouse operator](../../01-users/personas/u15-warehouse-operator.md),
[U13 Owner](../../01-users/personas/u13-owner.md), [U05 Accounting](../../01-users/personas/u05-accounting.md),
[U04 Purchasing and stock](../../01-users/personas/u04-purchasing.md),
[U23 Store manager](../../01-users/personas/u23-store-manager.md),
[U17 Cashier](../../01-users/personas/u17-cashier.md).

## Out of scope

- Point of sale: F10.
- Orders, invoices and subscriptions themselves: F6 (F11 creates them).
- Stock and carriers: F7.
- Email campaigns: F5.

## Technical capabilities used

- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md) (payment providers, carriers,
  marketplaces)
- [T11 Legal corpora](../../03-technical/t11-legal-corpora/README.md) (the country pack)
- [T7 AI providers and models](../../03-technical/t07-ai-providers-and-models/README.md) (AI pages and texts)

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

⬅️ [Point of sale (plugin)](../f10-point-of-sale/README.md) · ⬆️ [Up](../README.md) ·
➡️ [Manufacturing (plugin)](../f12-manufacturing/README.md)
