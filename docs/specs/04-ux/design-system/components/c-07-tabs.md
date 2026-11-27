🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-07 Tabs

# 🧩 C-07 Tabs

**Status:** ✅ specified

## Purpose

Switches between parts of one record or editor without leaving it: the summary, transcript and actions of a meeting; the
fields, statuses and form of a record type.

## Anatomy

```text
[ Summary ]  Transcript   Decisions and actions (3)
-----------
the selected tab's panel
```

A row of tabs, the selected one underlined; an optional count; the panel under it.

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-07-tabs-desktop-light.png) | ![Variants and states, dark](../images/c-07-tabs-desktop-dark.png) |

## Variants

- **Page tabs:** at the top of a record or an editor, as on
  [S-F2-01 Record type editor](../../../02-functional/f02-no-code-configuration/screens/01-configure-a-record-type/s-f02-01-record-type-editor.md)
  and [S-F4-01 Meeting](../../../02-functional/f04-meetings/screens/01-record-an-online-meeting/s-f04-01-meeting.md).
- **Phone:** the row scrolls sideways; with more than four tabs, a list replaces it.

Tabs are not the bottom tab bar of phones, which is part of [C-08 Navigation](c-08-navigation.md).

## States

| State | Look |
|---|---|
| Default | `color-text-muted` label |
| Hover | `color-text` label |
| Focus | The `color-primary` focus ring |
| Selected | `color-primary` label, weight 600 and a 2 px underline |
| Disabled | `color-text-muted` at reduced emphasis, with a tooltip saying why |
| Error | A tab whose panel holds an error shows the (!) icon and the count of errors |
| Loading | The panel loads; the tab row stays |

## Tokens

`color-primary`, `color-text`, `color-text-muted`, `color-border` under the row; `font-label`
([Typography](../../visual-identity/typography.md)); motion 150 ms ([Motion](../../visual-identity/motion.md)).

## Accessibility

- The tabs pattern of WAI-ARIA: a tab list, tabs and panels; the selected tab is `aria-selected`.
- Arrow keys move between tabs, Home and End go to the first and last; Tab enters the panel.
- A count is part of the tab's name ("Decisions and actions, 3").

## Do and don't

- Do keep tabs for parts of the same thing, two to six of them.
- Do keep the order of tabs stable.
- Don't use tabs for steps to follow in order: use the [C-13 Stepper](c-13-stepper.md).
- Don't nest tabs in tabs.

## Used in

[S-F2-01 Record type editor](../../../02-functional/f02-no-code-configuration/screens/01-configure-a-record-type/s-f02-01-record-type-editor.md),
[S-F2-02 Status designer](../../../02-functional/f02-no-code-configuration/screens/01-configure-a-record-type/s-f02-02-status-designer.md),
[S-F2-03 Form designer](../../../02-functional/f02-no-code-configuration/screens/01-configure-a-record-type/s-f02-03-form-designer.md),
[S-F2-06 Document template editor](../../../02-functional/f02-no-code-configuration/screens/02-customise-documents-and-emails/s-f02-06-document-template-editor.md)
and [S-F4-01 Meeting](../../../02-functional/f04-meetings/screens/01-record-an-online-meeting/s-f04-01-meeting.md).

## Open questions

None.

---

⬅️ [Toast](c-06-toast.md) · ⬆️ [Up](README.md) · ➡️ [Navigation](c-08-navigation.md)
