🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 🔀 [Flows](README.md) › 🔀 FL-F10-02 Sell at the counter

# 🔀 FL-F10-02 Sell at the counter

**Status:** ✅ specified

## Summary

Covers UC-F10-02, UC-F10-08, UC-F10-06, UC-F10-03, UC-F10-05.

## Personas

- [U02 Manager](../../../01-users/personas/u02-manager.md)
- [U09 Customer](../../../01-users/personas/u09-customer.md)
- [U17 Cashier](../../../01-users/personas/u17-cashier.md)
- [U18 Waiter](../../../01-users/personas/u18-waiter.md)

## Flowchart

```mermaid
flowchart LR
  A[Scan or search] --> B[Weigh or read barcode]
  B --> C[Prices and promotions]
  C --> D[Payment]
  D --> E[Receipt or invoice]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U17 | [S-F10-02](../screens/02-sell-at-the-counter/s-f10-02-till.md) | [UC-F10-02](../use-cases/02-sell-at-the-counter/uc-f10-02-sell-at-the-counter.md) | Sell at the counter |
| 2 | U17 | [S-F10-08](../screens/02-sell-at-the-counter/s-f10-08-weighing.md) | [UC-F10-08](../use-cases/02-sell-at-the-counter/uc-f10-08-sell-by-weight-and-barcodes.md) | Sell by weight and barcodes |
| 3 | U17, U02 | [S-F10-06](../screens/02-sell-at-the-counter/s-f10-06-prices-and-promotions.md) | [UC-F10-06](../use-cases/02-sell-at-the-counter/uc-f10-06-apply-prices-promotions-and-combos.md) | Apply prices, promotions and combos |
| 4 | U17, U18 | [S-F10-03](../screens/02-sell-at-the-counter/s-f10-03-payment.md) | [UC-F10-03](../use-cases/02-sell-at-the-counter/uc-f10-03-take-payment.md) | Take payment |
| 5 | U17, U09 | [S-F10-05](../screens/02-sell-at-the-counter/s-f10-05-receipt.md) | [UC-F10-05](../use-cases/02-sell-at-the-counter/uc-f10-05-give-the-receipt-or-an-invoice.md) | Give the receipt or an invoice |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F6-08 Sales price list](../../f06-customers-and-sales/data/e-f06-08-sales-price-list.md) | Active | Shown elsewhere: [S-F6-10 Price lists](../../f06-customers-and-sales/screens/01-lead-to-quote/s-f06-10-price-lists.md) | Sales price lists |
| [E-F10-08 Price promotion](../data/e-f10-08-price-promotion.md) | Active | 3 [S-F10-06](../screens/02-sell-at-the-counter/s-f10-06-prices-and-promotions.md) | Price promotions |
| [E-F10-04 Till payment](../data/e-f10-04-till-payment.md) | Active | 4 [S-F10-03](../screens/02-sell-at-the-counter/s-f10-03-payment.md) | Till payments |
| [E-F10-05 Receipt](../data/e-f10-05-receipt.md) | Recorded | 5 [S-F10-05](../screens/02-sell-at-the-counter/s-f10-05-receipt.md) | Receipts |
| [E-F6-05 Invoice](../../f06-customers-and-sales/data/e-f06-05-invoice.md) | Sent, Received, Refused, Paid, Draft, Issued, Partly paid, Overdue | Shown elsewhere: [S-F6-06 Invoice](../../f06-customers-and-sales/screens/03-invoice-and-get-paid/s-f06-06-invoice.md) | Invoices |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U17 | desktop | [light](../images/02-sell-at-the-counter/u17-cashier/1-basket-desktop-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/1-basket-desktop-dark.png) |
| 1 | U17 | phone | [light](../images/02-sell-at-the-counter/u17-cashier/1-basket-phone-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/1-basket-phone-dark.png) |
| 1 | U17 | tablet | [light](../images/02-sell-at-the-counter/u17-cashier/1-basket-tablet-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/1-basket-tablet-dark.png) |
| 2 | U17 | desktop | [light](../images/02-sell-at-the-counter/u17-cashier/2-weigh-desktop-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/2-weigh-desktop-dark.png) |
| 2 | U17 | phone | [light](../images/02-sell-at-the-counter/u17-cashier/2-weigh-phone-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/2-weigh-phone-dark.png) |
| 2 | U17 | tablet | [light](../images/02-sell-at-the-counter/u17-cashier/2-weigh-tablet-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/2-weigh-tablet-dark.png) |
| 3 | U17 | desktop | [light](../images/02-sell-at-the-counter/u17-cashier/3-promotion-desktop-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/3-promotion-desktop-dark.png) |
| 3 | U17 | phone | [light](../images/02-sell-at-the-counter/u17-cashier/3-promotion-phone-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/3-promotion-phone-dark.png) |
| 3 | U17 | tablet | [light](../images/02-sell-at-the-counter/u17-cashier/3-promotion-tablet-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/3-promotion-tablet-dark.png) |
| 3 | U02 | desktop | [light](../images/02-sell-at-the-counter/u02-manager/3-promotion-desktop-light.png) | [dark](../images/02-sell-at-the-counter/u02-manager/3-promotion-desktop-dark.png) |
| 3 | U02 | phone | [light](../images/02-sell-at-the-counter/u02-manager/3-promotion-phone-light.png) | [dark](../images/02-sell-at-the-counter/u02-manager/3-promotion-phone-dark.png) |
| 4 | U17 | desktop | [light](../images/02-sell-at-the-counter/u17-cashier/4-payment-desktop-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/4-payment-desktop-dark.png) |
| 4 | U17 | phone | [light](../images/02-sell-at-the-counter/u17-cashier/4-payment-phone-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/4-payment-phone-dark.png) |
| 4 | U17 | tablet | [light](../images/02-sell-at-the-counter/u17-cashier/4-payment-tablet-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/4-payment-tablet-dark.png) |
| 4 | U18 | phone | [light](../images/02-sell-at-the-counter/u18-waiter/4-payment-phone-light.png) | [dark](../images/02-sell-at-the-counter/u18-waiter/4-payment-phone-dark.png) |
| 4 | U18 | tablet | [light](../images/02-sell-at-the-counter/u18-waiter/4-payment-tablet-light.png) | [dark](../images/02-sell-at-the-counter/u18-waiter/4-payment-tablet-dark.png) |
| 5 | U17 | desktop | [light](../images/02-sell-at-the-counter/u17-cashier/5-receipt-desktop-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/5-receipt-desktop-dark.png) |
| 5 | U17 | phone | [light](../images/02-sell-at-the-counter/u17-cashier/5-receipt-phone-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/5-receipt-phone-dark.png) |
| 5 | U17 | tablet | [light](../images/02-sell-at-the-counter/u17-cashier/5-receipt-tablet-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/5-receipt-tablet-dark.png) |
| 5 | U09 | phone | [light](../images/02-sell-at-the-counter/u09-customer/5-receipt-phone-light.png) | [dark](../images/02-sell-at-the-counter/u09-customer/5-receipt-phone-dark.png) |
| E1 | U17 | desktop | [light](../images/02-sell-at-the-counter/u17-cashier/e1-cash-limit-desktop-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/e1-cash-limit-desktop-dark.png) |
| E1 | U17 | phone | [light](../images/02-sell-at-the-counter/u17-cashier/e1-cash-limit-phone-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/e1-cash-limit-phone-dark.png) |
| E1 | U17 | tablet | [light](../images/02-sell-at-the-counter/u17-cashier/e1-cash-limit-tablet-light.png) | [dark](../images/02-sell-at-the-counter/u17-cashier/e1-cash-limit-tablet-dark.png) |

## Open questions

None.

---

⬅️ [FL-F10-01 Till session](fl-f10-01-till-session.md) · ⬆️ [Up](README.md) ·
➡️ [FL-F10-03 After sales](fl-f10-03-after-sales.md)
