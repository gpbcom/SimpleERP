# T0.07: Design tokens package

**Status:** ✅ Done · **Ticket:** [TICKET.md](TICKET.md) · **Choices and trade-offs:** [IMPLEMENTATION.md](IMPLEMENTATION.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🔭 What it does

- Adds the package `@simpleerp/tokens`: one JSON source of design tokens that builds a CSS file of variables and a TypeScript module.
- The CSS covers colour in light and dark (manual choice or device setting), spacing, density (comfortable and compact, phones always comfortable), typography, radius and elevation.
- The three typefaces are served by the package itself, with their open licences, so no font is fetched from a third party.
- A test suite checks the contrast of every text colour pair in light and in dark.

## ⚙️ How it works

1. **Command:** `pnpm --filter ./frontend/packages/tokens run build` runs [`../../../frontend/packages/tokens/src/build/main.ts:13`](../../../frontend/packages/tokens/src/build/main.ts#L13) through `tsx`, which calls the build with the source path and the `dist/` folder.
2. **Orchestration:** [`../../../frontend/packages/tokens/src/build/build-tokens.ts:33`](../../../frontend/packages/tokens/src/build/build-tokens.ts#L33) loads the source, removes only `dist/fonts`, writes `tokens.css` and `tokens.ts`, then copies the fonts.
3. **Load and validate:** [`../../../frontend/packages/tokens/src/source/load-source.ts:221`](../../../frontend/packages/tokens/src/source/load-source.ts#L221) reads [`../../../frontend/packages/tokens/src/source/tokens.json`](../../../frontend/packages/tokens/src/source/tokens.json) and checks each section (colours as hex, spacing, density, typography, radius, elevation, fonts), raising a `TokenSourceError`. Colours are checked from [`../../../frontend/packages/tokens/src/source/load-source.ts:105`](../../../frontend/packages/tokens/src/source/load-source.ts#L105).
4. **Font faces:** [`../../../frontend/packages/tokens/src/generate/render-font-faces.ts:14`](../../../frontend/packages/tokens/src/generate/render-font-faces.ts#L14) writes the `@font-face` rules, which only point at `./fonts/...`.
5. **CSS variables:** [`../../../frontend/packages/tokens/src/generate/render-css.ts:84`](../../../frontend/packages/tokens/src/generate/render-css.ts#L84) writes six blocks in order: base (typography, radius, spacing), light on `:root` and `[data-theme="light"]` ([line 87](../../../frontend/packages/tokens/src/generate/render-css.ts#L87)), dark on `[data-theme="dark"]` ([line 88](../../../frontend/packages/tokens/src/generate/render-css.ts#L88)), dark again under `prefers-color-scheme` through `:root:not([data-theme="light"])` ([line 89](../../../frontend/packages/tokens/src/generate/render-css.ts#L89)), comfortable density on `:root`, and compact only inside `min-width: 768px` ([line 94](../../../frontend/packages/tokens/src/generate/render-css.ts#L94)).
6. **TypeScript module:** [`../../../frontend/packages/tokens/src/generate/render-typescript.ts:25`](../../../frontend/packages/tokens/src/generate/render-typescript.ts#L25) writes `export const tokens = {...} as const` and the `Tokens` type, with colours and elevation split by theme.
7. **Fonts:** [`../../../frontend/packages/tokens/src/generate/copy-fonts.ts:19`](../../../frontend/packages/tokens/src/generate/copy-fonts.ts#L19) resolves each pinned `@fontsource` package with `require.resolve` ([line 26](../../../frontend/packages/tokens/src/generate/copy-fonts.ts#L26)), copies the woff2 file and, once per package, its licence.
8. **Contrast check (tests only):** [`../../../frontend/packages/tokens/src/contrast/contrast-ratio.ts:15`](../../../frontend/packages/tokens/src/contrast/contrast-ratio.ts#L15) and [line 33](../../../frontend/packages/tokens/src/contrast/contrast-ratio.ts#L33) compute the WCAG ratio, used by [`../../../frontend/packages/tokens/tests/contrast/palette-contrast.test.ts`](../../../frontend/packages/tokens/tests/contrast/palette-contrast.test.ts).

## 🧱 Files and lines changed

<!-- changes -->
| File | Change | Lines in the new version | Added | Removed |
| --- | --- | --- | --- | --- |
| [`.gitignore`](../../../.gitignore) | Modified | [4-7](../../../.gitignore#L4) | +4 | −1 |
| [`frontend/packages/tokens/.gitignore`](../../../frontend/packages/tokens/.gitignore) | Added | [1-2](../../../frontend/packages/tokens/.gitignore#L1) | +2 | −0 |
| [`frontend/packages/tokens/README.md`](../../../frontend/packages/tokens/README.md) | Added | [1-103](../../../frontend/packages/tokens/README.md#L1) | +103 | −0 |
| [`frontend/packages/tokens/package.json`](../../../frontend/packages/tokens/package.json) | Added | [1-29](../../../frontend/packages/tokens/package.json#L1) | +29 | −0 |
| [`frontend/packages/tokens/src/build/build-tokens.ts`](../../../frontend/packages/tokens/src/build/build-tokens.ts) | Added | [1-45](../../../frontend/packages/tokens/src/build/build-tokens.ts#L1) | +45 | −0 |
| [`frontend/packages/tokens/src/build/main.ts`](../../../frontend/packages/tokens/src/build/main.ts) | Added | [1-33](../../../frontend/packages/tokens/src/build/main.ts#L1) | +33 | −0 |
| [`frontend/packages/tokens/src/contrast/contrast-ratio.ts`](../../../frontend/packages/tokens/src/contrast/contrast-ratio.ts) | Added | [1-37](../../../frontend/packages/tokens/src/contrast/contrast-ratio.ts#L1) | +37 | −0 |
| [`frontend/packages/tokens/src/generate/copy-fonts.ts`](../../../frontend/packages/tokens/src/generate/copy-fonts.ts) | Added | [1-42](../../../frontend/packages/tokens/src/generate/copy-fonts.ts#L1) | +42 | −0 |
| [`frontend/packages/tokens/src/generate/font-file-missing-error.ts`](../../../frontend/packages/tokens/src/generate/font-file-missing-error.ts) | Added | [1-17](../../../frontend/packages/tokens/src/generate/font-file-missing-error.ts#L1) | +17 | −0 |
| [`frontend/packages/tokens/src/generate/render-css.ts`](../../../frontend/packages/tokens/src/generate/render-css.ts) | Added | [1-100](../../../frontend/packages/tokens/src/generate/render-css.ts#L1) | +100 | −0 |
| [`frontend/packages/tokens/src/generate/render-font-faces.ts`](../../../frontend/packages/tokens/src/generate/render-font-faces.ts) | Added | [1-28](../../../frontend/packages/tokens/src/generate/render-font-faces.ts#L1) | +28 | −0 |
| [`frontend/packages/tokens/src/generate/render-typescript.ts`](../../../frontend/packages/tokens/src/generate/render-typescript.ts) | Added | [1-40](../../../frontend/packages/tokens/src/generate/render-typescript.ts#L1) | +40 | −0 |
| [`frontend/packages/tokens/src/source/load-source.ts`](../../../frontend/packages/tokens/src/source/load-source.ts) | Added | [1-239](../../../frontend/packages/tokens/src/source/load-source.ts#L1) | +239 | −0 |
| [`frontend/packages/tokens/src/source/token-source-error.ts`](../../../frontend/packages/tokens/src/source/token-source-error.ts) | Added | [1-15](../../../frontend/packages/tokens/src/source/token-source-error.ts#L1) | +15 | −0 |
| [`frontend/packages/tokens/src/source/token-source.ts`](../../../frontend/packages/tokens/src/source/token-source.ts) | Added | [1-66](../../../frontend/packages/tokens/src/source/token-source.ts#L1) | +66 | −0 |
| [`frontend/packages/tokens/src/source/tokens.json`](../../../frontend/packages/tokens/src/source/tokens.json) | Added | [1-62](../../../frontend/packages/tokens/src/source/tokens.json#L1) | +62 | −0 |
| [`frontend/packages/tokens/tests/build/build-tokens.test.ts`](../../../frontend/packages/tokens/tests/build/build-tokens.test.ts) | Added | [1-322](../../../frontend/packages/tokens/tests/build/build-tokens.test.ts#L1) | +322 | −0 |
| [`frontend/packages/tokens/tests/contrast/contrast-ratio.test.ts`](../../../frontend/packages/tokens/tests/contrast/contrast-ratio.test.ts) | Added | [1-37](../../../frontend/packages/tokens/tests/contrast/contrast-ratio.test.ts#L1) | +37 | −0 |
| [`frontend/packages/tokens/tests/contrast/palette-contrast.test.ts`](../../../frontend/packages/tokens/tests/contrast/palette-contrast.test.ts) | Added | [1-44](../../../frontend/packages/tokens/tests/contrast/palette-contrast.test.ts#L1) | +44 | −0 |
| [`frontend/packages/tokens/tests/generate/copy-fonts.test.ts`](../../../frontend/packages/tokens/tests/generate/copy-fonts.test.ts) | Added | [1-78](../../../frontend/packages/tokens/tests/generate/copy-fonts.test.ts#L1) | +78 | −0 |
| [`frontend/packages/tokens/tests/generate/render-css.test.ts`](../../../frontend/packages/tokens/tests/generate/render-css.test.ts) | Added | [1-148](../../../frontend/packages/tokens/tests/generate/render-css.test.ts#L1) | +148 | −0 |
| [`frontend/packages/tokens/tests/generate/render-font-faces.test.ts`](../../../frontend/packages/tokens/tests/generate/render-font-faces.test.ts) | Added | [1-66](../../../frontend/packages/tokens/tests/generate/render-font-faces.test.ts#L1) | +66 | −0 |
| [`frontend/packages/tokens/tests/generate/render-typescript.test.ts`](../../../frontend/packages/tokens/tests/generate/render-typescript.test.ts) | Added | [1-150](../../../frontend/packages/tokens/tests/generate/render-typescript.test.ts#L1) | +150 | −0 |
| [`frontend/packages/tokens/tests/source/load-source.test.ts`](../../../frontend/packages/tokens/tests/source/load-source.test.ts) | Added | [1-122](../../../frontend/packages/tokens/tests/source/load-source.test.ts#L1) | +122 | −0 |
| [`frontend/packages/tokens/tsconfig.json`](../../../frontend/packages/tokens/tsconfig.json) | Added | [1-14](../../../frontend/packages/tokens/tsconfig.json#L1) | +14 | −0 |
| [`frontend/packages/tokens/vitest.config.ts`](../../../frontend/packages/tokens/vitest.config.ts) | Added | [1-8](../../../frontend/packages/tokens/vitest.config.ts#L1) | +8 | −0 |
| [`pnpm-lock.yaml`](../../../pnpm-lock.yaml) | Modified | [44-68](../../../pnpm-lock.yaml#L44), [78-233](../../../pnpm-lock.yaml#L78), [273-281](../../../pnpm-lock.yaml#L273), [584-588](../../../pnpm-lock.yaml#L584), [945-949](../../../pnpm-lock.yaml#L945), [961-965](../../../pnpm-lock.yaml#L961), [1106-1183](../../../pnpm-lock.yaml#L1106), [1218-1223](../../../pnpm-lock.yaml#L1218), [1425](../../../pnpm-lock.yaml#L1425), [1432](../../../pnpm-lock.yaml#L1432), [1485-1513](../../../pnpm-lock.yaml#L1485), [1837-1842](../../../pnpm-lock.yaml#L1837), [1859-1860](../../../pnpm-lock.yaml#L1859), [1871](../../../pnpm-lock.yaml#L1871), [1880](../../../pnpm-lock.yaml#L1880), [1883](../../../pnpm-lock.yaml#L1883), [1885](../../../pnpm-lock.yaml#L1885), [1888](../../../pnpm-lock.yaml#L1888), [1899](../../../pnpm-lock.yaml#L1899) | +334 | −7 |
| **27 files** | | | **+2185** | **−8** |
<!-- /changes -->

- [`.gitignore`](../../../.gitignore): the `build/` rule now covers only the root and the Python packages, so `src/build/` of the new package is tracked (plan change approved by the person).
- [`../../../frontend/packages/tokens/package.json`](../../../frontend/packages/tokens/package.json), lines [`10-28`](../../../frontend/packages/tokens/package.json#L10-L28): exports (`dist/tokens.ts`, `tokens.css`, `fonts/*`), scripts and exactly pinned dev dependencies.
- [`../../../frontend/packages/tokens/tsconfig.json`](../../../frontend/packages/tokens/tsconfig.json), [`../../../frontend/packages/tokens/vitest.config.ts`](../../../frontend/packages/tokens/vitest.config.ts), [`../../../frontend/packages/tokens/.gitignore`](../../../frontend/packages/tokens/.gitignore), [`../../../frontend/packages/tokens/README.md`](../../../frontend/packages/tokens/README.md): strict TypeScript, test setup, ignored `dist/`, and the package documentation.
- [`../../../frontend/packages/tokens/src/source/`](../../../frontend/packages/tokens/src/source/tokens.json): the token data, its types, the validating loader and its error.
- [`../../../frontend/packages/tokens/src/generate/`](../../../frontend/packages/tokens/src/generate/render-css.ts): the three renderers, the font copy and its error.
- [`../../../frontend/packages/tokens/src/build/`](../../../frontend/packages/tokens/src/build/build-tokens.ts) and [`../../../frontend/packages/tokens/src/contrast/contrast-ratio.ts`](../../../frontend/packages/tokens/src/contrast/contrast-ratio.ts): the build and the contrast formula.
- [`../../../frontend/packages/tokens/tests/`](../../../frontend/packages/tokens/tests/build/build-tokens.test.ts): eight Vitest files (255 tests) for the loader, contrast, renderers, fonts and the whole build.
- [`pnpm-lock.yaml`](../../../pnpm-lock.yaml): the importer of the new package, regenerated.

## 🧪 How to test it

```bash
pnpm install --frozen-lockfile
pnpm --filter ./frontend/packages/tokens run test
pnpm --filter ./frontend/packages/tokens run typecheck
pnpm --filter ./frontend/packages/tokens run build
```

The build writes `dist/tokens.css`, `dist/tokens.ts` and `dist/fonts/` (seven woff2 files and three licences).

## 🔗 Evidence

- [Tests](tests-evidences/test.txt): 8 files, 255 tests passed.
- [Type check](tests-evidences/typecheck.txt): `pnpm -r --if-present typecheck`.
- [Lint](tests-evidences/lint.txt): `pnpm -r --if-present lint` (the package has no lint script yet).
- [Install](tests-evidences/pnpm-install.txt): `pnpm install --frozen-lockfile` passes on the regenerated lock.
- [Ticket references](tests-evidences/ticket-refs.txt) and [plan view](tests-evidences/plan-view.txt).

## 📝 Assumptions accepted

- K07: the scaffold was already correct, so only [`pnpm-lock.yaml`](../../../pnpm-lock.yaml) needed regenerating.
- K07: exact pins (typescript 5.9.3, vitest 5.1.2, tsx 4.23.15, @types/node 22.20.7, @fontsource/* 5.3.0).
- Fonts are packaged in `frontend/packages/tokens`, copied from the pinned `@fontsource` packages with their OFL licences (D44).
- T0.01 provides the pnpm workspace.
- A plain JSON source and a small build script, with no token tool.
- The Accessibility budget has no measures yet, so WCAG 2.2 AA and the ratios of the Colours page are used.
- No lint script and no `@simpleerp/config` until T0.02 lands.
- Seven latin-subset font files, including Inter 600, since the specifications name no subset.
- `dist/` is generated and ignored, and the module ships as `dist/tokens.ts`.
- CSS variable names the Tokens page leaves open (`--space-<px>`, `--radius-*`, `--font-family-*`, `--color-surface-raised-1` and `-2`).
- Raised surfaces: #FFFFFF in light, #1E2029 and #282A36 in dark.
- The root [`.gitignore`](../../../.gitignore) change, approved by the person.

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| [`docs/technical/architecture/frontend.md`](../../technical/architecture/frontend.md) | Update "Today" to say that the tokens package is built (T0.07), link its README and refresh "Last reviewed". K15's change was refused while the page was T0.02's file. |
| [`../../../frontend/packages/tokens/package.json`](../../../frontend/packages/tokens/package.json), [`../../../frontend/packages/tokens/tsconfig.json`](../../../frontend/packages/tokens/tsconfig.json) | Add an ESLint config spreading `@simpleerp/config/eslint`, a `lint` script, `@simpleerp/config` as a workspace devDependency, and extend its tsconfig. CI lints nothing here today. |
| [`../../../frontend/packages/tokens/package.json`](../../../frontend/packages/tokens/package.json), [`pnpm-lock.yaml`](../../../pnpm-lock.yaml) | Align on the workspace's TypeScript 6 (5.9.3 here, ^6.0.3 in config), keeping the exact pin. D415 only asks for pins in the lock, which caret ranges give, so the "meets D415" reason is overstated. |
| [`../../../frontend/packages/tokens/src/source/tokens.json`](../../../frontend/packages/tokens/src/source/tokens.json) | Add the latin-ext subsets with `unicode-range` when a country pack needs Polish, Czech, Romanian or Turkish glyphs. |
| [`docs/tickets/T0.07/tests-evidences/`](tests-evidences/test.txt) | No evidence runs the real `build` command (`main.ts` through `tsx`). Keep one real build output or add a test. Consumers need `dist/` built first (T0.15). |
| [`../../../frontend/packages/tokens/src/source/load-source.ts`](../../../frontend/packages/tokens/src/source/load-source.ts#L112) | The hex example of the colour error message is #4B4FCE, a near-miss of the primary #4B4FC9. Use #4B4FC9, and in [its test](../../../frontend/packages/tokens/tests/source/load-source.test.ts). |
