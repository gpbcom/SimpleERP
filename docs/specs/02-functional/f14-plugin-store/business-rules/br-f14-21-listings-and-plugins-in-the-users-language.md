🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🧰 [F14 Plugin store](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F14-21 Listings and plugins in the user's language

# 📏 BR-F14-21 Listings and plugins in the user's language

**Status:** ✅ specified

## Statement

A listing and a plugin's texts are shown in the user's language when the publisher provides it, otherwise in English;
the listing shows which languages are available, and machine translations are marked as such.

## Why

Users choose plugins they can read (D471).

## Examples

| Case | Result |
|---|---|
| French user, French listing provided | passes: French shown |
| French user, only English provided | passes: English shown with "available in English" |
| Machine translation not marked | fails: refused at submission |

## Applies to

- [UC-F14-26 Translate a listing and a plugin](../use-cases/03-publish/uc-f14-26-translate-a-listing-and-a-plugin.md)

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F14-20 Staged rollout pauses on failures](br-f14-20-staged-rollout-pauses-on-failures.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F14-22](br-f14-22-support-terms-shown-before-purchase-and-measured.md)
