# T0.07: Design tokens package

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.07](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S01](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01), 7 to 18 December 2026: The layout, its rules and the first shared code
- **Epic:** [E0.6 Back-office foundation](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): Tokens, base components, i18n, the app shell, the error pattern on screen and the Playwright scaffold

## What it delivers

- The colour, spacing, density, typography, radius and elevation tokens of [Tokens](../../specs/04-ux/design-system/tokens.md), generated from [Colours](../../specs/04-ux/visual-identity/colours.md) and [Typography](../../specs/04-ux/visual-identity/typography.md) into CSS variables and a TypeScript module, in `frontend/packages/tokens`.
- A light and a dark set of values for every colour token, following [📜 D41 Indigo primary colour](../../specs/06-decisions/ux/d41-indigo-primary.md) and [📜 D43 Light and dark modes](../../specs/06-decisions/ux/d43-light-and-dark.md).
- The comfortable and compact density values (`row-height`, `cell-padding`, `field-height`, `body-size`) of [📜 D42 Density per role](../../specs/06-decisions/ux/d42-density-per-role.md).
- The three typefaces (Plus Jakarta Sans, Inter, JetBrains Mono) served by the package itself, with no call to a third party, as [📜 D44 Typefaces](../../specs/06-decisions/ux/d44-typefaces.md) decides.
- A test that every text colour pair meets the contrast of [Colours](../../specs/04-ux/visual-identity/colours.md), as [📜 D46 Accessibility standard](../../specs/06-decisions/ux/d46-accessibility-standard.md) requires.
- The package sits at `frontend/packages/tokens`, a path of [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md), built with Vue 3, TypeScript and Vite tooling as [📜 D407 Front end](../../specs/06-decisions/technical/d407-front-end.md) decides.

## Features, use cases and business rules

- The roadmap names no use case, business rule, entity, flow or requirement for this ticket. It builds on these decisions:
  - [📜 D41 Indigo primary colour](../../specs/06-decisions/ux/d41-indigo-primary.md): "Indigo: primary #4B4FC9, accent #F2B134, success #2E7D32, error #C62828".
  - [📜 D42 Density per role](../../specs/06-decisions/ux/d42-density-per-role.md): each role has a default density, compact or comfortable, and each user can override it.
  - [📜 D43 Light and dark modes](../../specs/06-decisions/ux/d43-light-and-dark.md): "Light and dark themes, following the device's setting, with a manual switch per user. Both meet the contrast rules."
  - [📜 D44 Typefaces](../../specs/06-decisions/ux/d44-typefaces.md): Plus Jakarta Sans for headings, Inter for body, JetBrains Mono for codes, "all served by SimpleERP itself (no call to Google Fonts)".
  - [📜 D46 Accessibility standard](../../specs/06-decisions/ux/d46-accessibility-standard.md): text and icons meet WCAG 2.2 AA.
  - [📜 D407 Front end](../../specs/06-decisions/technical/d407-front-end.md): the components are built on the design system's tokens.
  - [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md): the front-end packages live under `frontend/packages/<pkg>`.

## Technical pages it builds on

- [🏗️ Front end](../../technical/architecture/frontend.md): "a component library built on the design system's tokens", Vue 3 with TypeScript and Vite.
- [🏗️ Repository layout](../../technical/architecture/repository-layout.md): the place of `frontend/packages/` in the pnpm workspace.
- [🏗️ Supply chain and licences](../../technical/security/supply-chain-and-licences.md): dependencies pinned in the lock, licences compatible with AGPL-3.0, as the P0 page lists it.
- [🏗️ Tests and traceability](../../technical/delivery/tests-and-traceability.md): the way the package's tests are written and kept.

## Screens touched

- ➖ No screen: the package holds design tokens and fonts only, and builds no screen, as the back-office shell of T0.17 comes later.

## Budgets touched

- [♿ Accessibility](../../specs/05-non-functional/accessibility.md#requirement): WCAG 2.2 level AA; every text colour pair of the tokens meets the contrast ratios of the Colours page in light and dark. The page's measures are still to be specified.

## Acceptance criteria

1. **Given** the token source, **when** a value in it is changed and the package is built, **then** the CSS variables and the TypeScript module carry the new value. ([📜 D41](../../specs/06-decisions/ux/d41-indigo-primary.md), [Tokens](../../specs/04-ux/design-system/tokens.md))
2. **Given** the generated tokens, **when** every text colour pair is tested in light and in dark, **then** each meets the contrast of [Colours](../../specs/04-ux/visual-identity/colours.md). ([📜 D46](../../specs/06-decisions/ux/d46-accessibility-standard.md), [📜 D43](../../specs/06-decisions/ux/d43-light-and-dark.md))
3. **Given** the built package, **when** its output and fonts are inspected, **then** the three typefaces are served by the package and no font is fetched from a third party. ([📜 D44](../../specs/06-decisions/ux/d44-typefaces.md))
4. **Given** the built package, **when** it is read, **then** it holds the colour, spacing, density (comfortable and compact), typography, radius and elevation tokens of [Tokens](../../specs/04-ux/design-system/tokens.md), as CSS variables and as a TypeScript module, in light and dark. ([📜 D42](../../specs/06-decisions/ux/d42-density-per-role.md), [📜 D43](../../specs/06-decisions/ux/d43-light-and-dark.md))

## Out of scope

- The base UI components built on the tokens, see [T0.15](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02).
- The back-office app shell and its theme switch, see [T0.17](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The internationalisation base, see [T0.16](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).

## Assumptions

- The roadmap row says "the three typefaces served by the package itself": the font files are taken to be packaged in `frontend/packages/tokens`, the package folder name being Claude's name confirmed by the owner (D572), as the phase page states.
- The ticket graph gives T0.01 (mono-repo folders and workspaces) as its prerequisite; it is taken to provide the pnpm workspace this package joins.
- The format of the token source and the generator tool are not specified; the most conservative choice is a plain data file read by a small build script.
- The "Accessibility" budget page has no measures yet ("To be specified"); only its requirement (WCAG 2.2 AA) and the contrast ratios of the Colours page are used.
