🏠 [Specs](../../README.md) › 🎨 [UX](../README.md) › 📐 [Design system](README.md) › ♿ Accessibility

# ♿ Accessibility

**Status:** ✅ specified

## Standard

WCAG 2.2 level AA everywhere, plus the French RGAA 4.1 checklist. See
[D46](../../06-decisions/ux/d46-accessibility-standard.md).

## Checks

- Automated: axe-core runs in every Playwright test of the front ends (TEST-6), and a violation fails the
  test.
- Manual: an RGAA audit of the main journeys before each release.

## Assistive technologies

Tested with NVDA and Firefox on Windows, VoiceOver and Safari on macOS and iOS, TalkBack on Android, and with
the keyboard only.

---

⬅️ [Responsive](responsive.md) · ⬆️ [Up](README.md) · ➡️ [Components](components/README.md)
