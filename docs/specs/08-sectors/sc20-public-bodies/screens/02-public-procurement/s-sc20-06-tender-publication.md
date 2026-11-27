🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏛️ [SC20 Public bodies](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC20-02 Public procurement](README.md) › 🖥️ S-SC20-06 Tender publication

# 🖥️ S-SC20-06 Tender publication

**Status:** 🔄 waiting for the owner

## Personas

- [U54 Public finance officer](../../../../01-users/personas/u54-public-finance-officer.md): the notice, the media, the
  deadline and the questions of bidders.

## Purpose

Publish the tender in the legal media and handle the questions of bidders.

## Entry points

Public bodies › Tender files › Publish; an approved file.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Publish AO-2027-014: School catering                         [Publish] [Corrective notice]       |
| Medium                        Required   Published      Reference                                |
| Official bulletin             yes        20 Mar 2027    B-4411                                   |
| National buyers' platform     yes        20 Mar 2027    P-77120                                  |
| Buyer profile                 yes        20 Mar 2027    -                                        |
| Minimum deadline: 30 days   Deadline set: 12 May 2027        Questions: 3 answered               |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC20-02 step 2, U54 | desktop | ![FL-SC20-02 step 2, U54, light](../../images/02-public-procurement/u54-public-finance-officer/2-tender-publication-desktop-light.png) | ![FL-SC20-02 step 2, U54, dark](../../images/02-public-procurement/u54-public-finance-officer/2-tender-publication-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc20-06-tender-publication-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc20-06-tender-publication-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc20-06-tender-publication-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc20-06-tender-publication-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc20-06-tender-publication-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc20-06-tender-publication-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc20-06-tender-publication-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc20-06-tender-publication-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Medium | E-SC20-05 media | list of medium, required and date | no | yes |
| Minimum deadline | E-SC20-05 minimum | number of days | no | yes |
| Deadline | E-SC20-05 deadline | date and time | yes | yes |
| Questions | E-SC20-05 questions | list of question and answer | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Publish | header | public finance officer | the notice goes to each required medium |
| Corrective notice | header | public finance officer | a correction is published |
| Answer | row | public finance officer | the answer goes to all bidders |

## States

- Normal: the media with required, published date and reference, the deadline and the questions.
- Empty: No approved file to publish.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a medium that
  refuses, a deadline too short, with the medium named.
- Read-only: the record in a locked state: values shown, no action offered.
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

- [FL-SC20-02 Public procurement](../../flows/fl-sc20-02-public-procurement.md)

## Open questions

None.

---

⬅️ [S-SC20-05 Tender file](s-sc20-05-tender-file.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC20-07 Bid analysis](s-sc20-07-bid-analysis.md)
