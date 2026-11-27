🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-06 Toast

# 🧩 C-06 Toast

**Status:** ✅ specified

## Purpose

Confirms, briefly, that an action is done, without stopping the user: "Invoice out. Acme pays by 12 Dec."
([Tone of voice](../../visual-identity/tone-of-voice.md)).

## Anatomy

```text
+---------------------------------------------+
| (v) 12 tasks moved.          [Undo]  [x]   |
+---------------------------------------------+
```

An icon, one sentence, an optional action and a close button.

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-06-toast-desktop-light.png) | ![Variants and states, dark](../images/c-06-toast-desktop-dark.png) |

## Variants

- **Success:** a check icon.
- **Information:** an information icon, for something done in the background, such as an export ready to
  download. A lost network is a banner, not a toast ([error message pattern](../patterns/error-messages.md)).
- **With an action:** such as Undo, when the action can be reverted
  ([D158](../../../06-decisions/f03-assistant/d158-assistant-undo.md)).

Errors that need an action are not toasts: they follow the [error message pattern](../patterns/error-messages.md).
Notifications that must be kept go to the bell of the top bar
([D92](../../../06-decisions/f01-administration/d92-notification-channels.md)).

## States

Entering (150 ms, [Motion](../../visual-identity/motion.md)), shown, paused while hovered or focused, leaving.
A toast without an action closes after 6 seconds; a toast with an action stays until closed or until the user
leaves the page. At most one toast at a time: a new one replaces the old.

## Tokens

`color-text` background with `color-surface` text, so it stands out in both modes; radius 8 px;
`elevation-2`; `font-body`; icons at 20 px. Position: bottom right on a desktop, above the bottom tab bar on
a phone.

## Accessibility

- Announced politely to screen readers (`role="status"`); it never takes the focus.
- Its action can be reached by keyboard and stays while focused.
- Nothing important lives only in a toast: the result is also on the page or in the record's history.

## Do and don't

- Do say what was done, with the real values ("12 tasks moved").
- Do offer Undo when the batch can be reverted ([D158](../../../06-decisions/f03-assistant/d158-assistant-undo.md)).
- Don't use a toast for an error the user must fix.
- Don't stack toasts.

## Used in

[S-F4-04 Call](../../../02-functional/f04-meetings/screens/02-record-in-person-or-by-phone/s-f04-04-call.md); and the
confirmation images of the flows that end with a short message.

## Open questions

None.

---

⬅️ [Modal](c-05-modal.md) · ⬆️ [Up](README.md) · ➡️ [Tabs](c-07-tabs.md)
