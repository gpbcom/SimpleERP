🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-08 AI connectors, office suites, warehouse and firms](README.md) ›
🖥️ S-F24-26 AI connector builder

# 🖥️ S-F24-26 AI connector builder

**Status:** 🔄 waiting for the owner

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md): the drafts of the company, their tests and
  their approval.
- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md): the drafts built for their
  clients.

## Purpose

Have the AI assistant draft a connector from a tool's documentation, test it in the sandbox and approve it.

## Entry points

Integrations › AI connector builder; a missing connector request; the catalogue's Build with AI button.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| AI connector builder      Tool: ticket tool      Docs: docs.example.com/api         [Draft]  |
|---------------------------------------------------------------------------------------------|
| Draft v2   Sign-in: API key   Direction: two-way   Fields mapped: 14 of 16                    |
| TEST                    RESULT     DETAIL                                                    |
| Sign in                 Passed     -                                                         |
| Read tickets            Passed     200 records in 4 s                                        |
| Write a ticket          Passed     created and deleted in the test account                   |
| Rate limit              Failed     429 after 60 calls, no wait                               |
| [Ask the AI to fix] [Edit mapping] [Run again] [Approve]                                    |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-08 step 1, U07 | desktop | ![FL-F24-08 step 1, U07, light](../../images/08-ai-connectors-suites-and-warehouse/u07-administrator/1-ai-connector-builder-desktop-light.png) | ![FL-F24-08 step 1, U07, dark](../../images/08-ai-connectors-suites-and-warehouse/u07-administrator/1-ai-connector-builder-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/08-ai-connectors-suites-and-warehouse/u07-administrator/e1-a-sandbox-test-fails-desktop-light.png) | ![Error E1, U07, dark](../../images/08-ai-connectors-suites-and-warehouse/u07-administrator/e1-a-sandbox-test-fails-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-26-ai-connector-builder-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-26-ai-connector-builder-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-26-ai-connector-builder-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-26-ai-connector-builder-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-26-ai-connector-builder-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-26-ai-connector-builder-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f24-26-ai-connector-builder-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f24-26-ai-connector-builder-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Tool and documentation | E-F24-17 tool, documentation | text and link | while Drafted | yes |
| Sign-in and direction | E-F24-17 sign-in, direction | badges | while Drafted | yes |
| Field mapping | E-F24-17 mapping | list of field pairs | while Drafted | yes |
| Tests | E-F24-17 test results | name, result, detail | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Draft | header | administrator | has the AI assistant draft the connector |
| Ask the AI to fix | row | administrator | drafts a new version from the failed test |
| Run again | toolbar | administrator | runs the tests in the sandbox |
| Approve | header | administrator | asks for the credentials and makes the connection, when every test has passed |

## States

- Normal: the draft with its sign-in, direction, mapping and the test results.
- Empty: No draft yet, with Draft and a note on what documentation to give.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a failed test
  shows the call, the answer received and Ask the AI to fix.
- Read-only: A Live or Withdrawn draft shows its code, mapping and last tests; it is not editable.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F24-17 Connector draft](../../data/e-f24-17-connector-draft.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-17 Connector draft | Drafted | Badge "Drafted"; a new record starts here; next: Testing or Withdrawn (BR-F24-17, UC-F24-28); fields editable within the role | U07, U11 | `u07-administrator/s-f24-26-ai-connector-builder-e-f24-17-connector-draft-drafted-desktop-{light,dark}.png`, `u11-provider-admin/s-f24-26-ai-connector-builder-e-f24-17-connector-draft-drafted-desktop-{light,dark}.png` |
| E-F24-17 Connector draft | Testing | Badge "Testing"; next: Failed or Approved (BR-F24-17); fields editable within the role | U07, U11 | `u07-administrator/s-f24-26-ai-connector-builder-e-f24-17-connector-draft-testing-desktop-{light,dark}.png`, `u11-provider-admin/s-f24-26-ai-connector-builder-e-f24-17-connector-draft-testing-desktop-{light,dark}.png` |
| E-F24-17 Connector draft | Failed | Badge "Failed"; next: Drafted (UC-F24-28); fields editable within the role | U07, U11 | `u07-administrator/s-f24-26-ai-connector-builder-e-f24-17-connector-draft-failed-desktop-{light,dark}.png`, `u11-provider-admin/s-f24-26-ai-connector-builder-e-f24-17-connector-draft-failed-desktop-{light,dark}.png` |
| E-F24-17 Connector draft | Approved | Badge "Approved"; next: Live (UC-F24-28); fields editable within the role | U07, U11 | `u07-administrator/s-f24-26-ai-connector-builder-e-f24-17-connector-draft-approved-desktop-{light,dark}.png`, `u11-provider-admin/s-f24-26-ai-connector-builder-e-f24-17-connector-draft-approved-desktop-{light,dark}.png` |
| E-F24-17 Connector draft | Live | Badge "Live"; next: Withdrawn (UC-F24-17); fields editable within the role | U07, U11 | `u07-administrator/s-f24-26-ai-connector-builder-e-f24-17-connector-draft-live-desktop-{light,dark}.png`, `u11-provider-admin/s-f24-26-ai-connector-builder-e-f24-17-connector-draft-live-desktop-{light,dark}.png` |
| E-F24-17 Connector draft | Withdrawn | Badge "Withdrawn"; final: read-only, no next state; the history shows how it got here | U07, U11 | `u07-administrator/s-f24-26-ai-connector-builder-e-f24-17-connector-draft-withdrawn-desktop-{light,dark}.png`, `u11-provider-admin/s-f24-26-ai-connector-builder-e-f24-17-connector-draft-withdrawn-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

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

- [FL-F24-08](../../flows/fl-f24-08-ai-connectors-suites-and-warehouse.md)

## Open questions

None.

---

⬅️ [S-F24-25 Icon library](../05-keep-the-catalogue/s-f24-25-icon-library.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-27 Office suites](s-f24-27-office-suites.md)
