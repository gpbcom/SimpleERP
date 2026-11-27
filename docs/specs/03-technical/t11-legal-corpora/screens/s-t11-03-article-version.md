🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) › 🏛️ [T11 Legal corpora](../README.md) ›
🖥️ [Screens](README.md) › 🖥️ S-T11-03 Article version

# 🖥️ S-T11-03 Article version

**Status:** 🔄 (Proposed) drawn in step 36j from its entity and list page; waits for the owner

## Personas

- [U07 Administrator](../../../01-users/personas/u07-administrator.md)

(Proposed) Each persona sees the fields and the actions its roles allow, as on
[S-T11-L03 Article versions](00-lists/s-t11-l03-article-versions.md): the record rules and field rules of T2.

## Purpose

(Proposed) See one [E-T11-03 Article version](../data/e-t11-03-article-version.md) and act on it: its fields, its state
and the changes its state allows. It is the page the rows of
[S-T11-L03 Article versions](00-lists/s-t11-l03-article-versions.md) open (VR-13).

## Entry points

- [S-T11-L03 Article versions](00-lists/s-t11-l03-article-versions.md) › a row's Open ›.
- (Proposed) A link to the record wherever another page names it, and global search.
- The flows of Shown in.

## Wireframe

```text
+--------------------------------------------------------------------------+
| < Article versions   CGI                                      [Recorded] |
|--------------------------------------------------------------------------|
| source, article, valid CGI, 278, 2014-01-01, ...                         |
|--------------------------------------------------------------------------|
| History: every change, by whom and when                                  |
|--------------------------------------------------------------------------|
| [Edit]   [Change state v]   [Ask the AI assistant]                       |
+--------------------------------------------------------------------------+
```

**Example images** (drawn from its wireframe, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Recorded (Article version), U07 | desktop | ![Recorded (Article version), U07, light](../images/states/u07-administrator/s-t11-03-article-version-e-t11-03-article-version-recorded-desktop-light.png) | ![Recorded (Article version), U07, dark](../images/states/u07-administrator/s-t11-03-article-version-e-t11-03-article-version-recorded-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../images/states/s-t11-03-article-version-empty-desktop-light.png) | ![Empty, dark](../images/states/s-t11-03-article-version-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../images/states/s-t11-03-article-version-loading-desktop-light.png) | ![Loading, dark](../images/states/s-t11-03-article-version-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../images/states/s-t11-03-article-version-read-only-desktop-light.png) | ![Read-only, dark](../images/states/s-t11-03-article-version-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../images/states/s-t11-03-article-version-offline-desktop-light.png) | ![Offline, dark](../images/states/s-t11-03-article-version-offline-desktop-dark.png) |

## Fields and columns

As [E-T11-03 Article version](../data/e-t11-03-article-version.md#fields). (Proposed) A field is read-only when the
record's state is final or the role's field rules lock it; personal-data fields show only to the roles that may read
them (VR-12); secrets never show.

## Actions

| Action | Who | Result |
|---|---|---|
| Edit | the personas whose roles may change it | (Proposed) saves the fields; audited |
| Change state | the personas whose roles may change it | (Proposed) one of the Lifecycle's transitions: none: the record has one state |
| Ask the AI assistant | every persona of the page | (Proposed) an answer about this record from the data the user may see, with its sources |
| Back to the list | every persona of the page | [S-T11-L03 Article versions](00-lists/s-t11-l03-article-versions.md) |

## States

- Normal: the record with its fields, its state badge and the actions its state allows, as the wireframe shows.
- Empty: never: a record page always has its record.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122); what was typed stays.
- Read-only: a record in a final state, or a role that may only read it.
- Offline: not available offline: a back-office screen on live, shared data (D38). The app shows that it is offline and
  reloads the screen when the network is back.

Shown entities (VD-15): [E-T11-03 Article version](../data/e-t11-03-article-version.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-T11-03 Article version | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-t11-03-article-version-e-t11-03-article-version-recorded-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

(Proposed) Desktop and tablet; on a phone the fields stack in one column and the actions move to a menu.

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

- [S-T11-L03 Article versions](00-lists/s-t11-l03-article-versions.md)
- [FL-F15-01 Ask a legal question](../../../02-functional/f15-legal-assistant/flows/fl-f15-01-ask-a-legal-question.md)
- [FL-F15-02 Receive a legal warning](../../../02-functional/f15-legal-assistant/flows/fl-f15-02-receive-a-legal-warning.md)
- [FL-F15-03 Check a document against the law](../../../02-functional/f15-legal-assistant/flows/fl-f15-03-check-a-document-against-the-law.md)
- [FL-F15-04 Set up the legal assistant](../../../02-functional/f15-legal-assistant/flows/fl-f15-04-set-up-the-legal-assistant.md)

## Open questions

None.

---

⬅️ [S-T11-02 Country rule](s-t11-02-country-rule.md) · ⬆️ [Up](README.md) ·
➡️ [S-T11-04 Rule flag](s-t11-04-rule-flag.md)
