# @simpleerp/ui

The component library of the SimpleERP front ends: six base components, plus the icon and the spinner they are built
on. Every colour, space, radius, elevation and type style comes from the design tokens of
[`@simpleerp/tokens`](../tokens/README.md), so a component never holds a value of its own. The components follow the
design system of the [components](../../../docs/specs/04-ux/design-system/components/README.md) pages and the
[design tokens](../../../docs/specs/04-ux/design-system/tokens.md) page, and the front-end decision
[D407](../../../docs/specs/06-decisions/technical/d407-front-end.md) (Vue 3, TypeScript, Vite).

## What the package holds

| Component | Specification | Use |
| --- | --- | --- |
| `UiButton` | [C-01](../../../docs/specs/04-ux/design-system/components/c-01-button.md) | An action, or a link that looks like one |
| `UiFormField` | [C-02](../../../docs/specs/04-ux/design-system/components/c-02-form-field.md) | A labelled input with its help, error, unit and lock |
| `UiCard` | [C-04](../../../docs/specs/04-ux/design-system/components/c-04-card.md) | A titled block, a dashboard figure, or a selectable choice |
| `UiModal` | [C-05](../../../docs/specs/04-ux/design-system/components/c-05-modal.md) | A dialog that holds the focus until it is closed |
| `UiToast` | [C-06](../../../docs/specs/04-ux/design-system/components/c-06-toast.md) | A short message that closes by itself, unless it offers an action |
| `UiNavItem` | [C-08](../../../docs/specs/04-ux/design-system/components/c-08-navigation.md) | A link of the sidebar, with its current-page state and badge |
| `UiIcon` | [D45](../../../docs/specs/06-decisions/ux/d45-lucide-icons.md) | One Lucide icon, at 16, 20 or 24 px |
| `UiSpinner` | [C-01](../../../docs/specs/04-ux/design-system/components/c-01-button.md), [C-02](../../../docs/specs/04-ux/design-system/components/c-02-form-field.md) | A turning icon for a busy action or field |

The accessibility rules that the components meet are in the [accessibility](../../../docs/specs/04-ux/design-system/accessibility.md)
page and [D46](../../../docs/specs/06-decisions/ux/d46-accessibility-standard.md).

## How to import them

The package entry point is `@simpleerp/ui` (`src/index.ts`), which is meant to export every component above by name:

```ts
import "@simpleerp/ui/style.css";
import { UiButton, UiFormField } from "@simpleerp/ui";
```

The stylesheet is the built `dist/ui.css`. The components use the tokens' CSS variables, so the front end must also
import the tokens stylesheet once, at its entry point, as the [tokens package](../tokens/README.md) describes.

## Props, slots and events

Props are read from `src/components/*.vue`. A prop without a default is required. Every prop has a description in its
source file.

### UiButton

- **Props:** `label` (required, also the accessible name when `iconOnly` is set); `variant` (`primary`, `secondary`,
  `danger` or `ghost`, default `primary`); `icon` (a Lucide component); `iconOnly` (default `false`); `type` (`button`,
  `submit` or `reset`, default `button`); `href` (renders an `<a>` instead of a `<button>`); `loading` (default `false`);
  `disabled` (default `false`); `disabledReason` (the tooltip of a disabled button); `block` (full width on phones).
- **Events:** `click` (the `MouseEvent`). A loading or disabled button does not emit it.
- **Slots:** none.

### UiFormField

- **Props:** `label` (required, always shown above the input); `modelValue` (`string | number`, default `''`); `type`
  (`text`, `number`, `date`, `email`, `tel` or `url`, default `text`); `id` (generated when absent); `required`,
  `disabled`, `readonly`, `locked` (a value the user sees but cannot change, drawn with a lock), `loading` (default
  `false`); `help`; `error` (replaces the help); `unit`; `placeholder`; `icon`.
- **Events:** `update:modelValue` (the new `string`), `blur` (the `FocusEvent`).
- **Slots:** none.

### UiCard

- **Props:** `title` (required, in a heading); `headingLevel` (2 to 6, default 3); `href` (makes the title the only
  link); `selectable` (`radio` or `checkbox`); `selected`; `name` and `value` (of the input of a selectable card);
  `figure` (a dashboard figure); `change` (the line under the figure); `loading` (skeleton lines, busy card).
- **Events:** `update:selected` (the new `boolean`), for a selectable card.
- **Slots:** the default slot holds the content, and `actions` holds the buttons at the foot of the card.

### UiModal

- **Props:** `open` (required); `title` (required, names the dialog); `variant` (`confirmation`, `form` or `error`,
  default `confirmation`; `error` is an `alertdialog`); `closeLabel` (required, the accessible name of the close button).
- **Events:** `close`, on the close button and on Escape.
- **Slots:** the default slot holds the content, and `actions` the buttons of the footer.

### UiToast

- **Props:** `message` (required, one sentence); `kind` (`success` or `info`, default `success`); `actionLabel` (such as
  Undo: with an action the toast never closes by itself); `closeLabel` (required); `durationMs` (default `6000`).
- **Events:** `action`, on the action button; `close`, when the close button is used or the time runs out.
- **Slots:** none.

### UiNavItem

- **Props:** `href` and `label` (both required; the label stays as hidden text when `collapsed`); `icon`; `current`
  (sets `aria-current="page"`); `badge` (a count, part of the accessible name); `collapsed` (default `false`).
- **Events:** none, it is a link.
- **Slots:** none.

### UiIcon and UiSpinner

- **Props:** `icon` (required, for `UiIcon`) and `size` (16, 20 or 24, default 20); `label` (the accessible name; without
  it the icon is hidden from screen readers).
- **Events:** none. **Slots:** none.

## Light and dark

The components only use the tokens' CSS variables, so they follow the theme that the tokens set
([D43](../../../docs/specs/06-decisions/ux/d43-light-and-dark.md)). A `data-theme="light"` or `data-theme="dark"`
attribute on the root element chooses the theme. Without it, the device setting (`prefers-color-scheme`) applies. A
component never tests the theme itself.

## Icons

The icons are the Lucide icons, bundled from `lucide-vue-next` into the package build
([D45](../../../docs/specs/06-decisions/ux/d45-lucide-icons.md)). Nothing is fetched from a third party at run time.

## Commands

Run these from the root of the repository:

```bash
pnpm --filter ./frontend/packages/ui run lint
pnpm --filter ./frontend/packages/ui run typecheck
pnpm --filter ./frontend/packages/ui run test
pnpm --filter ./frontend/packages/ui run build
```

- `lint` runs ESLint on the package.
- `typecheck` runs `vue-tsc` without emitting files.
- `test` runs the Vitest suites of `tests/` in jsdom.
- `build` writes `dist/ui.js` and `dist/ui.css`.

**Colour contrast is not tested here.** jsdom cannot compute colours, so the axe runs of the component tests disable
the `color-contrast` rule. Contrast is checked by the contrast test of the [tokens package](../tokens/README.md), and by
the Playwright axe runs of the screens ([accessibility](../../../docs/specs/04-ux/design-system/accessibility.md)).
