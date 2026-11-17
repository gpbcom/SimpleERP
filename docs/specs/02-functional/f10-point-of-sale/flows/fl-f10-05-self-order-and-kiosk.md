🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🏪 [F10 Point of sale (plugin)](../README.md) › 🔀 [Flows](README.md) › 🔀 FL-F10-05 Self-order and kiosk

# 🔀 FL-F10-05 Self-order and kiosk

**Status:** ✅ specified

## Summary

Covers UC-F10-12, UC-F10-13, UC-F10-19.

## Personas

- [U09 Customer](../../../01-users/personas/u09-customer.md)
- [U17 Cashier](../../../01-users/personas/u17-cashier.md)

## Flowchart

```mermaid
flowchart LR
  A[QR or kiosk] --> B[Order and pay]
  B --> C[Preparation]
  C --> D[Status screen]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U09 | [S-F10-12](../screens/05-self-order-and-kiosk/s-f10-12-qr-menu.md) | [UC-F10-12](../use-cases/05-self-order-and-kiosk/uc-f10-12-self-order-by-qr-at-the-table.md) | Self-order by QR at the table |
| 2 | U09 | [S-F10-13](../screens/05-self-order-and-kiosk/s-f10-13-kiosk.md) | [UC-F10-13](../use-cases/05-self-order-and-kiosk/uc-f10-13-order-at-a-kiosk.md) | Order at a kiosk |
| 3 | U09, U17 | [S-F10-19](../screens/05-self-order-and-kiosk/s-f10-19-customer-display.md) | [UC-F10-19](../use-cases/05-self-order-and-kiosk/uc-f10-19-show-the-customer-display-and-order-status.md) | Show the customer display and order status |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F10-21 Table QR code](../data/e-f10-21-table-qr-code.md) | Active | 1 [S-F10-12](../screens/05-self-order-and-kiosk/s-f10-12-qr-menu.md) | Table QR codes |
| [E-F10-14 Point of sale device](../data/e-f10-14-point-of-sale-device.md) | Active | 3 [S-F10-19](../screens/05-self-order-and-kiosk/s-f10-19-customer-display.md) | Point of sale devices |
| [E-F10-03 Point of sale order](../data/e-f10-03-point-of-sale-order.md) | Draft, Paid, Invoiced, Refunded | 1 [S-F10-12](../screens/05-self-order-and-kiosk/s-f10-12-qr-menu.md); 2 [S-F10-13](../screens/05-self-order-and-kiosk/s-f10-13-kiosk.md); 3 [S-F10-19](../screens/05-self-order-and-kiosk/s-f10-19-customer-display.md) | Point of sale orders |
| [E-F10-13 Preparation ticket](../data/e-f10-13-preparation-ticket.md) | To prepare, Ready, Served | Shown elsewhere: [S-F10-10 Preparation screen](../screens/04-restaurant-service/s-f10-10-preparation-screen.md) | Preparation tickets |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U09 | phone | [light](../images/05-self-order-and-kiosk/u09-customer/1-qr-order-phone-light.png) | [dark](../images/05-self-order-and-kiosk/u09-customer/1-qr-order-phone-dark.png) |
| 2 | U09 | phone | [light](../images/05-self-order-and-kiosk/u09-customer/2-kiosk-phone-light.png) | [dark](../images/05-self-order-and-kiosk/u09-customer/2-kiosk-phone-dark.png) |
| 3 | U09 | phone | [light](../images/05-self-order-and-kiosk/u09-customer/3-status-screen-phone-light.png) | [dark](../images/05-self-order-and-kiosk/u09-customer/3-status-screen-phone-dark.png) |
| 3 | U17 | desktop | [light](../images/05-self-order-and-kiosk/u17-cashier/3-status-screen-desktop-light.png) | [dark](../images/05-self-order-and-kiosk/u17-cashier/3-status-screen-desktop-dark.png) |
| 3 | U17 | phone | [light](../images/05-self-order-and-kiosk/u17-cashier/3-status-screen-phone-light.png) | [dark](../images/05-self-order-and-kiosk/u17-cashier/3-status-screen-phone-dark.png) |
| 3 | U17 | tablet | [light](../images/05-self-order-and-kiosk/u17-cashier/3-status-screen-tablet-light.png) | [dark](../images/05-self-order-and-kiosk/u17-cashier/3-status-screen-tablet-dark.png) |
| E1 | U09 | phone | [light](../images/05-self-order-and-kiosk/u09-customer/e1-closed-phone-light.png) | [dark](../images/05-self-order-and-kiosk/u09-customer/e1-closed-phone-dark.png) |

## Open questions

None.

---

⬅️ [FL-F10-04 Restaurant service](fl-f10-04-restaurant-service.md) · ⬆️ [Up](README.md) ·
➡️ [FL-F10-06 Mobile and delivery](fl-f10-06-mobile-and-delivery.md)
