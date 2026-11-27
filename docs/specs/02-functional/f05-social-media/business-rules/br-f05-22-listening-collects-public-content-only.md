🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📣 [F5 Social media and marketing](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F5-22 Listening collects public content only

# 📏 BR-F5-22 Listening collects public content only

**Status:** 🔄 waiting for the owner

## Statement

Listening collects only content that anyone can read without signing in or being a member of a private group, from
sources whose terms allow reading it; it never reads private messages, closed groups or accounts that restrict their
posts.

## Why

Collecting private content would breach the author's expectation and the sources' terms; public posts are still personal
data when they name a person
([CR-FR-050](../../../10-country-packs/france/data-protection/cr-fr-050-privacy-by-design.md),
[CR-FR-052](../../../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md)). The owner asked for
brand listening ([D524](../../../06-decisions/f05-social-media/d524-benchmark-gaps-f05-social-media.md)).

## Examples

| Case | Result |
|---|---|
| A public post on a network | collected |
| A post in a closed group | never collected |
| A review on a public review site | collected, with its link |
| A source whose terms forbid reading | marked unavailable, no workaround |
| A mention that names a private person | kept 90 days, then only the counts stay |

## Applies to

- [UC-F5-27](../use-cases/10-referrals-push-and-listening/uc-f05-27-listen-to-brand-mentions.md)
- [E-F5-24 Brand mention](../data/e-f05-24-brand-mention.md)
- [E-F5-04 Social message](../data/e-f05-04-social-message.md)

## Exceptions

None.

## Configurable

Yes: the watched terms, the sources and the alert threshold, by marketing.

## Open questions

None.

---

⬅️ [BR-F5-21 Push needs the device's opt-in](br-f05-21-push-needs-the-devices-opt-in.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F5-23 Postal campaigns honour opt-outs](br-f05-23-postal-campaigns-honour-opt-outs.md)
