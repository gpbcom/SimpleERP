🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧵 [Patterns](README.md) ›
🧵 Wizard

# 🧵 Wizard

**Status:** 🔄 waiting for the owner

## Purpose

How a task of several ordered steps is done once, without training: the guided setup is its model
([D54](../../../06-decisions/f01-administration/d54-guided-setup.md)).

## When to use

A task of three to seven steps (Proposed) that must be done in order and is rarely repeated: the guided setup, the
first-run guide (F21), an import ([Import and export pattern](import-export.md)). Not for a form of a single page.

## Anatomy

```text
+------------------------------------------------------------+
| Setup of Acme Bâtiment                       [Save, leave] |
| (v)--(v)--(3)--(4)--(5)--(6)--(7)                          |
| 3. Sites                                                   |
|   ... fields of the step ...                              |
|   Ask the assistant, or let it prefill this step: [AI]     |
|                               [Back]  [Save and continue]  |
+------------------------------------------------------------+
```

A [C-13 Stepper](../components/c-13-stepper.md), the current step's title and fields
([C-02 Form field](../components/c-02-form-field.md)), the AI assistant
([D62](../../../06-decisions/f01-administration/d62-assistant-in-setup.md)), and the buttons Back, Save and continue,
Save and leave, as on
[S-F1-01 Setup wizard](../../../02-functional/f01-administration/screens/01-guided-setup/s-f01-01-setup-wizard.md).

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/wizard-desktop-light.png) | ![Variants and states, dark](../images/wizard-desktop-dark.png) |

## Behaviour

- Each step is saved when the user continues; Back keeps what was saved, as on
  [S-F1-01 Setup wizard](../../../02-functional/f01-administration/screens/01-guided-setup/s-f01-01-setup-wizard.md).
- The wizard can be left and resumed at any time ([D54](../../../06-decisions/f01-administration/d54-guided-setup.md)).
- A step is done once answered; choosing "none" completes it
  ([D59](../../../06-decisions/f01-administration/d59-every-setup-step-required.md)).
- Errors show next to their field and stop the step from continuing ([error message pattern](error-messages.md)).
- The last step shows a checklist, then opens the result, such as the home screen
  ([D59](../../../06-decisions/f01-administration/d59-every-setup-step-required.md)).
- On a phone, a long setup asks to continue on a larger screen, as on
  [S-F1-01 Setup wizard](../../../02-functional/f01-administration/screens/01-guided-setup/s-f01-01-setup-wizard.md).

## Accessibility

- The stepper is a list with the current step marked `aria-current`, as on
  [S-F1-01 Setup wizard](../../../02-functional/f01-administration/screens/01-guided-setup/s-f01-01-setup-wizard.md).
- Moving to a step moves the focus to its title; errors are linked to their field and announced.
- Every action is reachable by keyboard.

## Used in

[S-F1-01 Setup wizard](../../../02-functional/f01-administration/screens/01-guided-setup/s-f01-01-setup-wizard.md);
[S-F21-01 Welcome](../../../02-functional/f21-onboarding-and-modules/screens/01-first-run/s-f21-01-welcome.md), the
first-run guide of F21; and imports ([Import and export pattern](import-export.md)).

---

⬅️ [List detail](list-detail.md) · ⬆️ [Up](README.md) · ➡️ [Approval](approval.md)
