# T0.15: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- Colours, spacing, radius and elevation come from the tokens only (acceptance criterion 5 of [TICKET.md](TICKET.md), [Tokens](../../specs/04-ux/design-system/tokens.md)). The test [`frontend/packages/ui/tests/styles/tokens-only.spec.ts`](../../../frontend/packages/ui/tests/styles/tokens-only.spec.ts) rejects any literal value.
- Both themes, with no theme test in a component ([D43](../../specs/06-decisions/ux/d43-light-and-dark.md)).
- Keyboard use with a visible focus, and no automated accessibility violation ([D46](../../specs/06-decisions/ux/d46-accessibility-standard.md), [Accessibility](../../specs/04-ux/design-system/accessibility.md)).
- Icons from the package, nothing from a third party ([D45](../../specs/06-decisions/ux/d45-lucide-icons.md)).
- Form field edges of 1 px by default and 2 px on focus or error ([C-02](../../specs/04-ux/design-system/components/c-02-form-field.md)).
- A toast without an action is a `role="status"` that never takes the focus ([C-06](../../specs/04-ux/design-system/components/c-06-toast.md)).
- One class per file, no nested function and the other rules of [AGENT.md](../../../AGENT.md) apply to Python only; the front end follows its own lint ([`frontend/packages/ui/eslint.config.js`](../../../frontend/packages/ui/eslint.config.js)).

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | How the focus and error edges of the form field are drawn | A 2 px solid border | An inset box-shadow | A 1 px shift of the content on focus |
| [D2](#d2) | How the tokens reach the tests | A tokens build before `test` and `typecheck` | A `pretest` script | A few seconds on every run |
| [D3](#d3) | How hover works in both themes | Mixing 8 % of `color-text` into the colour | A hover colour per theme | Relies on `color-mix` |
| [D4](#d4) | How the tests check the styles | Static parsing of each `<style>` with postcss | Computed styles in jsdom | Cannot see the cascade the browser computes |
| [D5](#d5) | Where the Lucide icons are bundled | `lucide-vue-next` kept external in the build | Bundling the icons into the package | The consuming app bundles them |

## <a id="d1"></a>D1: How the focus and error edges of the form field are drawn

**Chosen:** a 2 px solid border · **Where:** [`frontend/packages/ui/src/components/UiFormField.vue:142-144`](../../../frontend/packages/ui/src/components/UiFormField.vue#L142-L144) and [`frontend/packages/ui/src/components/UiFormField.vue:156-159`](../../../frontend/packages/ui/src/components/UiFormField.vue#L156-L159) · **Source:** K13

| Option | For | Against |
| --- | --- | --- |
| ✅ 2 px solid border | Needs no shadow token. Passes both the focus-ring test and the tokens-only test | The content moves by 1 px when the border goes from 1 px to 2 px |
| Inset box-shadow with a 1 px spread | No layout shift | A literal 1 px spread fails the tokens-only test |
| Outline of 2 px | No layout shift | Reported by the worker as an alternative. The reason it lost is not recorded beyond the border meeting both tests |

**Trade-off:** a cosmetic 1 px shift, which C-02 implies by asking for exactly a 1 px and a 2 px edge.

**Revisit when:** the design system defines an elevation or ring token for focus, or the shift is seen as a defect (padding can compensate).

## <a id="d2"></a>D2: How the tokens reach the tests

**Chosen:** prefix `test` and `typecheck` with `pnpm --filter @simpleerp/tokens run build &&` · **Where:** [`frontend/packages/ui/package.json:19-20`](../../../frontend/packages/ui/package.json#L19-L20) · **Source:** K20

| Option | For | Against |
| --- | --- | --- |
| ✅ Build prefix in both scripts | One file changes, and the tokens package is untouched. Covers `typecheck` as well | The build runs on every run, a few seconds |
| A `pretest` script | The usual npm hook | Does not cover `typecheck` |
| Point the tokens export at its source CSS | No build needed | Changes the tokens package of another ticket |
| A Vitest `globalSetup` that builds the tokens | Hidden from the scripts | Does not cover `typecheck` and adds code to maintain |

**Trade-off:** a few seconds per run for a change confined to this package.

**Revisit when:** the tokens package exports its source, or the workspace builds packages in dependency order before any test.

## <a id="d3"></a>D3: How hover works in both themes

**Chosen:** mix 8 % of `color-text` into the colour · **Where:** [`frontend/packages/ui/src/components/UiButton.vue:144`](../../../frontend/packages/ui/src/components/UiButton.vue#L144) · **Source:** read from the diff, from C-01 and D43

| Option | For | Against |
| --- | --- | --- |
| ✅ `color-mix` with `color-text` | One rule for both themes: darker in light mode, lighter in dark mode. The component never tests the theme (D43) | Depends on browser support for `color-mix` (not assessed in this ticket) |
| A hover token or colour per theme | Explicit | Needs tokens the tokens package does not hold, or a theme test in the component |

**Trade-off:** hover is derived, not designed per theme.

**Revisit when:** the tokens package adds hover tokens.

## <a id="d4"></a>D4: How the tests check the styles

**Chosen:** parse each `<style>` with postcss · **Where:** [`frontend/packages/ui/tests/styles/component-styles.ts`](../../../frontend/packages/ui/tests/styles/component-styles.ts) · **Source:** read from the diff and the review note

| Option | For | Against |
| --- | --- | --- |
| ✅ Static parsing | Fast, deterministic, can check every rule for tokens, the 2 px primary focus ring and a reduced-motion block | Does not compute contrast or the cascade. The axe check leaves `color-contrast` out ([`frontend/packages/ui/tests/helpers/expect-no-axe-violations.ts`](../../../frontend/packages/ui/tests/helpers/expect-no-axe-violations.ts)) |
| Computed styles in jsdom | Closer to the browser | jsdom cannot compute colours, as the helper states |

**Trade-off:** contrast is left to the tokens package's contrast test and the Playwright runs of later tickets, as the helper says.

**Revisit when:** the Playwright scaffold (T0.22) can run axe in a real browser on these components.

## <a id="d5"></a>D5: Where the Lucide icons are bundled

**Chosen:** `lucide-vue-next` is external in the build · **Where:** [`frontend/packages/ui/vite.config.ts:14`](../../../frontend/packages/ui/vite.config.ts#L14) · **Source:** read from the diff, noted by the reviewer

| Option | For | Against |
| --- | --- | --- |
| ✅ External | The app deduplicates and tree-shakes it. Nothing is fetched remotely, which meets D45 | The README says the icons are bundled into the package ([`frontend/packages/ui/README.md:104-105`](../../../frontend/packages/ui/README.md#L104-L105)), which is wrong |
| Bundled into the package | Matches the README | Not chosen; the reason is not recorded (open point) |

**Trade-off:** the consuming app must bundle the icons.

**Revisit when:** a consumer cannot resolve the dependency. Fix the README wording first (follow-up).

## 📝 Assumptions behind the choices

- K13, the 1 px shift is acceptable because C-02 sets the widths: supports [D1](#d1).
- K20, the setup file and the style helper read `tokens/dist`, and `pnpm -r` keeps the dependency order: supports [D2](#d2).
