🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
🔀 [Flows](README.md) › 🔀 FL-F14-03 Publish

# 🔀 FL-F14-03 Publish

**Status:** ✅ specified

## Summary

Covers UC-F14-08, UC-F14-09, UC-F14-10, UC-F14-11.

## Personas

- [U11 IT provider administrator](../../../01-users/personas/u11-provider-admin.md)
- [U46 Plugin publisher](../../../01-users/personas/u46-plugin-publisher.md)

## Flowchart

```mermaid
flowchart LR
  A[Submit] --> B[Automated checks]
  B --> C[Security review]
  C --> D[Release]
  D -.-> UUCF1421[Check the bill of materials and licences]
  UUCF1421 -.-> UUCF1426[Translate the listing and the plugin]
```

## Sequence diagram

See each use case.

## Steps

| Step | Persona | Screen | Use case | What happens |
|---|---|---|---|---|
| 1 | U46 | [S-F14-08](../screens/03-publish/s-f14-08-submission.md) | [UC-F14-08](../use-cases/03-publish/uc-f14-08-submit-a-plugin.md) | Submit a plugin |
| 2 | U46 | [S-F14-09](../screens/03-publish/s-f14-09-automated-checks.md) | [UC-F14-09](../use-cases/03-publish/uc-f14-09-pass-automated-checks.md) | Pass automated checks |
| 3 | U11, U46 | [S-F14-10](../screens/03-publish/s-f14-10-security-review.md) | [UC-F14-10](../use-cases/03-publish/uc-f14-10-pass-the-security-review-and-sign.md) | Pass the security review and sign |
| 4 | U46 | [S-F14-11](../screens/03-publish/s-f14-11-releases.md) | [UC-F14-11](../use-cases/03-publish/uc-f14-11-publish-versions-and-release-notes.md) | Publish versions and release notes |
| 5 | U46, U11 | [S-F14-21](../screens/03-publish/s-f14-21-dependency-report.md) | [UC-F14-21](../use-cases/03-publish/uc-f14-21-check-a-plugins-bill-of-materials-and-licences.md) | Check the bill of materials and licences |
| 6 | U46 | [S-F14-24](../screens/03-publish/s-f14-24-translations.md) | [UC-F14-26](../use-cases/03-publish/uc-f14-26-translate-a-listing-and-a-plugin.md) | Translate the listing and the plugin |

### Entities and screens

| Entity | States in this flow | Shown at step and screen | Aggregated view |
|---|---|---|---|
| [E-F14-07 Plugin check report](../data/e-f14-07-plugin-check-report.md) | Recorded | 2 [S-F14-09](../screens/03-publish/s-f14-09-automated-checks.md); 3 [S-F14-10](../screens/03-publish/s-f14-10-security-review.md); 5 [S-F14-21](../screens/03-publish/s-f14-21-dependency-report.md) | Plugin check reports |
| [E-F14-21 Plugin security review](../data/e-f14-21-plugin-security-review.md) | Active | 3 [S-F14-10](../screens/03-publish/s-f14-10-security-review.md) | Plugin security reviews |
| [E-F14-03 Plugin version](../data/e-f14-03-plugin-version.md) | New, Submitted, Published, Approved, Signed, Running | 1 [S-F14-08](../screens/03-publish/s-f14-08-submission.md); 2 [S-F14-09](../screens/03-publish/s-f14-09-automated-checks.md); 3 [S-F14-10](../screens/03-publish/s-f14-10-security-review.md); 4 [S-F14-11](../screens/03-publish/s-f14-11-releases.md) | Plugin versions |
| [E-F12-01 Bill of materials](../../f12-manufacturing/data/e-f12-01-bill-of-materials.md) | Draft, Approved, Retired | Shown elsewhere: [S-F12-01 Bill of materials](../../f12-manufacturing/screens/01-define-the-products/s-f12-01-bill-of-materials.md) | Bill of materials |
| [E-F14-14 Software bill of materials](../data/e-f14-14-software-bill-of-materials.md) | Generated, Checked, Published, Rescanned | 5 [S-F14-21](../screens/03-publish/s-f14-21-dependency-report.md) | Software bill of materials |
| [E-F14-01 Store listing](../data/e-f14-01-store-listing.md) | New, Paid, Refused, Complete | 1 [S-F14-08](../screens/03-publish/s-f14-08-submission.md) | Store listings |
| [E-T04-02 Plugin package](../../../03-technical/t04-plugin-runtime/data/e-t04-02-plugin-package.md) | Active | Shown elsewhere: [S-T04-02 Plugin package](../../../03-technical/t04-plugin-runtime/screens/s-t04-02-plugin-package.md), from the admin list [S-T04-L02](../../../03-technical/t04-plugin-runtime/screens/00-lists/s-t04-l02-plugin-packages.md) | Plugin packages |

## Errors

As each use case.

## Images

Every step and error, for each persona taking part, in light and dark mode (D120). Steps are numbered as in the Steps
table; E rows are the error cases.

| Step | Persona | Device | Light | Dark |
|---|---|---|---|---|
| 1 | U46 | desktop | [light](../images/03-publish/u46-plugin-publisher/1-submit-desktop-light.png) | [dark](../images/03-publish/u46-plugin-publisher/1-submit-desktop-dark.png) |
| 2 | U46 | desktop | [light](../images/03-publish/u46-plugin-publisher/2-checks-desktop-light.png) | [dark](../images/03-publish/u46-plugin-publisher/2-checks-desktop-dark.png) |
| 3 | U11 | desktop | [light](../images/03-publish/u11-provider-admin/3-review-desktop-light.png) | [dark](../images/03-publish/u11-provider-admin/3-review-desktop-dark.png) |
| 3 | U46 | desktop | [light](../images/03-publish/u46-plugin-publisher/3-review-desktop-light.png) | [dark](../images/03-publish/u46-plugin-publisher/3-review-desktop-dark.png) |
| 4 | U46 | desktop | [light](../images/03-publish/u46-plugin-publisher/4-release-desktop-light.png) | [dark](../images/03-publish/u46-plugin-publisher/4-release-desktop-dark.png) |
| E1 | U46 | desktop | [light](../images/03-publish/u46-plugin-publisher/e1-vulnerable-desktop-light.png) | [dark](../images/03-publish/u46-plugin-publisher/e1-vulnerable-desktop-dark.png) |
| 5 | U46 | desktop | [light](../images/03-publish/u46-plugin-publisher/5-dependency-report-desktop-light.png) | [dark](../images/03-publish/u46-plugin-publisher/5-dependency-report-desktop-dark.png) |
| 5 | U11 | desktop | [light](../images/03-publish/u11-provider-admin/5-dependency-report-desktop-light.png) | [dark](../images/03-publish/u11-provider-admin/5-dependency-report-desktop-dark.png) |
| 6 | U46 | desktop | [light](../images/03-publish/u46-plugin-publisher/6-translations-desktop-light.png) | [dark](../images/03-publish/u46-plugin-publisher/6-translations-desktop-dark.png) |

## Open questions

None.

---

⬅️ [FL-F14-02 Buy and licence](fl-f14-02-buy-and-licence.md) · ⬆️ [Up](README.md) ·
➡️ [FL-F14-04 Money and taxes](fl-f14-04-money-and-taxes.md)
