🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC08-06 Accounts and data](README.md) › 🖥️ S-SC08-15 Publication

# 🖥️ S-SC08-15 Publication

**Status:** 🔄 waiting for the owner

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to publish the yearly accounts above the thresholds,
[UC-SC08-15](../../use-cases/06-accounts-and-data/uc-sc08-15-publish-the-yearly-accounts-above-the-thresholds.md).

## Entry points

Non-profit association in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-06 step 2, U31 | desktop | ![FL-SC08-06 step 2, U31, light](../../images/06-accounts-and-data/u31-treasurer/2-publication-desktop-light.png) | ![FL-SC08-06 step 2, U31, dark](../../images/06-accounts-and-data/u31-treasurer/2-publication-desktop-dark.png) |
| FL-SC08-06 step 2, U31 | phone | ![FL-SC08-06 step 2, U31, light](../../images/06-accounts-and-data/u31-treasurer/2-publication-phone-light.png) | ![FL-SC08-06 step 2, U31, dark](../../images/06-accounts-and-data/u31-treasurer/2-publication-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc08-15-publication-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc08-15-publication-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc08-15-publication-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc08-15-publication-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc08-15-publication-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc08-15-publication-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-15-publication-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-15-publication-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC08-09 Grant report](../../data/e-sc08-09-grant-report.md), shown as the entity pages list them, with
their examples.

## Actions

- Check thresholds:
  [UC-SC08-15](../../use-cases/06-accounts-and-data/uc-sc08-15-publish-the-yearly-accounts-above-the-thresholds.md),
  step 1.
- Appoint the auditor:
  [UC-SC08-15](../../use-cases/06-accounts-and-data/uc-sc08-15-publish-the-yearly-accounts-above-the-thresholds.md),
  step 2.
- Prepare:
  [UC-SC08-15](../../use-cases/06-accounts-and-data/uc-sc08-15-publish-the-yearly-accounts-above-the-thresholds.md),
  step 3.
- Publish:
  [UC-SC08-15](../../use-cases/06-accounts-and-data/uc-sc08-15-publish-the-yearly-accounts-above-the-thresholds.md),
  step 4.

## States

- Normal: thresholds, auditor and publication state.
- Empty: "No year closed".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the deadline near: the treasurer is reminded.
- Read-only: a published year is read-only.
- Offline: not available offline: office work on members, gifts and accounts shared by the board. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC08-06 Accounts and data](../../flows/fl-sc08-06-accounts-and-data.md)

## Open questions

None.

---

⬅️ [S-SC08-14 Association accounts](s-sc08-14-association-accounts.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-16 Bequests](../02-donations-and-receipts/s-sc08-16-bequests.md)
