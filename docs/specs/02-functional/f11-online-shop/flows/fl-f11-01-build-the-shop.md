🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🛍️ [F11 Online shop (plugin)](../README.md) › 🔀 [Flows](README.md) › 🔀 FL-F11-01 Build the shop

# 🔀 FL-F11-01 Build the shop

**Status:** ✅ specified

## Summary

Covers UC-F11-01, UC-F11-02, UC-F11-03, UC-F11-16.

## Personas

- [U03 Sales](../../../01-users/personas/u03-sales.md)
- [U07 Administrator](../../../01-users/personas/u07-administrator.md)
- [U12 Marketing](../../../01-users/personas/u12-marketing.md)

## Flowchart

```mermaid
flowchart LR
  A[Design pages] --> B[Publish catalogue]
  B --> C[Prices and promotions]
  C --> D[SEO and languages]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U12, U07 | [S-F11-01](../screens/01-build-the-shop/s-f11-01-website-editor.md) | [UC-F11-01](../use-cases/01-build-the-shop/uc-f11-01-build-and-design-the-website.md) | Build and design the website |
| 2 | U12 | [S-F11-02](../screens/01-build-the-shop/s-f11-02-catalogue.md) | [UC-F11-02](../use-cases/01-build-the-shop/uc-f11-02-publish-the-catalogue.md) | Publish the catalogue |
| 3 | U12, U03 | [S-F11-03](../screens/01-build-the-shop/s-f11-03-online-prices.md) | [UC-F11-03](../use-cases/01-build-the-shop/uc-f11-03-set-online-prices-and-promotions.md) | Set online prices and promotions |
| 4 | U12, U07 | [S-F11-16](../screens/01-build-the-shop/s-f11-16-seo-and-languages.md) | [UC-F11-16](../use-cases/01-build-the-shop/uc-f11-16-manage-seo-languages-and-several-websites.md) | Manage SEO, languages and several websites |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F11-02 Web page](../data/e-f11-02-web-page.md) | Draft, Published | 1 [S-F11-01](../screens/01-build-the-shop/s-f11-01-website-editor.md); 4 [S-F11-16](../screens/01-build-the-shop/s-f11-16-seo-and-languages.md) | Web pages |
| [E-F11-03 Online product](../data/e-f11-03-online-product.md) | New, Published, Delivered, Complete | 2 [S-F11-02](../screens/01-build-the-shop/s-f11-02-catalogue.md) | Online products |
| [E-F6-08 Sales price list](../../f06-customers-and-sales/data/e-f06-08-sales-price-list.md) | Active | Shown elsewhere: [S-F6-10 Price lists](../../f06-customers-and-sales/screens/01-lead-to-quote/s-f06-10-price-lists.md) | Sales price lists |
| [E-F11-11 Online promotion code](../data/e-f11-11-online-promotion-code.md) | Active | 3 [S-F11-03](../screens/01-build-the-shop/s-f11-03-online-prices.md) | Online promotion codes |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U12 | desktop | [light](../images/01-build-the-shop/u12-marketing/1-website-editor-desktop-light.png) | [dark](../images/01-build-the-shop/u12-marketing/1-website-editor-desktop-dark.png) |
| 1 | U12 | phone | [light](../images/01-build-the-shop/u12-marketing/1-website-editor-phone-light.png) | [dark](../images/01-build-the-shop/u12-marketing/1-website-editor-phone-dark.png) |
| 1 | U07 | desktop | [light](../images/01-build-the-shop/u07-administrator/1-website-editor-desktop-light.png) | [dark](../images/01-build-the-shop/u07-administrator/1-website-editor-desktop-dark.png) |
| 2 | U12 | desktop | [light](../images/01-build-the-shop/u12-marketing/2-catalogue-desktop-light.png) | [dark](../images/01-build-the-shop/u12-marketing/2-catalogue-desktop-dark.png) |
| 2 | U12 | phone | [light](../images/01-build-the-shop/u12-marketing/2-catalogue-phone-light.png) | [dark](../images/01-build-the-shop/u12-marketing/2-catalogue-phone-dark.png) |
| 3 | U12 | desktop | [light](../images/01-build-the-shop/u12-marketing/3-prices-desktop-light.png) | [dark](../images/01-build-the-shop/u12-marketing/3-prices-desktop-dark.png) |
| 3 | U12 | phone | [light](../images/01-build-the-shop/u12-marketing/3-prices-phone-light.png) | [dark](../images/01-build-the-shop/u12-marketing/3-prices-phone-dark.png) |
| 3 | U03 | desktop | [light](../images/01-build-the-shop/u03-sales/3-prices-desktop-light.png) | [dark](../images/01-build-the-shop/u03-sales/3-prices-desktop-dark.png) |
| 3 | U03 | phone | [light](../images/01-build-the-shop/u03-sales/3-prices-phone-light.png) | [dark](../images/01-build-the-shop/u03-sales/3-prices-phone-dark.png) |
| 3 | U03 | tablet | [light](../images/01-build-the-shop/u03-sales/3-prices-tablet-light.png) | [dark](../images/01-build-the-shop/u03-sales/3-prices-tablet-dark.png) |
| 4 | U12 | desktop | [light](../images/01-build-the-shop/u12-marketing/4-seo-languages-desktop-light.png) | [dark](../images/01-build-the-shop/u12-marketing/4-seo-languages-desktop-dark.png) |
| 4 | U12 | phone | [light](../images/01-build-the-shop/u12-marketing/4-seo-languages-phone-light.png) | [dark](../images/01-build-the-shop/u12-marketing/4-seo-languages-phone-dark.png) |
| 4 | U07 | desktop | [light](../images/01-build-the-shop/u07-administrator/4-seo-languages-desktop-light.png) | [dark](../images/01-build-the-shop/u07-administrator/4-seo-languages-desktop-dark.png) |
| E1 | U12 | desktop | [light](../images/01-build-the-shop/u12-marketing/e1-reduction-without-reference-desktop-light.png) | [dark](../images/01-build-the-shop/u12-marketing/e1-reduction-without-reference-desktop-dark.png) |
| E1 | U12 | phone | [light](../images/01-build-the-shop/u12-marketing/e1-reduction-without-reference-phone-light.png) | [dark](../images/01-build-the-shop/u12-marketing/e1-reduction-without-reference-phone-dark.png) |

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [FL-F11-02 Shop and check out](fl-f11-02-shop-and-check-out.md)
