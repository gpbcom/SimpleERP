🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-02 Kitchen stock and staff](README.md) › 🖥️ S-SC06-04 Perishables

# 🖥️ S-SC06-04 Perishables

**Status:** ✅ specified

## Personas

- [U19 Kitchen staff](../../../../01-users/personas/u19-kitchen-staff.md)
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)

## Purpose

Used to manage perishables, waste and counts,
[UC-SC06-04](../../use-cases/02-kitchen-stock-and-staff/uc-sc06-04-manage-perishables-waste-and-counts.md).

## Entry points

Restaurant and hospitality in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-02 step 1, U19 | desktop | ![FL-SC06-02 step 1, U19, light](../../images/02-kitchen-stock-and-staff/u19-kitchen-staff/1-perishables-desktop-light.png) | ![FL-SC06-02 step 1, U19, dark](../../images/02-kitchen-stock-and-staff/u19-kitchen-staff/1-perishables-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-04-perishables-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-04-perishables-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-04-perishables-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-04-perishables-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-04-perishables-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-04-perishables-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc06-04-perishables-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc06-04-perishables-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC06-04 Waste record](../../data/e-sc06-04-waste-record.md), shown as the entity pages list them, with
their examples.

## Actions

- Check dates:
  [UC-SC06-04](../../use-cases/02-kitchen-stock-and-staff/uc-sc06-04-manage-perishables-waste-and-counts.md), step 1.
- Record waste:
  [UC-SC06-04](../../use-cases/02-kitchen-stock-and-staff/uc-sc06-04-manage-perishables-waste-and-counts.md), step 2.
- Count: [UC-SC06-04](../../use-cases/02-kitchen-stock-and-staff/uc-sc06-04-manage-perishables-waste-and-counts.md),
  step 3.
- Validate: [UC-SC06-04](../../use-cases/02-kitchen-stock-and-staff/uc-sc06-04-manage-perishables-waste-and-counts.md),
  step 4.

## States

- Normal: products with dates, waste records and the open count.
- Empty: "No waste recorded".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a product past its date: it is blocked from use.
- Read-only: a closed count is read-only.
- Offline: waste and count lines are kept on the tablet and sync later,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC06-02 Kitchen stock and staff](../../flows/fl-sc06-02-kitchen-stock-and-staff.md)

## Open questions

None.

---

⬅️ [S-SC06-03 Hygiene records](../01-menus-and-food-safety/s-sc06-03-hygiene-records.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-05 Tips](s-sc06-05-tips.md)
