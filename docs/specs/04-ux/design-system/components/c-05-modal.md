🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-05 Modal

# 🧩 C-05 Modal

**Status:** ✅ specified

## Purpose

Asks for a decision or a short task without leaving the page: a confirmation, a refusal by a rule, a short form.

## Anatomy

```text
+------------------------------------------------+
| (i) Deactivate Luc Bernard                 [x] |  <- icon, title, close
|------------------------------------------------|
| Hand over to   [ Marie Dupont v ]              |  <- content
|                                                |
|          [Cancel]  [Hand over and deactivate]  |  <- actions
+------------------------------------------------+
```

The page behind is dimmed by a veil (`color-text` at 45 %, as drawn).

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-05-modal-desktop-light.png) | ![Variants and states, dark](../images/c-05-modal-desktop-dark.png) |

## Variants

- **Confirmation:** a question and two buttons; a destructive action uses the Danger button
  ([C-01 Button](c-01-button.md)).
- **Error:** a refusal by a rule, as in the [error message pattern](../patterns/error-messages.md), with its support
  reference.
- **Form:** a short form of a few fields, as on
  [S-F1-05 Offboarding](../../../02-functional/f01-administration/screens/03-user-lifecycle/s-f01-05-offboarding.md).
- **Phone:** full width from the bottom of the screen, with the buttons stacked, the primary first.

## States

Opening (a 250 ms panel motion, instant with reduced motion, [Motion](../../visual-identity/motion.md)), open,
submitting (the primary button loading), error (the message inside the dialog), closed.

## Tokens

`color-surface`, `elevation-2` for panels and modals, radius 12 px for panels ([Tokens](../tokens.md)); title in
`font-h3`; `color-error` icon for errors and `color-primary` icon for information; width 520 px on a desktop, at most
the 8 middle columns of the [Layout grid](../layout-grid.md).

## Accessibility

- `role="dialog"` (or `alertdialog` for an error) with `aria-modal`, named by its title.
- Focus moves to the first field, or to the dialog; it stays inside while the modal is open and returns to
  what opened it on closing.
- Escape cancels, as on
  [S-F1-05 Offboarding](../../../02-functional/f01-administration/screens/03-user-lifecycle/s-f01-05-offboarding.md);
  the close button has an accessible name.

## Do and don't

- Do keep one decision per modal and say its effect on the button.
- Do use it for refusals by a rule ([error message pattern](../patterns/error-messages.md)).
- Don't open a modal from a modal.
- Don't put a long form in a modal: use a page or the [Wizard pattern](../patterns/wizard.md).

## Used in

[S-F1-02 Sites](../../../02-functional/f01-administration/screens/02-manage-sites/s-f01-02-sites.md),
[S-F1-04 User page](../../../02-functional/f01-administration/screens/03-user-lifecycle/s-f01-04-user-page.md),
[S-F1-05 Offboarding](../../../02-functional/f01-administration/screens/03-user-lifecycle/s-f01-05-offboarding.md),
[S-F1-07 Connections](../../../02-functional/f01-administration/screens/05-connect-an-external-tool/s-f01-07-connections.md),
[S-F3-04 Show me overlay](../../../02-functional/f03-assistant/screens/05-find-and-get-guided/s-f03-04-show-me-overlay.md),
[S-F3-10 Share a conversation](../../../02-functional/f03-assistant/screens/08-manage-and-share-conversations/s-f03-10-share-a-conversation.md),
[S-F4-03 Phone recorder](../../../02-functional/f04-meetings/screens/02-record-in-person-or-by-phone/s-f04-03-phone-recorder.md);
and every error image that shows a dialog.

## Open questions

None.

---

⬅️ [Card](c-04-card.md) · ⬆️ [Up](README.md) · ➡️ [Toast](c-06-toast.md)
