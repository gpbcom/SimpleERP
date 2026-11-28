# Back office

The back-office web app, built with Vue 3, TypeScript, Vite, Pinia and vue-router
([D407](../../docs/specs/06-decisions/technical/d407-front-end.md)). It holds the app shell of
[D47](../../docs/specs/06-decisions/ux/d47-app-shell.md) and the navigation component
[C-08](../../docs/specs/04-ux/design-system/components/c-08-navigation.md). The business screens, the assistant panel
([D49](../../docs/specs/06-decisions/ux/d49-assistant-side-panel.md)) and the Playwright tests come in later tickets.

See [D438](../../docs/specs/06-decisions/technical/d438-repository-layout.md) and the
[Repository layout](../../docs/technical/architecture/repository-layout.md) page.

## The shell

The shell is the frame every screen sits in ([D47](../../docs/specs/06-decisions/ux/d47-app-shell.md)).

- **Sidebar.** A collapsible sidebar with the SimpleERP symbol, the navigation items and a button that collapses it to
  icons. The current page carries `aria-current="page"`. Items not yet built are shown disabled (`aria-disabled="true"`).
- **Top bar.** The search field, the assistant, the notifications, the site switcher, the user menu and the theme
  switch. Only the search and the theme switch are live in this ticket; the other places are placeholders marked
  `aria-disabled="true"`.
- **Bottom tab bar.** Replaces the sidebar below 768 px.
- **Skip link.** The first focusable element of the page, which moves the keyboard focus to the main content.
- **Theme.** The theme follows the device (`prefers-color-scheme`). A manual choice of light or dark is stored in
  `localStorage` under `simpleerp.theme`, and removed when the person chooses to follow the device again. The choice is
  written as `data-theme` on `<html>`, as [D43](../../docs/specs/06-decisions/ux/d43-light-and-dark.md) requires.
- **Languages.** French and English ([D21](../../docs/specs/06-decisions/foundations/d21-languages.md)). The active
  locale is written to `<html lang>`, and a change of language does not reload the page.
- **Accessibility.** The shell follows [D46](../../docs/specs/06-decisions/ux/d46-accessibility-standard.md) and the
  [responsive](../../docs/specs/04-ux/design-system/responsive.md) rules.

## The folders

| Folder | Holds |
| --- | --- |
| `src/app/` | Creation of the Vue application, with its plugins (router, Pinia, i18n) |
| `src/router/` | The routes and the router |
| `src/navigation/` | The navigation items, shared by the sidebar and the tab bar |
| `src/stores/` | The Pinia stores: the layout (sidebar state) and the theme |
| `src/shell/` | The shell components: the app shell, sidebar, top bar, tab bar, theme switch and skip link |
| `src/i18n/` | The i18n setup and the choice of the initial locale |
| `src/locales/` | The French and English message catalogues |
| `src/views/` | The page views |
| `src/styles/` | The base stylesheet |
| `src/assets/` | Static assets, such as the symbol |
| `tests/` | The Vitest unit tests, run in jsdom |
| `e2e/` | The Playwright tests, from ticket T0.22 on, against the real images |

## Commands

Run them from the root of the repository, with pnpm (Node 22):

```bash
pnpm --filter ./frontend/backoffice run dev
pnpm --filter ./frontend/backoffice run build
pnpm --filter ./frontend/backoffice run lint
pnpm --filter ./frontend/backoffice run typecheck
pnpm --filter ./frontend/backoffice run test
```

- `dev` starts the Vite development server. It is for building the app, not for its tests.
- `build` type-checks the project and builds it for production.
- `lint` runs ESLint, `typecheck` runs `vue-tsc`, and `test` runs the Vitest unit tests once.

## End-to-end tests

The Playwright tests of `e2e/` run against the real images started by `compose.e2e.yaml`, never a development server.
Their projects (four themes and languages, plus the phone size), their `@smoke` tag, the accessibility check and the
reports are described in the [Playwright section](../../docs/technical/delivery/tests-and-traceability.md#playwright)
of the tests and traceability page.

## The image

The image of the back office is one of the images of [D438](../../docs/specs/06-decisions/technical/d438-repository-layout.md),
built from a multi-stage `Dockerfile` in this folder, with the repository root as build context. The `Dockerfile` is not
part of this ticket, so the image is not built yet. Once it exists, it is built with:

```bash
docker build -f frontend/backoffice/Dockerfile .
```
