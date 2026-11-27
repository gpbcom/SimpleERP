# T0.16: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- A new workspace package `@simpleerp/i18n` holds one JSON catalogue per language (`en`, `fr`). It finds them with `import.meta.glob`, so adding a `<code>.json` file adds a language with no code change.
- `findMissingKeys` flattens every catalogue to dotted leaf paths. It reports each language that lacks a path, or holds a blank string for it, against the union of all languages. The test `catalogsComplete.test.ts` runs it on the shipped catalogues, so CI fails on a key added in one language only.
- `createI18n` is a Vue plugin whose active locale is a read-only ref. `t()` reads the ref on each call, so `setLocale` re-renders the components that use it with no reload. An unknown language is refused and the current one is kept.
- `formatMoney` keeps the amount as a decimal string and passes it straight to `Intl.NumberFormat` (ES2023 string input). It pads to the currency's minor digits and never rounds, leaving rounding to the country pack (REQ-T10-03).
- `formatNumber` and `formatDate` are thin wrappers over `Intl` that validate their input and throw `RangeError`. The time zone and other options stay the caller's choice.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. Given a key added in English only, when CI runs the catalogue check, then it fails | `findMissingKeys.test.ts` › "reports a key added in English only as missing in French"; `catalogsComplete.test.ts` › "has every key in every language"; tests-evidences/test.txt | ✅ Pass |
| 2. Given a component showing a translated text, when the user switches language, then it re-renders without reloading | `languageSwitch.test.ts` › "re-renders the same element in the new language", "does not reload the page when the language changes"; tests-evidences/test.txt | ✅ Pass |
| 3. Given a money amount, when it is formatted for a locale, then it keeps its exact decimals | `formatMoney.test.ts` › "keeps every digit of a large amount in French", "keeps a trailing zero of the amount", "keeps decimals beyond the minor digits without rounding" | ✅ Pass |
| 4. Given dates and numbers, when they are formatted, then they follow the locale | `formatDate.test.ts` › "puts the day and the month in the order of the %s locale"; `formatNumber.test.ts` › "groups thousands with a space and uses a decimal comma in French" | ✅ Pass |
| 5. Given the catalogues, when the package loads, then French and English are both present | `catalogs.test.ts` › "lists English and French among the available languages"; `index.test.ts` | ✅ Pass |

Lint, typecheck and a frozen install pass: tests-evidences/lint.txt, typecheck.txt, pnpm-install.txt. The package runs 75 tests in 9 files.

## Look at first

- The exact-money path: the cast `amount as unknown as number` relies on the runtime reading decimal strings exactly (Node 22, current browsers). Read `frontend/packages/i18n/src/format/formatMoney.ts` lines 17-33.
- Reactivity of the switch: `t()` reads `locale.value` and picks the catalogue on each call, and `Object.hasOwn` guards key and parameter lookup against prototype members. Read `frontend/packages/i18n/src/translate/createI18n.ts` lines 19-61.
- The missing-key algorithm and its sort order: `frontend/packages/i18n/src/check/findMissingKeys.ts`.
- The package wiring: exact pins, TypeScript 6 to meet the peer range of `@simpleerp/config`, the `vite/client` types for `import.meta.glob`, the jsdom environment, and the lockfile importer. See `frontend/packages/i18n/package.json`, `tsconfig.json`, `vitest.config.ts` and `pnpm-lock.yaml`.
- No identity, permission or company data is touched. The package runs only in the browser and holds no secret.

## Assumptions accepted

- **Ticket:** no use case or business rule applies, the Localisation measures are not yet specified, and there is no design page of its own. All accepted: the specification pages confirm each point.
- **Catalogue check (K01, K02, K11):** dotted paths, blank strings counted as missing, a string-or-object clash reported on both sides, and an empty object ignored. Accepted as the conservative reading of REQ-T10-01 and D21.
- **Formatting (K03 to K05, K12, K13):** the tests allow either minus sign, use fixed dates in UTC and normalise ICU spaces. The minor digits default to 2. Accepted: deterministic, and they do not depend on the ICU version.
- **Translator (K06, K07, K15):** the ref keeps the full tag, subtags match case-insensitively, only hyphenated tags are supported, and a missing plugin throws. Accepted, in line with BCP 47 and Vue.
- **Package (K08, K09, K16):** `catalogs` is a value, the pins are exact, vue is a peer, the environment is jsdom, and the lockfile drift in the worktree was restored. Accepted: D415 asks for locked dependencies, and the frozen install passes.
- **Environment (K10 to K14):** offline installs in the worktrees changed no tracked file. Accepted.
- **Docs (K17, K18):** the API comes from the brief and matches `src/index.ts`, the review workflow is deferred to P2, and the Target design section is untouched. Accepted. The list of consumers is the target, see the follow-ups.
- **Screens (TKT-21):** "➖ No screen" is sound: the ticket builds a library package and no screen.

## Follow-ups

- `formatNumber`'s doc comment says a decimal string "stays exact", but the default options round it to 3 fraction digits. Document this, or default to the string's own decimals (K13).
- `findMissingKeys` silently drops number or array leaves and throws on null. Report them as missing (K11, K01).
- The README says the package is "built on the design system's tokens", but it does not depend on them. The list of consuming apps is the target, not today (K17).
- Quote and semicolon style is mixed across the package. Add a formatter rule to `@simpleerp/config`.
- The private helpers (`flatten`, `compare`, `pickCatalog`, `resolveKey`) lack the full TSDoc the public functions have.
