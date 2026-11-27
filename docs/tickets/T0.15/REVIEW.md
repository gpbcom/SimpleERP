# T0.15: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- A new package, `@simpleerp/ui`, holds the six base components of the design system (button, form field, navigation item, toast, modal, card). They are built on the shared `UiIcon` and `UiSpinner`, and every style uses the tokens' CSS variables only.
- Hover in both themes works by mixing 8 % of `color-text` into the colour (C-01: darker in light mode, lighter in dark mode), and a component never tests the theme itself (D43).
- Accessibility is built into the components: the modal is a dialog (an `alertdialog` for the error variant) that moves, traps and restores the focus. The toast uses `role="status"`, never takes the focus, closes after 6 s without an action, and pauses while it is hovered or focused. A selectable card is a real radio button or checkbox.
- Decision K13: the focus and error edges of the form field are a 2 px border, as C-02 states. Decision K20: the `test` and `typecheck` scripts build the tokens package first.
- The tests are static: style tests parse each component's `<style>` with postcss (only tokens, a 2 px primary focus ring, a reduced-motion block), and a build test checks that no third-party URL reaches `dist`.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. Component tests pass in the light and the dark theme | tests-evidences/test.txt (12 files, 247 tests); `describe.each(THEMES)` in every `tests/components/*.spec.ts` | ✅ Pass |
| 2. The automated accessibility check finds no violation | `expectNoAxeViolations` (WCAG 2.0 to 2.2 A and AA tags, contrast left out because jsdom cannot compute it) on every state of each component, in both themes | ✅ Pass |
| 3. Each interactive component is reachable by keyboard with a visible focus | the keyboard tests of ui-button, ui-form-field, ui-nav-item, ui-toast, ui-modal and ui-card; tests/styles/focus-visible.spec.ts | ✅ Pass |
| 4. The Lucide icon comes from the package and nothing comes from a third party | tests/build/no-third-party.spec.ts (no URL in `src`, icons only from `lucide-vue-next` at an exact version, no URL in the build output) | ✅ Pass |
| 5. Colours, spacing, radius and elevation come from the tokens | tests/styles/tokens-only.spec.ts (including "only uses custom properties that exist") | ✅ Pass |
| 6. A toast without an action is announced politely and never takes the focus | ui-toast.spec.ts: "is announced politely with role status and never as an alert", "never takes the focus when it mounts" | ✅ Pass |

Lint (0 errors, 58 warnings) and type checks pass: tests-evidences/lint.txt and tests-evidences/typecheck.txt.

## Look at first

- **Modal focus management:** `frontend/packages/ui/src/components/UiModal.vue`, lines 864-928. The trap listens on the veil, so a click on the veil lets the focus leave (follow-up).
- **Toast timer:** `frontend/packages/ui/src/components/UiToast.vue`, lines 1271-1294, the pause and resume logic.
- **Form field states:** `frontend/packages/ui/src/components/UiFormField.vue`, lines 742-763: the 2 px focus and error edges (K13), and the error state, which has no separate focus look.
- **Icons:** `frontend/packages/ui/vite.config.ts` makes `lucide-vue-next` external, so the app that uses the package bundles the icons. Nothing is fetched remotely, which meets D45, but the README wording is wrong.
- **Scripts:** `frontend/packages/ui/package.json`, lines 19-20, the tokens build prefix (K20).
- No identity, permission or company data is involved: this is a front-end component library with no API calls and no secrets.

## Assumptions accepted

- K13, the 1 px shift when the border goes from 1 px to 2 px: accepted, because C-02 sets these widths and the shift is cosmetic.
- K20, the typecheck also builds the tokens package: accepted, because the setup file and the style tests read `tokens/dist`, and `pnpm -r` keeps the dependency order.
- The TICKET.md assumptions (the C-08 item only, axe-core, the accessibility budget without measures, ➖ No screen because the screens come with T0.17 and T0.23): accepted, because they match the roadmap row and the design system.

## Follow-ups

- UiModal: keep the focus trapped after a click on the veil, and use the 767 px phone breakpoint of the layout grid instead of 639 px.
- UiFormField: a distinct focus look for a field in error. This needs a design system decision first.
- README: correct the claim that Lucide is bundled into the package build, and change "is meant to export" to "exports".
- Align the peer versions of `@testing-library/jest-dom` and `@testing-library/dom`.
- Fix the 58 ESLint warnings.
- UiButton: make the disabled reason reachable by keyboard and screen readers.
- UiToast: track hover and focus separately so that a focusout does not resume while the toast is hovered, and draw the leaving motion.
