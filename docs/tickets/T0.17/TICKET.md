# T0.17: Back-office app shell

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.17](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S03](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03), 18 to 29 Jan 2027: the contracts and the shell (what can be shown: the shell in light and dark, in French and English; a removed field fails CI)
- **Epic:** [E0.6 Back-office foundation](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): tokens, base components, i18n, the app shell, the error pattern on screen and the Playwright scaffold

## What it delivers

- `frontend/backoffice` as a Vue 3, Vite, Pinia and router app, as [Front end](../../technical/architecture/frontend.md#target-design-specified-in-gh-2-not-built-yet) (framework of D407).
- The app shell: the collapsible sidebar with the symbol (`docs/assets/symbol.svg`), and the top bar with places for search, the assistant, notifications, the site switcher and the user menu, as [C-08 Navigation](../../specs/04-ux/design-system/components/c-08-navigation.md).
- The bottom tab bar on phones, as [Responsive](../../specs/04-ux/design-system/responsive.md).
- Light and dark following the device, with a manual switch, as [D43](../../specs/06-decisions/ux/d43-light-and-dark.md).
- The "skip to content" link and `aria-current`, as [D46](../../specs/06-decisions/ux/d46-accessibility-standard.md).
- The back-office's own image, one image per front end, as [D438](../../specs/06-decisions/technical/d438-repository-layout.md).

## Features, use cases and business rules

- [📜 D407 Front end](../../specs/06-decisions/technical/d407-front-end.md)
- [📜 D47 App shell](../../specs/06-decisions/ux/d47-app-shell.md)
- [📜 D49 Assistant side panel](../../specs/06-decisions/ux/d49-assistant-side-panel.md)
- [📜 D43 Light and dark modes](../../specs/06-decisions/ux/d43-light-and-dark.md)
- [📜 D46 Accessibility standard](../../specs/06-decisions/ux/d46-accessibility-standard.md)
- [📜 D21 Languages](../../specs/06-decisions/foundations/d21-languages.md)
- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md)

## Technical pages it builds on

- [🏗️ Front end](../../technical/architecture/frontend.md): Vue 3, TypeScript, Vite and Pinia, one back-office web app with its own image and Playwright tests.
- [🏗️ Repository layout](../../technical/architecture/repository-layout.md): where `frontend/backoffice` sits in the mono-repo.

## Screens touched

- ➖ No screen: the phase page says "The back-office shell has no business screen", and no screen page of `docs/specs/02-functional/` specifies the shell, which D47 and C-08 Navigation specify (linked above). The shell's own screens are listed for the Playwright tests of T0.22.

## Budgets touched

- [♿ Accessibility](../../specs/05-non-functional/accessibility.md#requirement): WCAG 2.2 level AA, with the skip link and `aria-current` of the shell; the page's measures are still to be specified.
- [🌍 Localisation](../../specs/05-non-functional/localisation.md): the shell renders in French and English.

## Acceptance criteria

1. **Given** the back-office app, **when** its Vitest tests run, **then** they pass (done when of T0.17).
2. **Given** the shell, **when** it renders in light and in dark, and in French and in English, **then** it displays correctly in each (D43, D21).
3. **Given** the desktop sidebar, **when** the user collapses it, **then** it shows icons only (D47, C-08).
4. **Given** a phone width, **when** the shell renders, **then** a bottom tab bar replaces the sidebar (D47, Responsive).
5. **Given** the top bar, **when** it renders, **then** it has places for search, the assistant, notifications, the site switcher and the user menu (D47, D49).
6. **Given** the shell, **when** a keyboard user starts to tab, **then** the "skip to content" link comes first and the current page carries `aria-current` (D46, C-08).
7. **Given** the device's colour scheme, **when** the app loads, **then** the theme follows it, and a manual switch overrides it (D43).
8. **Given** CI, **when** the image of the back-office is built, **then** it builds (D438).

## Out of scope

- The Playwright tests of the shell's screens, see [T0.22](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The error message component, see [T0.23](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The internationalisation package, see [T0.16](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The base UI components, see [T0.15](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02).
- Business screens: none in P0, see [P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md).

## Assumptions

- No screen page specifies the shell, so the ticket lists no screen; the shell's states come from D47 and C-08.
- The roadmap row has no anchor of its own, so the sprint anchor `#s03` stands for it.
- The shell uses the tokens (T0.07), the base components (T0.15) and the i18n package (T0.16) when they exist; the roadmap does not list them as prerequisites here, so the start rule's graph decides.
- The accessibility page has no measures yet, so the ticket keeps to the standard of D46.
