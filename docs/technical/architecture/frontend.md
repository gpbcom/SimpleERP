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

## Error messages on screen

How a refusal of the platform reaches the screen, following [D122](../../specs/06-decisions/ux/d122-error-message-standard.md)
and the [error messages pattern](../../specs/04-ux/design-system/patterns/error-messages.md).

1. **The platform answers.** A refused call comes back as `application/problem+json` with a D122 code, as
   [REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md) requires
   ([API](../../technical/interfaces/api.md) describes the contract).
2. **The typed client throws.** [`frontend/packages/api-client/src/problem/api-problem-error.ts`](../../../frontend/packages/api-client/src/problem/api-problem-error.ts)
   defines `ApiProblemError`, which carries that code.
3. **The app turns it into a refusal.** `platformClient.ts` (the client of the back office, whose test is
   [`platformClient.test.ts`](../../../frontend/backoffice/tests/api/platformClient.test.ts))
   maps the error to a `Refusal` ([`Refusal.ts`](../../../frontend/backoffice/src/errors/Refusal.ts),
   built by [`toRefusal.ts`](../../../frontend/backoffice/src/errors/toRefusal.ts)). The keys and the reference of the
   refusal come from `errorCatalog` ([`errorCatalog.ts`](../../../frontend/packages/i18n/src/errors/errorCatalog.ts)),
   which a test keeps in step with the catalogue of T0.04. The refusal goes into the Pinia error store
   ([`errors.ts`](../../../frontend/backoffice/src/stores/errors.ts)).
4. **The shell shows it.** The `ErrorOutlet` of the shell (its test is
   [`ErrorOutlet.test.ts`](../../../frontend/backoffice/tests/errors/ErrorOutlet.test.ts))
   renders the refusal with the ui components [`ErrorDialog.vue`](../../../frontend/packages/ui/src/errors/ErrorDialog.vue)
   or [`ErrorBanner.vue`](../../../frontend/packages/ui/src/errors/ErrorBanner.vue), translated in the current language.
5. **A field refusal goes to its field.** [`useFieldErrors.ts`](../../../frontend/backoffice/src/errors/useFieldErrors.ts)
   gives a form the messages of its fields, next to the field that is refused.

**Which presentation is used when.** A **dialog** answers a user's action, such as saving or deleting. A **banner**
reports a call the user did not start, such as a background refresh. A field refusal is shown **next to the field**.
These are the rules of the [error messages pattern](../../specs/04-ux/design-system/patterns/error-messages.md) and
[D46](../../specs/06-decisions/ux/d46-accessibility-standard.md) (messages announced to assistive technology).

**Where the texts live.** The French and English texts are in the catalogues
[`fr/errors.json`](../../../frontend/packages/i18n/src/catalogues/fr/errors.json) and
[`en/errors.json`](../../../frontend/packages/i18n/src/catalogues/en/errors.json) of `@simpleerp/i18n`, under the keys of
the error catalogues of the back end (`error_codes.yaml` of the models and of the platform, and `refusal_codes.yaml` of
the context library), in the languages of [D21](../../specs/06-decisions/foundations/d21-languages.md). The package
exports them as `errorCatalogs`, and the error outlet of the back office translates with them first, so a refusal
never shows a raw key.

**The store keeps keys, never text.** The error store holds the keys and the reference of a refusal, not the translated
message. So a language switch re-renders the message in the new language, with no refusal to replay.

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

Last reviewed: 2026-11-28 (T0.23)
