🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F8-09 Pay, analyse and report](README.md) › 🖥️ S-F8-28 Sustainability report

# 🖥️ S-F8-28 Sustainability report

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Draft the sustainability report from simple-ERP's data and complete it.

## Entry points

Reports › Sustainability.

## Wireframe

```text
+------------------------------------------------------------------+
| Sustainability report 2026 (VSME)   31 of 40 figures filled       |
| Energy        410 MWh       source: 14 bills                      |
| Emissions     560 t CO2e    purchases + energy                    |
| Workforce     60, turnover 12 %   source: HR                      |
| Water         [      ] m3   missing                               |
|                                         [Export]                  |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-09 step 3, U13 | desktop | ![FL-F8-09 step 3, U13, light](../../images/09-pay-analyse-and-report/u13-owner/3-sustainability-report-desktop-light.png) | ![FL-F8-09 step 3, U13, dark](../../images/09-pay-analyse-and-report/u13-owner/3-sustainability-report-desktop-dark.png) |
| FL-F8-09 step 3, U13 | phone | ![FL-F8-09 step 3, U13, light](../../images/09-pay-analyse-and-report/u13-owner/3-sustainability-report-phone-light.png) | ![FL-F8-09 step 3, U13, dark](../../images/09-pay-analyse-and-report/u13-owner/3-sustainability-report-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-28-sustainability-report-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-28-sustainability-report-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-28-sustainability-report-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-28-sustainability-report-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-28-sustainability-report-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-28-sustainability-report-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f08-28-sustainability-report-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f08-28-sustainability-report-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Figures, sources | E-F8-25 | missing figures |

## Actions

| Action | Who | Result |
|---|---|---|
| Export | owner | Report in the standard's layout |

## States

- Normal: draft the sustainability report from simple-ERP's data and complete it.
- Empty: no year with data: "Data appears as bills and records come in".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: an exported report.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F8-25 Sustainability report](../../data/e-f08-25-sustainability-report.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-25 Sustainability report | Draft | Badge "Draft"; a new record starts here; next: Exported (UC-F8-28); fields editable within the role | U13 | `u13-owner/s-f08-28-sustainability-report-e-f08-25-sustainability-report-draft-{desktop,phone}-{light,dark}.png` |
| E-F8-25 Sustainability report | Exported | Badge "Exported"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f08-28-sustainability-report-e-f08-25-sustainability-report-exported-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F8-09 Pay, analyse and report](../../flows/fl-f08-09-pay-analyse-and-report.md)

## Open questions

None.

---

⬅️ [S-F8-27 Flux analysis](s-f08-27-flux-analysis.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-29 Loans](../11-treasury-and-payment-means/s-f08-29-loans.md)
