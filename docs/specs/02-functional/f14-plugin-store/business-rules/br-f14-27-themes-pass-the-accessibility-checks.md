🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F14-27 Themes pass the accessibility checks

# 📏 BR-F14-27 Themes pass the accessibility checks

**Status:** ✅ specified

## Statement

A theme is published, and stays installable, only while its automated accessibility checks pass for its current version:
text contrast, keyboard focus, text resizing and form labels; a company's own colour choice is checked again before it
is saved.

## Why

A theme sets how everyone, including people with low vision or who use only a keyboard, reads the site
([CR-FR-072](../../../10-country-packs/france/consumer/cr-fr-072-web-accessibility-eaa.md)). The owner asked for website
themes ([D533](../../../06-decisions/f14-plugin-store/d533-benchmark-gaps-f14-plugin-store.md)); the checks are part of
the store's automated checks ([BR-F14-06 Automated checks before review](br-f14-06-automated-checks-before-review.md)).

## Examples

| Case | Result |
|---|---|
| A theme with text contrast 7 to 1 | passes |
| A theme with no visible keyboard focus | refused at submission |
| A company's grey text on white at 3 to 1 | refused with a passing suggestion |
| An update that breaks form labels | withdrawn until fixed, the installed copy is warned |
| A report older than the checks | Needs a new check, not installable |

## Applies to

- [UC-F14-32](../use-cases/08-trials-instances-and-partners/uc-f14-32-install-a-website-theme.md)
- [E-F14-25 Theme](../data/e-f14-25-theme.md)
- [E-F14-07 Plugin check report](../data/e-f14-07-plugin-check-report.md)

## Exceptions

None.

## Configurable

No: the limits come from the accessibility standard of the country pack.

## Open questions

None.

---

⬅️ [BR-F14-26 Partner rankings are transparent](br-f14-26-partner-rankings-are-transparent.md) · ⬆️ [Up](README.md)
