🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F14-18 Abandoned plugins can be taken over

# 📏 BR-F14-18 Abandoned plugins can be taken over

**Status:** ✅ specified

## Statement

A plugin with no release and no answer from its publisher for 12 months, or whose end of life has passed, is
marked abandoned; another verified publisher may take it over after the security review, and each installing company
consents before receiving its versions.

## Why

AGPL code may be continued by others (D377), but installers must trust who ships their updates (BR-F14-07).

## Examples

| Case | Result |
|---|---|
| No release since 2025-10-01 and 3 unanswered support requests | passes: marked abandoned |
| Take-over by a verified publisher passing the review | passes |
| Installer that does not consent | passes: stays on the last old version |
| Take-over by an unverified publisher | fails: refused (BR-F14-09) |

## Applies to

- [UC-F14-23 Take over an abandoned plugin](../use-cases/07-plugin-end-of-life/uc-f14-23-take-over-an-abandoned-plugin.md)

## Exceptions

The original publisher may object within 30 days and resume maintenance.

## Configurable

The store operator sets the silence period.

## Open questions

None.

---

⬅️ [BR-F14-17 End of life announced in advance](br-f14-17-end-of-life-announced-in-advance.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F14-19 Beta versions only where companies opt in](br-f14-19-beta-versions-only-where-companies-opt-in.md)
