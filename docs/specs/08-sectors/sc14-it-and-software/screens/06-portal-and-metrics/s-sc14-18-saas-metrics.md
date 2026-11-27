🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-06 Portal and metrics](README.md) › 🖥️ S-SC14-18 SaaS metrics

# 🖥️ S-SC14-18 SaaS metrics

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U41 Customer success manager](../../../../01-users/personas/u41-customer-success-manager.md)

## Purpose

Used to follow SaaS metrics ([UC-SC14-18](../../use-cases/06-portal-and-metrics/uc-sc14-18-follow-saas-metrics.md)).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-06 step 2, U13 | desktop | ![FL-SC14-06 step 2, U13, light](../../images/06-portal-and-metrics/u13-owner/2-metrics-desktop-light.png) | ![FL-SC14-06 step 2, U13, dark](../../images/06-portal-and-metrics/u13-owner/2-metrics-desktop-dark.png) |
| FL-SC14-06 step 2, U13 | phone | ![FL-SC14-06 step 2, U13, light](../../images/06-portal-and-metrics/u13-owner/2-metrics-phone-light.png) | ![FL-SC14-06 step 2, U13, dark](../../images/06-portal-and-metrics/u13-owner/2-metrics-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-18-saas-metrics-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-18-saas-metrics-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-18-saas-metrics-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-18-saas-metrics-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-18-saas-metrics-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-18-saas-metrics-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-18-saas-metrics-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-18-saas-metrics-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC14-01 Software subscription](../../data/e-sc14-01-software-subscription.md),
[E-SC14-09 Health score](../../data/e-sc14-09-health-score.md), shown as the entity pages list them, with their
examples.

## Actions

- Open: [UC-SC14-18](../../use-cases/06-portal-and-metrics/uc-sc14-18-follow-saas-metrics.md), step 1.
- Compare: [UC-SC14-18](../../use-cases/06-portal-and-metrics/uc-sc14-18-follow-saas-metrics.md), step 2.
- Drill into churn: [UC-SC14-18](../../use-cases/06-portal-and-metrics/uc-sc14-18-follow-saas-metrics.md), step 3.
- Export: [UC-SC14-18](../../use-cases/06-portal-and-metrics/uc-sc14-18-follow-saas-metrics.md), step 4.

## States

- Normal: recurring revenue, churn and retention with cohorts.
- Empty: "No data".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, data missing: it is shown.
- Read-only: managers read only.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC14-06 Portal and metrics](../../flows/fl-sc14-06-portal-and-metrics.md)

## Open questions

None.

---

⬅️ [S-SC14-17 Customer portal](s-sc14-17-customer-portal.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-19 Partners](../02-licences-and-renewals/s-sc14-19-partners.md)
