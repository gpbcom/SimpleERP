🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛍️ [F11 Online shop (plugin)](../README.md) › 🔀 [Flows](README.md) ›
🔀 FL-F11-04 B2B, subscriptions, rentals and digital

# 🔀 FL-F11-04 B2B, subscriptions, rentals and digital

**Status:** ✅ specified

## Summary

Covers UC-F11-11, UC-F11-12, UC-F11-13.

## Personas

- [U03 Sales](../../../01-users/personas/u03-sales.md)
- [U09 Customer](../../../01-users/personas/u09-customer.md)
- [U12 Marketing](../../../01-users/personas/u12-marketing.md)

## Flowchart

```mermaid
flowchart LR
  A[B2B access] --> B[Orders on account]
  C[Period or dates] --> D[Recurring or rental]
  E[Digital] --> F[Download]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U03, U09 | [S-F11-11](../screens/04-special-sales/s-f11-11-b2b-access.md) | [UC-F11-11](../use-cases/04-special-sales/uc-f11-11-sell-b2b-online.md) | Sell B2B online |
| 2 | U09, U12 | [S-F11-12](../screens/04-special-sales/s-f11-12-subscriptions-and-rentals.md) | [UC-F11-12](../use-cases/04-special-sales/uc-f11-12-sell-subscriptions-and-rentals-online.md) | Sell subscriptions and rentals online |
| 3 | U09 | [S-F11-13](../screens/04-special-sales/s-f11-13-digital-products.md) | [UC-F11-13](../use-cases/04-special-sales/uc-f11-13-sell-digital-products.md) | Sell digital products |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F11-09 Customer account](../data/e-f11-09-customer-account.md) | Active | 1 [S-F11-11](../screens/04-special-sales/s-f11-11-b2b-access.md) | Customer accounts |
| [E-F6-04 Order](../../f06-customers-and-sales/data/e-f06-04-order.md) | Open, In progress, Cancelled, Done | Shown elsewhere: [S-F6-05 Order](../../f06-customers-and-sales/screens/02-quote-to-order/s-f06-05-order.md) | Orders |
| [E-F6-07 Subscription contract](../../f06-customers-and-sales/data/e-f06-07-subscription-contract.md) | Active | Shown elsewhere: [S-F6-09 Subscriptions](../../f06-customers-and-sales/screens/04-subscriptions/s-f06-09-subscriptions.md) | Subscription contracts |
| [E-F6-09 Rental](../../f06-customers-and-sales/data/e-f06-09-rental.md) | Booked, Picked up, Returned, Late | Shown elsewhere: [S-F6-13 Rentals](../../f06-customers-and-sales/screens/05-benchmark-additions/s-f06-13-rentals.md) | Rentals |
| [E-F11-03 Online product](../data/e-f11-03-online-product.md) | New, Published, Delivered, Complete | 2 [S-F11-12](../screens/04-special-sales/s-f11-12-subscriptions-and-rentals.md); 3 [S-F11-13](../screens/04-special-sales/s-f11-13-digital-products.md) | Online products |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U03 | desktop | [light](../images/04-special-sales/u03-sales/1-b2b-access-desktop-light.png) | [dark](../images/04-special-sales/u03-sales/1-b2b-access-desktop-dark.png) |
| 1 | U03 | phone | [light](../images/04-special-sales/u03-sales/1-b2b-access-phone-light.png) | [dark](../images/04-special-sales/u03-sales/1-b2b-access-phone-dark.png) |
| 1 | U03 | tablet | [light](../images/04-special-sales/u03-sales/1-b2b-access-tablet-light.png) | [dark](../images/04-special-sales/u03-sales/1-b2b-access-tablet-dark.png) |
| 1 | U09 | phone | [light](../images/04-special-sales/u09-customer/1-b2b-access-phone-light.png) | [dark](../images/04-special-sales/u09-customer/1-b2b-access-phone-dark.png) |
| 2 | U09 | phone | [light](../images/04-special-sales/u09-customer/2-subscription-rental-phone-light.png) | [dark](../images/04-special-sales/u09-customer/2-subscription-rental-phone-dark.png) |
| 2 | U12 | desktop | [light](../images/04-special-sales/u12-marketing/2-subscription-rental-desktop-light.png) | [dark](../images/04-special-sales/u12-marketing/2-subscription-rental-desktop-dark.png) |
| 2 | U12 | phone | [light](../images/04-special-sales/u12-marketing/2-subscription-rental-phone-light.png) | [dark](../images/04-special-sales/u12-marketing/2-subscription-rental-phone-dark.png) |
| 3 | U09 | phone | [light](../images/04-special-sales/u09-customer/3-digital-phone-light.png) | [dark](../images/04-special-sales/u09-customer/3-digital-phone-dark.png) |
| E1 | U09 | phone | [light](../images/04-special-sales/u09-customer/e1-prices-hidden-phone-light.png) | [dark](../images/04-special-sales/u09-customer/e1-prices-hidden-phone-dark.png) |

## Open questions

None.

---

⬅️ [FL-F11-03 After the order](fl-f11-03-after-the-order.md) · ⬆️ [Up](README.md) ·
➡️ [FL-F11-05 Grow the shop](fl-f11-05-grow-the-shop.md)
