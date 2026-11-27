🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F9-09 Train and protect](README.md) › 🖥️ S-F9-24 Risk assessment

# 🖥️ S-F9-24 Risk assessment

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U06 Human resources](../../../../01-users/personas/u06-hr.md)
- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)

## Purpose

Keep the risk assessment per work unit with its actions and versions.

## Entry points

HR › Risk assessment.

## Wireframe

```text
+------------------------------------------------------------------+
| Risk assessment   version 2026-11-20   [Work unit: Site teams v]  |
| Hazard            Sev  Lik  Measures             Actions          |
| Work at height    4    3    harness              platform ladders |
| Manual handling   3    3    trolleys             training 02-03   |
| Linked accidents: 1                    [New version] [PDF]        |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-09 step 4, U13 | desktop | ![FL-F9-09 step 4, U13, light](../../images/09-train-and-protect/u13-owner/4-risk-assessment-desktop-light.png) | ![FL-F9-09 step 4, U13, dark](../../images/09-train-and-protect/u13-owner/4-risk-assessment-desktop-dark.png) |
| FL-F9-09 step 4, U13 | phone | ![FL-F9-09 step 4, U13, light](../../images/09-train-and-protect/u13-owner/4-risk-assessment-phone-light.png) | ![FL-F9-09 step 4, U13, dark](../../images/09-train-and-protect/u13-owner/4-risk-assessment-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f09-24-risk-assessment-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f09-24-risk-assessment-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f09-24-risk-assessment-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f09-24-risk-assessment-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f09-24-risk-assessment-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f09-24-risk-assessment-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f09-24-risk-assessment-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f09-24-risk-assessment-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Hazard, ratings, measures, actions | E-F9-24 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| New version | owner, HR | Dated version |
| PDF | anyone allowed | For display |

## States

- Normal: keep the risk assessment per work unit with its actions and versions.
- Empty: no work unit yet: Add a work unit.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for employees and representatives: read.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F9-09 Train and protect](../../flows/fl-f09-09-train-and-protect.md)

## Open questions

None.

---

⬅️ [S-F9-23 Work accident](s-f09-23-work-accident.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-25 Surveys and exit interviews](../10-listen-to-employees/s-f09-25-surveys-and-exit-interviews.md)
