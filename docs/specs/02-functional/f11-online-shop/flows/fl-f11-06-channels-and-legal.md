🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛍️ [F11 Online shop (plugin)](../README.md) › 🔀 [Flows](README.md) › 🔀 FL-F11-06 Channels and legal pages

# 🔀 FL-F11-06 Channels and legal pages

**Status:** ✅ specified

## Summary

Covers UC-F11-18, UC-F11-19.

## Personas

- [U07 Administrator](../../../01-users/personas/u07-administrator.md)
- [U12 Marketing](../../../01-users/personas/u12-marketing.md)

## Flowchart

```mermaid
flowchart LR
  A[Connect a channel] --> B[Orders and item stock sync]
  C[Legal pages] --> D[Linked at checkout]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U12, U07 | [S-F11-18](../screens/06-channels-and-legal/s-f11-18-channels.md) | [UC-F11-18](../use-cases/06-channels-and-legal/uc-f11-18-connect-marketplaces-and-other-shops.md) | Connect marketplaces and other shops |
| 2 | U07, U12 | [S-F11-19](../screens/06-channels-and-legal/s-f11-19-legal-pages.md) | [UC-F11-19](../use-cases/06-channels-and-legal/uc-f11-19-publish-the-legal-pages.md) | Publish the legal pages |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F24-02 Tool connection](../../f24-integrations-hub/data/e-f24-02-tool-connection.md) | Proposed, Active, Revoked | Shown elsewhere: [S-F21-10 Connections](../../f21-onboarding-and-modules/screens/03-team-and-data/s-f21-10-connections.md) | Tool connections |
| [E-F6-04 Order](../../f06-customers-and-sales/data/e-f06-04-order.md) | Open, In progress, Cancelled, Done | Shown elsewhere: [S-F6-05 Order](../../f06-customers-and-sales/screens/02-quote-to-order/s-f06-05-order.md) | Orders |
| [E-F7-06 Item](../../f07-purchasing-and-stock/data/e-f07-06-item.md) | Active | Shown elsewhere: [S-F7-21 Stock levels](../../f07-purchasing-and-stock/screens/03-replenish/s-f07-21-stock-levels.md) | Items |
| [E-F11-14 Legal page](../data/e-f11-14-legal-page.md) | Active | 2 [S-F11-19](../screens/06-channels-and-legal/s-f11-19-legal-pages.md) | Legal pages |
| [E-F11-05 Checkout](../data/e-f11-05-checkout.md) | Recorded | Shown elsewhere: [S-F11-05 Checkout](../screens/02-shop-and-check-out/s-f11-05-checkout.md) | Checkouts |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U07 | desktop | [light](../images/06-channels-and-legal/u07-administrator/1-channels-desktop-light.png) | [dark](../images/06-channels-and-legal/u07-administrator/1-channels-desktop-dark.png) |
| 1 | U12 | desktop | [light](../images/06-channels-and-legal/u12-marketing/1-channels-desktop-light.png) | [dark](../images/06-channels-and-legal/u12-marketing/1-channels-desktop-dark.png) |
| 1 | U12 | phone | [light](../images/06-channels-and-legal/u12-marketing/1-channels-phone-light.png) | [dark](../images/06-channels-and-legal/u12-marketing/1-channels-phone-dark.png) |
| 2 | U15 | phone | [light](../images/06-channels-and-legal/u15-warehouse-operator/2-picking-phone-light.png) | [dark](../images/06-channels-and-legal/u15-warehouse-operator/2-picking-phone-dark.png) |
| 2 | U07 | desktop | [light](../images/06-channels-and-legal/u07-administrator/2-picking-desktop-light.png) | [dark](../images/06-channels-and-legal/u07-administrator/2-picking-desktop-dark.png) |
| 2 | U12 | desktop | [light](../images/06-channels-and-legal/u12-marketing/2-picking-desktop-light.png) | [dark](../images/06-channels-and-legal/u12-marketing/2-picking-desktop-dark.png) |
| 2 | U12 | phone | [light](../images/06-channels-and-legal/u12-marketing/2-picking-phone-light.png) | [dark](../images/06-channels-and-legal/u12-marketing/2-picking-phone-dark.png) |
| 3 | U07 | desktop | [light](../images/06-channels-and-legal/u07-administrator/3-legal-pages-desktop-light.png) | [dark](../images/06-channels-and-legal/u07-administrator/3-legal-pages-desktop-dark.png) |
| E1 | U07 | desktop | [light](../images/06-channels-and-legal/u07-administrator/e1-connector-down-desktop-light.png) | [dark](../images/06-channels-and-legal/u07-administrator/e1-connector-down-desktop-dark.png) |
| E2 | U07 | desktop | [light](../images/06-channels-and-legal/u07-administrator/e2-notice-missing-desktop-light.png) | [dark](../images/06-channels-and-legal/u07-administrator/e2-notice-missing-desktop-dark.png) |

## Open questions

None.

---

⬅️ [FL-F11-05 Grow the shop](fl-f11-05-grow-the-shop.md) · ⬆️ [Up](README.md) ·
➡️ [FL-F11-07 Payment risk](fl-f11-07-payment-risk.md)
