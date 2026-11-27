🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🔭 [F17 Competitive analysis](../README.md) › 🔀 [Flows](README.md) › 🔀 FL-F17-02 Collect signals

# 🔀 FL-F17-02 Collect signals

**Status:** ✅ specified

## Summary

Covers UC-F17-03, UC-F17-04, UC-F17-05, UC-F17-06, UC-F17-07, UC-F17-08, UC-F17-09.

## Personas

- [U03 Sales](../../../01-users/personas/u03-sales.md)
- [U12 Marketing](../../../01-users/personas/u12-marketing.md)
- [U13 Owner](../../../01-users/personas/u13-owner.md)

## Flowchart

```mermaid
flowchart LR
  A[Sources] --> B[Prices and products]
  A --> C[Jobs and tenders]
  A --> D[Reviews and news]
  A --> E[IP and deals]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U12, U03 | [S-F17-03](../screens/02-collect-signals/s-f17-03-products-and-prices.md) | [UC-F17-03](../use-cases/02-collect-signals/uc-f17-03-track-products-and-prices.md) | Track products and prices |
| 2 | U12, U13 | [S-F17-04](../screens/02-collect-signals/s-f17-04-hiring-signals.md) | [UC-F17-04](../use-cases/02-collect-signals/uc-f17-04-follow-job-offers.md) | Follow job offers |
| 3 | U03, U13 | [S-F17-05](../screens/02-collect-signals/s-f17-05-tenders-won.md) | [UC-F17-05](../use-cases/02-collect-signals/uc-f17-05-follow-tenders-won.md) | Follow tenders won |
| 4 | U13 | [S-F17-06](../screens/02-collect-signals/s-f17-06-intellectual-property.md) | [UC-F17-06](../use-cases/02-collect-signals/uc-f17-06-follow-patents-trademarks-and-designs.md) | Follow patents, trademarks and designs |
| 5 | U12 | [S-F17-07](../screens/02-collect-signals/s-f17-07-reviews.md) | [UC-F17-07](../use-cases/02-collect-signals/uc-f17-07-follow-customer-reviews-and-ratings.md) | Follow customer reviews and ratings |
| 6 | U12 | [S-F17-08](../screens/02-collect-signals/s-f17-08-news.md) | [UC-F17-08](../use-cases/02-collect-signals/uc-f17-08-follow-news-press-and-social-media.md) | Follow news, press and social media |
| 7 | U13 | [S-F17-09](../screens/02-collect-signals/s-f17-09-corporate-events.md) | [UC-F17-09](../use-cases/02-collect-signals/uc-f17-09-follow-funding-deals-and-legal-events.md) | Follow funding, deals and legal events |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F17-09 Data provider](../data/e-f17-09-data-provider.md) | Active | Shown elsewhere: [S-F17-10 Data providers](../screens/01-set-up-and-profiles/s-f17-10-data-providers.md) | Data providers |
| [E-F17-03 Price point](../data/e-f17-03-price-point.md) | Active | 1 [S-F17-03](../screens/02-collect-signals/s-f17-03-products-and-prices.md) | Price points |
| [E-F17-04 Job signal](../data/e-f17-04-job-signal.md) | Recorded | 2 [S-F17-04](../screens/02-collect-signals/s-f17-04-hiring-signals.md) | Job signals |
| [E-F17-05 Tender award](../data/e-f17-05-tender-award.md) | Active | 3 [S-F17-05](../screens/02-collect-signals/s-f17-05-tenders-won.md) | Tender awards |
| [E-F17-07 Review digest](../data/e-f17-07-review-digest.md) | Active | 5 [S-F17-07](../screens/02-collect-signals/s-f17-07-reviews.md) | Review digests |
| [E-F17-08 Mention](../data/e-f17-08-mention.md) | Recorded | 6 [S-F17-08](../screens/02-collect-signals/s-f17-08-news.md); 7 [S-F17-09](../screens/02-collect-signals/s-f17-09-corporate-events.md) | Mentions |
| [E-F17-06 IP filing](../data/e-f17-06-ip-filing.md) | Active | 4 [S-F17-06](../screens/02-collect-signals/s-f17-06-intellectual-property.md) | IP filings |
| [E-F9-38 Job offer](../../f09-hr-and-projects/data/e-f09-38-job-offer.md) | Active | Shown elsewhere: [S-F9-07 Offer](../../f09-hr-and-projects/screens/02-recruit/s-f09-07-offer.md) | Job offers |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U12 | desktop | [light](../images/02-collect-signals/u12-marketing/1-prices-desktop-light.png) | [dark](../images/02-collect-signals/u12-marketing/1-prices-desktop-dark.png) |
| 1 | U12 | phone | [light](../images/02-collect-signals/u12-marketing/1-prices-phone-light.png) | [dark](../images/02-collect-signals/u12-marketing/1-prices-phone-dark.png) |
| 1 | U03 | desktop | [light](../images/02-collect-signals/u03-sales/1-prices-desktop-light.png) | [dark](../images/02-collect-signals/u03-sales/1-prices-desktop-dark.png) |
| 1 | U03 | phone | [light](../images/02-collect-signals/u03-sales/1-prices-phone-light.png) | [dark](../images/02-collect-signals/u03-sales/1-prices-phone-dark.png) |
| 1 | U03 | tablet | [light](../images/02-collect-signals/u03-sales/1-prices-tablet-light.png) | [dark](../images/02-collect-signals/u03-sales/1-prices-tablet-dark.png) |
| 2 | U12 | desktop | [light](../images/02-collect-signals/u12-marketing/2-jobs-desktop-light.png) | [dark](../images/02-collect-signals/u12-marketing/2-jobs-desktop-dark.png) |
| 2 | U12 | phone | [light](../images/02-collect-signals/u12-marketing/2-jobs-phone-light.png) | [dark](../images/02-collect-signals/u12-marketing/2-jobs-phone-dark.png) |
| 2 | U13 | desktop | [light](../images/02-collect-signals/u13-owner/2-jobs-desktop-light.png) | [dark](../images/02-collect-signals/u13-owner/2-jobs-desktop-dark.png) |
| 2 | U13 | phone | [light](../images/02-collect-signals/u13-owner/2-jobs-phone-light.png) | [dark](../images/02-collect-signals/u13-owner/2-jobs-phone-dark.png) |
| 3 | U03 | desktop | [light](../images/02-collect-signals/u03-sales/3-tenders-desktop-light.png) | [dark](../images/02-collect-signals/u03-sales/3-tenders-desktop-dark.png) |
| 3 | U03 | phone | [light](../images/02-collect-signals/u03-sales/3-tenders-phone-light.png) | [dark](../images/02-collect-signals/u03-sales/3-tenders-phone-dark.png) |
| 3 | U03 | tablet | [light](../images/02-collect-signals/u03-sales/3-tenders-tablet-light.png) | [dark](../images/02-collect-signals/u03-sales/3-tenders-tablet-dark.png) |
| 3 | U13 | desktop | [light](../images/02-collect-signals/u13-owner/3-tenders-desktop-light.png) | [dark](../images/02-collect-signals/u13-owner/3-tenders-desktop-dark.png) |
| 3 | U13 | phone | [light](../images/02-collect-signals/u13-owner/3-tenders-phone-light.png) | [dark](../images/02-collect-signals/u13-owner/3-tenders-phone-dark.png) |
| 4 | U13 | desktop | [light](../images/02-collect-signals/u13-owner/4-ip-desktop-light.png) | [dark](../images/02-collect-signals/u13-owner/4-ip-desktop-dark.png) |
| 4 | U13 | phone | [light](../images/02-collect-signals/u13-owner/4-ip-phone-light.png) | [dark](../images/02-collect-signals/u13-owner/4-ip-phone-dark.png) |
| 5 | U12 | desktop | [light](../images/02-collect-signals/u12-marketing/5-reviews-desktop-light.png) | [dark](../images/02-collect-signals/u12-marketing/5-reviews-desktop-dark.png) |
| 5 | U12 | phone | [light](../images/02-collect-signals/u12-marketing/5-reviews-phone-light.png) | [dark](../images/02-collect-signals/u12-marketing/5-reviews-phone-dark.png) |
| 6 | U12 | desktop | [light](../images/02-collect-signals/u12-marketing/6-news-desktop-light.png) | [dark](../images/02-collect-signals/u12-marketing/6-news-desktop-dark.png) |
| 6 | U12 | phone | [light](../images/02-collect-signals/u12-marketing/6-news-phone-light.png) | [dark](../images/02-collect-signals/u12-marketing/6-news-phone-dark.png) |
| 7 | U13 | desktop | [light](../images/02-collect-signals/u13-owner/7-events-desktop-light.png) | [dark](../images/02-collect-signals/u13-owner/7-events-desktop-dark.png) |
| 7 | U13 | phone | [light](../images/02-collect-signals/u13-owner/7-events-phone-light.png) | [dark](../images/02-collect-signals/u13-owner/7-events-phone-dark.png) |
| E1 | U12 | desktop | [light](../images/02-collect-signals/u12-marketing/e1-paywalled-desktop-light.png) | [dark](../images/02-collect-signals/u12-marketing/e1-paywalled-desktop-dark.png) |
| E1 | U12 | phone | [light](../images/02-collect-signals/u12-marketing/e1-paywalled-phone-light.png) | [dark](../images/02-collect-signals/u12-marketing/e1-paywalled-phone-dark.png) |

## Open questions

None.

---

⬅️ [FL-F17-01 Set up and profiles](fl-f17-01-set-up-and-profiles.md) · ⬆️ [Up](README.md) ·
➡️ [FL-F17-03 Analyse and arm sales](fl-f17-03-analyse-and-arm-sales.md)
