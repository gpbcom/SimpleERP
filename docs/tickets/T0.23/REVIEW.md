# T0.23: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- A refused call to `platform` now reaches the screen through these steps:
  - the typed client throws `ApiProblemError`;
  - `toRefusal` maps the D122 code to message keys and a support reference only, and never copies the body, the detail or a stack trace;
  - the Pinia error store holds the refusal as keys, so a language switch re-renders it without replaying the call;
  - `ErrorOutlet` in the shell shows it as a dialog, a banner or a field message.
- `@simpleerp/ui` gains `ErrorBanner` (role `alert`) and `ErrorDialog` (role `alertdialog`, built on `UiModal`). Each has the title, the why, the action button, the error colour with the circle-alert icon, and the small `ref.` line.
- `@simpleerp/i18n` gains the fr/en `errors.json` and `errorCatalog`. A test keeps `errorCatalog` in step with the back-end catalogues: `error_codes.yaml` of the models and of platform, and `refusal_codes.yaml` of the context library.
- The back-office image proxies `/v1/` to platform. Since K24, the address is set at run time: an nginx template, `ERP_PLATFORM_URL` (default `http://platform:8000`) and the container's local resolver. The image no longer exits where no `platform` host exists.
- At start, the app checks `/v1/health`. A refusal shows as a banner, and its action runs the check again.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. A refused call shows the title, the why, the action and the reference of its code, in fr and en | `tests-evidences/playwright-refused-call.txt` ("the banner shows the title, the why, the action and the reference", 4 projects light/dark × en/fr); `ErrorOutlet.test.ts` (switches to French without a reload) | ✅ Pass |
| 2. A field error highlights its field with the message next to it | `useFieldErrors.test.ts` ("a field refusal highlights the field with its message next to it", "only the faulty field is highlighted") | ✅ Pass (from the store onwards. A server field does not arrive yet: see the follow-ups in PROGRESS.md) |
| 3. It is announced, linked to its field, and the colour comes with the icon and the words | `ErrorBanner.spec.ts` / `ErrorDialog.spec.ts` (role alert/alertdialog, aria-describedby, icon, axe in every theme); `useFieldErrors.test.ts` (aria-describedby, aria-invalid); Playwright "announced and drawn with the error colour and an icon" and "no accessibility violation" | ✅ Pass |
| 4. Against the real images of `compose.e2e.yaml`, a refused call shows the message | `tests-evidences/playwright-refused-call.txt`: 16 passed. The curl through the proxy returns CONTEXT-COMPANY-01 as `application/problem+json` | ✅ Pass |

The other checks also pass: `tests-evidences/test.txt`, `typecheck.txt` and `lint.txt` (0 errors).

## Look at first

- **The runtime upstream (K24):** `frontend/backoffice/nginx.conf:18-26`, `frontend/backoffice/Dockerfile:18,20`.
  - Envsubst only replaces variables that are defined, so `$host`, `$uri` and `$erp_platform` stay as they are.
  - With `proxy_pass` through a variable and no path in it, the request URI goes through unchanged.
  - The evidence shows the image alone running healthy, and the stack answering through the proxy.
- **What a refusal may carry:** `frontend/backoffice/src/errors/toRefusal.ts:27-41`. It copies only the code, the keys, the reference, `field` and scalar `values`, never `detail` or the body (tested in `toRefusal.test.ts`, "holds no raw body").
  - No company data or identity is handled here. The proxy passes the client's headers to platform unchanged, exactly as a direct call would, and the company context stays platform's to check.
- **How the e2e test refuses a call:** `frontend/backoffice/e2e/errors/refused-call.e2e.ts:215-220`. It reroutes `/v1/health` to `/v1/anything`, which the real platform refuses with CONTEXT-COMPANY-01 (no company), as the person decided at 02:16.
- **The translator order:** `frontend/backoffice/src/errors/ErrorOutlet.vue:8-16`. A second translator uses `errorCatalogs` first, then the app's own catalogue. This choice is already a recorded follow-up.

## Assumptions accepted

- K24, the hand-trimmed evidence: accepted. It agrees with the code (the test line numbers and the problem+json body), and the person had already recorded the 16 passes. Keeping the raw output is a follow-up.
- K24, host port 8081 for the image-alone check: accepted. Only the host side of the mapping changes.
- `➖ No screen`: accepted. The ticket builds the design-system pattern and its shell outlet, not a functional screen page. Playwright covers the banner state in both themes and both languages.
- No budget touched, and the `#s04` anchor: accepted, as the specifications give no measure and no per-ticket anchor.

## Follow-ups

- Helm: `ERP_PLATFORM_URL` must be a fully qualified name in Kubernetes, because nginx's resolver ignores search domains. A read-only root filesystem would need an emptyDir on `/etc/nginx/conf.d` (`infra/helm/charts/backoffice/values.yaml`).
- Document the `/v1/` proxy and `ERP_PLATFORM_URL` in `docs/technical/architecture/frontend.md`. Say that the value takes no path.
- Keep the Playwright reporter's raw output and HTML report in `tests-evidences/` instead of a hand-written summary.
- The follow-ups of the earlier rounds stay as listed in `PROGRESS.md`:
  - the API client should keep `field` and `values`;
  - `crypto.randomUUID` only works in a secure context;
  - the action labels are long;
  - the translator order;
  - the naming of the ui components;
  - and the other points recorded there.
