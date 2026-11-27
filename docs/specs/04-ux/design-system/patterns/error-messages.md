🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧵 [Patterns](README.md) ›
🧵 Error messages

# 🧵 Error messages

**Status:** 🔄 waiting for the owner

## Purpose

How every error is shown to users, on every screen, so that a non-technical user understands it and knows what to do.
See [D122](../../../06-decisions/ux/d122-error-message-standard.md).

## When to use

Every refusal and failure: a form field that is wrong, an action refused by a rule, a missing permission, an outside
service down, a lost network.

## Anatomy

```text
+--------------------------------------------+
| (!) This site still has stock              |
|                                            |
| The Lyon yard holds 40 items and 3         |
| employees. Move them before closing it.    |
|                                            |
| [See what is left]   [Cancel]              |
|                        ref. SITE-CLOSE-01  |
+--------------------------------------------+
```

1. **Title:** what happened, in plain words, as a short sentence ("This site still has stock").
2. **Why:** one sentence with the real values ("The Lyon yard holds 40 items and 3 employees.").
3. **What to do:** the action that fixes it, as the main button ("See what is left"), and a way out ("Cancel").
4. **Faulty field:** highlighted, with the message next to it, when the error is about a field.
5. **Support reference:** a small code at the bottom ("ref. SITE-CLOSE-01"), for support only.

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/error-messages-desktop-light.png) | ![Variants and states, dark](../images/error-messages-desktop-dark.png) |

## Behaviour

- Field errors show next to the field, as soon as the field is left, and again on saving.
- Rule refusals show in a dialog or a banner at the top of the page.
- (Proposed) Outside services down or no network: a banner that says what still works ("Your time is saved and will
  sync").
- Never a technical code, a stack trace or English jargon in the message itself; never blame ("You entered...").

## Accessibility

- The error is announced to screen readers; focus moves to the first faulty field or to the dialog.
- The error colour always comes with the (!) icon and the words (D46).
- The message is linked to its field (`aria-describedby`).

## Used in

Every error image of the flows' mockups (D120), and every screen's error state.

---

⬆️ [Up](README.md) · ➡️ [Aggregated list view](aggregated-list-view.md)
