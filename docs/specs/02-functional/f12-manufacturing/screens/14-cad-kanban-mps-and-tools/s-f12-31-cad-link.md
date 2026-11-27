🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F12-14](README.md) ›
🖥️ S-F12-31 CAD link

# 🖥️ S-F12-31 CAD link

**Status:** ✅ specified

## Personas

- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md): reviews and releases, on a desktop.
- [U21 Production planner](../../../../01-users/personas/u21-production-planner.md): checks the revisions the plan uses.

## Purpose

Link drawings to products and release the revisions the shop floor may use.

## Entry points

Manufacturing › CAD link; a bill of materials › Drawings; the notification of a revision to review.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| CAD link                      Kettle K2                                     [Link a file]   |
| ------------------------------------------------------------------------------------------- |
| REFERENCE  REV   FORMAT   LINKED TO          CHANGE   STATE         ACTION                  |
| K2-017     C     step     BoM Kettle K2      ECO-19   In review     [Release] [Send back]   |
| K2-017     B     step     BoM Kettle K2      ECO-14   Released      [Withdraw]              |
| K2-017     A     step     BoM Kettle K2      -        Superseded                            |
| Preview: K2-017 revision C   Shop floor shows: revision B   Orders on B: 3                  |
+---------------------------------------------------------------------------------------------+
```

Example images of the empty, loading, read-only and offline states, drawn in the image round
([D120](../../../../06-decisions/ux/d120-png-mockups.md)): `s-f12-31-cad-link-empty-desktop-{light,dark}.png`,
`s-f12-31-cad-link-loading-desktop-{light,dark}.png`, `s-f12-31-cad-link-offline-desktop-{light,dark}.png`,
`s-f12-31-cad-link-read-only-desktop-{light,dark}.png`.

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-14 step 1, U27 | desktop | ![FL-F12-14 step 1, U27, light](../../images/14-cad-kanban-mps-and-tools/u27-quality-manager/1-cad-link-desktop-light.png) | ![FL-F12-14 step 1, U27, dark](../../images/14-cad-kanban-mps-and-tools/u27-quality-manager/1-cad-link-desktop-dark.png) |
| FL-F12-14 step 1, U27 | desktop | ![FL-F12-14 step 1, U27, light](../../images/14-cad-kanban-mps-and-tools/u27-quality-manager/1-cad-link-desktop-light.png) | ![FL-F12-14 step 1, U27, dark](../../images/14-cad-kanban-mps-and-tools/u27-quality-manager/1-cad-link-desktop-dark.png) |
| FL-F12-14 step 1, U27 | tablet | ![FL-F12-14 step 1, U27, light](../../images/14-cad-kanban-mps-and-tools/u27-quality-manager/1-cad-link-tablet-light.png) | ![FL-F12-14 step 1, U27, dark](../../images/14-cad-kanban-mps-and-tools/u27-quality-manager/1-cad-link-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f12-31-cad-link-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f12-31-cad-link-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f12-31-cad-link-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f12-31-cad-link-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f12-31-cad-link-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f12-31-cad-link-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-f12-31-cad-link-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-f12-31-cad-link-offline-tablet-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Reference and revision | E-F12-30 reference, revision | text | link only | yes |
| Linked object | E-F12-30 linked to | text | yes | yes |
| Change | E-F12-30 change reason | text | yes | no |
| Preview | file store | image | no | no |
| State | E-F12-30 state | badge | by action | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Link a file | header | an engineer, the planner | a Draft link (UC-F12-32) |
| Send to review | row | an engineer | the revision goes to review |
| Release | row | the quality manager | the revision reaches the shop floor |
| Send back | row | the quality manager | the revision returns to Draft with a reason |
| Withdraw | row | the quality manager | the revision is withdrawn |

## States

- Normal: the revisions of the product with their linked object, change and state, and the preview.
- Empty: No file linked to this product yet: a hint to link the first.
- Loading: The revisions as placeholders, then the preview.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a file not
  found in the store says so with its reference.
- Read-only: a superseded or withdrawn revision: shown, with no action.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F12-30 CAD document](../../data/e-f12-30-cad-document.md),
[E-F12-01 Bill of materials](../../data/e-f12-01-bill-of-materials.md),
[E-F12-03 Routing operation](../../data/e-f12-03-routing-operation.md),
[E-F12-11 Engineering change](../../data/e-f12-11-engineering-change.md),
[E-F12-22 Work instruction version](../../data/e-f12-22-work-instruction-version.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F12-30 CAD document | Draft | Badge "Draft"; a new record starts here; next: In review or Withdrawn (UC-F12-32); fields editable within the role | U27, U21 | `u27-quality-manager/s-f12-31-cad-link-e-f12-30-cad-document-draft-{desktop,tablet}-{light,dark}.png`; `u21-production-planner/s-f12-31-cad-link-e-f12-30-cad-document-draft-{desktop,phone}-{light,dark}.png` |
| E-F12-30 CAD document | In review | Badge "In review"; next: Draft or Released (UC-F12-32, BR-F12-27); fields editable within the role | U27, U21 | `u27-quality-manager/s-f12-31-cad-link-e-f12-30-cad-document-in-review-{desktop,tablet}-{light,dark}.png`; `u21-production-planner/s-f12-31-cad-link-e-f12-30-cad-document-in-review-{desktop,phone}-{light,dark}.png` |
| E-F12-30 CAD document | Released | Badge "Released"; next: Superseded or Withdrawn (BR-F12-27, UC-F12-32); fields editable within the role | U27, U21 | `u27-quality-manager/s-f12-31-cad-link-e-f12-30-cad-document-released-{desktop,tablet}-{light,dark}.png`; `u21-production-planner/s-f12-31-cad-link-e-f12-30-cad-document-released-{desktop,phone}-{light,dark}.png` |
| E-F12-30 CAD document | Superseded | Badge "Superseded"; final state, read-only | U27, U21 | `u27-quality-manager/s-f12-31-cad-link-e-f12-30-cad-document-superseded-{desktop,tablet}-{light,dark}.png`; `u21-production-planner/s-f12-31-cad-link-e-f12-30-cad-document-superseded-{desktop,phone}-{light,dark}.png` |
| E-F12-30 CAD document | Withdrawn | Badge "Withdrawn"; final state, read-only | U27, U21 | `u27-quality-manager/s-f12-31-cad-link-e-f12-30-cad-document-withdrawn-{desktop,tablet}-{light,dark}.png`; `u21-production-planner/s-f12-31-cad-link-e-f12-30-cad-document-withdrawn-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per persona, device and theme; the
image round draws them. Rows are derived from each entity's Lifecycle: the badge is the state's name, the next states
are its transitions, and a final state is read-only.

## Responsive behaviour

Desktop; the preview also opens full-screen on a tablet.

## Accessibility

States are words; the preview has a text description of the part; keyboard: next revision, release.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F12-14 CAD, kanban, MPS and tools](../../flows/fl-f12-14-cad-kanban-mps-and-tools.md)

## Open questions

None.

---

⬅️ [S-F12-30 Recipe and batch](../09-recipes-and-batches/s-f12-30-recipe-and-batch.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-32 Kanban](s-f12-32-kanban.md)
