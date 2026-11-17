🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-02 Licences and renewals](README.md) › 🖥️ S-SC14-19 Partners

# 🖥️ S-SC14-19 Partners

**Status:** 🔄 waiting for the owner

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to manage partners and resellers
([UC-SC14-19](../../use-cases/02-licences-and-renewals/uc-sc14-19-manage-partners-and-resellers.md)).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-02 step 4, U03 | desktop | ![FL-SC14-02 step 4, U03, light](../../images/02-licences-and-renewals/u03-sales/4-partners-desktop-light.png) | ![FL-SC14-02 step 4, U03, dark](../../images/02-licences-and-renewals/u03-sales/4-partners-desktop-dark.png) |
| FL-SC14-02 step 4, U03 | phone | ![FL-SC14-02 step 4, U03, light](../../images/02-licences-and-renewals/u03-sales/4-partners-phone-light.png) | ![FL-SC14-02 step 4, U03, dark](../../images/02-licences-and-renewals/u03-sales/4-partners-phone-dark.png) |
| FL-SC14-02 step 4, U03 | tablet | ![FL-SC14-02 step 4, U03, light](../../images/02-licences-and-renewals/u03-sales/4-partners-tablet-light.png) | ![FL-SC14-02 step 4, U03, dark](../../images/02-licences-and-renewals/u03-sales/4-partners-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-19-partners-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-19-partners-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-19-partners-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-19-partners-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-19-partners-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-19-partners-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-19-partners-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-19-partners-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC14-15 Partner deal](../../data/e-sc14-15-partner-deal.md),
[E-F6-19 Commission line](../../../../02-functional/f06-customers-and-sales/data/e-f06-19-commission-line.md), shown as
the entity pages list them, with their examples.

## Actions

- Register the deal: [UC-SC14-19](../../use-cases/02-licences-and-renewals/uc-sc14-19-manage-partners-and-resellers.md),
  step 1.
- Bill: [UC-SC14-19](../../use-cases/02-licences-and-renewals/uc-sc14-19-manage-partners-and-resellers.md), step 2.
- Compute the commission:
  [UC-SC14-19](../../use-cases/02-licences-and-renewals/uc-sc14-19-manage-partners-and-resellers.md), step 3.
- Pay: [UC-SC14-19](../../use-cases/02-licences-and-renewals/uc-sc14-19-manage-partners-and-resellers.md), step 4.

## States

- Normal: partners, deals and commissions.
- Empty: "No partner".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a deal conflict: sales decides.
- Read-only: partners read their own.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC14-15 Partner deal](../../data/e-sc14-15-partner-deal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-15 Partner deal | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U05 | `u03-sales/s-sc14-19-partners-e-sc14-15-partner-deal-active-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-sc14-19-partners-e-sc14-15-partner-deal-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC14-02 Licences and renewals](../../flows/fl-sc14-02-licences-and-renewals.md)

## Open questions

None.

---

⬅️ [S-SC14-18 SaaS metrics](../06-portal-and-metrics/s-sc14-18-saas-metrics.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-20 Software assistant](../06-portal-and-metrics/s-sc14-20-software-assistant.md)
