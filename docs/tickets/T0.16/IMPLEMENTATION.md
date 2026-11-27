# T0.16: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- A key added in one language only must fail CI, and French and English must both be present (acceptance criteria 1 and 5 of [TICKET.md](TICKET.md), [REQ-T10-01](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-01-translation-catalogues.md), [D21](../../specs/06-decisions/foundations/d21-languages.md)).
- Money keeps its exact decimals ([REQ-T10-03](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md), criterion 3).
- A language switch re-renders without reloading (criterion 2).
- The front end is Vue 3 with TypeScript ([D407](../../specs/06-decisions/technical/d407-front-end.md)), and the package extends the shared settings of `@simpleerp/config` ([`tsconfig.json`](../../../frontend/packages/i18n/tsconfig.json)).
- Dependencies are locked ([D415](../../specs/06-decisions/technical/d415-supply-chain-controls.md) as cited by K09).
- Tests come first (TKT-4), and the Python rules of [AGENT.md](../../../AGENT.md) do not apply to front-end code.

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | How an amount stays exact | The string goes to `Intl.NumberFormat` with a cast | `Number()` or a decimal library | Relies on runtime support for string input |
| [D2](#d2) | How catalogues are found | Eager `import.meta.glob` | A lazy glob, or hard-coded imports | Every language ships in the bundle |
| [D3](#d3) | How missing keys are found | Flatten to dotted leaves, compare to the union | Recursive comparison | A little more memory |
| [D4](#d4) | How the switch is reactive | Full tag in a `ref`, catalogue picked in each `t()` | A second computed ref | A small scan per call |
| [D5](#d5) | Fraction digits of money | Minor digits up to the amount's own decimals | Default rounding or a fixed maximum | Rounding is left to the country pack |
| [D6](#d6) | Sort order of the result | Code-unit comparison | `localeCompare` | Not linguistic order |
| [D7](#d7) | Key and parameter lookup | `Object.hasOwn` | Plain access or `in` | Needs ES2022 lib |
| [D8](#d8) | Public API | Named re-exports | `export *` | A new export needs an edit |
| [D9](#d9) | Package wiring | Exact pins, shared ESLint and tsconfig bases | Caret ranges, a standalone config | Manual bumps |
| [D10](#d10) | Test layout | Inline fixtures, `it.each`, local `plain()` helpers | Fixture files, one test per case | Small module-level helpers in tests |
| [D11](#d11) | Invalid input | `RangeError` with a full sentence | Return an empty string or let `Intl` throw | The caller must handle errors |

## <a id="d1"></a>D1: How an amount stays exact

**Chosen:** the decimal string is validated, then passed to `Intl.NumberFormat.format` with `amount as unknown as number` · **Where:** [`frontend/packages/i18n/src/format/formatMoney.ts:33`](../../../frontend/packages/i18n/src/format/formatMoney.ts#L33), and [`formatNumber.ts:26`](../../../frontend/packages/i18n/src/format/formatNumber.ts#L26) for numbers · **Source:** K12, K13

| Option | For | Against |
| --- | --- | --- |
| ✅ String passed to `Intl` | Exact, as REQ-T10-03 asks. No dependency | The TypeScript lib types `format` as taking a number, hence the cast. Relies on Node 22 and current browsers reading strings |
| `Number()` | Matches the typing | Loses digits beyond about 16 |
| A decimal library such as decimal.js | Exact on any runtime | A new dependency to pin and bump |
| Formatting by hand | No runtime reliance | Reimplements the locale separators |

**Trade-off:** the code leans on runtime support instead of adding a library. The tests on large amounts and trailing zeros cover it.

**Revisit when:** a supported browser cannot read decimal strings, or the typings declare string input.

## <a id="d2"></a>D2: How the catalogues are found

**Chosen:** `import.meta.glob('./*.json', { eager: true, import: 'default' })` and a small `build` that takes the code from the file name · **Where:** [`frontend/packages/i18n/src/catalogs/catalogs.ts:3`](../../../frontend/packages/i18n/src/catalogs/catalogs.ts#L3) · **Source:** K10

| Option | For | Against |
| --- | --- | --- |
| ✅ Eager glob | Adding `<code>.json` adds a language with no code change. `availableLanguages()` and `catalogs` stay synchronous | Every language is in the bundle, small at two languages |
| Lazy glob | Loads a language on demand | Makes the API asynchronous, which the tests and the brief do not expect |
| Hard-coded `en` and `fr` imports | Simple | A code change per language, which the brief rules out |

**Trade-off:** bundle size for a synchronous API. The inline loop was also considered (K10) and a named `build` was kept for readability.

**Revisit when:** the number of languages makes the bundle matter.

## <a id="d3"></a>D3: How missing keys are found

**Chosen:** flatten each catalogue to a map of dotted leaves and compare with the union of all keys · **Where:** [`frontend/packages/i18n/src/check/findMissingKeys.ts:26-50`](../../../frontend/packages/i18n/src/check/findMissingKeys.ts#L26-L50) · **Source:** K11

| Option | For | Against |
| --- | --- | --- |
| ✅ Flatten and union | Simple. Matches the dotted keys of `t()`. A string-or-object clash is reported on both sides with no special case | A little more memory |
| Recursive comparison | No flattening | More branches for clashes and blank values |
| Flatten, then check blanks in a second pass | Separate concerns | Two passes for one answer |

**Trade-off:** memory for simplicity. Known gap: a number, array or null leaf is not handled (see the follow-ups of [EXPLAIN.md](EXPLAIN.md)).

**Revisit when:** catalogues grow large, or a non-string leaf is allowed.

## <a id="d4"></a>D4: How the language switch stays reactive

**Chosen:** the full tag lives in a `ref`, and `t()` picks the catalogue on each call · **Where:** [`frontend/packages/i18n/src/translate/createI18n.ts:40-45`](../../../frontend/packages/i18n/src/translate/createI18n.ts#L40-L45) · **Source:** K15

| Option | For | Against |
| --- | --- | --- |
| ✅ One ref, lookup per call | One piece of reactive state. `locale.value` returns the full tag the tests expect | A small linear scan per call |
| A second computed ref for the catalogue | No scan per call | More reactive state |
| Store only the language subtag | Simpler lookup | Loses the full tag |

`locale` is exposed with `readonly(ref)` ([`createI18n.ts:43`](../../../frontend/packages/i18n/src/translate/createI18n.ts#L43)): `shallowReadonly` and a computed getter were the alternatives, and `readonly` fits `Readonly<Ref<string>>` and stays watchable (K15).

**Trade-off:** a tiny cost per call for less state. **Revisit when:** profiling shows `t()` in a hot path.

## <a id="d5"></a>D5: Fraction digits of money

**Chosen:** minimum is the currency's minor digits, maximum is the larger of those and the amount's own decimals · **Where:** [`frontend/packages/i18n/src/format/formatMoney.ts:24-32`](../../../frontend/packages/i18n/src/format/formatMoney.ts#L24-L32) · **Source:** K12

| Option | For | Against |
| --- | --- | --- |
| ✅ Pad, never round | Keeps trailing zeros and extra decimals (criterion 3) | A long amount shows all its decimals |
| Default currency rounding | Familiar output | Rounds, which loses exactness |
| A fixed maximum such as 20 | Simple | An arbitrary limit |

**Trade-off:** rounding is left to the country pack, which is not decided here. The fallback of 2 minor digits when `resolvedOptions` omits them is an accepted assumption.

**Revisit when:** the country pack defines rounding.

## <a id="d6"></a>D6: Sort order of the missing keys

**Chosen:** `<` and `>` on language, then key · **Where:** [`frontend/packages/i18n/src/check/findMissingKeys.ts:14-19`](../../../frontend/packages/i18n/src/check/findMissingKeys.ts#L14-L19) · **Source:** K11

| Option | For | Against |
| --- | --- | --- |
| ✅ Code-unit comparison | Same order on every machine and in CI | Not linguistic order |
| `localeCompare` | Linguistic order | Depends on locale and ICU |

**Trade-off:** a stable CI output over a natural one. **Revisit when:** the report is shown to translators.

## <a id="d7"></a>D7: Key and parameter lookup

**Chosen:** `Object.hasOwn` · **Where:** [`frontend/packages/i18n/src/translate/createI18n.ts:22`](../../../frontend/packages/i18n/src/translate/createI18n.ts#L22), [`:50`](../../../frontend/packages/i18n/src/translate/createI18n.ts#L50) · **Source:** K15

| Option | For | Against |
| --- | --- | --- |
| ✅ `Object.hasOwn` | A key such as `constructor` does not resolve to a prototype member | Needs the ES2022 lib, which lint and typecheck accepted |
| Plain access or `in` | Shorter | Resolves prototype members |

**Trade-off:** none found in this repository. **Revisit when:** a target runtime lacks it.

## <a id="d8"></a>D8: Public API

**Chosen:** named re-exports, `export type` for types · **Where:** [`frontend/packages/i18n/src/index.ts:1-8`](../../../frontend/packages/i18n/src/index.ts#L1-L8) · **Source:** K16

| Option | For | Against |
| --- | --- | --- |
| ✅ Named re-exports | Explicit API, no internal helper leaks | A new export needs an edit |
| `export *` from each module | No edit | Leaks helpers |

**Revisit when:** the API grows past what is easy to list.

## <a id="d9"></a>D9: Package wiring

**Chosen:** exact pins ([`package.json:22-32`](../../../frontend/packages/i18n/package.json#L22-L32)), ESLint re-exported from `@simpleerp/config` ([`eslint.config.js:1`](../../../frontend/packages/i18n/eslint.config.js#L1)), tsconfig extending the shared one with a lib override ([`tsconfig.json:2-7`](../../../frontend/packages/i18n/tsconfig.json#L2-L7)) · **Source:** K09

| Option | For | Against |
| --- | --- | --- |
| ✅ Exact pins and shared bases | Reproducible, follows D415, one source of rules | Manual bumps. The lib override is needed for string input to `Intl.NumberFormat` |
| Caret ranges, as config uses | Automatic bumps | Less reproducible |
| Copy config's own ESLint file, or a standalone tsconfig like tokens' | Self-contained | Duplicates rules, and the package has no node-only code |

TypeScript 6.0.3 and ESLint 10.16.0 satisfy the peer ranges of `@simpleerp/config`. Vue is a peer (`^3.5.0`) and a pinned dev dependency, standard for a library, and the tests use jsdom to mount a component ([`vitest.config.ts:6`](../../../frontend/packages/i18n/vitest.config.ts#L6)).

**Revisit when:** a dependency bot is adopted.

## <a id="d10"></a>D10: Test layout

**Chosen:** inline fixtures, `it.each` tables, and local `plain()` helpers that turn U+202F and U+00A0 into plain spaces, written with `\u` escapes · **Where:** [`tests/format/formatMoney.test.ts`](../../../frontend/packages/i18n/tests/format/formatMoney.test.ts), [`formatNumber.test.ts`](../../../frontend/packages/i18n/tests/format/formatNumber.test.ts), [`formatDate.test.ts`](../../../frontend/packages/i18n/tests/format/formatDate.test.ts), [`findMissingKeys.test.ts`](../../../frontend/packages/i18n/tests/check/findMissingKeys.test.ts) · **Source:** K01, K03, K04, K05

| Option | For | Against |
| --- | --- | --- |
| ✅ Inline fixtures and `plain()` | Self-contained tests, readable expected strings, independent of the ICU version. Escapes pass `no-irregular-whitespace` | A module-level helper function, which the Python rules of AGENT.md do not cover for TypeScript |
| Fixture files | Reusable | Extra files for small data |
| Literal ICU spaces in expectations | No helper | Fragile and invisible, and lint refuses them (an `eslint-disable` was the other option) |
| One test per case | Names each row | Duplicates code. The percent style keeps one test per locale for that reason |

Other test choices: the walk helpers in [`catalogs.test.ts`](../../../frontend/packages/i18n/tests/catalogs/catalogs.test.ts) keep the tests independent of the checker (K02). The completeness message lists each missing key (K02). The switch test keeps a DOM node reference to prove a re-render and not a re-mount, and builds its component with `h()` (K07). `catalogs` has its own `toBeDefined` case in [`index.test.ts`](../../../frontend/packages/i18n/tests/index.test.ts) (K08).

**Revisit when:** a front-end style rule is added to `@simpleerp/config`.

## <a id="d11"></a>D11: Invalid input

**Chosen:** validate and throw `RangeError` with a full sentence. A `Date` is formatted as it is and only a string is parsed. No default option, so the time zone stays the caller's · **Where:** [`frontend/packages/i18n/src/format/formatDate.ts:11-14`](../../../frontend/packages/i18n/src/format/formatDate.ts#L11-L14), [`formatMoney.ts:18-23`](../../../frontend/packages/i18n/src/format/formatMoney.ts#L18-L23) · **Source:** K13, K14

| Option | For | Against |
| --- | --- | --- |
| ✅ Explicit `RangeError` | Same failure for a `Date` and a string, clear message | The caller handles it |
| Let `Intl` throw | Less code | A less explicit message |
| Return an empty string | No throw | Hides a bad value in a money screen |

**Revisit when:** the error pattern on screen (T0.23) sets a convention.

## 📝 Assumptions behind the choices

- A key that is a string in one language and an object in another is reported on both sides, and an empty object is ignored: supports [D3](#d3).
- Blank strings count as missing (D21): supports [D3](#d3).
- The locale ref keeps the full tag, subtags match case-insensitively, and only hyphenated tags are supported: supports [D4](#d4).
- The minor digits default to 2: supports [D5](#d5).
- Exact pins with TypeScript 6.0.3, ESLint 10.16.0, vue as a peer and a jsdom environment: supports [D9](#d9).
- Module-level helpers and `\u` escapes in tests are fine because the Python rules do not apply to front-end code: supports [D10](#d10).
