🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-02 Form field

# 🧩 C-02 Form field

**Status:** 🔄 waiting for the owner

## Purpose

Lets a user enter or change one value, with its label, help and error, on forms, wizards and editable tables.

## Anatomy

```text
Due date *                        <- label, required mark
+--------------------------------+
| [icon] 19/11/2026              |  <- input
+--------------------------------+
(!) The date must be after the order date.   <- error, or help text
```

1. **Label:** above the input, always visible; a required field is marked and says so to screen readers.
2. **Input:** with an optional icon or unit inside.
3. **Help:** one short line under the input (`font-caption`, `color-text-muted`).
4. **Error:** replaces the help, with the (!) icon and the words of the
   [error message pattern](../patterns/error-messages.md).

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-02-form-field-desktop-light.png) | ![Variants and states, dark](../images/c-02-form-field-desktop-dark.png) |

## Variants

One per field type of F2 ([D101](../../../06-decisions/f02-no-code-configuration/d101-custom-field-types.md)): text,
string, number, date, yes or no (a switch or a checkbox), list (a select, or radio buttons up to five choices
(Proposed)), money (with its currency), percentage, duration, link to a record (a search with suggestions), files and
images ([C-12 File upload](c-12-file-upload.md)), computed (read-only), location (address with suggestions), phone
number. A **locked** variant shows a value the user may see but not change, with a lock icon (Proposed: as drawn, on
`color-surface-alt` with a dashed edge).

## States

| State | Look |
|---|---|
| Default | 1 px `color-border-strong` edge (3.98:1, WCAG 1.4.11, [Colours](../../visual-identity/colours.md)) |
| Hover | (Proposed) The edge in `color-text-muted` |
| Focus | 2 px `color-primary` edge |
| Filled | As default, with the value |
| Disabled or read-only | `color-surface-alt` fill and `color-text-muted` text (Proposed) |
| Error | 2 px `color-error` edge and the message under it ([error message pattern](../patterns/error-messages.md)) |
| Loading | (Proposed) A spinner inside, during a lookup such as SIRENE ([S-F1-01 Setup wizard](../../../02-functional/f01-administration/screens/01-guided-setup/s-f01-01-setup-wizard.md)) |

## Tokens

`field-height` (44 px comfortable, 32 px compact), `body-size`, radius 8 px for fields ([Tokens](../tokens.md));
`color-border-strong`, `color-primary`, `color-error`, `color-surface`, `color-surface-alt`, `color-text-muted`;
`font-label`, `font-body`, `font-caption`, `font-code` for codes and IDs
([Typography](../../visual-identity/typography.md)).

## Accessibility

- Every input has a visible label tied to it; placeholders never replace labels.
- Help and error are linked with `aria-describedby`; an invalid field has `aria-invalid`.
- Field errors show as soon as the field is left and again on saving; focus moves to the first faulty field
  ([error message pattern](../patterns/error-messages.md)).
- Text can be enlarged to 200 % without loss ([Typography](../../visual-identity/typography.md)).

## Do and don't

- Do say what is expected in the user's words: "The date must be after the order date"
  ([Tone of voice](../../visual-identity/tone-of-voice.md)).
- Do prefill what SimpleERP knows (SIRENE, a customer's price list).
- Don't blame: never "You entered an invalid date" ([Tone of voice](../../visual-identity/tone-of-voice.md)).
- Don't hide the label inside the input.

## Used in

About 680 screens list it among their components, for example
[S-F1-01 Setup wizard](../../../02-functional/f01-administration/screens/01-guided-setup/s-f01-01-setup-wizard.md),
[S-F9-09 Time off](../../../02-functional/f09-hr-and-projects/screens/03-time/s-f09-09-time-off.md) and
[S-F13-14 Sick leave](../../../02-functional/f13-payroll/screens/04-events/s-f13-14-sick-leave.md).

## Open questions

None.

---

⬅️ [Button](c-01-button.md) · ⬆️ [Up](README.md) · ➡️ [Data table](c-03-data-table.md)
