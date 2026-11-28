# T0.23: Error messages on screen

**Status:** ✅ Done · **Ticket:** [TICKET.md](TICKET.md) · **Choices and trade-offs:** [IMPLEMENTATION.md](IMPLEMENTATION.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🔭 What it does

- A refused call to `platform` shows on screen as the D122 pattern: title, why, action and reference, in French and English.
- A refusal that names a field is shown next to that field, with the field highlighted.
- The back office proxies `/v1/` to `platform` and checks `/v1/health` at start, so a refusal has a real place to show.
- The platform address is set when the image starts, not when it is built.

## ⚙️ How it works

1. **The shell starts:** once the router is ready the app is mounted, then the health check runs, in [`frontend/backoffice/src/main.ts:10-11`](../../../frontend/backoffice/src/main.ts#L10-L11).
2. **The call goes through one typed client:** `callPlatform` builds the client on the page's own origin and runs the call, in [`frontend/backoffice/src/api/platformClient.ts:10`](../../../frontend/backoffice/src/api/platformClient.ts#L10) and [`:24-34`](../../../frontend/backoffice/src/api/platformClient.ts#L24-L34). The health check is [`frontend/backoffice/src/api/checkPlatform.ts:7-18`](../../../frontend/backoffice/src/api/checkPlatform.ts#L7-L18), shown as a banner, with itself as the retry action.
3. **The image proxies the call:** nginx sends `/v1/` to the address resolved at request time, in [`frontend/backoffice/nginx.conf:18-26`](../../../frontend/backoffice/nginx.conf#L18-L26). The template and the default `ERP_PLATFORM_URL` are set in [`frontend/backoffice/Dockerfile:18-20`](../../../frontend/backoffice/Dockerfile#L18-L20).
4. **A refusal is thrown and mapped:** on an error, `callPlatform` calls `toRefusal` and puts the result in the store, then rethrows ([`platformClient.ts:30-32`](../../../frontend/backoffice/src/api/platformClient.ts#L30-L32)). [`toRefusal.ts:27-58`](../../../frontend/backoffice/src/errors/toRefusal.ts#L27-L58) turns an `ApiProblemError` into keys, a reference, scalar params and an optional field. It never copies the body or the detail. Anything else gets the fallback entry ([`toRefusal.ts:29-42`](../../../frontend/backoffice/src/errors/toRefusal.ts#L29-L42)). The type is [`Refusal.ts:7-17`](../../../frontend/backoffice/src/errors/Refusal.ts#L7-L17).
5. **The code is resolved to keys:** `resolveErrorCode` looks the D122 code up in the front-end catalogue, in [`frontend/packages/i18n/src/errors/errorCatalog.ts:102`](../../../frontend/packages/i18n/src/errors/errorCatalog.ts#L102), with the fallback keys at [`:97-99`](../../../frontend/packages/i18n/src/errors/errorCatalog.ts#L97-L99). A test keeps it in step with the back-end YAML catalogues ([`errorCatalog.test.ts:26-29`](../../../frontend/packages/i18n/tests/errors/errorCatalog.test.ts#L26-L29)).
6. **The store keeps keys, not text:** [`frontend/backoffice/src/stores/errors.ts:33-37`](../../../frontend/backoffice/src/stores/errors.ts#L33-L37) adds the refusal and its action. `dialog`, `banner` and `fieldErrors` are computed by presentation ([`errors.ts:18-26`](../../../frontend/backoffice/src/stores/errors.ts#L18-L26)). `act` runs the action then dismisses ([`errors.ts:46-50`](../../../frontend/backoffice/src/stores/errors.ts#L46-L50)).
7. **The outlet renders it:** [`frontend/backoffice/src/errors/ErrorOutlet.vue:11-19`](../../../frontend/backoffice/src/errors/ErrorOutlet.vue#L11-L19) translates with the error catalogue first, then the app's own, and follows the language without a reload. The banner and the dialog are at [`ErrorOutlet.vue:26-49`](../../../frontend/backoffice/src/errors/ErrorOutlet.vue#L26-L49). It is mounted in the shell at [`frontend/backoffice/src/App.vue:10`](../../../frontend/backoffice/src/App.vue#L10).
8. **The components draw it:** [`ErrorBanner.vue:32-49`](../../../frontend/packages/ui/src/errors/ErrorBanner.vue#L32-L49) is a `role="alert"` with the circle-alert icon, and [`ErrorDialog.vue:54-86`](../../../frontend/packages/ui/src/errors/ErrorDialog.vue#L54-L86) is an error `UiModal` whose panel is described by the why ([`ErrorDialog.vue:32-35`](../../../frontend/packages/ui/src/errors/ErrorDialog.vue#L32-L35)).
9. **A field refusal goes to its field:** [`frontend/backoffice/src/errors/useFieldErrors.ts:22-26`](../../../frontend/backoffice/src/errors/useFieldErrors.ts#L22-L26) returns the translated why of the field's refusal, to pass to the form field's `error`. `clear` removes it ([`useFieldErrors.ts:32-34`](../../../frontend/backoffice/src/errors/useFieldErrors.ts#L32-L34)).

## 🧱 Files and lines changed

<!-- changes -->
| File | Change | Lines in the new version | Added | Removed |
| --- | --- | --- | --- | --- |
| [`docs/technical/architecture/frontend.md`](../../../docs/technical/architecture/frontend.md) | Modified | [27-66](../../../docs/technical/architecture/frontend.md#L27), [86](../../../docs/technical/architecture/frontend.md#L86) | +41 | −1 |
| [`frontend/backoffice/Dockerfile`](../../../frontend/backoffice/Dockerfile) | Modified | [18](../../../frontend/backoffice/Dockerfile#L18), [20](../../../frontend/backoffice/Dockerfile#L20) | +2 | −1 |
| [`frontend/backoffice/e2e/errors/refused-call.e2e.ts`](../../../frontend/backoffice/e2e/errors/refused-call.e2e.ts) | Added | [1-100](../../../frontend/backoffice/e2e/errors/refused-call.e2e.ts#L1) | +100 | −0 |
| [`frontend/backoffice/nginx.conf`](../../../frontend/backoffice/nginx.conf) | Modified | [18-27](../../../frontend/backoffice/nginx.conf#L18) | +10 | −0 |
| [`frontend/backoffice/package.json`](../../../frontend/backoffice/package.json) | Modified | [19](../../../frontend/backoffice/package.json#L19) | +1 | −0 |
| [`frontend/backoffice/src/App.vue`](../../../frontend/backoffice/src/App.vue) | Modified | [4](../../../frontend/backoffice/src/App.vue#L4), [10](../../../frontend/backoffice/src/App.vue#L10) | +2 | −0 |
| [`frontend/backoffice/src/api/checkPlatform.ts`](../../../frontend/backoffice/src/api/checkPlatform.ts) | Added | [1-18](../../../frontend/backoffice/src/api/checkPlatform.ts#L1) | +18 | −0 |
| [`frontend/backoffice/src/api/platformClient.ts`](../../../frontend/backoffice/src/api/platformClient.ts) | Added | [1-34](../../../frontend/backoffice/src/api/platformClient.ts#L1) | +34 | −0 |
| [`frontend/backoffice/src/errors/ErrorOutlet.vue`](../../../frontend/backoffice/src/errors/ErrorOutlet.vue) | Added | [1-57](../../../frontend/backoffice/src/errors/ErrorOutlet.vue#L1) | +57 | −0 |
| [`frontend/backoffice/src/errors/Refusal.ts`](../../../frontend/backoffice/src/errors/Refusal.ts) | Added | [1-17](../../../frontend/backoffice/src/errors/Refusal.ts#L1) | +17 | −0 |
| [`frontend/backoffice/src/errors/toRefusal.ts`](../../../frontend/backoffice/src/errors/toRefusal.ts) | Added | [1-58](../../../frontend/backoffice/src/errors/toRefusal.ts#L1) | +58 | −0 |
| [`frontend/backoffice/src/errors/useFieldErrors.ts`](../../../frontend/backoffice/src/errors/useFieldErrors.ts) | Added | [1-37](../../../frontend/backoffice/src/errors/useFieldErrors.ts#L1) | +37 | −0 |
| [`frontend/backoffice/src/main.ts`](../../../frontend/backoffice/src/main.ts) | Modified | [5](../../../frontend/backoffice/src/main.ts#L5), [11](../../../frontend/backoffice/src/main.ts#L11) | +2 | −0 |
| [`frontend/backoffice/src/stores/errors.ts`](../../../frontend/backoffice/src/stores/errors.ts) | Added | [1-53](../../../frontend/backoffice/src/stores/errors.ts#L1) | +53 | −0 |
| [`frontend/backoffice/tests/api/checkPlatform.test.ts`](../../../frontend/backoffice/tests/api/checkPlatform.test.ts) | Added | [1-76](../../../frontend/backoffice/tests/api/checkPlatform.test.ts#L1) | +76 | −0 |
| [`frontend/backoffice/tests/api/platformClient.test.ts`](../../../frontend/backoffice/tests/api/platformClient.test.ts) | Added | [1-117](../../../frontend/backoffice/tests/api/platformClient.test.ts#L1) | +117 | −0 |
| [`frontend/backoffice/tests/api/standInPlatform.ts`](../../../frontend/backoffice/tests/api/standInPlatform.ts) | Added | [1-60](../../../frontend/backoffice/tests/api/standInPlatform.ts#L1) | +60 | −0 |
| [`frontend/backoffice/tests/errors/ErrorOutlet.test.ts`](../../../frontend/backoffice/tests/errors/ErrorOutlet.test.ts) | Added | [1-181](../../../frontend/backoffice/tests/errors/ErrorOutlet.test.ts#L1) | +181 | −0 |
| [`frontend/backoffice/tests/errors/toRefusal.test.ts`](../../../frontend/backoffice/tests/errors/toRefusal.test.ts) | Added | [1-104](../../../frontend/backoffice/tests/errors/toRefusal.test.ts#L1) | +104 | −0 |
| [`frontend/backoffice/tests/errors/useFieldErrors.test.ts`](../../../frontend/backoffice/tests/errors/useFieldErrors.test.ts) | Added | [1-170](../../../frontend/backoffice/tests/errors/useFieldErrors.test.ts#L1) | +170 | −0 |
| [`frontend/backoffice/tests/stores/errors.test.ts`](../../../frontend/backoffice/tests/stores/errors.test.ts) | Added | [1-174](../../../frontend/backoffice/tests/stores/errors.test.ts#L1) | +174 | −0 |
| [`frontend/backoffice/tsconfig.app.json`](../../../frontend/backoffice/tsconfig.app.json) | Modified | [6](../../../frontend/backoffice/tsconfig.app.json#L6) | +1 | −0 |
| [`frontend/backoffice/tsconfig.vitest.json`](../../../frontend/backoffice/tsconfig.vitest.json) | Modified | [6](../../../frontend/backoffice/tsconfig.vitest.json#L6), [11](../../../frontend/backoffice/tsconfig.vitest.json#L11) | +2 | −1 |
| [`frontend/packages/i18n/package.json`](../../../frontend/packages/i18n/package.json) | Modified | [31](../../../frontend/packages/i18n/package.json#L31) | +1 | −0 |
| [`frontend/packages/i18n/src/catalogues/en/errors.json`](../../../frontend/packages/i18n/src/catalogues/en/errors.json) | Added | [1-82](../../../frontend/packages/i18n/src/catalogues/en/errors.json#L1) | +82 | −0 |
| [`frontend/packages/i18n/src/catalogues/fr/errors.json`](../../../frontend/packages/i18n/src/catalogues/fr/errors.json) | Added | [1-82](../../../frontend/packages/i18n/src/catalogues/fr/errors.json#L1) | +82 | −0 |
| [`frontend/packages/i18n/src/errors/errorCatalog.ts`](../../../frontend/packages/i18n/src/errors/errorCatalog.ts) | Added | [1-110](../../../frontend/packages/i18n/src/errors/errorCatalog.ts#L1) | +110 | −0 |
| [`frontend/packages/i18n/src/index.ts`](../../../frontend/packages/i18n/src/index.ts) | Modified | [9-10](../../../frontend/packages/i18n/src/index.ts#L9) | +2 | −0 |
| [`frontend/packages/i18n/tests/errors/errorCatalog.test.ts`](../../../frontend/packages/i18n/tests/errors/errorCatalog.test.ts) | Added | [1-90](../../../frontend/packages/i18n/tests/errors/errorCatalog.test.ts#L1) | +90 | −0 |
| [`frontend/packages/i18n/tests/errors/errorTexts.test.ts`](../../../frontend/packages/i18n/tests/errors/errorTexts.test.ts) | Added | [1-110](../../../frontend/packages/i18n/tests/errors/errorTexts.test.ts#L1) | +110 | −0 |
| [`frontend/packages/ui/src/errors/ErrorBanner.vue`](../../../frontend/packages/ui/src/errors/ErrorBanner.vue) | Added | [1-102](../../../frontend/packages/ui/src/errors/ErrorBanner.vue#L1) | +102 | −0 |
| [`frontend/packages/ui/src/errors/ErrorDialog.vue`](../../../frontend/packages/ui/src/errors/ErrorDialog.vue) | Added | [1-106](../../../frontend/packages/ui/src/errors/ErrorDialog.vue#L1) | +106 | −0 |
| [`frontend/packages/ui/src/index.ts`](../../../frontend/packages/ui/src/index.ts) | Modified | [9-16](../../../frontend/packages/ui/src/index.ts#L9) | +8 | −0 |
| [`frontend/packages/ui/tests/errors/ErrorBanner.spec.ts`](../../../frontend/packages/ui/tests/errors/ErrorBanner.spec.ts) | Added | [1-81](../../../frontend/packages/ui/tests/errors/ErrorBanner.spec.ts#L1) | +81 | −0 |
| [`frontend/packages/ui/tests/errors/ErrorDialog.spec.ts`](../../../frontend/packages/ui/tests/errors/ErrorDialog.spec.ts) | Added | [1-133](../../../frontend/packages/ui/tests/errors/ErrorDialog.spec.ts#L1) | +133 | −0 |
| [`pnpm-lock.yaml`](../../../pnpm-lock.yaml) | Modified | [17-19](../../../pnpm-lock.yaml#L17), [40](../../../pnpm-lock.yaml#L40), [59](../../../pnpm-lock.yaml#L59), [80](../../../pnpm-lock.yaml#L80), [83](../../../pnpm-lock.yaml#L83), [119](../../../pnpm-lock.yaml#L119), [150](../../../pnpm-lock.yaml#L150), [171](../../../pnpm-lock.yaml#L171), [174](../../../pnpm-lock.yaml#L174), [181-183](../../../pnpm-lock.yaml#L181), [207](../../../pnpm-lock.yaml#L207), [223](../../../pnpm-lock.yaml#L223), [235](../../../pnpm-lock.yaml#L235), [259](../../../pnpm-lock.yaml#L259), [262](../../../pnpm-lock.yaml#L262), [2266-2270](../../../pnpm-lock.yaml#L2266), [2593](../../../pnpm-lock.yaml#L2593), [2603](../../../pnpm-lock.yaml#L2603), [2744](../../../pnpm-lock.yaml#L2744), [2747](../../../pnpm-lock.yaml#L2747), [2750](../../../pnpm-lock.yaml#L2750), [2757](../../../pnpm-lock.yaml#L2757), [3994](../../../pnpm-lock.yaml#L3994), [4003](../../../pnpm-lock.yaml#L4003), [4013](../../../pnpm-lock.yaml#L4013), [4026](../../../pnpm-lock.yaml#L4026), [4028](../../../pnpm-lock.yaml#L4028), [4031](../../../pnpm-lock.yaml#L4031), [4042](../../../pnpm-lock.yaml#L4042), [4077](../../../pnpm-lock.yaml#L4077), [4093](../../../pnpm-lock.yaml#L4093), [4099](../../../pnpm-lock.yaml#L4099), [4184-4185](../../../pnpm-lock.yaml#L4184) | +42 | −28 |
| **36 files** | | | **+2266** | **−31** |
<!-- /changes -->

- [`frontend/packages/ui/src/errors/ErrorBanner.vue`](../../../frontend/packages/ui/src/errors/ErrorBanner.vue), [`ErrorDialog.vue`](../../../frontend/packages/ui/src/errors/ErrorDialog.vue) and [`frontend/packages/ui/src/index.ts:9-16`](../../../frontend/packages/ui/src/index.ts#L9-L16): the two pattern components and their exports, with their specs in [`frontend/packages/ui/tests/errors/`](../../../frontend/packages/ui/tests/errors/ErrorBanner.spec.ts).
- [`frontend/packages/i18n/src/errors/errorCatalog.ts`](../../../frontend/packages/i18n/src/errors/errorCatalog.ts), [`en/errors.json`](../../../frontend/packages/i18n/src/catalogues/en/errors.json), [`fr/errors.json`](../../../frontend/packages/i18n/src/catalogues/fr/errors.json), [`frontend/packages/i18n/src/index.ts:9-10`](../../../frontend/packages/i18n/src/index.ts#L9-L10) and [`frontend/packages/i18n/package.json`](../../../frontend/packages/i18n/package.json): the code-to-keys catalogue, the texts, the exports and the `yaml` dev dependency the catalogue test reads the back-end YAML with. Tests: [`errorCatalog.test.ts`](../../../frontend/packages/i18n/tests/errors/errorCatalog.test.ts), [`errorTexts.test.ts`](../../../frontend/packages/i18n/tests/errors/errorTexts.test.ts).
- [`frontend/backoffice/src/errors/`](../../../frontend/backoffice/src/errors/toRefusal.ts), [`frontend/backoffice/src/stores/errors.ts`](../../../frontend/backoffice/src/stores/errors.ts) and [`frontend/backoffice/src/api/`](../../../frontend/backoffice/src/api/platformClient.ts): the refusal type, the mapping, the store, the outlet, the field binding, the client and the load check.
- [`frontend/backoffice/src/App.vue`](../../../frontend/backoffice/src/App.vue) and [`src/main.ts`](../../../frontend/backoffice/src/main.ts): mount the outlet and start the check.
- [`frontend/backoffice/nginx.conf`](../../../frontend/backoffice/nginx.conf) and [`frontend/backoffice/Dockerfile`](../../../frontend/backoffice/Dockerfile): the `/v1/` proxy with a run-time upstream.
- [`frontend/backoffice/package.json`](../../../frontend/backoffice/package.json), [`tsconfig.app.json`](../../../frontend/backoffice/tsconfig.app.json), [`tsconfig.vitest.json`](../../../frontend/backoffice/tsconfig.vitest.json) and [`pnpm-lock.yaml`](../../../pnpm-lock.yaml): the `@simpleerp/api-client` dependency and the `development` condition so the back office type-checks against the sources of the workspace packages.
- [`frontend/backoffice/e2e/errors/refused-call.e2e.ts`](../../../frontend/backoffice/e2e/errors/refused-call.e2e.ts): Playwright against the real images. It reroutes `/v1/health` ([`:11-12`](../../../frontend/backoffice/e2e/errors/refused-call.e2e.ts#L11-L12), [`:40`](../../../frontend/backoffice/e2e/errors/refused-call.e2e.ts#L40)) to a call platform really refuses, then checks the banner, its announcement and icon, axe, and the retry ([`:47`](../../../frontend/backoffice/e2e/errors/refused-call.e2e.ts#L47), [`:61`](../../../frontend/backoffice/e2e/errors/refused-call.e2e.ts#L61), [`:80`](../../../frontend/backoffice/e2e/errors/refused-call.e2e.ts#L80), [`:87`](../../../frontend/backoffice/e2e/errors/refused-call.e2e.ts#L87)).
- Vitest tests in [`frontend/backoffice/tests/`](../../../frontend/backoffice/tests/errors/toRefusal.test.ts): `toRefusal`, the outlet, the store, the field binding, and the client against a stand-in platform ([`standInPlatform.ts`](../../../frontend/backoffice/tests/api/standInPlatform.ts)).
- [`docs/technical/architecture/frontend.md`](../../../docs/technical/architecture/frontend.md), lines [`27-66`](../../../docs/technical/architecture/frontend.md#L27-L66): the design page section "Error messages on screen".

## 🧪 How to test it

```bash
pnpm --filter ./frontend/packages/ui run test
pnpm --filter ./frontend/packages/i18n run test
pnpm --filter ./frontend/backoffice run test
pnpm --filter ./frontend/backoffice run lint
pnpm --filter ./frontend/backoffice run typecheck
pnpm --filter ./frontend/backoffice run e2e
```

The last one needs the real images of [`compose.e2e.yaml`](../../../compose.e2e.yaml) started. The first five need no server.

## 🔗 Evidence

- [Tests](tests-evidences/test.txt): Vitest suites pass.
- [Playwright, refused call](tests-evidences/playwright-refused-call.txt): 16 passed (4 projects, light and dark, en and fr), and the curl through the proxy returns CONTEXT-COMPANY-01 as problem+json.
- [Type check](tests-evidences/typecheck.txt) and [lint](tests-evidences/lint.txt): 0 errors.
- [Install](tests-evidences/pnpm-install.txt), [ticket references](tests-evidences/ticket-refs.txt) and [plan view](tests-evidences/plan-view.txt): the other checks.

## 📝 Assumptions accepted

- K24: the evidence file was written by hand from the real command outputs, trimmed. Its content agrees with the code. Keeping the raw reporter output is a follow-up.
- K24: the "image alone" check used host port 8081 so as not to clash with the stack's 8080. Only the host side of the mapping changes.
- TICKET.md: "No screen". The ticket builds the design-system pattern and its shell outlet, not a functional screen page. Playwright covers the banner in light and dark, fr and en.
- TICKET.md: no budget touched, because the accessibility page specifies no measure yet. axe still runs in Vitest and Playwright.
- TICKET.md: the ticket anchor is the sprint anchor `#s04`, as the phase page has no per-ticket anchor.

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| [`infra/helm/charts/backoffice/values.yaml`](../../../infra/helm/charts/backoffice/values.yaml) | nginx's own resolver ignores the search domains of resolv.conf, so in Kubernetes `ERP_PLATFORM_URL` must be a fully qualified name such as `http://<release>-platform.<namespace>.svc.cluster.local:8000`. Set it through the chart's env when the Helm wiring is done. The envsubst entrypoint writes `/etc/nginx/conf.d` at start, so a `readOnlyRootFilesystem` would need an emptyDir there |
| [`docs/technical/architecture/frontend.md`](../../../docs/technical/architecture/frontend.md) | Document the `/v1/` same-origin proxy, `ERP_PLATFORM_URL` (default `http://platform:8000`) and the run-time resolver. Say the value is `scheme://host:port` with no path: with `proxy_pass` through a variable, a path would replace every request URI |
| [`docs/tickets/T0.23/tests-evidences/playwright-refused-call.txt`](tests-evidences/playwright-refused-call.txt) | The Playwright section was written by hand and grouped by test, so it is not the reporter's raw output, and no HTML report is kept. Keep both once the shell allows a redirect |
| [`frontend/backoffice/src/errors/ErrorOutlet.vue`](../../../frontend/backoffice/src/errors/ErrorOutlet.vue) | Other follow-ups of the earlier rounds are in [PROGRESS.md](PROGRESS.md): the API client should keep `field` and `values`, `crypto.randomUUID` needs a secure context, the action labels are long, the translator order, the naming of the ui components |
