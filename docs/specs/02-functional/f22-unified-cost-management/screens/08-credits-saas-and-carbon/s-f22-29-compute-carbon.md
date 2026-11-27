🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-08 Credits, SaaS subscriptions, carbon and routing](README.md) › 🖥️ S-F22-29 Compute carbon

# 🖥️ S-F22-29 Compute carbon

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md): the footprint of the compute, with each figure's method.

## Purpose

Show the carbon of self-hosted machines and paid AI and scraping usage, with the method of each figure.

## Entry points

Platform costs › Compute carbon; the owner's briefing; the sustainability report.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Compute carbon   Period [2026-11 v]   Total 16.2 kg CO2e   Estimated 40 %          [Export]  |
|---------------------------------------------------------------------------------------------|
| SOURCE            ENERGY    FACTOR (SOURCE, YEAR)         KG CO2E   KIND                     |
| Machine node-1    80 kWh    0.052 national grid, 2025     4.2       measured                 |
| AI provider A     210 kWh   estimate per 1 M tokens       9.8       estimated, 7 to 13       |
| Scraping          20 kWh    0.052 national grid, 2025     1.0       estimated                |
| [Open method] [Compare months] [See savings]                                                |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-08 step 3, U13 | desktop | ![FL-F22-08 step 3, U13, light](../../images/08-credits-saas-and-carbon/u13-owner/3-compute-carbon-desktop-light.png) | ![FL-F22-08 step 3, U13, dark](../../images/08-credits-saas-and-carbon/u13-owner/3-compute-carbon-desktop-dark.png) |
| FL-F22-08 step 3, U13 | phone | ![FL-F22-08 step 3, U13, light](../../images/08-credits-saas-and-carbon/u13-owner/3-compute-carbon-phone-light.png) | ![FL-F22-08 step 3, U13, dark](../../images/08-credits-saas-and-carbon/u13-owner/3-compute-carbon-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-29-compute-carbon-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-29-compute-carbon-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-29-compute-carbon-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-29-compute-carbon-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-29-compute-carbon-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-29-compute-carbon-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f22-29-compute-carbon-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f22-29-compute-carbon-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Source | machine, provider or module | text | no | yes |
| Energy | kWh | number | no | yes |
| Factor, source and year | emission factor | number and text | no | yes |
| Carbon | kg CO2 equivalent | number with range when estimated | no | yes |
| Kind | measured, estimated | badge | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Open method | row | owner, administrator | shows the formula, factor, source and year |
| Compare months | toolbar | owner, administrator | shows two periods side by side |
| Export | header | owner, administrator | a file of the figures with their methods |
| See savings | toolbar | owner, administrator | opens the savings recommendations |

## States

- Normal: the energy, factor, carbon and kind of each source for the period.
- Empty: No metered usage in the period, with the link to the cost screen.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a missing
  emission factor names the country and the year and offers the settings.
- Read-only: The figures of a closed period are read-only.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F22-08](../../flows/fl-f22-08-credits-saas-and-carbon.md)

## Open questions

None.

---

⬅️ [S-F22-28 SaaS subscriptions](s-f22-28-saas-subscriptions.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-30 Model routing](s-f22-30-model-routing.md)
