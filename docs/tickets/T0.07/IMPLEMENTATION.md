# T0.07: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- A changed token value must reach both the CSS and the TypeScript module, and every text pair must meet the Colours contrast (acceptance criteria of [TICKET.md](TICKET.md)).
- No font may come from a third party, and the package serves the three typefaces (D44, [TICKET.md](TICKET.md)).
- The manual theme choice must beat the device setting (D43), and compact density must not apply on phones (D42).
- Dependencies are pinned and licensed (D415, [supply chain page](../../technical/security/supply-chain-and-licences.md)).
- The specifications name no token tool or font subset, so the most conservative option applies (TKT-8).
- The package joins the pnpm workspace of T0.01 ([`pnpm-lock.yaml`](../../../pnpm-lock.yaml)).

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | Dependency versions | Exact pins | Caret ranges, TypeScript 6 | Manual upgrades, two TypeScript majors |
| [D2](#d2) | Token source and generator | Plain JSON and a small `tsx` script | A token tool | Own validation code |
| [D3](#d3) | Where the fonts come from | Copied from pinned `@fontsource` packages | Vendoring the mock-up files | Build needs the packages |
| [D4](#d4) | Theme and density selectors | Attribute selectors plus media queries | Media query only | Dark values written twice |
| [D5](#d5) | Shipped form | Generated `dist/`, ignored, TypeScript module | Committed output | Consumers must build first |
| [D6](#d6) | Shared settings | Own tsconfig, no lint | `@simpleerp/config` now | CI lints nothing here |

## <a id="d1"></a>D1: Dependency versions

**Chosen:** exact versions · **Where:** [`../../../frontend/packages/tokens/package.json:20-28`](../../../frontend/packages/tokens/package.json#L20-L28) · **Source:** K07

| Option | For | Against |
| --- | --- | --- |
| ✅ Exact pins | Reproducible lock, reasoned as meeting D415 | Upgrades are manual |
| Caret ranges | The lock already pins them, which is all D415 asks for (review) | Versions can drift on regeneration |
| TypeScript 6 | Matches `@simpleerp/config` | Not chosen by K07, no reason recorded |

**Trade-off:** two TypeScript majors are installed (5.9.3 here, ^6.0.3 in config).

**Revisit when:** the package moves to the shared settings (follow-up).

## <a id="d2"></a>D2: Token source and generator

**Chosen:** JSON read by a small script · **Where:** [`../../../frontend/packages/tokens/src/source/load-source.ts:221`](../../../frontend/packages/tokens/src/source/load-source.ts#L221) · **Source:** PLAN.md

| Option | For | Against |
| --- | --- | --- |
| ✅ JSON and `tsx` script | The specifications state no tool, so no dependency is added | The loader validates by hand |
| A token tool such as Style Dictionary | Ready-made outputs | Unspecified, adds a dependency |

**Trade-off:** more own code to test (the loader has its own tests).

**Revisit when:** a specification names a token tool or more output formats are needed.

## <a id="d3"></a>D3: Where the fonts come from

**Chosen:** copy from `@fontsource` at build time · **Where:** [`../../../frontend/packages/tokens/src/generate/copy-fonts.ts:19`](../../../frontend/packages/tokens/src/generate/copy-fonts.ts#L19) · **Source:** PLAN.md

| Option | For | Against |
| --- | --- | --- |
| ✅ Pinned OFL packages | Licences travel with files, no binary in git | Needs the packages installed to build |
| Vendor the mock-up woff2 files | Same files as the mock-ups | They sit in Git LFS under `docs/specs/` (PLAN.md) |
| A third-party font service | No files to ship | Forbidden by D44 |

**Trade-off:** only the latin subset ships (seven files, including Inter 600 which the scale does not use).

**Revisit when:** a country pack needs latin-ext glyphs.

## <a id="d4"></a>D4: Theme and density selectors

**Chosen:** attributes and media queries · **Where:** [`../../../frontend/packages/tokens/src/generate/render-css.ts:87-97`](../../../frontend/packages/tokens/src/generate/render-css.ts#L87-L97) · **Source:** PLAN.md

| Option | For | Against |
| --- | --- | --- |
| ✅ `data-theme` plus `prefers-color-scheme` | D43 manual switch wins both ways, as in the mock-ups | Dark values appear twice in the CSS |
| Media query only | One block | No manual switch (D43) |

Compact is limited to `min-width: 768px` so phones stay comfortable (D42). Density uses an attribute where the mock-ups use a class.

**Trade-off:** a larger CSS file.

**Revisit when:** D42 or D43 change.

## <a id="d5"></a>D5: Shipped form

**Chosen:** `dist/` generated and ignored, exported as `dist/tokens.ts` · **Where:** [`../../../frontend/packages/tokens/package.json:10-14`](../../../frontend/packages/tokens/package.json#L10-L14) · **Source:** PLAN.md

| Option | For | Against |
| --- | --- | --- |
| ✅ Generated, ignored | No generated file to review, consumers are Vite-based | T0.15 needs a build step first |
| Committed output | Works without a build | Not recorded as considered by the plan (open point) |

The root [`.gitignore`](../../../.gitignore) `build/` rule was narrowed so `src/build/` is tracked, a change the person approved.

**Revisit when:** a consumer cannot build first.

## <a id="d6"></a>D6: Shared settings

**Chosen:** own strict tsconfig, no lint script · **Where:** [`../../../frontend/packages/tokens/tsconfig.json`](../../../frontend/packages/tokens/tsconfig.json) · **Source:** PLAN.md

| Option | For | Against |
| --- | --- | --- |
| ✅ Standalone | T0.02 was not a prerequisite | CI skips lint (`--if-present`) |
| `@simpleerp/config` | Same rules as the workspace | T0.02 had not landed |

**Revisit when:** now, T0.02 is committed (follow-up).

## 📝 Assumptions behind the choices

- Exact pins accepted, TypeScript 6 alignment deferred: supports [D1](#d1).
- Plain JSON source accepted as the conservative choice: supports [D2](#d2).
- Fonts packaged in the tokens package, latin subset only: supports [D3](#d3).
- Names the Tokens page leaves open and the raised surface colours: supports [D4](#d4).
- `dist/` ignored, [`.gitignore`](../../../.gitignore) change approved: supports [D5](#d5).
- No shared settings until T0.02: supports [D6](#d6).
