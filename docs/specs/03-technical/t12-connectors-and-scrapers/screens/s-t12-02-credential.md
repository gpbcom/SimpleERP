🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🕸️ [T12 Connectors and scrapers](../README.md) › 🖥️ [Screens](README.md) › 🖥️ S-T12-02 Credential

# 🖥️ S-T12-02 Credential

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../01-users/personas/u07-administrator.md)

Each persona sees the fields and the actions its roles allow, as on
[S-T12-L02 Credentials](00-lists/s-t12-l02-credentials.md): the record rules and field rules of T2.

## Purpose

See one [E-T12-02 Credential](../data/e-t12-02-credential.md) and act on it: its fields, its state and the
changes its state allows. It is the page the rows of [S-T12-L02 Credentials](00-lists/s-t12-l02-credentials.md) open
(VR-13).

## Entry points

- [S-T12-L02 Credentials](00-lists/s-t12-l02-credentials.md) › a row's Open ›.
- A link to the record wherever another page names it, and global search.
- The flows of Shown in.

## Wireframe

```text
+--------------------------------------------------------------------------+
| < Credentials   zendesk-support                                 [Active] |
|--------------------------------------------------------------------------|
| handle                 zendesk-support                                   |
| kind                   OAuth token                                       |
| last four              ...7f2a                                           |
| connector              Zendesk                                           |
| owner                  Claire Martin                                     |
| rotate by              2027-02-10                                        |
| key                    platform                                          |
|--------------------------------------------------------------------------|
| History: every change, by whom and when                                  |
|--------------------------------------------------------------------------|
| [Edit]   [Change state v]   [Ask the AI assistant]                       |
+--------------------------------------------------------------------------+
```

**Example images** (drawn from its wireframe, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Active (Credential), U07 | desktop | ![Active (Credential), U07, light](../images/states/u07-administrator/s-t12-02-credential-e-t12-02-credential-active-desktop-light.png) | ![Active (Credential), U07, dark](../images/states/u07-administrator/s-t12-02-credential-e-t12-02-credential-active-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../images/states/s-t12-02-credential-empty-desktop-light.png) | ![Empty, dark](../images/states/s-t12-02-credential-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../images/states/s-t12-02-credential-loading-desktop-light.png) | ![Loading, dark](../images/states/s-t12-02-credential-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../images/states/s-t12-02-credential-read-only-desktop-light.png) | ![Read-only, dark](../images/states/s-t12-02-credential-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../images/states/s-t12-02-credential-offline-desktop-light.png) | ![Offline, dark](../images/states/s-t12-02-credential-offline-desktop-dark.png) |

## Fields and columns

As [E-T12-02 Credential](../data/e-t12-02-credential.md#fields). A field is read-only when the record's state
is final or the role's field rules lock it; personal-data fields show only to the roles that may read them (VR-12);
secrets never show.

## Actions

| Action | Who | Result |
|---|---|---|
| Edit | the personas whose roles may change it | saves the fields; audited |
| Change state | the personas whose roles may change it | one of the Lifecycle's transitions: none: the record has one state |
| Ask the AI assistant | every persona of the page | an answer about this record from the data the user may see, with its sources |
| Back to the list | every persona of the page | [S-T12-L02 Credentials](00-lists/s-t12-l02-credentials.md) |

## States

- Normal: the record with its fields, its state badge and the actions its state allows, as the wireframe shows.
- Empty: never: a record page always has its record.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122); what was typed stays.
- Read-only: a record in a final state, or a role that may only read it.
- Offline: not available offline: a back-office screen on live, shared data (D38). The app shows that it is offline and
  reloads the screen when the network is back.

Shown entities (VD-15): [E-T12-02 Credential](../data/e-t12-02-credential.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-T12-02 Credential | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-t12-02-credential-e-t12-02-credential-active-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet; on a phone the fields stack in one column and the actions move to a menu.

## Accessibility

The state badge has its state as text; Change state is a menu of buttons named by the next state; the history is a list
whose length is announced.

## Components

- [C-01 Button](../../../04-ux/design-system/components/c-01-button.md)
- [C-02 Form field](../../../04-ux/design-system/components/c-02-form-field.md)
- [C-05 Modal](../../../04-ux/design-system/components/c-05-modal.md)
- [C-14 Timeline](../../../04-ux/design-system/components/c-14-timeline.md)

## Shown in

The list page whose rows open this page (Row opens), then the flows whose Entities and screens table names it:

- [S-T12-L02 Credentials](00-lists/s-t12-l02-credentials.md)
- [FL-F1-05 Connect an external tool](../../../02-functional/f01-administration/flows/fl-f01-05-connect-an-external-tool.md)
- [FL-F1-06 Choose an AI provider](../../../02-functional/f01-administration/flows/fl-f01-06-choose-an-ai-provider.md)
- [FL-F2-06 Share a configuration](../../../02-functional/f02-no-code-configuration/flows/fl-f02-06-share-a-configuration.md)
- [FL-F5-04 Connect accounts](../../../02-functional/f05-social-media/flows/fl-f05-04-connect-accounts.md)
- [FL-F22-01 See and set up](../../../02-functional/f22-unified-cost-management/flows/fl-f22-01-see-and-set-up.md)

## Open questions

None.

---

⬅️ [S-T12-01 Connector](s-t12-01-connector.md) · ⬆️ [Up](README.md) ·
➡️ [S-T12-03 Generated connector](s-t12-03-generated-connector.md)
