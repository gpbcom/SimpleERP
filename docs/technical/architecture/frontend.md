# Front end

The front ends: framework, design system in code, offline and mobile, accessibility, Playwright tests. Nothing of the
target is built yet.

## Today

[`frontend/backoffice`](../../../frontend/backoffice/README.md) holds the app shell of [D47](../../specs/06-decisions/ux/d47-app-shell.md)
and the navigation of [C-08](../../specs/04-ux/design-system/components/c-08-navigation.md), on Vue 3, Vite, Pinia and
vue-router ([D407](../../specs/06-decisions/technical/d407-front-end.md)): a collapsible sidebar, a top bar, a bottom
tab bar under 768 px, the theme that follows the device with a manual switch, and French and English. Its own image
follows the layout of [D438](../../specs/06-decisions/technical/d438-repository-layout.md), and it is not built yet.
The back office has Playwright tests in `frontend/backoffice/e2e/`, run against the real images, not a development
server ([Playwright](../delivery/tests-and-traceability.md#playwright)). The business screens and the assistant panel come
later, with the screens of the feature phases.

[`frontend/packages/config`](../../../frontend/packages/config/)
(`@simpleerp/config`) holds the shared settings that every front end extends: the ESLint flat config
(`@simpleerp/config/eslint`) and the strict TypeScript settings (`@simpleerp/config/tsconfig`).
[`frontend/packages/i18n`](../../../frontend/packages/i18n/README.md) (`@simpleerp/i18n`) holds the French and English
message catalogues of [D21](../../specs/06-decisions/foundations/d21-languages.md), the formatting of dates, numbers and
money per locale, with money as an exact decimal ([REQ-T10-03](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md)),
a language switch without reloading, and a check that fails CI when a key is missing in one language
([REQ-T10-01](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-01-translation-catalogues.md),
review workflow in P2). It is built on Vue 3 and the platform `Intl` API ([D407](../../specs/06-decisions/technical/d407-front-end.md)).

## Target design (specified in GH-2, not built yet)

**Framework (D407).** Vue 3 with TypeScript and Vite, Pinia for state, a component library built on the design system's
tokens ([UX](../../specs/04-ux/README.md)).

**Front ends.** One back-office web app whose menus follow the modules switched on (F21) and the user's roles; the
customer and supplier portals and the public website (F18) as separate front ends; one installable mobile app for tills,
waiters, field workers, carers and drivers, offline-first (TC-06). Each has its own image and Playwright tests against
the real images (`AGENT.md`, TKT-21).

**Mobile.** A progressive web app first, wrapped in a native shell (for example Capacitor) only where hardware needs it:
card terminals, receipt printers, scales, barcode scanners.

**Extensions.** Plugins and generated features declare their screens with the design system's components (forms, tables,
dashboards), rendered by the app; custom widgets run in a sandboxed iframe; the assistant panel is part of the shell on
every screen.

Decided in [D407](../../specs/06-decisions/technical/d407-front-end.md).

Last reviewed: 2026-11-28 (T0.22)
