# T0.07: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- A new package, `@simpleerp/tokens`, takes one JSON source, `src/source/tokens.json`, and builds `dist/tokens.css` (CSS variables) and `dist/tokens.ts` (the `tokens` constant, `as const`) from it. Nothing else holds a token value by hand.
- Themes (D43). Light is on `:root` and on `[data-theme="light"]`. Dark is on `[data-theme="dark"]`, and also under `prefers-color-scheme: dark` through `:root:not([data-theme="light"])`. A manual choice in either direction therefore wins over the device setting.
- Density (D42). Comfortable is the default on `:root`. `[data-density="compact"]` only applies inside `@media (min-width: 768px)`, so phones always stay comfortable.
- Fonts (D44). Seven latin woff2 files (Inter, Plus Jakarta Sans, JetBrains Mono) and their OFL licences are copied from pinned `@fontsource` packages into `dist/fonts/`. The `@font-face` rules point only at `./fonts/...`, so no font is fetched from a third party.
- Contrast (D46). A Vitest suite checks every text colour pair of the Colours page in light and in dark, on `surface` and `surface-alt`. The root `.gitignore` `build/` rule now covers only the Python packages, so `src/build/` is tracked (a plan change the person approved).

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. Given the token source, when a value in it is changed and the package is built, then the CSS variables and the TypeScript module carry the new value | `build-tokens.test.ts` › "follows the new primary colour and compact row height in both outputs"; `render-css.test.ts` and `render-typescript.test.ts` › "follows a change..."; tests-evidences/test.txt (255 passed) | ✅ Pass |
| 2. Given the generated tokens, when every text colour pair is tested in light and in dark, then each meets the contrast of Colours | `palette-contrast.test.ts` › "text colour pairs" (light at 4.5, text at 7, white on primary; dark at 7 as the page's AAA values; border-strong at 3 and 4.5); `contrast-ratio.test.ts` › "gives the 6.44:1 of the Colours page"; tests-evidences/test.txt | ✅ Pass |
| 3. Given the built package, when its output and fonts are inspected, then the three typefaces are served by the package and no font is fetched from a third party | `build-tokens.test.ts` › "holds the seven woff2 files...", "points every url() of tokens.css to a relative file that exists", "holds no %s in the built files", "has an @font-face for the family of %s"; `copy-fonts.test.ts`; tests-evidences/test.txt | ✅ Pass |
| 4. Given the built package, when it is read, then it holds the colour, spacing, density, typography, radius and elevation tokens of Tokens, as CSS variables and as a TypeScript module, in light and dark | `build-tokens.test.ts` › "built from the real source" (every colour, density, font, radius, elevation and spacing token, in CSS and in tokens.ts); `render-typescript.test.ts` › "type-checks with no diagnostics under strict mode"; tests-evidences/test.txt, typecheck.txt | ✅ Pass |

## Look at first

- Theme and density selectors and how they override each other. Read the order and specificity of the six blocks: a manual light choice must beat a dark device setting, and compact must never apply under 768 px. See `frontend/packages/tokens/src/generate/render-css.ts`.
- Values against the specifications: every hex of Colours and Tokens, the typography scale, the radii and the two elevations. The raised surfaces (`surface-raised-1` and `-2`) are a recorded assumption. See `frontend/packages/tokens/src/source/tokens.json`.
- Where the fonts come from and their licences. Resolution goes through `require.resolve` of the pinned package, the OFL licence is copied beside the files, and the `fonts/` folder is the only thing removed before a build. See `frontend/packages/tokens/src/generate/copy-fonts.ts` and `frontend/packages/tokens/src/build/build-tokens.ts`.
- What the package exports. It exports `./dist/tokens.ts` (TypeScript source, not JS), and `dist/` is gitignored and built on demand. T0.15 will need a build step before it imports the package. See `frontend/packages/tokens/package.json`.
- Not applicable to this ticket: identity, permissions and company data isolation (no back end, no data). There is no secret anywhere in the diff.

## Assumptions accepted

- K07, only the lock needed regenerating: accepted. The scaffold matches the brief, and `pnpm install --frozen-lockfile` passes.
- K07 decision, exact pins: accepted. Aligning on TypeScript 6 is a follow-up.
- Fonts packaged in the tokens package (D44): accepted.
- A JSON source and a small `tsx` build script: accepted as the conservative choice.
- Accessibility budget without measures, so WCAG 2.2 AA and the ratios of the Colours page are used: accepted.
- No lint script and no shared settings until T0.02 lands: accepted for now, as a follow-up.
- Latin subset, seven files: accepted, because the specifications name no subset.
- CSS variable names the Tokens page leaves open, and the raised surfaces (#FFFFFF in light, #1E2029 and #282A36 in dark): accepted. They follow the page and the mock-ups.
- Root `.gitignore` limited to the Python build folders: accepted, approved by the person.

## Follow-ups

- Update the "Today" section of `docs/technical/architecture/frontend.md` to name the tokens package. K15's change to that page was refused while it was T0.02's file.
- Move the package onto `@simpleerp/config`: add an ESLint config, a `lint` script and the shared tsconfig. CI lints nothing in the package today.
- Align on the workspace's TypeScript 6. Two majors are installed now (5.9.3 here, ^6.0.3 in config).
- Add the latin-ext font subsets when a country pack needs them.
- Keep one real `run build` output (through `tsx` and `main.ts`) in tests-evidences/, or add a test that runs it.
- Use #4B4FC9 instead of the near-miss #4B4FCE in the colour error message and its test fixture.
