# T0.15: Base UI components

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.15](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S02](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02), 4 to 15 January 2027: the service kit and the first service
- **Epic:** [E0.6 Back-office foundation](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): tokens, base components, i18n, the app shell, the error pattern on screen and the Playwright scaffold

## What it delivers

- `frontend/packages/ui`, built on the design tokens, with the six base components: button, form field, navigation item, toast, modal and card, as [Front end](../../technical/architecture/frontend.md) ("a component library built on the design system's tokens").
- Every component in light and dark, as [D43](../../specs/06-decisions/ux/d43-light-and-dark.md) asks.
- Every component reachable by keyboard with a visible focus, as [D46](../../specs/06-decisions/ux/d46-accessibility-standard.md) and [Accessibility](../../specs/04-ux/design-system/accessibility.md) ask.
- Lucide icons served by the package itself, as [D45](../../specs/06-decisions/ux/d45-lucide-icons.md) decides ("Lucide (ISC licence), served by SimpleERP itself").
- Vitest component tests in both themes and an automated accessibility check on each component.

## Features, use cases and business rules

- [📜 D407 Front end](../../specs/06-decisions/technical/d407-front-end.md): Vue 3 with TypeScript, the component library on the tokens.
- [📜 D45 Lucide icons](../../specs/06-decisions/ux/d45-lucide-icons.md): the icon set, served by SimpleERP.
- [📜 D46 Accessibility standard](../../specs/06-decisions/ux/d46-accessibility-standard.md): WCAG 2.2 AA and RGAA 4.1.
- [📜 D43 Light and dark modes](../../specs/06-decisions/ux/d43-light-and-dark.md): both themes.
- [🎟️ Tokens](../../specs/04-ux/design-system/tokens.md): the colour, spacing, density, typography, radius and elevation tokens the components use, built by T0.07.
- [♿ Accessibility](../../specs/04-ux/design-system/accessibility.md): axe-core checks and keyboard use.
- [🧩 C-01 Button](../../specs/04-ux/design-system/components/c-01-button.md): variants, states, tokens and accessibility of the button.
- [🧩 C-02 Form field](../../specs/04-ux/design-system/components/c-02-form-field.md): the form field.
- [🧩 C-04 Card](../../specs/04-ux/design-system/components/c-04-card.md): the card.
- [🧩 C-05 Modal](../../specs/04-ux/design-system/components/c-05-modal.md): the modal.
- [🧩 C-06 Toast](../../specs/04-ux/design-system/components/c-06-toast.md): the toast, announced with `role="status"`.
- [🧩 C-08 Navigation](../../specs/04-ux/design-system/components/c-08-navigation.md): the navigation item.

## Technical pages it builds on

- [🏗️ Front end](../../technical/architecture/frontend.md): Vue 3, TypeScript and Vite, with a component library built on the design system's tokens.

## Screens touched

- ➖ No screen: `frontend/packages/ui` is a shared component package, and the roadmap row lists no screen. The screens that use the components come with the app shell (T0.17) and the error messages (T0.23).

## Budgets touched

- [♿ Accessibility](../../specs/05-non-functional/accessibility.md#measures): WCAG 2.2 level AA; the page's measures are still to be specified, so the roadmap's check (no automated violation on each component) is the measure kept.

## Acceptance criteria

1. **Given** the components button, form field, navigation item, toast, modal and card, **when** the Vitest component tests run, **then** they pass in the light and in the dark theme. ([T0.15](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02), [D43](../../specs/06-decisions/ux/d43-light-and-dark.md))
2. **Given** each component rendered, **when** the automated accessibility check runs, **then** it finds no violation. ([Accessibility](../../specs/04-ux/design-system/accessibility.md), [D46](../../specs/06-decisions/ux/d46-accessibility-standard.md))
3. **Given** each interactive component, **when** it is used with the keyboard only, **then** it is reachable and its focus is visible. ([C-01 Button](../../specs/04-ux/design-system/components/c-01-button.md), [D46](../../specs/06-decisions/ux/d46-accessibility-standard.md))
4. **Given** a component with an icon, **when** it is built, **then** the Lucide icon comes from the package itself and nothing is fetched from a third party. ([D45](../../specs/06-decisions/ux/d45-lucide-icons.md))
5. **Given** the components, **when** their styles are read, **then** colours, spacing, radius and elevation come from the tokens package. ([Tokens](../../specs/04-ux/design-system/tokens.md))
6. **Given** a toast without an action, **when** it is shown, **then** it is announced politely (`role="status"`) and never takes the focus. ([C-06 Toast](../../specs/04-ux/design-system/components/c-06-toast.md))

## Out of scope

- The internationalisation base, see [T0.16](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The back-office app shell and its navigation, see [T0.17](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The Playwright scaffold, see [T0.22](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The error message component, see [T0.23](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The other components of the design system (data table, tabs and the rest), which the roadmap row does not list.

## Assumptions

- The roadmap names no use case, screen, business rule or entity for this ticket; the component pages of the design system settle what each component does.
- "Navigation item" is taken as the item of [C-08 Navigation](../../specs/04-ux/design-system/components/c-08-navigation.md) alone, not the whole sidebar, which T0.17 builds.
- The tokens package of T0.07 is assumed available; the ticket graph is the authority on that prerequisite.
- The accessibility check tool is not named in the roadmap row; the design system names axe-core for Playwright, and the same tool is assumed for the component tests.
- The Accessibility budget page has no measures yet, so none is stated beyond the roadmap row.
